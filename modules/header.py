#!/usr/bin/env python3

__version__ = "1.0.2"

import json
import re
import os
import sys

class RegexFinder():
	def __init__(self):
		self.options = {
			"flags": re.MULTILINE | re.ASCII
		}
		self.compile_all_regex()

	def compile_all_regex(self):
		self.re_c_files = re.compile(r'.*\.c$', re.ASCII)
		self.re_h_files = re.compile(r'.*\.h$', re.ASCII)
		self.re_inc_lib = re.compile(r'# include <(.*)>')
		self.re_inc_hea = re.compile(r'# include "(.*)"')
		self.re_c_lib = re.compile(r'#include <(.*)>')
		self.re_c_hea = re.compile(r'#include "(.*)"')
		self.re_get_header = re.compile(r'.*/(.*\.h)')
		self.re_function_infile_1 = re.compile(
			r'^(?!static)\w+\*?\*?\s+\*?\*?(?!main\()(\w+)\(.*\);$',
			**self.options
		)
		self.re_function_infile_2 = re.compile(
			r'^(?!static)\w+\*?\*?\s+\*?\*?(?!main\()\*?\*?\s+\*?\*?(\w+)\(.*\);$',
			**self.options
		)
		self.re_function_infile_1_2 = re.compile(
			r'^(?!static)\w+\*?\*?\s+\*?\*?(?!main\()(\w+)\(.*\)$',
			**self.options
		)
		self.re_function_infile_2_2 = re.compile(
			r'^(?!static)\w+\*?\*?\s+\*?\*?(?!main\()\*?\*?\s+\*?\*?(\w+)\(.*\)$',
			**self.options
		)
		self.re_define_infile = re.compile(
			r'^#\s+define\s+(\w+)'
			r'[\s\'\"]+?\w+?[\s\'\"]+?',
			**self.options
		)
		self.re_typedef_infile = re.compile(r'(t_\w+);$', **self.options)

class PrintColor():
	def __init__(self):
		self.red = "\033[38;5;196m"
		self.green = "\033[38;5;82m"
		self.orange = "\033[38;5;214m"
		self.blue = "\033[38;5;75m"
		self.blinking = "\033[5m"
		self.reset = "\033[0m"
		self.red_minus = "[" + self.red + "-" + self.reset + "]"
		self.green_plus= "[" + self.green + "+" + self.reset + "]"
		self.orange_star = "[" + self.orange + "*" + self.reset + "]"

	def print_error(self, msg):
		print(self.red_minus + f" {msg}")

	def print_good(self, msg):
		print(self.green_plus + f" {msg}")

