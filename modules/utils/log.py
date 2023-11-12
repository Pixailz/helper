from modules import *

from modules import __DEBUG__
from modules import __HELPER_DIR__

class	p(enum.Enum):
	INFO	= 0
	DEBUG	= 1
	WARN	= 2
	SUCCESS	= 3
	FAILURE	= 4
	RAW		= 5

class	Log():

	def	__init__(self):
		self.log_file = None

	def	set_log_file(self, log_file):
		if not log_file:
			return
		self.log_file = os.path.join(__HELPER_DIR__, log_file + ".log")
		date = datetime.now().strftime("%d-%m-%Y - %H:%M:%S")
		self.print("New run " + date)

	@staticmethod
	def	get_caller(index = 0):
		previous_frame = inspect.stack()[1 + index]
		filename = os.path.basename(previous_frame.filename)
		position = f"{previous_frame.lineno}"
		return (f"{filename}|{previous_frame.function}:{position}")

	def	print(self, msg, mode = p.INFO, level = 0, in_out = 3):
		if mode == p.DEBUG:
			if (__DEBUG__ != -1 and level > __DEBUG__) or __DEBUG__ == 0:
				return
		match mode:
			case p.INFO:
				title_color = a.CYA
				title_str = "*"
			case p.DEBUG:
				title_color = a.BLU
				title_str = "+"
			case p.WARN:
				title_color = a.ORA
				title_str = "!"
			case p.SUCCESS:
				title_color = a.GRE
				title_str = "+"
			case p.FAILURE:
				title_color = a.RED
				title_str = "-"
			case p.RAW:
				title_color = ""
				title_str = ""

		if in_out == 1 or in_out == 3:
			header = f"[{a.RED}{level}{a.RST}]" if __DEBUG__ else ""
			header += f"[{a.BOL}{title_color}{title_str}{a.RST}]"
			if mode == p.RAW:
				text = msg
			else:
				text = header + a.SEP + msg
			print(text)

		if in_out == 2 or in_out == 3:
			if self.log_file != None:
				header = f"[{a.RED}{level}{a.RST}]" if __DEBUG__ else ""
				header += f"[{a.BOL}{title_color}{title_str}{a.RST}]"
				header += f"[{a.ITA}" + title_color + Log.get_caller(1) + a.RST + "]"
				if mode == p.RAW:
					text = msg
				else:
					text = header + a.SEP + msg
				with open(self.log_file, "a") as f:
					f.write(text + '\n')

log = Log()
