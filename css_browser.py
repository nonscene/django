import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
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

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://daily.dev'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow()
app.exec_()

# import sys
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QPushButton, QLabel, QLineEdit
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from selenium import webdriver

# class DeveloperBrowser(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.browser = QWebEngineView()
#         self.browser.setUrl(QUrl("https://www.bing.com"))

#         self.setup_ui()
    
#     def setup_ui(self):

#         self.setWindowTitle("Developer Browser")
#         self.setGeometry(100, 100, 800, 600)

#         # Layout Making from Here

#         layout = QVBoxLayout()

#         # Button for use tool

#         position_button = QPushButton("Enable Position Change")
#         size_button = QPushButton("Enable Size Change")
#         color_button = QPushButton("Enable Color Change")

#         # button to function

#         position_button.clicked.connect(self.enable_position_change)
#         size_button.clicked.connect(self.enable_size_change)
#         color_button.clicked.connect(self.enable_color_change)


#         # layout to button

#         layout.addWidget(position_button)
#         layout.addWidget(size_button)
#         layout.addWidget(color_button)

#         # making frame to hold browser
#         frame = QFrame()
#         frame.setLayout(layout)

#         # make an main layout
#         main_layout = QVBoxLayout()
#         main_layout.addWidget(frame)
#         main_layout.addWidget(self.browser)

#         # set central widget and apply the layout

#         central_widget = QFrame()
#         central_widget.setLayout(main_layout)
#         self.setCentralWidget(central_widget)

#     def enable_position_change(self):
#         # Implement logic for position change here
#         print("Position Change Enabled")

#     def enable_size_change(self):
#         # Implement logic for size change here
#         print("Size Change Enabled")

#     def enable_color_change(self):
#         # Implement logic for color change here
#         print("Color Change Enabled")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = DeveloperBrowser()
#     window.show()
#     sys.exit(app.exec_())