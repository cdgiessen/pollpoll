#!/usr/bin/env python2.7

import sys
from PyQt4 import QtGui

class PollPollUI(QtGui.QWidget):

        def __init__(self):
                super(PollPollUI, self).__init__()
                self.initUI()

        def initUI(self):
                member_layout = QtGui.QHBoxLayout()
                #member_layout.addStretch(1)
                member_description = QtGui.QLabel("Member")
                member_layout.addWidget(member_description)

                member_model = QtGui.QStringListModel()
                member_model.setStringList(['VHF', 'Drug war', 'Serbian Centro', 'radar', 'CCS', 'Mossberg', 'MD5', 'Ft. Bragg', 'Oscor', 'embassy', 'XS4ALL', 'Osama', 'Mayfly', 'HALO'])
                member_completer = QtGui.QCompleter()
                member_completer.setModel(member_model)
                member_le = QtGui.QLineEdit(self)
                member_le.setCompleter(member_completer)
                member_layout.addWidget(member_le)

                keyword_layout = QtGui.QHBoxLayout()
                #keyword_layout.addStretch(1)
                keyword_description = QtGui.QLabel("Keyword")
                keyword_layout.addWidget(keyword_description)
                keyword_model = QtGui.QStringListModel()
                keyword_model.setStringList(['ANZUS', 'Plot', 'NATO', 'Attorney General', 'CDMA', 'Ansar al-Islam', 'PBX', 'tempest', 'Mayfly', 'Intiso', 'gamma', 'Zachawi', 'afsatcom', 'CIA', 'Saddam Hussein'])

                keyword_completer = QtGui.QCompleter()
                keyword_completer.setModel(keyword_model)

                keyword_le = QtGui.QLineEdit(self)
                keyword_le.setCompleter(keyword_completer)
                keyword_layout.addWidget(keyword_le)

                description_layout = QtGui.QHBoxLayout()
                #description_layout.addStretch(1)
                bill_description = QtGui.QLabel("Bill")
                description_layout.addWidget(bill_description)
                voter_description = QtGui.QLabel("Voter")
                description_layout.addWidget(voter_description)
                passed_description = QtGui.QLabel("Passed")
                description_layout.addWidget(passed_description)
                description_description = QtGui.QLabel("Description")
                description_layout.addWidget(description_description)

                main_layout = QtGui.QVBoxLayout()
                #main_layout.addStretch(1)
                main_layout.addLayout(member_layout)
                main_layout.addLayout(keyword_layout)
                main_layout.addLayout(description_layout)
                self.setLayout(main_layout)

                self.setGeometry(300, 300, 800, 600)
                self.setWindowTitle('Buttons')
                self.show()

def main():
        app = QtGui.QApplication(sys.argv)
        ex = PollPollUI()
        sys.exit(app.exec_())


if __name__ == '__main__':
        main()

