from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QTextEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Calculadora(QWidget):

    def __init__(self):
        super(Calculadora,self).__init__()
        self.resize(500,400)
        self.setWindowTitle("Calculadora")
        self.display_widgets()

    def display_widgets(self):
        self.setStyleSheet("Calculadora { background-color: #2E89B9; }")

        lbl_titulo = QLabel("Calculadora", self)
        lbl_titulo.setFont(QFont("Arial", 20))
        lbl_titulo.setAlignment(Qt.AlignCenter)

        self.lbl_operaciones = QLabel("", self)
        self.lbl_operaciones.setAlignment(Qt.AlignRight)
        self.lbl_operaciones.setFont(QFont("Arial", 12))

        lbl_historial = QLabel("Historial", self)
        lbl_historial.setAlignment(Qt.AlignCenter)
        lbl_historial.setFont(QFont("Arial", 16))

        self.txt_edit = QTextEdit(self)
        self.txt_edit_resultado = QTextEdit(self)

        self.lbl_resultado = QLabel("")

        #Grid de botones
        glyt_botones = QGridLayout()
        self.btn_0 = QPushButton("0", self)
        self.btn_1 = QPushButton("1", self)
        self.btn_2 = QPushButton("2", self)
        self.btn_3 = QPushButton("3", self)
        self.btn_4 = QPushButton("4", self)
        self.btn_5 = QPushButton("5", self)
        self.btn_6 = QPushButton("6", self)
        self.btn_7 = QPushButton("7", self)
        self.btn_8 = QPushButton("8", self)
        self.btn_9 = QPushButton("9", self)
        self.btn_borrar = QPushButton("Borrar", self)
        self.btn_suma = QPushButton("+", self)
        self.btn_resta = QPushButton("-", self)
        self.btn_multiplicacion = QPushButton("*", self)
        self.btn_division = QPushButton("/", self)
        self.btn_igual = QPushButton("=", self)
        self.btn_punto = QPushButton(".", self)

        #Agregar botones en su posición
        glyt_botones.addWidget(self.btn_borrar, 0,0)
        glyt_botones.addWidget(self.btn_suma, 0, 1)
        glyt_botones.addWidget(self.btn_resta, 0, 2)

        glyt_botones.addWidget(self.btn_multiplicacion, 1, 0)
        glyt_botones.addWidget(self.btn_division, 1, 1)
        glyt_botones.addWidget(self.btn_igual, 1, 2)

        glyt_botones.addWidget(self.btn_7, 2, 0)
        glyt_botones.addWidget(self.btn_8, 2, 1)
        glyt_botones.addWidget(self.btn_9, 2, 2)

        glyt_botones.addWidget(self.btn_4, 3, 0)
        glyt_botones.addWidget(self.btn_5, 3, 1)
        glyt_botones.addWidget(self.btn_6, 3, 2)

        glyt_botones.addWidget(self.btn_1, 4, 0)
        glyt_botones.addWidget(self.btn_2, 4, 1)
        glyt_botones.addWidget(self.btn_3, 4, 2)

        glyt_botones.addWidget(self.btn_0, 5, 0, 1, 2)
        glyt_botones.addWidget(self.btn_punto, 5, 2)

        glyt_principal = QGridLayout(self)
        glyt_principal.addWidget(lbl_titulo, 0,0,1,2) #El titulo dentro del grid va a estar en posición 0,0 y ocpará 1 fila y 2 columnas
        glyt_principal.addWidget(self.lbl_operaciones, 1,0,1,1) #Fila 1, columna 0, 1 fila y 1 columna
        glyt_principal.addWidget(lbl_historial, 1, 1, 1, 1)
        glyt_principal.addWidget(self.txt_edit_resultado, 2, 0, 1, 1)
        glyt_principal.addWidget(self.txt_edit, 2,1,2,1)
        glyt_principal.addLayout(glyt_botones, 3, 0)

        self.btn_0.clicked.connect(self.numero)
        self.btn_1.clicked.connect(self.numero)
        self.btn_2.clicked.connect(self.numero)
        self.btn_3.clicked.connect(self.numero)
        self.btn_4.clicked.connect(self.numero)
        self.btn_5.clicked.connect(self.numero)
        self.btn_6.clicked.connect(self.numero)
        self.btn_7.clicked.connect(self.numero)
        self.btn_8.clicked.connect(self.numero)
        self.btn_9.clicked.connect(self.numero)
        self.btn_suma.clicked.connect(self.numero)
        self.btn_resta.clicked.connect(self.numero)
        self.btn_multiplicacion.clicked.connect(self.numero)
        self.btn_division.clicked.connect(self.numero)
        self.btn_punto.clicked.connect(self.numero)

        self.btn_igual.clicked.connect(self.resultado)

        self.btn_borrar.clicked.connect(self.borrar)

    def numero(self):
        sender = self.sender()
        texto = self.lbl_operaciones.text()
        self.lbl_operaciones.setText(texto+sender.text())

    def resultado(self):
        resultado = eval(self.lbl_operaciones.text())
        self.lbl_resultado.setText(str(resultado))
        self.txt_edit_resultado.append(self.lbl_resultado.text())
        self.historial()

    def historial(self):
        self.txt_edit.append(f"{self.lbl_operaciones.text()} = {self.lbl_resultado.text()}")

    def borrar(self):
        self.lbl_operaciones.setText(self.lbl_operaciones.text()[:-1])

    def keyPressEvent(self, event):
        print(event.key())
        if event.text().isnumeric():
            self.operacion(event.text())
        elif event.key() in [43,45,42,47,61,46,40,41]:
            self.operacion(event.text())
        elif event.key() == 16777220:
            self.resultado()
        elif event.key() == 16777219:
            self.borrar()

    def operacion(self, letra):
        texto = self.lbl_operaciones.text()
        self.lbl_operaciones.setText(texto + letra)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())