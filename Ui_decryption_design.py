
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_decryption_window(object):
    def setupUi(self, decryption_window):
        decryption_window.setObjectName("decryption_window")
        decryption_window.resize(470, 430)
        decryption_window.setStyleSheet(
            "background-color: rgb(183, 229, 176);")
        self.centralwidget = QtWidgets.QWidget(decryption_window)
        self.centralwidget.setObjectName("centralwidget")
        self.decryption = QtWidgets.QPushButton(self.centralwidget)
        self.decryption.setGeometry(QtCore.QRect(190, 190, 75, 23))
        self.decryption.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 0, 0);")
        self.decryption.setObjectName("decryption")
        self.output_decrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.output_decrypt.setGeometry(QtCore.QRect(80, 240, 301, 71))
        self.output_decrypt.setFrameShape(QtWidgets.QFrame.Box)
        self.output_decrypt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output_decrypt.setObjectName("output_decrypt")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(80, 220, 111, 16))
        self.output_label.setObjectName("output_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.pathLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(130, 40, 291, 21))
        self.pathLabel.setText("")
        self.pathLabel.setObjectName("pathLabel")
        self.encrypted_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.encrypted_text_2.setGeometry(QtCore.QRect(50, 80, 131, 16))
        self.encrypted_text_2.setObjectName("encrypted_text_2")
        self.selectPathButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.selectPathButton2.setGeometry(QtCore.QRect(50, 40, 75, 23))
        self.selectPathButton2.setObjectName("selectPathButton2")
        self.input_decrypt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_decrypt.setGeometry(QtCore.QRect(50, 100, 361, 71))
        self.input_decrypt.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_decrypt.setObjectName("input_decrypt")
        decryption_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(decryption_window)
        QtCore.QMetaObject.connectSlotsByName(decryption_window)

    def retranslateUi(self, decryption_window):
        _translate = QtCore.QCoreApplication.translate
        decryption_window.setWindowTitle(
            _translate("decryption_window", "Decryption"))
        self.decryption.setText(_translate("decryption_window", "Decryption"))
        self.output_label.setText(_translate(
            "decryption_window", "Output/Plain Text"))
        self.label.setText(_translate("decryption_window", "Decryption"))
        self.encrypted_text_2.setText(_translate(
            "decryption_window", "Encrypted Text"))
        self.selectPathButton2.setText(
            _translate("decryption_window", "Select path"))
