import sys

from qtpy import QtCore, QtWidgets

from ..widgets import DynamicFontSizeLabel, DynamicFontSizePushButton


def create_window() -> QtWidgets.QMainWindow:
    main = QtWidgets.QMainWindow()
    main.resize(894, 216)

    # The central widget
    central_widget = QtWidgets.QWidget(main)
    grid_layout = QtWidgets.QGridLayout(central_widget)
    grid_layout.setContentsMargins(11, 11, 11, 11)
    grid_layout.setSpacing(6)
    fixed_pushbutton = DynamicFontSizePushButton(
        "Fixed size DynamicFontSizePushButton", central_widget
    )
    fixed_pushbutton.setMinimumSize(QtCore.QSize(200, 30))
    fixed_pushbutton.setMaximumSize(QtCore.QSize(200, 30))
    grid_layout.addWidget(fixed_pushbutton, 1, 1, 1, 1)

    # Our dynamic font label with min expanding size policy
    exp_label = DynamicFontSizeLabel("Expanding DynamicFontSizeLabel", central_widget)
    policy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.MinimumExpanding,
        QtWidgets.QSizePolicy.MinimumExpanding,
    )
    policy.setHorizontalStretch(0)
    policy.setVerticalStretch(0)
    policy.setHeightForWidth(exp_label.sizePolicy().hasHeightForWidth())
    exp_label.setSizePolicy(policy)
    exp_label.setFrameShape(QtWidgets.QFrame.Box)
    exp_label.setIndent(0)
    grid_layout.addWidget(exp_label, 1, 2, 1, 1)

    # Our dynamic font label with fixed size
    fixed_label = DynamicFontSizeLabel(
        "Fixed size DynamicFontSizeLabel", central_widget
    )
    policy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
    )
    policy.setHorizontalStretch(0)
    policy.setVerticalStretch(0)
    policy.setHeightForWidth(fixed_label.sizePolicy().hasHeightForWidth())
    fixed_label.setSizePolicy(policy)
    fixed_label.setMinimumSize(QtCore.QSize(300, 50))
    fixed_label.setFrameShape(QtWidgets.QFrame.Box)
    grid_layout.addWidget(fixed_label, 3, 0, 1, 1)

    # Our dynamic pushbutton with min expanding size policy
    exp_button = DynamicFontSizePushButton(
        "Expanding DynamicFontSizePushButton\nwith new line", central_widget
    )
    policy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.MinimumExpanding,
        QtWidgets.QSizePolicy.MinimumExpanding,
    )
    policy.setHorizontalStretch(0)
    policy.setVerticalStretch(0)
    policy.setHeightForWidth(exp_button.sizePolicy().hasHeightForWidth())
    exp_button.setSizePolicy(policy)
    grid_layout.addWidget(exp_button, 0, 1, 1, 1)

    # A standard label
    preferred_label = DynamicFontSizeLabel(
        "Prefered DynamicFontSizeLabel \nwith new line", central_widget
    )
    preferred_label.setFrameShape(QtWidgets.QFrame.Box)
    preferred_label.setAlignment(QtCore.Qt.AlignCenter)
    policy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Preferred,
        QtWidgets.QSizePolicy.Preferred,
    )
    policy.setHorizontalStretch(0)
    policy.setVerticalStretch(0)
    policy.setHeightForWidth(preferred_label.sizePolicy().hasHeightForWidth())
    grid_layout.addWidget(preferred_label, 4, 0, 1, 1)
    preferred_label.setSizePolicy(policy)
    main.setCentralWidget(central_widget)

    main.setWindowTitle("DynamicFontSizeLabel and DynamicFontPushButton example")
    return main


def main():
    if QtWidgets.QApplication.instance() is None:
        app = QtWidgets.QApplication(sys.argv)

    main = create_window()
    main.show()
    app.exec_()


if __name__ == "__main__":
    main()
