from modules import *

from modules import __CWD__

class	Makefile():
	def	__init__(self, makefile, src_dir):
		self.makefile = os.path.join(__CWD__, makefile)
		self.src_dir = os.path.join(__CWD__, src_dir)
		log.print(f"Makefile target{a.SEP}{self.makefile}", p.DEBUG, 1)
		log.print(f"Makefile src   {a.SEP}{self.src_dir}", p.DEBUG, 1)
		self.makefile_var = []

	def	add_var(self, var, folder=None):
		log.print(f"{var}{a.SEP}{folder}", p.DEBUG, 1)
		self.makefile_var.append({var: folder})

	def	format_src(self, var, *srcs):
		srcs = [ item for item in sorted(srcs) ]
		formated = []
		formated.append(f"{var} := {srcs[0]}")
		if (len(srcs) != 1):
			srcs.pop(0)
			var_len = len(var) + 4
			tab_str = '\t' * int(var_len / 4) + ' ' * (var_len % 4)
			formated[0] += " \\"
			for item in srcs:
				formated.append(f"{tab_str}{item} \\")
		last_id = len(formated) - 1
		formated[last_id] = formated[last_id].removesuffix(" \\")
		formated = [ item + '\n' for item in formated ]
		formated[last_id] = formated[last_id].removesuffix('\n')
		formated = ''.join(formated)
		log.print(f"[{var}] formated\n{formated}", p.DEBUG, 2)
		return formated

	def	get_src(self, var, folder):
		if folder:
			target_dir = os.path.join(self.src_dir, folder)
		else:
			target_dir = self.src_dir
		log.print(f"target dir{a.SEP}[{target_dir}]", p.DEBUG, 1)
		files = []
		for (dirpath, dirname, filename) in os.walk(target_dir):
			for file in filename:
				file_path = f"{dirpath}/{file}".removeprefix(self.src_dir + '/')
				log.print(f"file found [{file_path}]", p.DEBUG, 3)
				files.append(file_path)
		log.print(f"[{a.GRE}{len(files)}{a.RST}] file found for "
				  f"[{a.YEL}{var}{a.RST}]", p.SUCCESS)
		return (self.format_src(var, *files))

	def	update_makefile(self):
		with open(self.makefile, 'r') as f:
			self.makefile_str = f.read()
		for item in self.makefile_var:
			for var, folder in item.items():
				from_replace = reg.get_var_make(var, self.makefile_str)
				if not from_replace:
					log.print(f"[{var}] not found", p.WARN)
					continue
				to_replace = self.get_src(var, folder)
				self.makefile_str = self.makefile_str.replace(from_replace, to_replace)
		log.print(f"[{self.makefile}] formated\n{self.makefile_str}", p.DEBUG, 4)
		with open(self.makefile, 'w') as f:
			f.write(self.makefile_str)
