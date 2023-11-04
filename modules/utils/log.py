from modules import *
from modules import __DEBUG__

class	p(enum.Enum):
	INFO	= 0
	DEBUG	= 1
	WARN	= 2
	SUCCESS	= 3
	FAILURE	= 4

class	Log():

	@staticmethod
	def	get_caller(index = 0):
		previous_frame = inspect.stack()[1 + index]
		filename = os.path.basename(previous_frame.filename)
		position = f"{previous_frame.lineno}"
		return (f"{filename}|{previous_frame.function}:{position}")

	@staticmethod
	def	print(msg, mode = p.INFO, level = 0):
		if mode == p.DEBUG:
			if (__DEBUG__ != -1 and level > __DEBUG__) or __DEBUG__ == 0:
				return
		match mode:
			case p.INFO:
				title_color = a.CYA
				title_str = "INFO"
			case p.DEBUG:
				title_color = a.BLU
				title_str = "__DEBUG__"
			case p.WARN:
				title_color = a.YEL
				title_str = "WARN"
			case p.SUCCESS:
				title_color = a.GRE
				title_str = "PASS"
			case p.FAILURE:
				title_color = a.RED
				title_str = "FAIL"
		header = f"[{a.RED}{level}{a.RST}]" if __DEBUG__ else ""
		header += f"[{a.BOL}{title_color}{title_str}{a.RST}]"
		header += f"[{a.ITA}" + title_color + Log.get_caller(1) + a.RST + "]"
		print(header + a.SEP + msg)

log = Log()
