from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextBrowser, QLabel, QScrollArea, QComboBox, QLineEdit, QHBoxLayout, QTabWidget, QFileDialog, QDialog, QMessageBox, QCheckBox
from replacer_text import ReplacerText
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer
from unit_audio_controller import UnitAudio
from audio_editor import AudioEditor
from player import Player


if __name__ == "__main__":
	exit()


class Tab:
	def __init__(self, app, window, number):
		self.app = app
		self.window = window
		self.number_audio = 0
		self.audios = {}
		self.deletes = []
		self.all_audio_path_default = "Куда сохранить"
		self.audio_name = ""
		self.audio_dir = "audio/"

		self.replacer = ReplacerText()
		self.audio_editor = AudioEditor()
		self.player = Player()

		self.ui_dir = "ui/"
		self.ui_path = { "tab": self.ui_dir+"tab.ui",
						"onetxt": self.ui_dir+"onetxt.ui" }
		self.ui_tab = QFile(self.ui_path["tab"])
		self.ui_tab.open(QFile.ReadOnly)
		self.wd_ui_tab = self.app.loader.load(self.ui_tab)
		self.find_all_object_qt()
		self.wd_tabs.addTab(self.wd_ui_tab, str(number))
		self.btn_add_text.clicked.connect(self.mgr_add_audio)
		self.btn_replace.clicked.connect(self.switch_show_replace)
		self.wd_replace.hide()
		self.rep_show = False

		self.rep.clicked.connect(self.replace_text)
		self.rep_reverse.clicked.connect(lambda: self.replace_text(reverse=1))
		self.words_path.clicked.connect(self.get_patch)
		self.rep_words.clicked.connect(lambda: self.replace_words(0))
		self.rep_reverse_words.clicked.connect(lambda: self.replace_words(1))
		self.save_all.clicked.connect(self.save_all_audio)
		self.get_path_all_audio.clicked.connect(self.get_all_path_audio_file)
		self.start_all.clicked.connect(self.play_audio)
		self.stop_all.clicked.connect(self.player.stop_audio)
		self.pause_all.clicked.connect(self.player.pause_audio)

		self.mgr_add_audio()

	def find_all_object_qt(self):
		self.wd_tabs = self.window.findChild(QTabWidget, "tabWidget")
		self.vlayt_text = self.wd_ui_tab.findChild(QVBoxLayout, "vlayout_text")
		self.btn_add_text = self.wd_ui_tab.findChild(QPushButton, "add_text")
		self.btn_replace = self.wd_ui_tab.findChild(QPushButton, "replace_all_btn")
		self.btn_del_text = self.wd_ui_tab.findChild(QPushButton, "remove_text")
		self.wd_replace = self.wd_ui_tab.findChild(QWidget, "wd_replace")

		self.replace_in = self.wd_ui_tab.findChild(QLineEdit, "tab_replace_in")
		self.replace_out = self.wd_ui_tab.findChild(QLineEdit, "tab_replace_out")
		self.rep = self.wd_ui_tab.findChild(QPushButton, "tab_replace_button")
		self.rep_reverse = self.wd_ui_tab.findChild(QPushButton, "tab_replace_reverse_button")
		self.words_path = self.wd_ui_tab.findChild(QPushButton, "tab_words_patch")
		self.path_to_words = self.wd_ui_tab.findChild(QLineEdit, "tab_path_to_words")
		self.rep_words = self.wd_ui_tab.findChild(QPushButton, "tab_replace_words")
		self.rep_reverse_words = self.wd_ui_tab.findChild(QPushButton, "tab_replace_reverse_words")
		self.save_all = self.wd_ui_tab.findChild(QPushButton, "save_all")
		self.start_all = self.wd_ui_tab.findChild(QPushButton, "start_all")
		self.stop_all = self.wd_ui_tab.findChild(QPushButton, "stop_all")
		self.pause_all = self.wd_ui_tab.findChild(QPushButton, "pause_all")
		self.all_audio_path = self.wd_ui_tab.findChild(QLineEdit, "audio_path")
		self.get_path_all_audio = self.wd_ui_tab.findChild(QPushButton, "get_path_all_audio")

	def play_audio(self):
		self.autogenerate_name_file()
		self.save_all_audio()
		self.player.play_audio()

	def save_all_audio(self):
		self.autogenerate_name_file()
		all_path_audio = self.get_all_path_audio()
		self.audio_editor.split_audio(all_path_audio, "wav", self.all_audio_path.text())
		self.player.set_audio_path(self.all_audio_path.text())

	def autogenerate_name_file(self):
		if self.all_audio_path.text() == self.all_audio_path_default:
			self.audio_name = self.wd_tabs.tabText(self.wd_tabs.count()-1)[:10]
			if len(self.audio_name) < 1:
				self.audio_name = self.audio_dir + "all_audio.wav"
			else:
				self.audio_name = self.audio_dir + self.audio_name + ".wav"
		else:
			self.audio_name = self.all_audio_path.text()
		self.all_audio_path.setText(self.audio_name)
		return self.audio_name

	def get_all_path_audio(self):
		audios_temp = self.audios.copy()
		path_audios = []
		for i in audios_temp:
			try:
				print(audios_temp[i][0])
			except:
				del self.audios[i]
				continue
			combine_this = audios_temp[i][0].findChild(QCheckBox, "combine_this")
			if combine_this.isChecked():
				if audios_temp[i][1].check_mutable_text():
					audios_temp[i][1].save_audio_thread()
				path_audios.append(audios_temp[i][1].get_audio_path())
			print("Audio path: ", audios_temp[i][1].get_audio_path())
		print("split_audio: ", path_audios)
		return path_audios

	def get_all_path_audio_file(self):
		all_audio_path = QFileDialog.getSaveFileName(self.window, filter="WAV Files (*.wav)")[0]
		self.all_audio_path.setText(all_audio_path)

	def get_patch(self):
		wd_patch = QFileDialog.getOpenFileName(self.window)[0]
		self.path_to_words.setText(wd_patch)

	def replace_words(self, reverse, path_to_words=0):
		if path_to_words == 0:
			path_to_words = self.path_to_words.text()

		for i in self.deletes:
			new_text = self.replacer.replace_dictonary(i.text_brow.toPlainText(),
													path_to_words, reverse=reverse)
			if new_text == -1:
				self.error_message("Не найден словарь")
				return -1
			i.text_brow.setPlainText(new_text)

	def replace_text(self, reverse=0, word_in=0,
					word_out=0):
		if word_in == 0 or word_out == 0:
			word_in = self.replace_in.text()
			word_out = self.replace_out.text()
			if reverse != 0:
				word_in, word_out = word_out, word_in

		for i in self.deletes:
			new_text = self.replacer.replace(i.text_brow.toPlainText(),
											word_in,
											word_out)
			i.text_brow.setPlainText(new_text)

	def error_message(self, text):
		dialog = QMessageBox(parent=self.window, text=text)
		dialog.setWindowTitle("Error")
		dialog.exec()

	def switch_show_replace(self):
		if self.rep_show:
			self.wd_replace.hide()
			self.rep_show = False
		else:
			self.wd_replace.show()
			self.rep_show = True

	def mgr_add_audio(self):
		self.ui_audio = QFile(self.ui_path["onetxt"])
		self.ui_audio.open(QFile.ReadOnly)
		self.wd_ui_audio = self.app.loader.load(self.ui_audio)
		self.vlayt_text.addWidget(self.wd_ui_audio)
		#self.deletes.append(UnitAudio(self.wd_ui_audio))
		self.deletes.append(UnitAudio())

		self.audios[self.number_audio] = [self.wd_ui_audio,
							self.deletes[self.number_audio]]
		self.number_audio += 1
