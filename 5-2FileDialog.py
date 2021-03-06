#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
示例中显示了一个菜单栏，中间设置了一个文本编辑框组件，和一个状态栏。点击菜单项会显示QtGui.QFileDialog（文件选择框）对话框，
用于选择一个文件。文件的内容会被读取并在文本编辑框组件中显示。


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
示例基于QMainWindow组件，因为我们中心需要设置一个文本编辑框组件。

fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
弹出文件选择框。第一个字符串参数是getOpenFileName()方法的标题。第二个字符串参数指定了对话框的工作目录。
默认的，文件过滤器设置成All files (*)。


if fname[0]:
    f = open(fname[0], 'r')

    with f:
        data = f.read()
        self.textEdit.setText(data)
选中文件后，读出文件的内容，并设置成文本编辑框组件的显示文本、

"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog,
                             QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
