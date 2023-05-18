from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
app = QApplication([])
win = QWidget()
win.show()

main_layout = QVBoxLayout() 
win.setLayout(main_layout) 
b1 = QPushButton("Button 1")
b2 = QPushButton("Button 2") #a
b3 = QPushButton("Button 3") #a
b4 = QPushButton("Button 4") #a
b5 = QPushButton("Button 5") #a

a = QHBoxLayout() 
main_layout.addLayout(a)
b =  QHBoxLayout() 
main_layout.addLayout(b)

a.addWidget(b1)
a.addWidget(b2)
a.addWidget(b3)
b.addWidget(b4)
b.addWidget(b5)
