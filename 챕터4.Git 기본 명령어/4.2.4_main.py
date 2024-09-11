# ch 4.2.3 main.py

import sys
# 터미널에 pip install PyQt5 입력하셨나요?
# 대소문자에 주의
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit)
# QPlainTextEdit 추가

from PyQt5.QtGui import QIcon #icon을 추가하기 위한 라이브러리 

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit() #텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)  #텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.btn1=QPushButton('Message', self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage) #버튼 클릭 시 핸들러 함수 연결

        vbox=QVBoxLayout()        #수직 레이아웃 위젯 생성
        vbox.addStretch(1)        #빈공간
        vbox.addWidget(self.btn1) #버튼 위치
        vbox.addWidget(self.te1)  #수직 레이아웃에 텍스트 에디트 위젯 추가
        vbox.addStretch(1)        #빈공간

        self.setLayout(vbox)      #빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))   #윈도 아이콘 추가
        self.resize(256, 256)
        self.show()

    def activateMessage(self): # 핸들러 함수 수정 : 메시지가 텍스트 에디트에 출력되도록
        #QMessageBox.information(self, "information", "Button cliked!")
        self.te1.appendPlainText("Button clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    # sys.argv가 궁금하다면? https://wikidocs.net/194003
    view = Calculator()
    sys.exit(app.exec_())