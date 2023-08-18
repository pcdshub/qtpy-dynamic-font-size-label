from typing import Optional, Union

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import QSize, Qt
from qtpy.QtWidgets import QWidget

from . import util


class DynamicFontSizeLabel(QtWidgets.QLabel):
    """
    Dynamic font size QLabel.  Font size adjusts as the widget resizes.

    Parameters
    ----------
    text : str = ""
        Starting text for the label.
    parent : QtWidgets.QWidget or None, optional
        The label's parent widget.
    flags : Union[Qt.WindowType, Qt.WindowFlags] or None, optional
        Window flags for the widget.
    pad_percent : float, optional
        The normalized padding percentage (0.0 - 1.0) to use in determining the
        maximum font size. Content margin settings determine the content
        rectangle, and this padding is applied as a percentage on top of that.
    """

    clicked = QtCore.Signal()

    def __init__(
        self,
        text: str = "",
        parent: Optional[QtWidgets.QWidget] = None,
        flags: Optional[Union[Qt.WindowType, Qt.WindowFlags]] = None,
        *,
        pad_percent: float = 0.,
    ) -> None:
        args = [flags] if flags is not None else []
        super().__init__(text, parent, *args)
        self.pad_percent = pad_percent

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.clicked.emit()
        return super().mousePressEvent(event)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        new_font = self.font()
        font_size = util.get_widget_maximum_font_size(
            self, self.text(),
            pad_width=self.width() * self.pad_percent,
            pad_height=self.height() * self.pad_percent,
        )
        if abs(font_size - new_font.pointSizeF()) > 0.1:
            new_font.setPointSizeF(font_size)
            self.setFont(new_font)
        return super().paintEvent(event)

    def minimumSizeHint(self) -> QSize:
        """Minimum size hint."""
        # Do not give any size hint as it it changes during paintEvent.
        return QWidget.minimumSizeHint(self)

    def sizeHint(self) -> QSize:
        """Size hint."""
        # Do not give any size hint as it it changes during paintEvent
        return QWidget.sizeHint(self)


class DynamicFontSizePushButton(QtWidgets.QPushButton):
    """
    Dynamic font size QPushButton.  Font size adjusts as the widget resizes.

    Parameters
    ----------
    text : str = ""
        Starting text for the button.
    parent : QtWidgets.QWidget or None, optional
        The button's parent widget.
    flags : Union[Qt.WindowType, Qt.WindowFlags] or None, optional
        Window flags for the widget.
    pad_percent : float, optional
        The normalized padding percentage (0.0 - 1.0) to use in determining the
        maximum font size. Content margin settings determine the content
        rectangle, and this padding is applied as a percentage on top of that.
    """

    def __init__(
        self,
        text: str = "",
        parent: Optional[QtWidgets.QWidget] = None,
        flags: Optional[Union[Qt.WindowType, Qt.WindowFlags]] = None,
        *,
        pad_percent: float = 0.,
    ) -> None:
        args = [flags] if flags is not None else []
        self.pad_percent = pad_percent
        super().__init__(text, parent, *args)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.clicked.emit()
        return super().mousePressEvent(event)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        new_font = self.font()
        font_size = util.get_widget_maximum_font_size(
            self, self.text(),
            pad_width=self.width() * self.pad_percent,
            pad_height=self.height() * self.pad_percent,
        )
        if abs(font_size - new_font.pointSizeF()) > 0.1:
            new_font.setPointSizeF(font_size)
            self.setFont(new_font)
        return super().paintEvent(event)

    def minimumSizeHint(self) -> QSize:
        """Minimum size hint."""
        # Do not give any size hint as it it changes during paintEvent.
        return QWidget.minimumSizeHint(self)

    def sizeHint(self) -> QSize:
        """Size hint."""
        # Do not give any size hint as it it changes during paintEvent
        return QWidget.sizeHint(self)
