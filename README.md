# helper

[![CI/CD](https://github.com/Pixailz/helper/actions/workflows/CI.yml/badge.svg)](https://github.com/Pixailz/helper/actions/workflows/CI.yml)

Helper to make life easier, and effiency btw

## TODO

1. commented section
	- commented section of code with `/**/`
	- causing to add those prototype even "if there is not here"
1. write usage

1. integrate Cult Of the Norm
	1. first check if the code is norminette approved :)
	1. identify header recursivly, it should search for the header in the system
	1. identify function, types and other defines, to make a dependency tree
	1. search for function, types, and other defines in each source file and check if
	the header is needed, according to the dependency tree
	1. add support for unssupported lib, Line 157
	1. debug a little to see if missing function / define in json

## requirements.txt

> to output required pac****kage to requirements.txt

```bash
pip install pipreqs
#then
pipreqs path/to/project
```
