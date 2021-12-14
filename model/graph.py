import dataclasses

__all__ = ("Graph", "GraphViewModel")

from typing import Optional, Union, Any

from PySide6.QtCore import QAbstractTableModel, QObject, QModelIndex, QPersistentModelIndex, Qt


@dataclasses.dataclass
class Graph:
    matrix: list[list[int]]
    header: list[str]


class GraphViewModel(QAbstractTableModel):
    def __init__(self, graph: Graph, parent: Optional[QObject] = None):
        super().__init__(parent)
        self._graph = graph

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self._graph.matrix)

    def columnCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return self.rowCount()

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        return self._graph.matrix[index.row()][index.column()]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.DisplayRole:
            return None
        return self._graph.header[section]
