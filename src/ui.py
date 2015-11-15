#!/usr/bin/env python2.7

import sys
from PyQt4 import QtGui, QtCore
import member_list_scraper
import search_bill_keywords
import vote_scraper

class PollPollUI(QtGui.QWidget):

        def __init__(self):
                super(PollPollUI, self).__init__()
                self.member_str = "foo"
                self.keyword_str = ""

        def keyPressEvent(self, e):
                if e.key() == QtCore.Qt.Key_Escape:
                        self.close()
                elif e.key() == QtCore.Qt.Key_R:
                        print("let's get more table stuff")

        def keyword_changed(self, keystr):
                self.keyword_str = keystr
                self.bill_list_display = search_bill_keywords.select_bills(self.bill_list,self.keyword_str)
                self.update_table()
                print("keyword: " + keystr)

        def update_table(self):
                self.table.setRowCount(len(self.bill_list_display))
                for i in range(len(self.bill_list_display)):
                        for j in range(0,len(self.bill_list_display[i])):
                                item = QtGui.QTableWidgetItem(self.bill_list_display[i][j])
                                self.table.setItem(i, j, item)

        def member_changed(self, memstr):
                if self.member_str == memstr:
                        return
                self.member_str = memstr
                self.bill_list = vote_scraper.get_vote_dictionary(self.member_list[str(self.member_str)])
                self.bill_list_display = search_bill_keywords.select_bills(self.bill_list,self.keyword_str)
                self.update_table()
                print("member: " + memstr)

        def set_member_list(self, member_list):
                self.member_list = member_list

        def initUI(self, member_string_list, keyword_string_list):
                member_layout = QtGui.QHBoxLayout()
                member_description = QtGui.QLabel("Member")
                member_layout.addWidget(member_description)

                member_model = QtGui.QStringListModel()
                member_model.setStringList(member_string_list)
                member_completer = QtGui.QCompleter()
                member_completer.setCompletionMode(QtGui.QCompleter().InlineCompletion)
                member_completer.setModel(member_model)
                member_completer.highlighted.connect(self.member_changed)
                member_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
                member_le = QtGui.QLineEdit(self)
                member_le.setCompleter(member_completer)
                member_layout.addWidget(member_le)

                keyword_layout = QtGui.QHBoxLayout()
                keyword_description = QtGui.QLabel("Keyword")
                keyword_layout.addWidget(keyword_description)
                keyword_model = QtGui.QStringListModel()
                keyword_model.setStringList(keyword_string_list)

                keyword_completer = QtGui.QCompleter()
                keyword_completer.activated.connect(self.keyword_changed)
                keyword_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

                keyword_completer.setModel(keyword_model)

                keyword_le = QtGui.QLineEdit(self)
                keyword_le.textEdited.connect(self.keyword_changed)
                keyword_le.setCompleter(keyword_completer)
                keyword_layout.addWidget(keyword_le)

                self.table = QtGui.QTableWidget()

                self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
                rows = self.table.rowCount()
                columns = self.table.columnCount()

                self.table.setRowCount(100)
                self.table.setColumnCount(5)
                self.table.setHorizontalHeaderLabels(["Bill", "Vote #", "Voted", "Passed", "Description"])

                main_layout = QtGui.QVBoxLayout()
                main_layout.addLayout(member_layout)
                main_layout.addLayout(keyword_layout)
                main_layout.addWidget(self.table)

                app_icon = QtGui.QIcon()
                app_icon.addFile('pp_icon.png', QtCore.QSize(256,256))
                self.setLayout(main_layout)
                self.setWindowIcon(app_icon)
                self.setGeometry(300, 300, 800, 600)
                self.setWindowTitle('Buttons')
                self.show()

def main():
        f = open('keywords.txt')
        sample_keywords = f.read().split(',')
        members = member_list_scraper.get_member_names()
        app = QtGui.QApplication(sys.argv)
        ex = PollPollUI()
        ex.initUI(members, sample_keywords)
        ex.set_member_list(member_list_scraper.get_full_member_links())
        sys.exit(app.exec_())


if __name__ == '__main__':
        main()

