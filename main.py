#!/usr/bin/env python3


import os
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextBrowser, QLabel, QScrollArea, QComboBox, QLineEdit, QHBoxLayout, QTabWidget, QFileDialog, QDialog, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer
from replacer_text import ReplacerText
from tabs import Tab
import threading

class Main():
	def __init__(self):
		self.app = QApplication([])

		self.path_main_ui = "ui/main.ui"
		self.ui_main = QFile(self.path_main_ui)
		self.ui_main.open(QFile.ReadOnly)
		self.loader = QUiLoader()
		self.window = self.loader.load(self.ui_main)
		self.find_all_object_qt()
		self.window.show()

		self.add_tab_button.clicked.connect(self.add_tab)

		self.del_tab_button.clicked.connect(self.del_tab)
		self.mv_tab_button.clicked.connect(self.mv_tab)
		self.tabs = []
		self.func_save = None
		self.tabs.append(Tab(self, self.window, len(self.tabs)))

		self.ssml_button.clicked.connect(self.switch_show_ssml)

		self.ssml_pause_button.clicked.connect(self.add_pause)

		self.ssml_wd.hide()
		self.ssml_show = False
		self.window.focusNextPrevChild(True)

		sys.exit(self.app.exec())
	
	def find_all_object_qt(self):
		self.add_tab_button = self.window.findChild(QPushButton, "add_tab")
		self.del_tab_button = self.window.findChild(QPushButton, "del_tab")
		self.mv_tab_button = self.window.findChild(QPushButton, "mv_tab")
		self.name_tab_lbl = self.window.findChild(QLineEdit, "name_tab")
		self.wd_tabs = self.window.findChild(QTabWidget, "tabWidget")
		self.ssml_button = self.window.findChild(QPushButton, "ssml_btn")
		self.ssml_pause_button = self.window.findChild(QPushButton, "add_pause")
		self.ssml_wd = self.window.findChild(QWidget, "ssml_wd")

	def add_tab(self):
		self.tabs.append(Tab(self, self.window, len(self.tabs)))
	
	def mv_tab(self):
		self.wd_tabs.setTabText(self.wd_tabs.currentIndex(), self.name_tab_lbl.text())

	def del_tab(self):
		self.wd_tabs.removeTab(self.wd_tabs.currentIndex())
	
	def switch_show_ssml(self):
		if self.ssml_show:
			self.ssml_wd.hide()
			self.ssml_show = False
		else:
			self.ssml_wd.show()
			self.ssml_show = True
	
	def add_pause(self):
		widget = QApplication.focusWidget()
		print(widget)

if __name__ == "__main__":
	main = Main()
