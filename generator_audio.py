#!/usr/bin/env python3

import os
import torch
import sys
import threading
import asyncio


if __name__ == "__main__":
	exit()


class GeneratorAudio:
	def __init__(self, model_file="model.pt", sample_rate=48000):
		self.sample_rate = sample_rate
		self.standart_speakers = ["aidar", "baya", "xenia", "kseniya", "eugene"]
		self.speaker = self.standart_speakers[0]
		self.text = "<speak> </speak>"

		self.model_file = model_file
		self.model_url = 'https://models.silero.ai/models/tts/ru/v3_1_ru.pt'
		self.threads = []

	def get_speakers(self):
		return self.standart_speakers

	def set_audio_path(self, path):
		self.audio_path = path

	def set_text(self, text: str):
		self.text = text
	
	def download_model(self):
		if not os.path.isfile(self.model_file):
			torch.hub.download_url_to_file(self.model_url,
											self.model_file)

		self.model = torch.package.PackageImporter(self.model_file).load_pickle("tts_models", "model")
		self.device = torch.device('cpu')
		torch.set_num_threads(8)
		self.model.to(self.device)
		self.put_accent = True
		self.put_yo = True
	

	def generate_audio(self):
		self.download_model()
		self.audio_wav = self.model.save_wav(ssml_text=self.text,
										audio_path=self.audio_path,
										speaker=self.speaker,
										sample_rate=self.sample_rate,
										put_accent=self.put_accent,
										put_yo=self.put_yo)
	
	def thread_generate_audio(self, text="", speaker="aidar"):
		self.text = "<speak>"+text+"</speak>"
		self.speaker = speaker
		self.threads.append(threading.Thread(target=self.generate_audio(), args=[1]))
		print("start thread")
		self.threads[-1].start()
		print("end thread")
