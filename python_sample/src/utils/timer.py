import time

class Timer:
	def __init__(self):
		self.__paused=False
		self.__start_time=time.perf_counter()
		self.__elapsed_paused=0

	def pause(self):
		if self.__paused:
			return
		self.__paused=True
		self.__pause_start=time.perf_counter()

	def resume(self):
		if not self.__paused:
			return
		self.__paused=False
		self.__elapsed_paused+=time.perf_counter()-self.__pause_start

	@property
	def elapsed(self):
		if self.__paused:
			return int((self.__pause_start-self.__start_time-self.__elapsed_paused)*1000)
		return int((time.perf_counter()-self.__start_time-self.__elapsed_paused)*1000)

	def restart(self):
		self.__paused=False
		self.__start_time=time.perf_counter()
		self.__elapsed_paused=0
