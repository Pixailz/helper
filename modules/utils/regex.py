from modules import *

class	RegexFinder():

	def	__init__(self):
		self.get_src_header = re.compile( r'^//.*?\.c.*?;$\n\n', re.S | re.M)
		self.re_compile_proto_func()

	def	re_compile_proto_func(self):
		ptr = r'\*?' * 3
		space = r'\s+'
		t_begin = r'\w+' + ptr
		t_between = ptr + r'\w+' + ptr + space
		t_end = ptr + r'\w+'
		re_begin = r'^(?!static)' + t_begin + space
		re_param = t_end + r'\(.*?\)$'
		re_func =	re_begin + re_param + r'|' + \
					re_begin + t_between + re_param + r'|' + \
					re_begin + t_between * 2 + re_param + r'|' + \
					re_begin + t_between * 3 + re_param
		re_type = r'^(.*?)\s+' + t_end + r'\('
		re_not_type = r'\s+(' + t_end + r'\(.*?\))$'

		self.proto_func = re.compile(re_func, flags = re.M | re.S)
		self.proto_type = re.compile(re_type)
		self.proto_not_type = re.compile(re_not_type, flags = re.M | re.S)

	@staticmethod
	def	get_var_make(var, from_str):
		re_var = re.compile(
			r'^' + re.escape(var) + r' := .*?\.c$',
			flags = re.S | re.M
		)
		re_match = re_var.search(from_str)
		log.print(f"pattern {a.SEP}{re_var.pattern}", mode=p.DEBUG, level=2)
		if not re_match:
			log.print(f"{var} not found", mode=p.WARN, level=1)
			return
		founded = re_match.group()
		log.print(f"\n{founded}", mode=p.DEBUG, level=3)
		return ''.join(founded)

reg = RegexFinder()
