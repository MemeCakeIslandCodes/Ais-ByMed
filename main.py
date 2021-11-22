#getting all our packages

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#creating our browser display

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()

        #adding the youtube url to make it a youtube browser
        self.browser.setUrl(QUrl('https://www.youtube.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # creating functions used in our buttons
        def navigate_home(self):
            self.browser.setUrl(QUrl('https://www.youtube.com'))

        def move_to_url(self):
            url = self.url_bar.text()
            self.browser.setUrl(QUrl(url))

        def new_url(self, m):
            self.url_bar.setText(m.toString())

            #navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #adding a button to return to previous page
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        #adding a button to go to next page you just left
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        #create a button to refresh the screen
        refresh_button = QAction('Refresh', self)
        refresh_button.triggered.connect(self.browser.refresh)
        navbar.addAction(refresh_button)


        #home button to return to original youtube.com
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        #allowing people to type urls
        self.url_bar = QLineEdit()
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.move_to_url)

        self.browser.urlChanged.connect(self.new_url)


        app = QApplication(sys.argv)
        QApplication.setApplicationName('Aisé By Med')
        window = MainWindow()
        app.exec_()