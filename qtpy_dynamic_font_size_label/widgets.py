from typing import Optional, Union

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import QSize, Qt
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QWidget

from . import util


class DynamicFontSizeLabel(QtWidgets.QLabel):
    """
    Dynamic font size label.
    """

    clicked = QtCore.Signal()

    def __init__(
        self,
        text: str = "",
        parent: Optional[QtWidgets.QWidget] = None,
        flags: Optional[Union[Qt.WindowType, Qt.WindowFlags]] = None,
    ) -> None:
        args = [flags] if flags is not None else []
        super().__init__(text, parent, *args)
        self.text_color = QColor("black")
        self.setIndent(0)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.clicked.emit()
        return super().mousePressEvent(event)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        new_font = self.font()
        font_size = util.get_widget_maximum_font_size(self, self.text())
        new_font.setPointSizeF(font_size)
        self.setFont(new_font)
        return super().paintEvent(event)

    def setTextColor(self, color: QColor) -> None:
        if not color.isValid() or color == self.textColor:
            return

        self.textColor = color
        self.setStyleSheet(f"color : {color.name};")

    def getTextColor(self) -> QColor:
        return self.textColor

    def setTextAndColor(self, text: str, color: QColor) -> None:
        self.setTextColor(color)
        self.setText(text)

    def minimumSizeHint(self) -> QSize:
        # Do not give any size hint as it it changes during paintEvent
        return QWidget.minimumSizeHint(self)

    def sizeHint(self) -> QSize:
        # Do not give any size hint as it it changes during paintEvent
        return QWidget.sizeHint(self)


class DynamicFontSizePushButton(QtWidgets.QPushButton):
    """
    Dynamic font size push button.
    """

    def __init__(
        self,
        text: str = "",
        parent: Optional[QtWidgets.QWidget] = None,
        flags: Optional[Union[Qt.WindowType, Qt.WindowFlags]] = None,
    ) -> None:
        args = [flags] if flags is not None else []
        super().__init__(text, parent, *args)
        self.text_color = QColor("black")

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.clicked.emit()
        return super().mousePressEvent(event)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        new_font = self.font()
        font_size = util.get_widget_maximum_font_size(self, self.text())
        new_font.setPointSizeF(font_size)
        self.setFont(new_font)
        return super().paintEvent(event)

    def setTextColor(self, color: QColor) -> None:
        if not color.isValid() or color == self.textColor:
            return

        self.textColor = color
        self.setStyleSheet(f"color : {color.name};")

    def getTextColor(self) -> QColor:
        return self.textColor

    def setTextAndColor(self, text: str, color: QColor) -> None:
        self.setTextColor(color)
        self.setText(text)

    def minimumSizeHint(self) -> QSize:
        # Do not give any size hint as it it changes during paintEvent
        return QWidget.minimumSizeHint(self)

    def sizeHint(self) -> QSize:
        # Do not give any size hint as it it changes during paintEvent
        return QWidget.sizeHint(self)
