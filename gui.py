# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_about.u.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1239, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pageStackWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.pageStackWidget.setObjectName("pageStackWidget")
        self.redditPage = QtWidgets.QWidget()
        self.redditPage.setObjectName("redditPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.redditPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.photo = QtWidgets.QLabel(self.redditPage)
        self.photo.setEnabled(True)
        self.photo.setScaledContents(False)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.gridLayout_2.addWidget(self.photo, 0, 0, 1, 4)
        self.searchLabel = QtWidgets.QLabel(self.redditPage)
        self.searchLabel.setObjectName("searchLabel")
        self.gridLayout_2.addWidget(self.searchLabel, 1, 1, 1, 1)
        self.searchTextEdit = QtWidgets.QTextEdit(self.redditPage)
        self.searchTextEdit.setMaximumSize(QtCore.QSize(500, 21))
        self.searchTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchTextEdit.setAcceptRichText(False)
        self.searchTextEdit.setObjectName("searchTextEdit")
        self.gridLayout_2.addWidget(self.searchTextEdit, 1, 3, 1, 1)
        self.subredditLabel = QtWidgets.QLabel(self.redditPage)
        self.subredditLabel.setObjectName("subredditLabel")
        self.gridLayout_2.addWidget(self.subredditLabel, 2, 1, 1, 1)
        self.subredditComboBox = QtWidgets.QComboBox(self.redditPage)
        self.subredditComboBox.setEditable(True)
        self.subredditComboBox.setObjectName("subredditComboBox")
        self.subredditComboBox.addItem("")
        self.subredditComboBox.addItem("")
        self.gridLayout_2.addWidget(self.subredditComboBox, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(784, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.categoryLabel = QtWidgets.QLabel(self.redditPage)
        self.categoryLabel.setObjectName("categoryLabel")
        self.gridLayout_2.addWidget(self.categoryLabel, 3, 1, 1, 1)
        self.categoryComboBox = QtWidgets.QComboBox(self.redditPage)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.gridLayout_2.addWidget(self.categoryComboBox, 3, 3, 1, 1)
        self.limitLabel = QtWidgets.QLabel(self.redditPage)
        self.limitLabel.setObjectName("limitLabel")
        self.gridLayout_2.addWidget(self.limitLabel, 4, 1, 1, 1)
        self.limitComboBox = QtWidgets.QComboBox(self.redditPage)
        self.limitComboBox.setEditable(True)
        self.limitComboBox.setObjectName("limitComboBox")
        self.limitComboBox.addItem("")
        self.limitComboBox.addItem("")
        self.limitComboBox.addItem("")
        self.gridLayout_2.addWidget(self.limitComboBox, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.redditPage)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 1, 1, 1)
        self.darkModeCheckBox = QtWidgets.QCheckBox(self.redditPage)
        self.darkModeCheckBox.setText("")
        self.darkModeCheckBox.setObjectName("darkModeCheckBox")
        self.gridLayout_2.addWidget(self.darkModeCheckBox, 5, 3, 1, 1)
        self.nextWallButton = QtWidgets.QPushButton(self.redditPage)
        self.nextWallButton.setObjectName("nextWallButton")
        self.gridLayout_2.addWidget(self.nextWallButton, 6, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.redditPage)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_2.addWidget(self.saveButton, 6, 2, 1, 1)
        self.wallpaperButton = QtWidgets.QPushButton(self.redditPage)
        self.wallpaperButton.setObjectName("wallpaperButton")
        self.gridLayout_2.addWidget(self.wallpaperButton, 6, 3, 1, 1)
        self.pageStackWidget.addWidget(self.redditPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.aboutPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.aboutPage)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.pageStackWidget.addWidget(self.aboutPage)
        self.gridLayout.addWidget(self.pageStackWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1239, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuNavigate = QtWidgets.QMenu(self.menubar)
        self.menuNavigate.setObjectName("menuNavigate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.helpAction = QtWidgets.QAction(MainWindow)
        self.helpAction.setObjectName("helpAction")
        self.redditAction = QtWidgets.QAction(MainWindow)
        self.redditAction.setCheckable(False)
        self.redditAction.setObjectName("redditAction")
        self.redditPageAction = QtWidgets.QAction(MainWindow)
        self.redditPageAction.setObjectName("redditPageAction")
        self.pageRedditAction = QtWidgets.QAction(MainWindow)
        self.pageRedditAction.setObjectName("pageRedditAction")
        self.menuHelp.addAction(self.aboutAction)
        self.menuHelp.addAction(self.helpAction)
        self.menuNavigate.addAction(self.pageRedditAction)
        self.menubar.addAction(self.menuNavigate.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.pageStackWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.photo.setText(_translate("MainWindow", "Set a random wallpaper from reddit!"))
        self.searchLabel.setText(_translate("MainWindow", "Search:"))
        self.subredditLabel.setText(_translate("MainWindow", "Subreddit : "))
        self.subredditComboBox.setItemText(0, _translate("MainWindow", "wallpapers"))
        self.subredditComboBox.setItemText(1, _translate("MainWindow", "amoledbackgrounds"))
        self.categoryLabel.setText(_translate("MainWindow", "Category :"))
        self.categoryComboBox.setItemText(0, _translate("MainWindow", "hot"))
        self.categoryComboBox.setItemText(1, _translate("MainWindow", "rising"))
        self.categoryComboBox.setItemText(2, _translate("MainWindow", "new"))
        self.categoryComboBox.setItemText(3, _translate("MainWindow", "top"))
        self.categoryComboBox.setItemText(4, _translate("MainWindow", "controversial"))
        self.limitLabel.setText(_translate("MainWindow", "Limit :"))
        self.limitComboBox.setItemText(0, _translate("MainWindow", "10"))
        self.limitComboBox.setItemText(1, _translate("MainWindow", "25"))
        self.limitComboBox.setItemText(2, _translate("MainWindow", "50"))
        self.label.setText(_translate("MainWindow", "Dark Mode :"))
        self.nextWallButton.setText(_translate("MainWindow", "Next wallpaper"))
        self.saveButton.setText(_translate("MainWindow", "Save to Pictures"))
        self.wallpaperButton.setText(_translate("MainWindow", "Set as wallpaper"))
        self.label_2.setText(_translate("MainWindow", "KustomPyper - Get amazing wallpapers for your desktop. <br> Created by Kriticalflare (<a href=\"https://github.com/kriticalflare\">Github</a>) </br>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuNavigate.setTitle(_translate("MainWindow", "Navigate"))
        self.aboutAction.setText(_translate("MainWindow", "About"))
        self.helpAction.setText(_translate("MainWindow", "Help"))
        self.redditAction.setText(_translate("MainWindow", "Reddit Walls"))
        self.redditPageAction.setText(_translate("MainWindow", "Reddit"))
        self.pageRedditAction.setText(_translate("MainWindow", "Reddit Walls"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
