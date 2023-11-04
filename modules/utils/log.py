from modules import *

class	p(enum.Enum):
	INFO	= 0
	DEBUG	= 1
	WARN	= 2
	SUCCESS	= 3
	FAILURE	= 4

class	a():
	ESC		= "\x1b"

	BLACK		= f"{ESC}[30"
	RED			= f"{ESC}[31m"
	GREEN		= f"{ESC}[32m"
	YELLOW		= f"{ESC}[33m"
	BLUE		= f"{ESC}[34m"
	PURPLE		= f"{ESC}[35m"
	CYAN		= f"{ESC}[36m"
	WHITE		= f"{ESC}[37m"

	RST			= f"{ESC}[0m"
	BOLD		= f"{ESC}[1m"
	ITALIC		= f"{ESC}[3m"
	UNDERLINE	= f"{ESC}[4m"
	BLINKING	= f"{ESC}[5m"
	SEP			= f"{RED}|{RST}"

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
			if (DEBUG != -1 and level > DEBUG) or DEBUG == 0:
				return
		match mode:
			case p.INFO:
				title_color = a.CYAN
				title_str = "INFO"
			case p.DEBUG:
				title_color = a.BLUE
				title_str = "DEBUG"
			case p.WARN:
				title_color = a.YELLOW
				title_str = "WARN"
			case p.SUCCESS:
				title_color = a.GREEN
				title_str = "PASS"
			case p.FAILURE:
				title_color = a.RED
				title_str = "FAIL"
		header = f"[{a.RED}{level}{a.RST}]" if DEBUG else ""
		header += f"[{a.BOLD}{title_color}{title_str}{a.RST}]"
		header += f"[{a.ITALIC}" + title_color + Log.get_caller(1) + a.RST + "]"
		print(header + a.SEP + msg)

log = Log()
