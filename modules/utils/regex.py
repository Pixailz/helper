from modules import *

class	RegexFinder():

	def	__init__(self) -> None:
		self.re_git()
		self.re_c()
		self.re_compile_proto()
		self.word = re.compile(r'\w+')

	def	re_git(self) -> None:
		re_git_name = r'^\[remote \"origin\"\]\n\s+url = (https://github\.com/|git@github\.com:).*?/(.*?)$'
		self.get_git_name = re.compile( re_git_name, re.S | re.M)

	def	re_c(self) -> None:
		self.get_src_header = re.compile( r'^// [\w/.]*?\.c$.*?;$\n\n', re.S | re.M)
		self.c_define = re.compile(r'^#\s*define\s+(\w+)', re.S | re.M)
		self.c_typedef = re.compile(r'typedef.*?(\w+);$', re.S | re.M)
		c_header_begin = r'#\s*include\s+'
		self.c_header = re.compile(c_header_begin + r'[<"](.+)[>"]')
		self.c_header_define = re.compile(r'#\s*define\s+(.*?)\s')
		self.c_enum_values = re.compile(r'enum\s+\w+?\s+?{\s+(\w.*?),?\s*}', re.S | re.M)
		self.c_enum_value = re.compile(r'\s*?(\w+).*?$', re.S | re.M)
		self.c_enum_name = re.compile(r'enum\s+(\w+)', re.S | re.M)
		self.c_compiler_inc = re.compile(
			r'<\.\.\.> search starts here:\n(.*?)End of search list\.$',
			re.S | re.M
		)

	def	re_compile_proto(self) -> None:
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
		re_param = ptr + r'(\w+)\(.*?\).*?;'
		re_proto = r'(?!static)\w+\*?\*?\*?\s+\*?\*?\*?(\w+)\s*\(.*?\).*?;'
		re_type = r'^(.*?)\s+' + t_end + r'\('
		re_not_type = r'\s+(' + t_end + r'\(.*?\))$'

		self.proto_func = re.compile(re_func, flags = re.M | re.S)
		self.proto = re.compile(re_proto, flags = re.M | re.S)
		self.proto_type = re.compile(re_type)
		self.proto_not_type = re.compile(re_not_type, flags = re.M | re.S)

	@staticmethod
	def	get_var_make(var: str, from_str: str) -> str:
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
