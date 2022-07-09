from cProfile import label
import sys
from PyQt5 import QtWidgets, QtGui

# Váriáveis globais
  
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
label_color = QtWidgets.QLabel(window)
line = QtWidgets.QLineEdit(window)
labelNewColor = QtWidgets.QLabel(window)
newColor = QtWidgets.QLabel(window)

def clickMethod():
    print('Color: ' + line.text())

# Desehando a janela
window.setGeometry(0, 0, 600, 400)
window.setWindowTitle('Colors')
window.setWindowIcon(QtGui.QIcon("python.jpg"))

# Desenhando os elementos
def drawInputColor(x, y):
    label_color.setText('Color: ')
    label_color.move(x, y)

    labelNewColor.setText('New color: ')
    labelNewColor.move(x, y + 25)

    newColor.setText('teste :')
    newColor.move(60 + x, y + 25)

    line.move(32 + x, y - 8)
    line.resize(200,32)


drawInputColor(200, 40)


pybutton = QtWidgets.QPushButton(text = 'OK', parent = window,)
pybutton.clicked.connect(clickMethod)
pybutton.resize(200,32)
pybutton.move(80, 80)


window.show()
sys.exit(app.exec_())