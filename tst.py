import sys
import time
from parser import *
from PyQt5 import QtWidgets , uic,QtGui
from lexy import build_lexer

from parsy import run_parser
def newscript():
    sc.close()
    sc2.show()
def openFile():
    global filename
    filename=QtWidgets.QFileDialog.getOpenFileName(None, "Select a file...","./", filter="*.t++")
    try:
        if filename != "":
            f = open(filename[0], "r")
            sc2.txt.setPlainText(f.read())
    except:
        print("none")
def saveFile():
    if filename != "":
        f=open(filename[0], "w")
        f.write(sc2.txt.toPlainText())
        f.close()
        sc2.statusbar.showMessage(filename[0] + "has been saved hh" + time.strftime("%d/%m/%y %H:%M"),1000)
def runFile():
    sys.stdout = open("output.txt", "w")
    f = open(filename[0], "r")
    run_parser(f.read())
    sys.stdout.close()
    output=open("output.txt", "r")
    sc3.txt.setPlainText(str(output.read()))
    sc3.show()
def debugFile():
    sys.stdout = open("output.txt", "w")
    f = open(filename[0], "r")
    build_lexer(f.read())
    sys.stdout.close()
    output=open("output.txt", "r")
    sc3.txt.setPlainText(str(output.read()))
    sc3.show()
def impscript():
    sc.close()
    sc2.show()
    openFile()
  
App=QtWidgets.QApplication(sys.argv)
sc3=uic.loadUi("output.ui")
sc2=uic.loadUi("editor.ui")
sc=uic.loadUi("untitled.ui")
sc.show()
sc.new_2.clicked.connect(newscript)
sc.imp_2.clicked.connect(impscript)
sc2.actionnewFile.triggered.connect(openFile)
sc2.actionSave.triggered.connect(saveFile)
sc2.actionrun.triggered.connect(runFile)
sc2.actiondebug.triggered.connect(debugFile)
App.exec_()
App.exit()
