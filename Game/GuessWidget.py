from PyQt4 import QtGui

import Ui_GuessWidget

class GuessWidget(QtGui.QWidget):
  def __init__(self):
    super(GuessWidget, self).__init__()
    self.ui = Ui_GuessWidget.Ui_GuessWidget()
    self.ui.setupUi(self)
