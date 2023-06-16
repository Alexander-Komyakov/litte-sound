from PySide6.QtWidgets import  QWidget, QPushButton, QTextBrowser, QComboBox, QLineEdit, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

if __name__ == "__main__":
	exit()

class UnitAudioView:
	def __init__(self):
		self.__load_audio_widget()
		self.__find_all_object_qt()

	def __load_audio_widget(self) -> None:
		file = QFile("ui/onetxt.ui")
		file.open(QFile.ReadOnly)
		loader = QUiLoader()
		self.audio_widget = loader.load(file)

	def __find_all_object_qt(self):
		self.btn_del = self.audio_widget.findChild(QPushButton, "delete_audio")
		self.text_brow = self.audio_widget.findChild(QTextBrowser, "txt_browser")
		self.wid_rep = self.audio_widget.findChild(QWidget, "widget_replace")
		self.led_rep_in = self.audio_widget.findChild(QLineEdit, "replace_in")
		self.led_rep_out = self.audio_widget.findChild(QLineEdit, "replace_out")
		self.btn_rep = self.audio_widget.findChild(QPushButton, "replace")
		self.btn_repp = self.audio_widget.findChild(QPushButton, "replace_button")
		self.led_path_to_words = self.audio_widget.findChild(QLineEdit, "path_to_words")
		self.btn_rep_words = self.audio_widget.findChild(QPushButton, "replace_words")
		self.btn_rep_reverse = self.audio_widget.findChild(QPushButton, "replace_reverse_button")
		self.btn_rep_rev_words = self.audio_widget.findChild(QPushButton, "replace_revers_words")
		self.btn_play = self.audio_widget.findChild(QPushButton, "start_audio")
		self.btn_path_audio_get = self.audio_widget.findChild(QPushButton, "get_path_audio")
		self.cbox_spk_audio = self.audio_widget.findChild(QComboBox, "speaker_audio")
		self.cbox_tone_audio = self.audio_widget.findChild(QComboBox, "tone_audio")
		self.cbox_speed_audio = self.audio_widget.findChild(QComboBox, "speed_audio")
		self.led_audio_path = self.audio_widget.findChild(QLineEdit, "audio_path")
		self.btn_save_audio = self.audio_widget.findChild(QPushButton, "save_audio")
		self.btn_pause_sound = self.audio_widget.findChild(QPushButton, "pause_audio")
		self.btn_stop_sound = self.audio_widget.findChild(QPushButton, "stop_audio")
		self.btn_words_path = self.audio_widget.findChild(QPushButton, "words_patch")
		self.wid_gen_prog = self.audio_widget.findChild(QWidget, "generate_progress")

	def error_message(self, text):
		dialog = QMessageBox(parent=self.audio_widget, text=text)
		dialog.setWindowTitle("Error")
		dialog.exec()

	def is_changed_text(self, func):
		pass
	
	def press_play_audio(self, func):
		self.btn_play.cliecked.connect(func)

	def delete(self):
		self.audio_widget.deleteLater()
