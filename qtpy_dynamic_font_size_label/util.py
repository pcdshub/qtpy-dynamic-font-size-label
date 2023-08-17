from qtpy import QtGui, QtWidgets
from qtpy.QtCore import QRectF, Qt


def get_widget_maximum_font_size(
    widget: QtWidgets.QWidget,
    text: str,
    *,
    precision: float = 0.5,
) -> float:
    font = widget.font()
    widgetRect = QRectF(widget.contentsRect())
    widgetWidth = widgetRect.width()
    widgetHeight = widgetRect.height()

    # QRectF newFontSizeRect
    currentSize = font.pointSizeF()

    if not text:
        return currentSize

    step = currentSize / 2.0

    # If too small, increase step
    if step <= precision:
        step = precision * 4.0

    lastTestedSize = currentSize
    currentHeight = 0.0
    currentWidth = 0.0

    # Only stop when step is small enough and new size is smaller than QWidget
    while (
        step > precision
        or (currentHeight > widgetHeight)
        or (currentWidth > widgetWidth)
    ):
        # Keep last tested value
        lastTestedSize = currentSize

        # Test label with its font
        font.setPointSizeF(currentSize)
        # Use font metrics to test
        fm = QtGui.QFontMetricsF(font)

        # Check if widget is QLabel
        if isinstance(widget, QtWidgets.QLabel):
            if widget.wordWrap():
                flags = Qt.TextWordWrap | widget.alignment()
            else:
                flags = widget.alignment()
            newFontSizeRect = fm.boundingRect(
                widgetRect, flags, text
            )
        else:
            newFontSizeRect = fm.boundingRect(widgetRect, 0, text)

        currentHeight = newFontSizeRect.height()
        currentWidth = newFontSizeRect.width()

        # If new font size is too big, decrease it
        if (currentHeight > widgetHeight) or (currentWidth > widgetWidth):
            # qDebug() << "-- contentsRect()" << label.contentsRect() << "rect"<< label.rect() << " newFontSizeRect" << newFontSizeRect << "Tight" << text << currentSize
            currentSize -= step
            # if step is small enough, keep it constant, so it converge to biggest font size
            if step > precision:
                step /= 2.0
            # Do not allow negative size
            if currentSize <= 0:
                break
        else:
            # If new font size is smaller than maximum possible size, increase it
            # qDebug() << "++ contentsRect()" << label.contentsRect() << "rect"<< label.rect() << " newFontSizeRect" << newFontSizeRect << "Tight" << text << currentSize
            currentSize += step

    return lastTestedSize
