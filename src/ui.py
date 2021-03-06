#!/usr/bin/env python2.7

import sys
from PyQt4 import QtGui, QtCore
import member_list_scraper
import search_bill_keywords
import vote_scraper

# Main class for the UI
class PollPollUI(QtGui.QWidget):

        # Constructor
        def __init__(self):
                super(PollPollUI, self).__init__()
                self.member_str = "foo"
                self.keyword_str = ""

        # Override of event handler,
        # exits on escape, gets full history of
        # current member for F11
        def keyPressEvent(self, e):
                if e.key() == QtCore.Qt.Key_Escape:
                        self.close()
                elif e.key() == QtCore.Qt.Key_F11:
                        self.bill_list = vote_scraper.get_vote_dictionary_all(self.member_list[str(self.member_str)])
                        self.bill_list_display = search_bill_keywords.select_bills(self.bill_list,self.keyword_str)
                        self.update_table()

        # Signal handler for when keyword buffer is changed/autocompleted
        def keyword_changed(self, keystr):
                self.keyword_str = keystr
                self.bill_list_display = search_bill_keywords.select_bills(self.bill_list,self.keyword_str)
                self.update_table()
                print("keyword: " + keystr)

        # Function to update the graphical table
        # from the dictionaries
        def update_table(self):
                self.table.clear()
                rowCount = 0
                self.table.setHorizontalHeaderLabels(["Bill", "Vote #", "Voted", "Passed", "Description"])
                if len(self.keyword_str) > 0:
                        for i in self.bill_list:
                                if search_bill_keywords.is_contained(self.bill_list[i], self.keyword_str) == 1:
                                        rowCount = rowCount + 1
                                        for j in range(0, len(self.bill_list[i])):
                                                item = QtGui.QTableWidgetItem(self.bill_list[i][j])
                                                self.table.setItem(rowCount-1, j, item)
                        self.table.setRowCount(rowCount)
                else:
                        self.table.setRowCount(len(self.bill_list))
                        for i in self.bill_list:
                                for j in range(0, len(self.bill_list[i])):
                                        item = QtGui.QTableWidgetItem(self.bill_list[i][j])
                                        self.table.setItem(i, j, item)

        # Signal handler for when the member buffer is changed/autocompleted
        def member_changed(self, memstr):
                if self.member_str == memstr:
                        return
                self.member_str = memstr
                if memstr == "Sir Donald Trump":
                        self.bill_list = self.mister_president()
                        self.update_table()
                        print("member: the president")
                        return
                self.bill_list = vote_scraper.get_vote_dictionary(self.member_list[str(self.member_str)])
                self.bill_list_display = search_bill_keywords.select_bills(self.bill_list,self.keyword_str)
                self.update_table()
                print("member: " + memstr)

        # Simple setter for member list
        def set_member_list(self, member_list):
                self.member_list = member_list

        # Defines mister president
        def mister_president(self):
                d = dict()
                for i in range(0, 88):
                        d[i] = ["H S PR3Z", "China", "The President", "Best Hair 2016", "Obviously, the President"]
                return d

        # Huge function that sets out the layout and initializes it
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
                self.setWindowTitle('PollPoll')
                self.show()

# Main entry point
def main():
        f = open('keywords.txt')
        sample_keywords = f.read().split(',')
        members = member_list_scraper.get_member_names()
        members.append("Sir Donald Trump")
        app = QtGui.QApplication(sys.argv)
        ex = PollPollUI()
        ex.initUI(members, sample_keywords)
        ex.set_member_list(member_list_scraper.get_full_member_links())
        sys.exit(app.exec_())


if __name__ == '__main__':
        main()

