#!/usr/bin/env python2.7

import sys
from PyQt4 import QtGui, QtCore
import member_list_scraper
import search_bill_keywords
import vote_scraper

class PollPollUI(QtGui.QWidget):

        def __init__(self):
                super(PollPollUI, self).__init__()

        def keyPressEvent(self, e):
                if e.key() == QtCore.Qt.Key_Escape:
                        self.close()

        def keyword_changed(self, keystr):
                self.keyword_str = keystr
                print("keyword: " + keystr)


        def member_changed(self, memstr):
                self.member_str = memstr
                print("member: " + memstr)

        def update_bill_list(self):
                self.bill_list = search_bill_keywords.select_bills(vote_scraper.main(search_bill_keywords.get_member_url_data(self.member_str)),self.keyword_str)

        def set_member_list(self, member_list):
                self.member_list = member_list

        def initUI(self, member_string_list, keyword_string_list):
                member_layout = QtGui.QHBoxLayout()
                member_description = QtGui.QLabel("Member")
                member_layout.addWidget(member_description)

                member_model = QtGui.QStringListModel()
                member_model.setStringList(member_string_list)
                self.member_completer = QtGui.QCompleter()
                self.member_completer.setCompletionMode(QtGui.QCompleter().InlineCompletion)
                self.member_completer.setModel(member_model)
                self.member_completer.highlighted.connect(self.member_changed)
                member_le = QtGui.QLineEdit(self)
                member_le.setCompleter(self.member_completer)
                member_layout.addWidget(member_le)

                keyword_layout = QtGui.QHBoxLayout()
                keyword_description = QtGui.QLabel("Keyword")
                keyword_layout.addWidget(keyword_description)
                keyword_model = QtGui.QStringListModel()
                keyword_model.setStringList(keyword_string_list)

                keyword_completer = QtGui.QCompleter()
                keyword_completer.activated.connect(self.keyword_changed)
                keyword_completer.setModel(keyword_model)

                keyword_le = QtGui.QLineEdit(self)
                keyword_le.setCompleter(keyword_completer)
                keyword_layout.addWidget(keyword_le)

                self.table = QtGui.QTableWidget()

                rows = self.table.rowCount()
                columns = self.table.columnCount()
                for i in range(rows):
                        for j in range(columns):
                                item = self.table.items(i,j)
                                item.setFlags(QtCore.Qt.ItemIsEditable, False)

                #table.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
                self.table.setRowCount(100)
                self.table.setColumnCount(4)
                self.table.setHorizontalHeaderLabels(["Bill", "Voter", "Passed", "Description"])

                main_layout = QtGui.QVBoxLayout()
                main_layout.addLayout(member_layout)
                main_layout.addLayout(keyword_layout)
                main_layout.addWidget(self.table)
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
        ex.set_member_list(members)
        sys.exit(app.exec_())


if __name__ == '__main__':
        main()

