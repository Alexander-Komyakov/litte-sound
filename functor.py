if __name__ == "__main__":
	exit()

class Functor:
	def __call__(self, *args, **kwargs):
		if str(type(args[0])) != "<class 'function'>":
			raise Exception("class Functor: first arg function, your arg not function")
		if len(args) > 1:
			args[0](*args)
		else:
			args[0]()
