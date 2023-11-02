# helper

[![CI/CD](https://github.com/Pixailz/helper/actions/workflows/CI.yml/badge.svg)](https://github.com/Pixailz/helper/actions/workflows/CI.yml)

Helper to make life easier, and effiency btw

## TODO

1. commented section
	- commented section of code with `/**/`
	- causing to add those prototype even "if there is not here"
1. write usage

1. integrate Header module (aka CON)
	1. [x] first check if the code is norminette approved :)
	1. [x] identify header recursivly
		1. [x] it should search for header in the system
		1. [x] make a dependency tree
			1. [x] identify function
			1. [x] types
			1. [x] defines
			1. [x] typedef
	1. [x] merge depency tree (DSF)
	1. [ ] search for function, types, and other defines in each source file and
	check if the header is needed, according to the dependency tree

## requirements.txt

> to output required package to requirements.txt

```bash
pip install pipreqs
#then
pipreqs path/to/project
```
