import os
import sys
from PIL import Image
from PySide6 import QtWidgets, QtGui, QtCore

# Build Application
app = QtWidgets.QApplication(sys.argv)

class spriteSheetGen(QtWidgets.QWidget): 
   def __init__(self):
      super().__init__()   

      # Image Directory
      self.imgDir = './images/'

      # List of files
      self.imgFiles = os.listdir(self.imgDir)

      # Sorting images
      self.imgFiles.sort()

      # Create list to store for export
      self.imgLst = []

      # Specify amount of rows
      self.nRows = 5

      # Specify amount of columns
      self.nCols = 5

      # Specify dimensions
      self.outWidth = 1024
      self.outHeight = 1024

      # Application Title
      self.setWindowTitle('Sprite Sheet Generator')

      # Building user interface buttons
      self.btnPath = QtWidgets.QPushButton('Image Path')
      self.btnPath.clicked.connect(self.selectDirectory)

      self.lblCount = QtWidgets.QLabel()

      self.lblWidth = QtWidgets.QLabel('Export Width:')
      self.edtWidth = QtWidgets.QLineEdit(str(self.outWidth))
      self.lblHeight = QtWidgets.QLabel('Export Height:')
      self.edtHeight = QtWidgets.QLineEdit(str(self.outHeight))

      self.lblRows = QtWidgets.QLabel('Rows:')
      self.edtRows = QtWidgets.QLineEdit(str(self.nRows))
      self.lblCols = QtWidgets.QLabel('Columns:')
      self.edtCols = QtWidgets.QLineEdit(str(self.nCols))

      self.btnExport = QtWidgets.QPushButton('Export Sprite Sheet')
      self.btnExport.clicked.connect(self.export)

      layout = QtWidgets.QVBoxLayout()
      layout.addWidget(self.btnPath)
      layout.addWidget(self.lblCount)
      layout.addWidget(self.lblWidth)
      layout.addWidget(self.edtWidth)
      layout.addWidget(self.lblHeight)
      layout.addWidget(self.edtHeight)
      layout.addWidget(self.lblRows)
      layout.addWidget(self.edtRows)
      layout.addWidget(self.lblCols)
      layout.addWidget(self.edtCols)
      layout.addWidget(self.btnExport)

      self.setLayout(layout)

   def selectDirectory(self):
       pathDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')

       if pathDir:
           self.imgDir = pathDir

           self.imgFiles = os.listdir(self.imgDir)
           self.imgFiles.sort()

           self.lblCount.setText(f'{len(self.imgFiles)} images found.')         
   
   def export(self):
        # Loop through images and add them to image list
        for file in self.imgFiles:
            image = Image.open(os.path.join(self.imgDir, file))
            self.imgLst.append(image)

        maxWidth = self.nCols * self.imgLst[0].width
        maxHeight = self.nRows * self.imgLst[0].height

        # Creating new sprite sheet
        imgOutput = Image.new('RGB', (maxWidth, maxHeight))

        # Loop through images
        for i, img in enumerate(self.imgLst):
            col = i % self.nCols
            row = i // self.nRows
            x = col * img.width
            y = row * img.height
            imgOutput.paste(image, (x, y))

        # Resizing images from the list and save to new single sprite sheet PNG
        imgOutput.resize((self.outWidth, self.outHeight)).save('spriteSheet.png')   

# Create instance of program
widget = spriteSheetGen()

widget.show()

sys.exit(app.exec()) 