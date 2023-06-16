import os
import pickle
import dill
import threading

if __name__ == "__main__":
	exit()


class SaverLoaderMain:
	def __init__(self, obj, path_to_obj):
		self.obj = obj
		self.path_to_obj = path_to_obj
	
	def load(self):
		if os.path.exists(self.path_to_obj):
			with open(self.path_to_obj, 'rb') as file:
				self.obj = dill.load(file)
			return self.obj
		else:
			self.save()
	
	def set_obj(self, obj):
		self.obj = obj

	def save(self):
		print("pzdc")
		self.locker = { 'data': self.obj, 'lock': threading.Lock() }
		with open(self.path_to_obj, 'wb') as file:
			dill.dump(self.locker, file)