class CheckUselessHeader():
	def __init__(self, project_folder=None, json_file="data.json"):
		self.project_folder = project_folder
		self.json_file = self.load_json(json_file)
		self.lib = {
			"curses.h": self.json_file['curses.h'],
			"dirent.h": self.json_file['dirent.h'],
			"errno.h": self.json_file['errno.h'],
			"fcntl.h": self.json_file['fcntl.h'],
			"limits.h": self.json_file['limits.h'],
			"pthread.h": self.json_file['pthread.h'],
			"readline/history.h": self.json_file['readline/history.h'],
			"readline/readline.h": self.json_file['readline/readline.h'],
			"semaphore.h": self.json_file['semaphore.h'],
			"signal.h": self.json_file['signal.h'],
			"sys/wait.h": self.json_file['sys/wait.h'],
			"sys/types.h": self.json_file['sys/types.h'],
			"sys/stat.h": self.json_file['sys/stat.h'],
			"stdarg.h": self.json_file['stdarg.h'],
			"stddef.h":  self.json_file['stddef.h'],
			"stdint.h": self.json_file['stdint.h'],
			"stdio.h": self.json_file['stdio.h'],
			"stdlib.h": self.json_file['stdlib.h'],
			"string.h": self.json_file['string.h'],
			"unistd.h": self.json_file['unistd.h']
		}
		self.regex = RegexFinder()
		self.color = PrintColor()
		self.result = dict()
		self.get_files()
		self.append_proto_to_lib()
		self.get_library()
		self.get_lib_in_c_files()
		self.check_function_in_c_files()
		self.print_result()

	def get_proto(self, header_path):
		with open(header_path) as f:
			file_str = f.read()
		tmp_list = list()
		tmp_list.extend(self.regex.re_function_infile_1.findall(file_str))
		tmp_list.extend(self.regex.re_function_infile_2.findall(file_str))
		tmp_list.extend(self.regex.re_define_infile.findall(file_str))
		tmp_list.extend(self.regex.re_typedef_infile.findall(file_str))
		return (self.make_list_uniq(tmp_list))

	def append_proto_to_lib(self):
		for header in self.h_files:
			tmp_header = self.regex.re_get_header.findall(header)[0]
			self.lib[tmp_header] = self.get_proto(header)

	def check_flib_in_c_files(self, file_name, functions):
		with open(file_name) as f:
			file_str = f.read()
		tmp_result = list()
		current_file_function = list()
		current_file_function.extend(self.regex.re_function_infile_1_2.findall(file_str))
		current_file_function.extend(self.regex.re_function_infile_2_2.findall(file_str))
		for func in functions:
			if func not in current_file_function:
				tmp_finded = re.findall(
					r'\W' + re.escape(func) + r'\W',
					file_str,
					flags = re.MULTILINE | re.ASCII
				)
				if len(tmp_finded) != 0:
					tmp_result.append(func)
		return (tmp_result)

	def check_function_in_c_files(self):
		for c_files in self.c_files:
			self.result[c_files] = dict()
			for lib in self.c_files[c_files]:
				if lib in self.lib:
					self.result[c_files][lib] = \
						self.check_flib_in_c_files(
							c_files,
							self.lib[lib]
						)

	def load_json(self, json_file):
		"""
		load data.json nearby the CON.py
		(should be next to the script)
		"""
		data_path = os.path.abspath(os.path.dirname(__file__)) + f"/{json_file}"
		with open(data_path) as f:
			data = json.load(f)
		return (data)

	def get_files(self):
		self.files = list()
		for (dirpath, dirname, filename) in os.walk(self.project_folder):
			for file in filename:
				self.files.append(os.path.join(dirpath, file))
		self.files = sorted(self.files)
		self.c_files = { f: list()
			for f in self.files if self.regex.re_c_files.findall(f)
		}
		self.h_files = { f: list()
			for f in self.files if self.regex.re_h_files.findall(f)
		}

	def make_list_uniq(self, list_to_uniq):
		uniq_list = list()
		for elem in list_to_uniq:
			if elem not in uniq_list:
				uniq_list.append(elem)
		return (sorted(uniq_list))

	def get_library(self):
		for include in self.h_files:
			with open(include) as f:
				file_str = f.read()
			self.h_files[include] = self.regex.re_inc_lib.findall(file_str)
			self.h_files[include].extend(self.regex.re_get_header.findall(include))
		for include in self.h_files:
			with open(include) as f:
				file_str = f.read()
			for header in self.regex.re_inc_hea.findall(file_str):
				for include2 in self.h_files:
					if header in include2:
						tmp_header = include2
				self.h_files[include].extend(self.h_files[tmp_header])
		for include in self.h_files:
			self.h_files[include] = self.make_list_uniq(self.h_files[include])

	def get_lib_in_c_files(self):
		for c_files in self.c_files:
			with open(c_files) as f:
				file_str = f.read()
			self.c_files[c_files].extend(self.regex.re_c_lib.findall(file_str))
			for header in self.regex.re_c_hea.findall(file_str):
				for include in self.h_files:
					if header in include:
						tmp_include = include
				self.c_files[c_files].extend(self.h_files[tmp_include])
		for include in self.c_files:
			self.c_files[include] = self.make_list_uniq(self.c_files[include])

	def print_result(self):
		for c_files in self.result:
			need_header = 0
			for lib in self.result[c_files]:
				if len(self.result[c_files][lib]) > 0 :
					need_header = 1
					continue
			if not need_header:
				if len(self.result[c_files]) != 0:
					self.color.print_error(c_files + "\nError: USELESS_HEADER")
				else:
					self.color.print_good(c_files + ": OK!")
			else:
				self.color.print_good(c_files + ": OK!")

	def debug_print_formated_data(self):
		print("C_FILES:")
		for c_files in self.c_files:
			print(f"\t{c_files}")
			if len(self.c_files[c_files]) == 0:
				print("\t\tNone")
			else:
				for lib in self.c_files[c_files]:
					print(f"\t\t{lib}")
		print("H_FILES:")
		for h_files in self.h_files:
			print(f"\t{h_files}")
			if len(self.h_files[h_files]) == 0:
				print("\t\tNone")
			else:
				for lib in self.h_files[h_files]:
					print(f"\t\t{lib}")

	def debug_print_formated_json(self, var):
		for function in var['function']:
			print(function)

	def debug_print_formated_result(self):
		for c_files in self.result:
			print(f"{c_files}")
			for lib in self.result[c_files]:
				print(f"\t{lib}")
				for result in self.result[c_files][lib]:
					print(f"\t\t{result}")

def	write_all_json_to_file(folder_name="resource"):
	tmp_data = None
	regex = RegexFinder()
	for file in os.listdir(folder_name):
		if file.endswith(".json"):
			print(file)
			with open(os.path.join(folder_name, file)) as f:
				if tmp_data is None:
					tmp_data = json.load(f)
				else:
					tmp_data.update(json.load(f))
	with open("data.json", "w") as f:
		json.dump(tmp_data, f, indent=4)

def usage(msg=None):
	print(f"Usage: {sys.argv[0]} <PROJECT_PATH>\n"
		"\tTake only one arg: the project path, relative or absolute")
	print(f"Version: {__version__}")
	if msg is not None:
		print(f"\n\t{msg}")
	exit(1)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage("One arg needed")
	if sys.argv[1] == "--help":
		usage()
	if not os.path.isdir(sys.argv[1]):
		usage("Wrong path")
	check_useless_header = CheckUselessHeader(sys.argv[1])
