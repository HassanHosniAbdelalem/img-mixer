# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 617)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(355, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img1_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img1_label.sizePolicy().hasHeightForWidth())
        self.img1_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.img1_label.setFont(font)
        self.img1_label.setObjectName("img1_label")
        self.verticalLayout_2.addWidget(self.img1_label)
        self.img1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img1.sizePolicy().hasHeightForWidth())
        self.img1.setSizePolicy(sizePolicy)
        self.img1.setText("")
        self.img1.setPixmap(QtGui.QPixmap("images/No_Image_Available.jpg"))
        self.img1.setScaledContents(True)
        self.img1.setObjectName("img1")
        self.verticalLayout_2.addWidget(self.img1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.img1_display_selector = QtWidgets.QComboBox(self.centralwidget)
        self.img1_display_selector.setObjectName("img1_display_selector")
        self.verticalLayout.addWidget(self.img1_display_selector)
        self.img1_component_display = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img1_component_display.sizePolicy().hasHeightForWidth())
        self.img1_component_display.setSizePolicy(sizePolicy)
        self.img1_component_display.setText("")
        self.img1_component_display.setPixmap(QtGui.QPixmap("images/No_Image_Available.jpg"))
        self.img1_component_display.setScaledContents(True)
        self.img1_component_display.setObjectName("img1_component_display")
        self.verticalLayout.addWidget(self.img1_component_display)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img2_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img2_label.sizePolicy().hasHeightForWidth())
        self.img2_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.img2_label.setFont(font)
        self.img2_label.setObjectName("img2_label")
        self.verticalLayout_3.addWidget(self.img2_label)
        self.img2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img2.sizePolicy().hasHeightForWidth())
        self.img2.setSizePolicy(sizePolicy)
        self.img2.setText("")
        self.img2.setPixmap(QtGui.QPixmap("images/No_Image_Available.jpg"))
        self.img2.setScaledContents(True)
        self.img2.setObjectName("img2")
        self.verticalLayout_3.addWidget(self.img2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.img2_display_selector = QtWidgets.QComboBox(self.centralwidget)
        self.img2_display_selector.setObjectName("img2_display_selector")
        self.verticalLayout_4.addWidget(self.img2_display_selector)
        self.img2_component_display = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img2_component_display.sizePolicy().hasHeightForWidth())
        self.img2_component_display.setSizePolicy(sizePolicy)
        self.img2_component_display.setText("")
        self.img2_component_display.setPixmap(QtGui.QPixmap("images/No_Image_Available.jpg"))
        self.img2_component_display.setScaledContents(True)
        self.img2_component_display.setObjectName("img2_component_display")
        self.verticalLayout_4.addWidget(self.img2_component_display)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_14.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem3)
        self.mixing_panel = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.mixing_panel.setFont(font)
        self.mixing_panel.setObjectName("mixing_panel")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.mixing_panel)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.output_selector_label = QtWidgets.QLabel(self.mixing_panel)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.output_selector_label.setFont(font)
        self.output_selector_label.setObjectName("output_selector_label")
        self.horizontalLayout_3.addWidget(self.output_selector_label)
        self.output_selector = QtWidgets.QComboBox(self.mixing_panel)
        self.output_selector.setObjectName("output_selector")
        self.horizontalLayout_3.addWidget(self.output_selector)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.component1 = QtWidgets.QGroupBox(self.mixing_panel)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.component1.setFont(font)
        self.component1.setObjectName("component1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.component1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.component1_img_selector = QtWidgets.QComboBox(self.component1)
        self.component1_img_selector.setObjectName("component1_img_selector")
        self.horizontalLayout_4.addWidget(self.component1_img_selector)
        self.component1_component_selector = QtWidgets.QComboBox(self.component1)
        self.component1_component_selector.setObjectName("component1_component_selector")
        self.horizontalLayout_4.addWidget(self.component1_component_selector)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.component1_slider_ratio = QtWidgets.QSlider(self.component1)
        self.component1_slider_ratio.setOrientation(QtCore.Qt.Horizontal)
        self.component1_slider_ratio.setObjectName("component1_slider_ratio")
        self.verticalLayout_6.addWidget(self.component1_slider_ratio)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addWidget(self.component1)
        self.component2 = QtWidgets.QGroupBox(self.mixing_panel)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.component2.setFont(font)
        self.component2.setObjectName("component2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.component2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.component2_img_selector = QtWidgets.QComboBox(self.component2)
        self.component2_img_selector.setObjectName("component2_img_selector")
        self.horizontalLayout_5.addWidget(self.component2_img_selector)
        self.component2_component_selector = QtWidgets.QComboBox(self.component2)
        self.component2_component_selector.setObjectName("component2_component_selector")
        self.horizontalLayout_5.addWidget(self.component2_component_selector)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.component2_slider_ratio = QtWidgets.QSlider(self.component2)
        self.component2_slider_ratio.setOrientation(QtCore.Qt.Horizontal)
        self.component2_slider_ratio.setObjectName("component2_slider_ratio")
        self.verticalLayout_8.addWidget(self.component2_slider_ratio)
        self.verticalLayout_10.addWidget(self.component2)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_15.addWidget(self.mixing_panel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.output1_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output1_label.sizePolicy().hasHeightForWidth())
        self.output1_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.output1_label.setFont(font)
        self.output1_label.setObjectName("output1_label")
        self.verticalLayout_12.addWidget(self.output1_label)
        self.output1_display = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output1_display.sizePolicy().hasHeightForWidth())
        self.output1_display.setSizePolicy(sizePolicy)
        self.output1_display.setText("")
        self.output1_display.setPixmap(QtGui.QPixmap("images/No_Image_Available.jpg"))
        self.output1_display.setScaledContents(True)
        self.output1_display.setObjectName("output1_display")
        self.verticalLayout_12.addWidget(self.output1_display)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.output2_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output2_label.sizePolicy().hasHeightForWidth())
        self.output2_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.output2_label.setFont(font)
        self.output2_label.setObjectName("output2_label")
        self.verticalLayout_13.addWidget(self.output2_label)
        self.output2_display = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output2_display.sizePolicy().hasHeightForWidth())
        self.output2_display.setSizePolicy(sizePolicy)
        self.output2_display.setText("")
        self.output2_display.setPixmap(QtGui.QPixmap("images/No_Image_Available.jpg"))
        self.output2_display.setScaledContents(True)
        self.output2_display.setObjectName("output2_display")
        self.verticalLayout_13.addWidget(self.output2_display)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_15.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_15)
        self.verticalLayout_16.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionnew_window = QtWidgets.QAction(MainWindow)
        self.actionnew_window.setObjectName("actionnew_window")
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionnew_window)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img1_label.setText(_translate("MainWindow", "Image 1"))
        self.img2_label.setText(_translate("MainWindow", "Image 2"))
        self.mixing_panel.setTitle(_translate("MainWindow", "Mixing Panel"))
        self.output_selector_label.setText(_translate("MainWindow", "Mixer output to:"))
        self.component1.setTitle(_translate("MainWindow", "Component 1"))
        self.component2.setTitle(_translate("MainWindow", "Component 2"))
        self.output1_label.setText(_translate("MainWindow", "Output 1"))
        self.output2_label.setText(_translate("MainWindow", "Output 2"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionnew_window.setText(_translate("MainWindow", "new window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
