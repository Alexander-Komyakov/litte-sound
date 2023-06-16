from pydub import AudioSegment


if __name__ == "__main__":
	exit()


class AudioEditor:
	def __init__(self):
		pass
	
	def split_audio(self, audio_path=[], audio_format="wav", out_path="split.wav"):
		for i in range(0, len(audio_path)):
			if i == 0:
				out_sounds = AudioSegment.from_file(file=audio_path[i], format=audio_format)
				continue 
			out_sounds = out_sounds + AudioSegment.from_file(file=audio_path[i], format=audio_format)
		out_sounds.export(out_f=out_path, format=audio_format)
