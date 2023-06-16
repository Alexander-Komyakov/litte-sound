import vlc


if __name__ == "__main__":
	exit()


class Player:
	def __init__(self, audio_path=""):
		pass
	
	def set_audio_path(self, audio_path):
		self.audio_path = audio_path
		self.media = vlc.MediaPlayer(self.audio_path)
	
	def play_audio(self):
		if str(self.media.get_state()) == "State.Ended":
			self.media.stop()
			self.media.play()
		elif self.media.get_length() != -1:
			self.media.pause()
		else:
			self.media.stop()
			self.media.play()

	def stop_audio(self):
		self.media.stop()

	def pause_audio(self):
		self.media.pause()
