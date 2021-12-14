from typing import Optional

from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPainter, QMouseEvent, Qt, QResizeEvent
from PySide6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene

from .edge import Edge
from .node import Node

__all__ = ("Graph",)


class Graph(QGraphicsView):
    selected = Signal(Node, bool)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._edges: set[Edge] = set()
        self._nodes: set[Node] = set()
        self._selected: Optional[Node] = None
        self._next_val = 0

        self._scene = QGraphicsScene(self)
        self._scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        self._scene.setSceneRect(0, 0, 400, 400)
        self.setScene(self._scene)

        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.scale(1, 1)
        self.setMinimumSize(400, 400)

        self.selected.connect(self.on_selected)

    @property
    def nodes(self) -> set[Node]:
        return self._nodes

    @property
    def edges(self) -> set[Edge]:
        return self._edges

    def add_node(self, node: Node):
        self._nodes.add(node)
        self._scene.addItem(node)

    def remove_node(self, node: Node):
        if self._selected == node:
            self._selected = None
        self._nodes.remove(node)
        self._scene.removeItem(node)

    def find_edge(self, src: Node, dest: Node) -> Optional[Edge]:
        for e in self._edges:
            if e.src == src and e.dest == dest:
                return e
        return None

    def add_edge(self, edge: Edge):
        edge.src.add_edge(edge)
        if edge.src != edge.dest:
            edge.dest.add_edge(edge)
        self._edges.add(edge)
        self._scene.addItem(edge)

    def remove_edge(self, edge: Edge):
        edge.src.remove_edge(edge)
        if edge.src != edge.dest:
            edge.dest.remove_edge(edge)
        self._edges.remove(edge)
        self._scene.removeItem(edge)

    @Slot(Node, bool)
    def on_selected(self, node: Node, self_select: bool):
        if node is None:
            self._selected = None
            return

        if not self._selected and not self_select:
            self._selected = node
            return

        other = self._selected if not self_select else node

        edge = self.find_edge(other, node)
        if edge:
            self.remove_edge(edge)
            if self_select:
                node.self_connected = False
        else:
            self.add_edge(Edge(other, node))
            if self_select:
                node.self_connected = True

        node.selected = False
        other.selected = False

        node.update()
        other.update()
        self.update()
        self._selected = None

    def mousePressEvent(self, event: QMouseEvent):
        p = self.mapToScene(event.pos())
        if self.items(p.toPoint()):
            super().mousePressEvent(event)
            return

        if event.button() & Qt.LeftButton:
            self._next_val += 1
            node = Node(self, str(self._next_val))

            node.setPos(p)
            self.add_node(node)

            if self._selected:
                self.add_edge(Edge(self._selected, node))
                self._selected.selected = False

    def resizeEvent(self, event: QResizeEvent):
        size = event.size()
        self._scene.setSceneRect(0, 0, size.width(), size.height())
