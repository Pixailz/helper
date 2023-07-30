#!/usr/bin/env python3

from modules.log import log, p, a

import re

class	RegexFinder():

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
