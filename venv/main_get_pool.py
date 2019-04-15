import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import mainView  # Это наш конвертированный файл дизайна
from aceEditor import *
from  SectionSpliter import *



class ExampleApp(QtWidgets.QMainWindow, mainView.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.get_button.clicked.connect(self.getPool)
        self.set_button.clicked.connect(self.setItemExpression)
        self.urlInput.setText("334546")
        test = self.urlInput
        print(self.urlInput.text())
        AceWebView.AddAceToLayout(self, self.gridLayout_2)
        ## Вызов сплиттера
        ##slitedPool = SectionSplitter()
        self.copyButton.clicked.connect(self.testShow)
    def testShow(self):
        slitedPool = SectionSplitter(self.pool_textarea.toPlainText())
        slitedPool.showAll()

    def getPool(self):
        if len(self.urlInput.text()) > 0:
            import getJson as planIOJson
            print(self.urlInput.text())

            try:
                planIOJson.Logic().GetJsonFromItem(self.pool_textarea, "6735ebd44e9850ab188356ffba5cbb7cad8aa756", self.urlInput.text())#"325864"


            except Exception:
                print("wrong link")
    def setItemExpression(self):
        if len(self.urlInput.text()) > 0:
            confirmDialog = QtWidgets.\
                QMessageBox.\
                question(self, "Set expression" + self.urlInput.text(), "Set value for item %s?" % (self.urlInput.text()),
                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if confirmDialog == QtWidgets.QMessageBox.Yes:
                import getJson as planIOJson
                print("Clicked yes")
                testedString = '<pre><code class="sql">%s</code></pre>' % (self.pool_textarea.toPlainText())
                planIOJson.Logic().PutJsonToItem(testedString, "6735ebd44e9850ab188356ffba5cbb7cad8aa756",
                                                 self.urlInput.text())  # 325864
            else:
                print("Canceled")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()