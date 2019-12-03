import sys, os
from untitled import Ui_Form
from PyQt5.QtWidgets import *
import you_get
from PyQt5.QtCore import *



def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('视频下载器')
        # 设置信号、槽
        self.ui.btn2.clicked.connect(self.getUrl)
        self.ui.btn1.clicked.connect(self.dir)
        self.statusBar().showMessage('版本：v0.1 -- 作者邮箱：admin@tyty.xyz')


    def dir(self):
        directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        print(directory)
        self.ui.line2.setText(directory)

    def getUrl(self):
        url = self.ui.line1.text()
        path = self.ui.line2.text()
        if not path:
            path = os.getcwd()
        print(path)
        if not url:
            dialog = QDialog()
            # 创建按钮到新创建的dialog对象中
            text = QLabel("没有输入地址哦", dialog)
            # 移动按钮，设置dialog的标题
            text.move(50, 50)
            dialog.setWindowTitle("小提示")
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()
        else:
            try:
                info = QMessageBox()
                info.setText("正在下载中。。。")
                info.setWindowTitle("Information")
                info.setStandardButtons(QMessageBox.Ok)
                info.button(QMessageBox.Ok).animateClick(3 * 1000)
                info.exec_()
                download(url,path)
            except Exception as e:
                print("error")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
