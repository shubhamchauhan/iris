from PyQt4 import QtGui, uic
import sys

iris_uic = uic.loadUiType('gui/iris.ui')[0]

class IrisGui(QtGui.QMainWindow,iris_uic):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.intialize()

	def intialize(self):
		self.select_file_button.clicked.connect(self.selectFileButtonClicked)
		self.get_relations_button.clicked.connect(self.getRelationsButtonClicked)

	def selectFileButtonClicked(self):
		selected_file = QtGui.QFileDialog.getOpenFileName()
		

	def getRelationsButtonClicked(self):
		pass

def main():
	app = QtGui.QApplication(sys.argv)
	iris = IrisGui()
	iris.show()
	app.exec_()

if __name__=="__main__":
	main()