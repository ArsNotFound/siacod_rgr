from typing import Optional

from PySide6.QtCore import Slot, QItemSelectionModel
from PySide6.QtWidgets import QMainWindow, QVBoxLayout

import model
from graph.graph import Graph
from views.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._graph = Graph()
        self._model: Optional[model.Graph] = None

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._graph)
        self._ui.graph_widget.setLayout(layout)

        self._ui.calculate_pushButton.pressed.connect(self.on_calculate)
        self._ui.firstNode_comboBox.currentTextChanged.connect(self.on_node_select)
        self._ui.secondNode_comboBox.currentTextChanged.connect(self.on_node_select)

    @Slot()
    def on_calculate(self):
        g = model.graph_to_model(self._graph)
        self._model = model.warshall(g)
        g_vm = model.GraphViewModel(g)
        self._ui.matrix_tableView.setModel(g_vm)
        self._ui.firstNode_comboBox.clear()
        self._ui.secondNode_comboBox.clear()
        self._ui.firstNode_comboBox.addItems(g.header)
        self._ui.secondNode_comboBox.addItems(g.header)

    @Slot()
    def on_node_select(self):
        if self._ui.firstNode_comboBox.currentText() == "" or self._ui.secondNode_comboBox.currentText() == "" or \
                self._model is None:
            self._ui.path_label.setText("")
            return

        i = self._model.header.index(self._ui.firstNode_comboBox.currentText())
        j = self._model.header.index(self._ui.secondNode_comboBox.currentText())

        try:
            self._ui.path_label.setText("Путь существует" if self._model.matrix[i][j] else "Путь не существует")
            index = self._ui.matrix_tableView.model().index(i, j)
            self._ui.matrix_tableView.selectionModel().select(index, QItemSelectionModel.ClearAndSelect)
        except IndexError:
            self._ui.path_label.setText("Ошибка")
