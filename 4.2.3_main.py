# ch 4.2.3 main.py

import sys
# 터미널에 pip install PyQt5 입력하셨나요?
# 대소문자에 주의
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)
# QMessageBox : 메시지박스 위젯

from PyQt5.QtGui import QIcon #icon을 추가하기 위한 라이브러리 

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def activateMessage(self): #버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        QMessageBox.information(self, "information", "Button cliked!")

    def initUI(self):
        self.btn1=QPushButton('Message', self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage) #버튼 클릭 시 핸들러 함수 연결

        vbox=QVBoxLayout()        #수직 레이아웃 위젯 생성
        vbox.addStretch(1)        #빈공간
        vbox.addWidget(self.btn1) #버튼 위치
        vbox.addStretch(1)        #빈공간

        self.setLayout(vbox)      #빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))   #윈도 아이콘 추가
        self.resize(256, 256)
        self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    # sys.argv가 궁금하다면? https://wikidocs.net/194003
    view = Calculator()
    sys.exit(app.exec_())