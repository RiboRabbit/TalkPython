import os
import sys
from datetime import timedelta
from time import sleep



class MustBeInt(Exception):
	pass


class Pomodoro:

	def __init__(self,hours=0,minutes=25,seconds=0):
		self.config(hours,minutes,seconds)

	def config(self,hours,minutes,seconds):
		if not isinstance(minutes,(int,float)) and not isinstance(hours,(int,float)):
			raise MustBeInt('Minutes and hours argument must be integer')
		self.duration = timedelta(hours=hours,minutes=minutes,seconds=seconds)
		self.now = self.duration

	def start(self):
		end = self.duration.seconds

		for i in reversed(range(end)):
			self.now = timedelta(seconds=i)
			sleep(1)
			self.clear()
			t = self.parse_elapsed_time()
			print(t)

	def parse_elapsed_time(self):
		sec = self.now.seconds
		return f"{sec // 3600} hours {(sec//60)%60} minutes {sec % 60} seconds elapsed"

	def clear(self):
		_ = os.system('clear' if os.name == 'posix' else 'cls')

	def __str__(self):
		return self.parse_elapsed_time()

				

if __name__ == '__main__':
	try:
		hours = int(sys.argv[1])
		minutes = int(sys.argv[2])
		seconds = int(sys.argv[3])
	except:
		raise Exception('No Argumnets provided')	
	timer = Pomodoro(hours=hours,minutes=minutes,seconds=seconds)
	print(timer)
	timer.start()	
