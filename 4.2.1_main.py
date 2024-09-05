# ch 4.2.1 main.py

import sys
# 터미널에 pip install PyQt5 입력하셨나요?
# 대소문자에 주의
from PyQt5.QtWidgets import QApplication, QWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.resize(256, 256)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    # sys.argv가 궁금하다면? https://wikidocs.net/194003
    view = Calculator()
    sys.exit(app.exec_())