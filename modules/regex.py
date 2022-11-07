#!/usr/bin/env python3

import re

class RegexFinder():
	def __init__(self):
		self.options = {
			"flags": re.MULTILINE | re.ASCII
		}

	def compile_all_regex(self, makefile_var):
		self.compile_c_regex()
		self.compile_h_regex()
		self.compile_makefile_regex(makefile_var)

	def compile_c_regex(self, ignore_main=True):
		begin_re = r'^(?!static)\w+\*?\*?\s+\*?\*?'
		if ignore_main:
			begin_re += r'(?!main\()'
		self.functions_c_file = re.compile(
			begin_re + r'\w+\*?\*?\s+\*?\*?\w+\(.*\)$|' +
			begin_re + r'\w+?\(.*\)$',
			**self.options
		)
		self.c_files = re.compile(r'.*\.c$', re.ASCII)
		self.function_type_len = re.compile(
			r'^(\w+\*?\*?\s+|\w+\*?\*?\s+\*?\*?\w+\*?\*?\s+)\*?\*?\w*\(.*\)$',
			**self.options
		)

	def compile_h_regex(self):
		self.h_files = re.compile(r'.*\.h$', re.ASCII)
		self.headers_file = re.compile(r'^#include "(.*)"')

	def compile_makefile_regex(self, makefile_var):
		self.first_src_makefile = re.compile(
			r'^' + re.escape(makefile_var) + r'\s+:=.*\\?$',
			**self.options
		)
		self.last_src_makefile = re.compile(
			r'^\s+\w+.*\.c$',
			**self.options
		)

	def	get_src_makefile(self, file_str):
		current_line = self.first_src_makefile.findall(file_str)
		if len(current_line[0]) == 0:
			print("Error finding makefile_var")
			exit()
		elif (current_line[0][-1] != '\\'):
			return (current_line[0])
		src_makefile = current_line[0]
		current_line = re.findall(
			re.escape(src_makefile) + r'\n(\s+\w+.*\.c ?\\?)$',
			file_str,
			**self.options
		)
		if len(current_line) == 0:
			return (src_makefile)
		while current_line[0][-1] == '\\':
			src_makefile += '\n' + current_line[0]
			current_line = re.findall(
				re.escape(src_makefile) + r'\n(\s+\w+.*\.c ?\\?)$',
				file_str,
				**self.options
			)
		src_makefile += '\n' + current_line[0]
		return (src_makefile)

	def	get_file_path(self, file_path, depth):
		return (re.findall(r'/(' + (r'\w+/' * (depth - 1)) + r'\w+\.c)', \
																file_path)[0])

if __name__ == "__main__":
	regex = RegexFinder()
	regex.compile_h_regex()
	regex.compile_c_regex(ignore_main=False)
	regex.compile_makefile_regex(makefile_var="SRC_C")
	with open("./minishell/src/minishell.c", 'r') as f:
		file_str = f.read()
	finded = regex.functions_c_file.findall(file_str)
	for item in finded:
		print(item)
