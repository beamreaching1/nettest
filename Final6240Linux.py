# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:41:52 2020

@author: Cayden
"""

# Network and Support Libraries
import subprocess
import sys
from hurry.filesize import size
from hurry.filesize import alternative
import speedtest
import platform
import re

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (FigureCanvas)
else:
    from matplotlib.backends.backend_qt4agg import (FigureCanvas)
from matplotlib.figure import Figure

from ui import Final

from PyQt5 import QtCore, QtGui, QtWidgets

_translate = QtCore.QCoreApplication.translate


class Window(QtWidgets.QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Final.Ui_Dialog()
        self.ui.setupUi(self)
        self.static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ui.gridLayout_4.addWidget(self.static_canvas)
        self._static_ax = self.static_canvas.figure.subplots()
        self.setWindowTitle("Net GUI Tool")
        self.setWindowIcon(QtGui.QIcon('ui/images/ping-pong-logo.jpg'))
        self.home()

    def home(self):
        # btn = QtWidgets.QPushButton("Quit", self)
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.ui.beginTest.clicked.connect(self.test)

        self.show()

    def pingt(self, target):

        if target == "":
            target = "8.8.8.8"

        current_os = platform.system().lower()

        arg = "-c"

        try:
            plist = []
            output = subprocess.check_output(["ping", arg, "16", target])
            temp = re.findall("time=\w+", output.decode("utf-8"))

            for t in temp:
                plist.append(int(t[5:-2]))


            return plist
        except:
            output = "Invalid IP or connection error"
            self.ui.outputBox.setPlainText(_translate("Dialog", output))
            app.processEvents()

            return []

    def sptest(self, st):
        servers = []
        st.get_servers(servers)
        st.get_best_server()
        st.download(threads=8)
        self.ui.outputBox.appendPlainText(_translate("Dialog", "\nCalculating Upload Speed"))
        app.processEvents()
        st.upload(threads=8)

    def test(self):
        target = self.ui.target.text()

        self.ui.outputBox.setPlainText(_translate("Dialog", "Calculating Ping"))
        app.processEvents()

        results = self.pingt(target)

        self.ui.outputBox.appendPlainText(_translate("Dialog", "\nCalculating Download Speed"))
        app.processEvents()

        st = speedtest.Speedtest()

        self.sptest(st)

        output = "Download Speed: " + size(st.results.download, system=alternative) \
                 + "\n\nUpload Speed: " + size(st.results.upload, system=alternative)

        self.ui.outputBox.setPlainText(_translate("Dialog", output))
        app.processEvents()

        jsum = 0
        trail = results[0]
        for i in results[1:]:
            jsum = jsum + abs(trail - i)
            trail = i


        jitter = jsum / (len(results) - 1)

        output = "\nJitter (Connection Stability): " + str(round(jitter, 2)) + "ms" + "\n\nPing: " \
                 + str(round(st.results.ping, 2)) + "ms"

        self.ui.outputBox.appendPlainText(_translate("Dialog", output))
        app.processEvents()


        self._static_ax.clear()
        self._static_ax.plot(range(len(results)), results, ".")
        self._static_ax.figure.canvas.draw()

def main():
    global app
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


main()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Final.Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.setWindowTitle("Net GUI Tool")
#     Dialog.show()
#     sys.exit(app.exec_())


#
#
# print(output.decode("utf-8"))
