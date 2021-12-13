from typing import TYPE_CHECKING, Optional

from PySide6.QtCore import Qt, QPointF, QLineF, QRectF, QSizeF, qFuzzyCompare
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem, QWidget

if TYPE_CHECKING:
    from .node import Node

__all__ = ("Edge",)


class Edge(QGraphicsItem):
    __default_color = QColor(Qt.black)

    __default_pen = QPen(__default_color, 1.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

    def __init__(self, src: 'Node', dest: 'Node'):
        super().__init__()
        self._src = src
        self._dest = dest

        self.setAcceptedMouseButtons(Qt.NoButton)

        self._src_point = QPointF()
        self._dest_point = QPointF()
        self.adjust()

    @property
    def src(self) -> 'Node':
        return self._src

    @property
    def dest(self) -> 'Node':
        return self._dest

    def __hash__(self):
        return hash(self._src) + hash(self._dest)

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self._src == other._src and self._dest == other._dest or \
                   self._src == other._dest and self._dest == other._src

        raise NotImplemented

    def adjust(self):
        line = QLineF(self.mapFromItem(self._src, 0, 0), self.mapFromItem(self._dest, 0, 0))
        length = line.length()

        self.prepareGeometryChange()

        if length > 2 * max(self._src.r, self._dest.r):
            src_offset = QPointF(line.dx() * self._src.r / length, line.dy() * self._src.r / length)
            self._src_point = line.p1() + src_offset

            dest_offset = QPointF(line.dx() * self._dest.r / length, line.dy() * self._dest.r / length)
            self._dest_point = line.p2() - dest_offset
        else:
            self._src_point = self._dest_point = line.p1()

    def boundingRect(self) -> QRectF:
        return QRectF(self._src_point, QSizeF(self._dest_point.x() - self._src_point.x(),
                                              self._dest_point.y() - self._src_point.y())).normalized()

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...):
        line = QLineF(self._src_point, self._dest_point)
        if qFuzzyCompare(line.length(), 0.):
            return

        painter.setPen(self.__default_pen)
        painter.drawLine(line)
