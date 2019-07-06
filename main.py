import os
import sys
from PyQt5 import QtWidgets
# from demo import Ui_Dialog

# class main(QtWidgets.QWidget,Ui_Dialog):
#     def __init__(self):
#         super(main,self).__init__()
#         self.setupUi(self)
#
#     #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
#     def btn_click(self):
#         self.textEdit.setText("你点击了按钮")

from index import Ui_Form


class Search(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Search, self).__init__()
        self.setupUi(self)
        self.show_all()

    def search(self):
        res = []
        self.listWidget_2.clear()
        text = self.lineEdit.text()
        for item in self.data:
            if text in item:
                res.append(item)
        if len(res) != 0:
            self.listWidget_2.addItems(res)
        else:
            self.listWidget_2.addItem('没有找到结果')

    def show_all(self):
        self.data = []
        for _, _, files in os.walk(os.getcwd()+'\\tab'):
            for file in files:
                self.data.append(file)
        # self.data = ['1','1','3','4','5']
        self.listWidget.addItems(self.data)

    # def click(self):


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = Search()
    my_pyqt_form.show()
    sys.exit(app.exec_())
