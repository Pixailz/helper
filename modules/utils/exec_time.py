from modules import *

class	TimerMode(enum.Enum):
	NORM	= 1
	MONO	= 2
	PERF	= 3
	PROC	= 4

class	Timer():
	def	__init__(self, mode=TimerMode.NORM):
		self._mode = mode

		self._begin = None
		self._end = None

	def	begin(self):
		self._begin = self.now()

	def	end(self):
		self._end = self.now()

	def	now(self) -> int:
		value = None
		match self._mode:
			case TimerMode.NORM:
				value = time.time_ns()
			case TimerMode.MONO:
				value = time.monotonic_ns()
			case TimerMode.PROC:
				value = time.process_time_ns()
			case TimerMode.PERF:
				value = time.perf_counter_ns()
		return value

	def	elapsed(self) -> int:
		elapsed_time = self._end - self._begin
		# elapsed_time = round(elapsed_time, 3)
		return elapsed_time

timer = Timer()
