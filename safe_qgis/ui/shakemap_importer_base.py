# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shakemap_importer_base.ui'
#
# Created: Mon Oct 20 08:47:44 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ShakemapImporterBase(object):
    def setupUi(self, ShakemapImporterBase):
        ShakemapImporterBase.setObjectName(_fromUtf8("ShakemapImporterBase"))
        ShakemapImporterBase.resize(526, 637)
        self.gridLayout_2 = QtGui.QGridLayout(ShakemapImporterBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.webView = QtWebKit.QWebView(ShakemapImporterBase)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout_2.addWidget(self.webView, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(ShakemapImporterBase)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.input_path = QtGui.QLineEdit(self.groupBox_2)
        self.input_path.setEnabled(True)
        self.input_path.setObjectName(_fromUtf8("input_path"))
        self.horizontalLayout_2.addWidget(self.input_path)
        self.open_input_tool = QtGui.QToolButton(self.groupBox_2)
        self.open_input_tool.setEnabled(True)
        self.open_input_tool.setObjectName(_fromUtf8("open_input_tool"))
        self.horizontalLayout_2.addWidget(self.open_input_tool)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.label_title = QtGui.QLabel(self.groupBox_2)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.gridLayout_4.addWidget(self.label_title, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_source = QtGui.QLabel(self.groupBox_2)
        self.label_source.setObjectName(_fromUtf8("label_source"))
        self.gridLayout_4.addWidget(self.label_source, 4, 0, 1, 1)
        self.line_edit_title = QtGui.QLineEdit(self.groupBox_2)
        self.line_edit_title.setObjectName(_fromUtf8("line_edit_title"))
        self.gridLayout_4.addWidget(self.line_edit_title, 3, 0, 1, 1)
        self.line_edit_source = QtGui.QLineEdit(self.groupBox_2)
        self.line_edit_source.setObjectName(_fromUtf8("line_edit_source"))
        self.gridLayout_4.addWidget(self.line_edit_source, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(ShakemapImporterBase)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.output_path = QtGui.QLineEdit(self.groupBox_3)
        self.output_path.setEnabled(False)
        self.output_path.setObjectName(_fromUtf8("output_path"))
        self.horizontalLayout.addWidget(self.output_path)
        self.open_output_tool = QtGui.QToolButton(self.groupBox_3)
        self.open_output_tool.setEnabled(False)
        self.open_output_tool.setObjectName(_fromUtf8("open_output_tool"))
        self.horizontalLayout.addWidget(self.open_output_tool)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.use_output_default = QtGui.QCheckBox(self.groupBox_3)
        self.use_output_default.setChecked(True)
        self.use_output_default.setObjectName(_fromUtf8("use_output_default"))
        self.gridLayout_3.addWidget(self.use_output_default, 0, 0, 1, 1)
        self.load_result = QtGui.QCheckBox(self.groupBox_3)
        self.load_result.setEnabled(True)
        self.load_result.setChecked(True)
        self.load_result.setObjectName(_fromUtf8("load_result"))
        self.gridLayout_3.addWidget(self.load_result, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(ShakemapImporterBase)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nearest_mode = QtGui.QRadioButton(self.groupBox)
        self.nearest_mode.setChecked(True)
        self.nearest_mode.setObjectName(_fromUtf8("nearest_mode"))
        self.gridLayout.addWidget(self.nearest_mode, 0, 0, 1, 1)
        self.inverse_distance_mode = QtGui.QRadioButton(self.groupBox)
        self.inverse_distance_mode.setObjectName(_fromUtf8("inverse_distance_mode"))
        self.gridLayout.addWidget(self.inverse_distance_mode, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 1)
        self.button_box = QtGui.QDialogButtonBox(ShakemapImporterBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout_2.addWidget(self.button_box, 4, 0, 1, 1)

        self.retranslateUi(ShakemapImporterBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), ShakemapImporterBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), ShakemapImporterBase.reject)
        QtCore.QObject.connect(self.use_output_default, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.output_path.setDisabled)
        QtCore.QObject.connect(self.use_output_default, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.open_output_tool.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(ShakemapImporterBase)

    def retranslateUi(self, ShakemapImporterBase):
        ShakemapImporterBase.setWindowTitle(_translate("ShakemapImporterBase", "InaSAFE - Shakemap Importer", None))
        self.groupBox_2.setTitle(_translate("ShakemapImporterBase", "Input", None))
        self.open_input_tool.setText(_translate("ShakemapImporterBase", "...", None))
        self.label_title.setText(_translate("ShakemapImporterBase", "Title", None))
        self.label.setText(_translate("ShakemapImporterBase", "Input File (grid.xml)", None))
        self.label_source.setText(_translate("ShakemapImporterBase", "Source", None))
        self.groupBox_3.setTitle(_translate("ShakemapImporterBase", "Output", None))
        self.open_output_tool.setText(_translate("ShakemapImporterBase", "...", None))
        self.label_2.setText(_translate("ShakemapImporterBase", "The output will be a .tif raster file", None))
        self.use_output_default.setText(_translate("ShakemapImporterBase", "Same directory as input file", None))
        self.load_result.setText(_translate("ShakemapImporterBase", "Add output layer to QGIS project", None))
        self.groupBox.setTitle(_translate("ShakemapImporterBase", "Algorithm", None))
        self.nearest_mode.setText(_translate("ShakemapImporterBase", "Nearest neighbour", None))
        self.inverse_distance_mode.setText(_translate("ShakemapImporterBase", "Inverse Distance", None))

from PyQt4 import QtWebKit
