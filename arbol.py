from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import completo
class MainWindow(QMainWindow):

	def __init__(self,dr,  parent=None):
		super(MainWindow,self).__init__(parent)
		self.drop = dr
		self.setStyleSheet("background-color:#0099FF; color: #fff;font-size:bold")
		self.initUI()

	def createGroup(self):
		groupBox = QGroupBox()
		self.treeWidget = QTreeWidget()
		t=self.drop.listarCarpetas()

		t2=t.getDirectorios()
		hijos=t.getHijos()
		header=QTreeWidgetItem(["Tree"])
		icon=QIcon('home-icon.png')
		icon2=QIcon('text-plain-icon.png')
		self.treeWidget.setHeaderItem(header)   #Another alternative is setHeaderLabels(["Tree","First",...])
		root = QTreeWidgetItem(self.treeWidget, ["dropbox"])
		for i in range(len(t2)):
			q=[]
			q.append(t2[i])
			A = QTreeWidgetItem(root,q)
			A.setIcon(0,icon)
			for j in range(len(hijos)):
				#print(hijos[j].getNombre())
				if ("/"+hijos[j].getPadre())==t2[i]:
					q=[]
					q.append(hijos[j].getNombre())
					barA = QTreeWidgetItem(A,q)
					barA.setIcon(0,icon2)

		"""

		barA = QTreeWidgetItem(A, ["bar", "i"])
		bazA = QTreeWidgetItem(A, ["baz", "a"])

		self.treeWidget.setEditTriggers(self.treeWidget.NoEditTriggers)

		self.treeWidget.itemDoubleClicked.connect(self.checkEdit)
		"""

		vbox = QVBoxLayout()
		vbox.addWidget(self.treeWidget)

		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox

	# in your connected slot, you can implement any edit-or-not-logic
	# you want
	def checkEdit(self, item, column):
	# e.g. to allow editing only of column 1:
		if column == 1:
			self.treeWidget.editItem(item, column)

	def initUI(self):
		self.resize(300, 220)

		self.grid = QGridLayout()

		self.widget = QWidget()
		self.widget.setLayout(self.grid)
		self.setCentralWidget(self.widget)
		self.grid.addWidget(self.createGroup(),1,0,1,2)

		self.show()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	app.setStyle(QStyleFactory.create("Fusion"))
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())
