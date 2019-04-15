from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtCore import QUrl
import os
# testing webView
# self.textBrowser = QtWidgets.QTextBrowser(self.aceTab)
# self.textBrowser.setObjectName("textBrowser")
# self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)

#self.webView = QWebView()
#self.webView.setHtml(testText)
#self.gridLayout_2.addWidget(self.webView, 0, 0, 1, 1)






# end of testing webView
class AceWebView:
    def AddAceToLayout(self, layout):
        testText = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>ACE in Action</title>
<style type="text/css" media="screen">
    #editor {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
    }
</style>

</head>
<body>

<div class="container-code">
    <div id="editor">some test sstring</div>
</div>
<script src="Lib/site-packages/ace/ace.js" type="text/javascript" charset="utf-8"></script>
<script>
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/ambiance");
    editor.getSession().setMode("ace/mode/csharp");
</script>
</body>
</html>
           """
        #print(testText)
        self.someTest = QWebEngineView()
        layout.addWidget(self.someTest, 0, 0, 1, 1)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ace_page.html"))
        self.someTest.load(QUrl.fromLocalFile(file_path))
        #self.someTest.setHtml(testText)
       
        #self.someTest.QWebEnginePage.triggerAction(9)




#test.triggerPageAction(9)
#<script src="http://d1n0x3qji82z53.cloudfront.net/src-min-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>