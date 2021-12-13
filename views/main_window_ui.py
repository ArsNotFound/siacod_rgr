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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(916, 626)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graph_widget = QWidget(self.centralwidget)
        self.graph_widget.setObjectName(u"graph_widget")

        self.verticalLayout.addWidget(self.graph_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.matrix_tableWidget = QTableWidget(self.centralwidget)
        self.matrix_tableWidget.setObjectName(u"matrix_tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrix_tableWidget.sizePolicy().hasHeightForWidth())
        self.matrix_tableWidget.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.matrix_tableWidget)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.firstNode_comboBox = QComboBox(self.centralwidget)
        self.firstNode_comboBox.setObjectName(u"firstNode_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firstNode_comboBox.sizePolicy().hasHeightForWidth())
        self.firstNode_comboBox.setSizePolicy(sizePolicy1)
        self.firstNode_comboBox.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.firstNode_comboBox)

        self.calculate_pushButton = QPushButton(self.centralwidget)
        self.calculate_pushButton.setObjectName(u"calculate_pushButton")
        self.calculate_pushButton.setMinimumSize(QSize(0, 48))

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.calculate_pushButton)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer)

        self.secondNode_comboBox = QComboBox(self.centralwidget)
        self.secondNode_comboBox.setObjectName(u"secondNode_comboBox")
        sizePolicy1.setHeightForWidth(self.secondNode_comboBox.sizePolicy().hasHeightForWidth())
        self.secondNode_comboBox.setSizePolicy(sizePolicy1)
        self.secondNode_comboBox.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.secondNode_comboBox)

        self.path_label = QLabel(self.centralwidget)
        self.path_label.setObjectName(u"path_label")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.path_label)

        self.path_lineEdit = QLineEdit(self.centralwidget)
        self.path_lineEdit.setObjectName(u"path_lineEdit")
        sizePolicy1.setHeightForWidth(self.path_lineEdit.sizePolicy().hasHeightForWidth())
        self.path_lineEdit.setSizePolicy(sizePolicy1)
        self.path_lineEdit.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.path_lineEdit)


        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SIACOD RGR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u0443\u044e \u0432\u0435\u0440\u0448\u0438\u043d\u0443:", None))
        self.calculate_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u0443\u044e \u0432\u0435\u0440\u0448\u0438\u043d\u0443:", None))
        self.path_label.setText("")
    # retranslateUi

