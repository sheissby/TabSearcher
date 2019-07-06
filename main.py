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

    def search(self):
        text = self.lineEdit.text()

    def show_all(self):
        self.tableView.


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = Search()
    my_pyqt_form.show()
    sys.exit(app.exec_())