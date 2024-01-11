# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.browser = QWebEngineView()
#         self.browser.setUrl(QUrl('http://bing.com'))
#         self.setCentralWidget(self.browser)
#         self.showMaximized()

#         # navbar
#         navbar = QToolBar()
#         self.addToolBar(navbar)

#         back_btn = QAction('Back', self)
#         back_btn.triggered.connect(self.browser.back)
#         navbar.addAction(back_btn)

#         forward_btn = QAction('Forward', self)
#         forward_btn.triggered.connect(self.browser.forward)
#         navbar.addAction(forward_btn)

#         reload_btn = QAction('Reload', self)
#         reload_btn.triggered.connect(self.browser.reload)
#         navbar.addAction(reload_btn)

#         home_btn = QAction('Home', self)
#         home_btn.triggered.connect(self.navigate_home)
#         navbar.addAction(home_btn)

#         self.url_bar = QLineEdit()
#         self.url_bar.returnPressed.connect(self.navigate_to_url)
#         navbar.addWidget(self.url_bar)

#         self.browser.urlChanged.connect(self.update_url)

#     def navigate_home(self):
#         self.browser.setUrl(QUrl('http://bing.com'))

#     def navigate_to_url(self):
#         url = self.url_bar.text()
#         self.browser.setUrl(QUrl(url))

#     def update_url(self, q):
#         self.url_bar.setText(q.toString())


# app = QApplication(sys.argv)
# QApplication.setApplicationName('My Cool Browser')
# window = MainWindow()
# app.exec_()

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebPage(QWebEnginePage):
    def __init__(self):
        super(WebPage, self).__init__()

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        print("Console Message:", level, message, lineNumber, sourceID)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setPage(WebPage())
        self.browser.setUrl(QUrl('http://bing.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        dev_mode_btn = QAction('Developer Mode', self)
        dev_mode_btn.setCheckable(True)
        dev_mode_btn.triggered.connect(self.toggle_developer_mode)
        navbar.addAction(dev_mode_btn)

        self.dev_mode = False

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://bing.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def toggle_developer_mode(self, enabled):
        self.dev_mode = enabled
        if enabled:
            # Enable developer mode - inject JavaScript code to manipulate the DOM
            self.browser.page().runJavaScript(self.get_inject_script())

    def get_inject_script(self):
        # This is just a simple example, you may need to modify it based on your needs
        return """
            // Example: Change the background color of all paragraphs to yellow
            var paragraphs = document.getElementsByTagName('p');
            for (var i = 0; i < paragraphs.length; i++) {
                paragraphs[i].style.backgroundColor = 'yellow';
            }
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('My Cool Browser')
    window = MainWindow()
    app.exec_()
