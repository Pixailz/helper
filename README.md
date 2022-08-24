# ft_helper

Helper to make life easier, and effiency btw

## TODO

1. make things clear
	- prototype work fine
	- src_makefile lil' bit messy, rewrite all the things
		1. get string to replace from
		2. get string to replace
		3. replace in str
		4. rewrite file

## TIPS

> better view of data https://jsonformatter.curiousconcept.com

> `\cp -r ../ft_helper ./scripts && ./scripts/ft_helper`

### CONFIGS

```python
# philosophers
config = {
	"makefile":		"philo/Makefile",
	"makefile_var":	"SRC_C",
	"header":		"philo/philosophers.h",
	"src_folder":	"philo"
}
philo = ft_helper(**config)

config = {
	"makefile":		"philo_bonus/Makefile",
	"makefile_var":	"SRC_C",
	"header":		"philo_bonus/philosophers_bonus.h",
	"src_folder":	"philo_bonus"
}
philo_bonus = ft_helper(**config)

# ft_libft
config = {
	"makefile":				"Makefile",
	"makefile_var":			"SRC_CHK",
	"header":				"include/libft_check.h",
	"src_folder":			"src/check",
	"makefile_path_depth":	2
}
ft_libft_check = ft_helper(**config)

config = {
	"makefile":				"Makefile",
	"makefile_var":			"SRC_INP",
	"header":				"include/libft_input.h",
	"src_folder":			"src/input",
	"makefile_path_depth":	2
}
ft_libft_input = ft_helper(**config)

config = {
	"makefile":				"Makefile",
	"makefile_var":			"SRC_INT",
	"header":				"include/libft_integer.h",
	"src_folder":			"src/integer",
	"makefile_path_depth":	2
}
ft_libft_integer = ft_helper(**config)

config = {
	"makefile":				"Makefile",
	"makefile_var":			"SRC_LST",
	"header":				"include/libft_list.h",
	"src_folder":			"src/list",
	"makefile_path_depth":	2
}
ft_libft_list = ft_helper(**config)

config = {
	"makefile":				"Makefile",
	"makefile_var":			"SRC_MEM",
	"header":				"include/libft_memory.h",
	"src_folder":			"src/memory",
	"makefile_path_depth":	2
}
ft_libft_memory = ft_helper(**config)

config = {
	"makefile":				"Makefile",
	"makefile_var":			"SRC_PRT",
	"header":				"include/libft_print.h",
	"src_folder":			"src/print",
	"makefile_path_depth":	2
}
ft_libft_print = ft_helper(**config)

config = {
	"makefile":				"Makefile",
	"makefile_var":			"SRC_STR",
	"header":				"include/libft_string.h",
	"src_folder":			"src/string",
	"makefile_path_depth":	2
}
ft_libft_string = ft_helper(**config)
```

## requirements.txt

> to output installed package to requirements.txt
`pip freeze`
