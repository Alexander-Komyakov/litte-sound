if __name__ == "__main__":
	exit()

class UnitAudioModel:
	def __init__(self, audio_text: str = "", speaker: str = "", speakers: list = [],
				audio_dir: str = "audio/", audio_path: str = "",
				join: bool = True, replace: dict = { "r_path": "", "r_in": "", "r_out": "" },
				is_generate: bool = False, hight_tone: int = 1,
				audio_speed: int = 1) -> None:

		self.set_speakers(speakers)
		self.set_audio_text(audio_text)
		self.set_audio_speaker(speaker)
		self.set_audio_dir(audio_dir)
		self.set_audio_path(audio_path)
		self.set_join(join)
		self.set_replace(replace)
		self.set_is_generate(is_generate)
		self.set_hight_tone(hight_tone)
		self.set_audio_speed(audio_speed)
	
	def set_speakers(self, speakers: list) -> None:
		self.speakers = speakers

	def set_audio_text(self, text: str) -> None:
		self.audio_text = text

	def set_audio_speaker(self, speaker: str) -> bool:
		if speaker in self.speakers:
			self.audio_speaker = speaker
			return True
		else:
			return False
	
	def set_audio_dir(self, audio_dir: str) -> None:
		self.audio_dir = audio_dir

	def set_audio_path(self, audio_path: str) -> None:
		self.audio_path = audio_path

	def set_join(self, join: bool) -> None:
		self.join = join

	def set_replace(self, replace: dict) -> None:
		self.replace = { "r_path": replace["r_path"],
						"r_in": replace["r_in"],
						"r_out": replace["r_out"], }

	def set_is_generate(self, is_generate: bool) -> None:
		self.is_generate = is_generate
	
	def set_hight_tone(self, hight_tone: int) -> None:
		self.hight_tone = hight_tone

	def set_audio_speed(self, audio_speed: int) -> None:
		self.audio_speed = audio_speed

	def get_speakers(self) -> list:
		return self.speakers

	def get_audio_text(self) -> str:
		return self.audio_text

	def get_audio_speaker(self) -> str:
		return self.audio_speaker
	
	def get_audio_dir(self) -> str:
		return self.audio_dir

	def get_audio_path(self) -> str:
		return self.audio_path

	def get_join(self) -> bool:
		return self.join

	def get_replace(self) -> dict:
		return self.replace

	def get_is_generate(self) -> bool:
		return self.is_generate
	
	def get_hight_tone(self) -> int:
		return self.hight_tone

	def get_audio_speed(self) -> int:
		return self.audio_speed
