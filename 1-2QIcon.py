#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
ZetCode PyQt5 tutorial

三个方法都继承自QWidgets类。setGeometry()做了两件事：将窗口在屏幕上显示，并设置了它的尺寸。

setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
事实上，这是将resize()和move()方法融合在一个方法内。

为了做好这个例子，我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(500, 400, 500, 320)
        self.setWindowTitle('虎鲸-上市公司公告下载工具')
        self.setWindowIcon(QIcon('256.ico'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
