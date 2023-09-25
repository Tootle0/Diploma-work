
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_encryption_window(object):
    def setupUi(self, encryption_window):
        encryption_window.setObjectName("encryption_window")
        encryption_window.resize(470, 430)
        encryption_window.setStyleSheet(
            "background-color: rgb(183, 229, 176);")
        self.centralwidget = QtWidgets.QWidget(encryption_window)
        self.centralwidget.setObjectName("centralwidget")
        self.encryption = QtWidgets.QPushButton(self.centralwidget)
        self.encryption.setGeometry(QtCore.QRect(190, 190, 75, 23))
        self.encryption.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 0, 0);")
        self.encryption.setObjectName("encryption")
        self.encryption_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.encryption_field.setGeometry(QtCore.QRect(50, 100, 361, 71))
        self.encryption_field.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.encryption_field.setObjectName("encryption_field")
        self.sabelforInputfield = QtWidgets.QLabel(self.centralwidget)
        self.sabelforInputfield.setGeometry(QtCore.QRect(150, 240, 191, 20))
        self.sabelforInputfield.setObjectName("sabelforInputfield")
        self.encrypted_text = QtWidgets.QLabel(self.centralwidget)
        self.encrypted_text.setGeometry(QtCore.QRect(50, 80, 131, 16))
        self.encrypted_text.setObjectName("encrypted_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.output_encrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.output_encrypt.setGeometry(QtCore.QRect(80, 270, 301, 71))
        self.output_encrypt.setFrameShape(QtWidgets.QFrame.Box)
        self.output_encrypt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output_encrypt.setObjectName("output_encrypt")
        self.selectPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectPathButton.setGeometry(QtCore.QRect(50, 40, 75, 23))
        self.selectPathButton.setObjectName("selectPathButton")
        self.pathLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(130, 40, 291, 21))
        self.pathLabel.setText("")
        self.pathLabel.setObjectName("pathLabel")
        encryption_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(encryption_window)
        self.statusbar.setObjectName("statusbar")
        encryption_window.setStatusBar(self.statusbar)

        self.retranslateUi(encryption_window)
        QtCore.QMetaObject.connectSlotsByName(encryption_window)

    def retranslateUi(self, encryption_window):
        _translate = QtCore.QCoreApplication.translate
        encryption_window.setWindowTitle(_translate(
            "encryption_window", "Encryption Tool(PET)"))
        self.encryption.setText(_translate("encryption_window", "Encryption"))
        self.sabelforInputfield.setText(_translate(
            "encryption_window", "Write down your message to Encrypt"))
        self.encrypted_text.setText(_translate(
            "encryption_window", "Encrypted Text"))
        self.label.setText(_translate("encryption_window", "Encryption"))
        self.selectPathButton.setText(
            _translate("encryption_window", "Select path"))
