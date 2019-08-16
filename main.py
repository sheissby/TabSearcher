import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from index import Ui_Form
from PyQt5.QtCore import *


class Search(QtWidgets.QWidget, Ui_Form):
    filelist = []
    res = []
    res_display = []
    detail_display = []

    def __init__(self):
        super(Search, self).__init__()
        self.setupUi(self)
        self.show_all()

    def search(self):
        self.res.clear()
        res_display = []
        self.listWidget.clear()
        text = self.lineEdit.text().strip()
        if text:
            for item in self.filelist:
                tmp = {}
                if text in item['filename']:
                    tmp['filename'] = item['filename']
                    tmp['filepath'] = item['filepath']
                    self.res.append(tmp)
                    res_display.append(item['filename'])
            if len(self.res) == len(res_display) and len(self.res) != 0:
                self.listWidget.addItems(res_display)
            elif len(self.res) == len(res_display) == 0:
                self.listWidget.addItem('没有找到结果')
            else:
                print(self.res)
                print(res_display)
                print('something wrong')
        else:
            self.filelist.clear()
            self.res.clear()
            self.lineEdit.clear()
            self.listWidget.clear()
            self.show_all()

    def show_all(self):
        display = []
        for root, _, files in os.walk(os.getcwd()+'\\tab\\文字谱'):
            for file in files:
                if file.split('.')[-1].lower() in ('txt'):
                    filedic = {}
                    fullfilepath = os.path.join(root, file)
                    filename = file
                    filedic['filename'] = filename.split('.')[0]
                    filedic['filepath'] = fullfilepath
                    self.filelist.append(filedic)
                    display.append(filename.split('.')[0])
        self.listWidget.addItems(display)

    def show_detail(self, item):
        self.detail_display.clear()
        self.textEdit.clear()
        text = item.text()
        if self.res:
            for i in self.res:
                if text == i['filename']:
                    try:
                        self.filepath = i['filepath']
                        with open(self.filepath, encoding='utf-8') as f:
                            content = f.read()
                        self.textEdit.setPlainText(content)
                        break
                    except Exception as e:
                        print(e)
        else:
            for i in self.filelist:
                if text == i['filename']:
                    try:
                        self.filepath = i['filepath']
                        with open(self.filepath, encoding='utf-8') as f:
                            content = f.read()
                        self.textEdit.setPlainText(content)
                        self.textEdit.toPlainText()
                        break
                    except Exception as e:
                        print(e)

    def save(self):
        print('save')
        content = self.textEdit.toPlainText()
        # print(content)
        # content = self.textEdit.toPlainText()
        # with open(self.filepath['filepath'], 'w', encoding='utf-8') as f:
        #     f.write(content)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = Search()
    my_pyqt_form.show()
    sys.exit(app.exec_())
