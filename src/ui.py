#!/usr/bin/env python2.7

import sys
from PyQt4 import QtGui, QtCore
import member_list_scraper

class PollPollUI(QtGui.QWidget):

        def __init__(self):
                super(PollPollUI, self).__init__()

        def initUI(self, member_string_list, keyword_string_list):
                member_layout = QtGui.QHBoxLayout()
                member_description = QtGui.QLabel("Member")
                member_layout.addWidget(member_description)

                member_model = QtGui.QStringListModel()
                member_model.setStringList(member_string_list)
                member_completer = QtGui.QCompleter()
                member_completer.setModel(member_model)
                member_le = QtGui.QLineEdit(self)
                member_le.setCompleter(member_completer)
                member_layout.addWidget(member_le)

                keyword_layout = QtGui.QHBoxLayout()
                keyword_description = QtGui.QLabel("Keyword")
                keyword_layout.addWidget(keyword_description)
                keyword_model = QtGui.QStringListModel()
                keyword_model.setStringList(keyword_string_list)

                keyword_completer = QtGui.QCompleter()
                keyword_completer.setModel(keyword_model)

                keyword_le = QtGui.QLineEdit(self)
                keyword_le.setCompleter(keyword_completer)
                keyword_layout.addWidget(keyword_le)

                table = QtGui.QTableWidget()

                rows = table.rowCount()
                columns = table.columnCount()
                for i in range(rows):
                        for j in range(columns):
                                item = table.items(i,j)
                                item.setFlags(QtCore.Qt.ItemIsEditable, false)

                #table.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
                table.setRowCount(100)
                table.setColumnCount(4)
                table.setHorizontalHeaderLabels(["Bill", "Voter", "Passed", "Description"])

                main_layout = QtGui.QVBoxLayout()
                main_layout.addLayout(member_layout)
                main_layout.addLayout(keyword_layout)
                main_layout.addWidget(table)
                self.setLayout(main_layout)

                self.setGeometry(300, 300, 800, 600)
                self.setWindowTitle('Buttons')
                self.show()

def main():
        f = open(keywords.txt)
        sample_keywords = f.readLine().split(',')
        members = member_list_scraper.get_member_names()
        app = QtGui.QApplication(sys.argv)
        ex = PollPollUI()
        ex.initUI(members, sample_keywords)
        sys.exit(app.exec_())


if __name__ == '__main__':
        main()

