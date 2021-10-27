#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
将几个组件放在一起使用
在上面的例子中，我们创建了菜单栏、工具栏和状态栏。下面我们将创建一个中心组件。

事例代码创建了一个带有菜单栏、工具栏和状态栏的经典GUI应用骨架。

textEdit = QTextEdit()
self.setCentralWidget(textEdit)

在这里我们创建了一个文本编辑框组件。我们将它设置成QMainWindow的中心组件。中心组件占据了所有剩下的空间。
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())