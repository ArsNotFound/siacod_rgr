from typing import TYPE_CHECKING, Optional, Any

import PySide6
from PySide6.QtCore import QRectF, QRect
from PySide6.QtGui import QPainterPath, QPainter, QColor, Qt, QBrush, QPen, QFont
from PySide6.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem, QGraphicsSceneMouseEvent

if TYPE_CHECKING:
    from .graph import Graph
    from .edge import Edge

__all__ = ("Node",)


class Node(QGraphicsItem):
    __background_color = QColor(Qt.lightGray)
    __selected_color = QColor(Qt.blue)
    __unselected_color = QColor(Qt.black)

    __title_font = QFont("Arial", 12)

    __background_brush = QBrush(__background_color)
    __selected_pen = QPen(__selected_color, 1.25)
    __unselected_pen = QPen(__unselected_color, 1.25)

    def __init__(self, graph: 'Graph', value: str, r: int = 20):
        super().__init__()
        self._graph = graph
        self._value = value
        self._r = r

        self._edges: set['Edge'] = set()
        self._selected = False
        self._self_connected = False

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(1)

    def add_edge(self, edge: 'Edge'):
        self._edges.add(edge)

    def remove_edge(self, edge: 'Edge'):
        self._edges.remove(edge)

    @property
    def r(self) -> int:
        return self._r

    @property
    def value(self) -> str:
        return self._value

    @property
    def graph(self) -> 'Graph':
        return self._graph

    @property
    def edges(self) -> set['Edge']:
        return self._edges

    @property
    def selected(self) -> bool:
        return self._selected

    @selected.setter
    def selected(self, selected: bool):
        self._selected = selected
        self.setZValue(10 if self._selected else 1)
        self.update()
        self._graph.selected.emit(self if self._selected else None, False)

    @property
    def self_connected(self):
        return self._self_connected

    @self_connected.setter
    def self_connected(self, self_connected: bool):
        self._self_connected = self_connected
        self.update()

    @property
    def background_color(self) -> QColor:
        return self.__background_color

    @background_color.setter
    def background_color(self, color: QColor):
        self.__background_color = color
        self.__background_brush.setColor(color)

    @property
    def selected_color(self) -> QColor:
        return self.__selected_color

    @selected_color.setter
    def selected_color(self, color: QColor):
        self.__selected_color = color
        self.__selected_pen.setColor(color)

    @property
    def unselected_color(self) -> QColor:
        return self.__unselected_color

    @unselected_color.setter
    def unselected_color(self, color: QColor):
        self.__unselected_color = color
        self.__unselected_pen.setColor(color)

    @property
    def title_font(self) -> QFont:
        return self.__title_font

    @title_font.setter
    def title_font(self, font: QFont):
        self.__title_font = font

    def __hash__(self):
        return hash(self.value)

    def boundingRect(self) -> QRectF:
        adjust = 1
        return QRectF(-self._r - adjust, -self._r - adjust, 2 * (self._r + adjust), 2 * (self._r + adjust))

    def shape(self) -> QPainterPath:
        path = QPainterPath()
        path.addEllipse(-self._r, -self._r, 2 * self._r, 2 * self._r)
        return path

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem,
              widget: Optional[PySide6.QtWidgets.QWidget] = ...):
        painter.setBrush(self.__background_brush)
        if self._selected:
            painter.setPen(self.__selected_pen)
        else:
            painter.setPen(self.__unselected_pen)

        rect = QRect(-self._r, -self._r, 2 * self._r, 2 * self._r)
        painter.drawEllipse(rect)
        painter.setFont(self.__title_font)
        painter.drawText(rect, 0x84, self._value + ("↩" if self._self_connected else ""))

    def itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any:
        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self._edges:
                edge.adjust()

        return super().itemChange(change, value)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        if event.button() & Qt.RightButton:
            if event.modifiers() & Qt.AltModifier:
                self._graph.selected.emit(self, True)
            else:
                self.selected = not self.selected

        if event.button() & Qt.LeftButton and event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            edges = self._edges.copy()
            for e in edges:
                self._graph.remove_edge(e)
            self._graph.remove_node(self)

        self.update()
        super().mousePressEvent(event)
