from replacer_text import ReplacerText
from generator_audio import GeneratorAudio
from player import Player
from unit_audio_model import  UnitAudioModel
from unit_audio_view import UnitAudioView

if __name__ == "__main__":
	exit()

class UnitAudio:
	def __init__(self):
		self.replacer = ReplacerText()
		self.gen_audio = GeneratorAudio()
		self.player = Player()
		self.unit_audio_model = UnitAudioModel()
		self.unit_audio_view = UnitAudioView()
	
#	def __tie_model_view(self):
#		self.nit_audio_view.press_play_audio(self.unit_audio_model.)
