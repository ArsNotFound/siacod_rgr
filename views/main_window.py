from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QVBoxLayout

from graph.graph import Graph
import model
from views.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._graph = Graph()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._graph)
        self._ui.graph_widget.setLayout(layout)

        self._ui.calculate_pushButton.pressed.connect(self.on_calculate)

    @Slot()
    def on_calculate(self):
        g = model.graph_to_model(self._graph)
        print(model.warshall(g))
