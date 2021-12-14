# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(916, 805)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.graph_widget = QWidget(self.centralwidget)
        self.graph_widget.setObjectName(u"graph_widget")

        self.verticalLayout_2.addWidget(self.graph_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.matrix_tableView = QTableView(self.centralwidget)
        self.matrix_tableView.setObjectName(u"matrix_tableView")
        self.matrix_tableView.horizontalHeader().setMinimumSectionSize(30)
        self.matrix_tableView.horizontalHeader().setDefaultSectionSize(30)
        self.matrix_tableView.verticalHeader().setMinimumSectionSize(30)
        self.matrix_tableView.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout.addWidget(self.matrix_tableView)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.firstNode_comboBox = QComboBox(self.centralwidget)
        self.firstNode_comboBox.setObjectName(u"firstNode_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstNode_comboBox.sizePolicy().hasHeightForWidth())
        self.firstNode_comboBox.setSizePolicy(sizePolicy)
        self.firstNode_comboBox.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.firstNode_comboBox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.secondNode_comboBox = QComboBox(self.centralwidget)
        self.secondNode_comboBox.setObjectName(u"secondNode_comboBox")
        sizePolicy.setHeightForWidth(self.secondNode_comboBox.sizePolicy().hasHeightForWidth())
        self.secondNode_comboBox.setSizePolicy(sizePolicy)
        self.secondNode_comboBox.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.secondNode_comboBox)

        self.path_label = QLabel(self.centralwidget)
        self.path_label.setObjectName(u"path_label")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.path_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer)

        self.calculate_pushButton = QPushButton(self.centralwidget)
        self.calculate_pushButton.setObjectName(u"calculate_pushButton")
        self.calculate_pushButton.setMinimumSize(QSize(0, 48))

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.calculate_pushButton)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_7)


        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SIACOD RGR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u0412\u0430\u0440\u0438\u0430\u043d\u0442 25. </span>\u0417\u0430\u0434\u0430\u043d \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u0433\u0440\u0430\u0444. \u0421 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u0423\u043e\u0440\u0448\u0430\u043b\u043b\u0430 \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438 \u0438 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u043b\u0438 \u043f\u0443\u0442\u044c \u043e\u0442 Vi \u043a Vj.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u0433\u0440\u0430\u0444:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u0443\u044e \u0432\u0435\u0440\u0448\u0438\u043d\u0443:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u0443\u044e \u0432\u0435\u0440\u0448\u0438\u043d\u0443:", None))
        self.path_label.setText("")
        self.calculate_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u043b:\n"
"\u0421\u0430\u0445\u0430\u043f\u043e\u0432 \u0410\u0440\u0441\u043b\u0430\u043d \u0410\u0439\u0440\u0430\u0442\u043e\u0432\u0438\u0447,\n"
"\u0441\u0442\u0443\u0434\u0435\u043d\u0442 \u0433\u0440\u0443\u043f\u043f\u044b \u041c\u041e-221", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u044f\u044e\u0449\u0438\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b:", None))
    # retranslateUi

