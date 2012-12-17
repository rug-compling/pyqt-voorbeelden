# Voor willekeurige nummers.
import random

from PyQt4 import QtGui

import Ui_GuessWidget

class GuessWidget(QtGui.QWidget):
  def __init__(self):
    super(GuessWidget, self).__init__()
    self.ui = Ui_GuessWidget.Ui_GuessWidget()
    self.ui.setupUi(self)

    # Schakel de knop standaard uit...
    self.ui.guessPushButton.setEnabled(False)

    # De invoer moet een getal tussen 1 en 10 zijn.
    self.ui.numberLineEdit.setValidator(QtGui.QIntValidator(1, 10))

    self.setupConnections()

  def setupConnections(self):
    self.ui.numberLineEdit.textChanged.connect(self.numberChanged)

    self.ui.guessPushButton.clicked.connect(self.guess)

  def guess(self):
    # Een willekeurig getal tussen 1 en 10.
    number = random.randint(1, 10)

    # Wat raadde de gebruiker?
    guess = int(self.ui.numberLineEdit.text())

    if guess == number:
      self.ui.resultLabel.setStyleSheet("QLabel { color: green; }")
      self.ui.resultLabel.setText("Congrats! Your guess was correct.")
    else:
      self.ui.resultLabel.setStyleSheet("QLabel { color: red; }")
      self.ui.resultLabel.setText("Unfortunately, the correct number was %d." % number)

  def numberChanged(self):
    # Schakel de knop aan, als de invoer acceptabel is.
    self.ui.guessPushButton.setEnabled(self.ui.numberLineEdit.hasAcceptableInput())
