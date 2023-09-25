
from inspect import trace
from lib2to3.pytree import Base
from multiprocessing.sharedctypes import Value
import re
import rsa
import PyQt5.QtWidgets as qwidgets
# import QMainWindow, QApplication, QLabel, QTextEdit,QPushButton
from PyQt5 import uic
import sys
import traceback
import ast
# saving private and public keys in folder keys


def generate_keys(path):
    (pubKey, privKey) = rsa.newkeys(1024)  # making a 128 byte key
    with open(path + '/pubkey.pem', 'wb') as f:  # saving public key in folder
        f.write(pubKey.save_pkcs1('PEM'))

    with open(path + '/privkey.pem', 'wb') as f:  # saving private key in folder
        f.write(privKey.save_pkcs1('PEM'))

# loading keys from files that was created previously


def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

# encryption msg function


def encrypt(msg, key):
    return rsa.encrypt(msg.encode('utf-8'), key)  # encoding message with utf-8

# decryption msg function


def decrypt(ciphertext, key):
    return rsa.decrypt(ciphertext, key).decode('utf-8')


class encryption_window(qwidgets.QMainWindow):
    def __init__(self):
        super(encryption_window, self).__init__()
        # Load the ui file
        uic.loadUi("encryption_design.ui", self)
        self.spathbutton = self.findChild(
            qwidgets.QPushButton, "selectPathButton")
        self.encrbutton = self.findChild(qwidgets.QPushButton, "encryption")
        self.pathlabel = (qwidgets.QLabel)(
            self.findChild(qwidgets.QLabel, "pathLabel"))
        self.encrfield = self.findChild(
            qwidgets.QPlainTextEdit, "encryption_field")
        self.messagefield = self.findChild(
            qwidgets.QTextEdit, "output_encrypt")
        # Define widgets
        self.encrfield.setReadOnly(True)
        # assigning actions to button
        self.spathbutton.clicked.connect(self.handle_select_path)
        self.encrbutton.clicked.connect(self.handle_encryption)

    def handle_select_path(self):
        self.filepath = qwidgets.QFileDialog.getOpenFileName(
            self, 'Select folder')
        self.pathlabel.setText(self.filepath[0])
        self.pathlabel.adjustSize()

    def handle_encryption(self):
        try:
            with open(self.filepath[0], 'rb') as f:
                pubKey = rsa.PublicKey.load_pkcs1(f.read())
        except (AttributeError, OSError):
            qwidgets.QMessageBox.about(
                self, "Error", "File is not selected or the wrong file selected")
            return
        except ValueError as e:
            qwidgets.QMessageBox.about(
                self, "Error", "Invalid file selected")
            return
        if self.messagefield.toPlainText() == "":
            qwidgets.QMessageBox.about(
                self, "Error", "Message cannot be empty")
            return
        try:
            #print(type(encrypt(self.messagefield.toPlainText(), pubKey)))
            encrypted = (str)(encrypt(self.messagefield.toPlainText(), pubKey))

            self.encrfield.setPlainText(encrypted)
        except Exception as e:
            traceback.print_exc()
            qwidgets.QMessageBox.about(self, "Error", str(e))


class decryption_window(qwidgets.QMainWindow):
    def __init__(self):
        super(decryption_window, self).__init__()
        # Load the ui file
        uic.loadUi("decryption_design.ui", self)
        self.spathbutton = self.findChild(
            qwidgets.QPushButton, "selectPathButton2")
        self.decrbutton = self.findChild(qwidgets.QPushButton, "decryption")
        self.pathlabel = (qwidgets.QLabel)(
            self.findChild(qwidgets.QLabel, "pathLabel"))
        self.decrfield = self.findChild(
            qwidgets.QTextEdit, "output_decrypt")
        self.messagefield = self.findChild(
            qwidgets.QPlainTextEdit, "input_decrypt")
        # assigning actions to button
        self.spathbutton.clicked.connect(self.handle_select_path)
        self.decrbutton.clicked.connect(self.handle_decryption)

    def handle_select_path(self):
        self.filepath = qwidgets.QFileDialog.getOpenFileName(
            self, 'Select folder')
        self.pathlabel.setText(self.filepath[0])
        self.pathlabel.adjustSize()

    def handle_decryption(self):
        try:
            with open(self.filepath[0], 'rb') as f:
                privkey = rsa.PrivateKey.load_pkcs1(f.read())
        except (AttributeError, OSError):
            qwidgets.QMessageBox.about(
                self, "Error", "File is not selected or the wrong file selected")
            return
        except ValueError as e:
            qwidgets.QMessageBox.about(
                self, "Error", "Invalid file selected")
            return
        if self.messagefield.toPlainText() == "":
            qwidgets.QMessageBox.about(
                self, "Error", "Message cannot be empty")
            return
        try:
            decrypted = (str)(
                decrypt(ast.literal_eval(self.messagefield.toPlainText()), privkey))

            self.decrfield.setPlainText(decrypted)
        except Exception as e:
            traceback.print_exc()
            qwidgets.QMessageBox.about(self, "Error", str(e))


class main_window(qwidgets.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        # Load the ui file
        uic.loadUi("welcome_screen.ui", self)
        # Define widgets
        self.gkbutton = self.findChild(
            qwidgets.QPushButton, "generate_keys_btn")
        self.edbutton = self.findChild(qwidgets.QPushButton, "encryption_btn")
        self.ddbuton = self.findChild(qwidgets.QPushButton, "decryption_btn")
        # assigning actions to buttons
        self.encrwindow = encryption_window()
        self.decrwindow = decryption_window()
        self.gkbutton.clicked.connect(self.handle_keys)
        self.edbutton.clicked.connect(self.encrwindow.show)
        self.ddbuton.clicked.connect(self.decrwindow.show)

        # show the app
        self.show()

    def handle_keys(self):
        try:
            dirpath = qwidgets.QFileDialog.getExistingDirectory(
                self, "Select folder")
            generate_keys(dirpath)
        except OSError:
            pass


# initialize the app
app = qwidgets.QApplication(sys.argv)
UIWindow = main_window()
app.exec_()
