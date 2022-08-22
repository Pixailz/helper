# ft_helper

Helper to make life easier, and effiency btw

## TODO

1. maybe make c_files dictionary to add:
	- header in it
	- path
	- function in it
2. get_header_all_files()

## TIPS

> 40 function in philo folder

> 17 c files

> better view of data https://jsonformatter.curiousconcept.com

> `\cp -r ../ft_helper ./scripts && ./scripts/ft_helper`

> current data

```json
{
	"philo/philosophers.c":[
		"philosophers.h",
		[
			"int\tmain(int argc, char **argv)"
		]
	],
	"philo/debug/debug.c":[
		"philosophers.h",
		[
			"void\tdebug_print_initial_config(t_main *config)",
			"void\tdebug_print_elapsed(t_stamp current_ts)"
		]
	],
	"philo/dataset/parse.c":[
		"philosophers.h",
		[
			"int\tparse_is_empty(t_main *config, char **argv)",
			"int\tparse_is_numeric(t_main *config, char **argv)",
			"int\tparse_is_good_number(t_main *config, char **argv)",
			"int\tparse(t_main *config, char **argv)"
		]
	],
	"philo/dataset/free.c":[
		"philosophers.h",
		[
			"void\tfree_philos(t_main *config)",
			"void\tfree_forks(t_main *config)",
			"void\tdestroy_mutex(t_main *config)",
			"void\tfree_entry(t_main *config)"
		]
	],
	"philo/dataset/init.c":[
		"philosophers.h",
		[
			"void\tinit_config(t_main *config, char **argv)",
			"int\tinit_philos(t_main *config)",
			"int\tinit_forks(t_main *config)",
			"int\tinit_mutex(t_main *config)",
			"int\tinit_entry(t_main *config, char **argv)"
		]
	],
	"philo/world/utils.c":[
		"philosophers.h",
		[
			"void\tft_lock_both(t_main *config)",
			"void\tft_unlock_both(t_main *config)"
		]
	],
	"philo/world/sleep_ng.c":[
		"philosophers.h",
		[
			"void\tsleep_ng(t_philo *philo, t_stamp begin, t_stamp time_to_wait)"
		]
	],
	"philo/world/solitary_life_manager.c":[
		"philosophers.h",
		[
			"void\t*solo_life(void *void_philo)",
			"int\tsolo_life_manager(t_main *config)"
		]
	],
	"philo/world/life_manager.c":[
		"philosophers.h",
		[
			"int\tcheck_all_good(t_philo *philo)",
			"void\tcycle_of_life(t_philo *philo)",
			"void\t*life(void *void_philo)",
			"int\tlife_manager(t_main *config)"
		]
	],
	"philo/world/say.c":[
		"philosophers.h",
		[
			"void\tsay(t_philo *philo, char *action)"
		]
	],
	"philo/world/eat.c":[
		"philosophers.h",
		[
			"void\ttake_forks(t_philo *philo)",
			"void\teat(t_philo *philo)"
		]
	],
	"philo/world/death.c":[
		"philosophers.h",
		[
			"void\tcheck_starving(t_philo *philo)",
			"void\tcheck_all_ate(t_philo *philo, int *nb_eat)",
			"void\t*death(void *void_config)"
		]
	],
	"philo/utils/ft_isnum.c":[
		"philosophers.h",
		[
			"int\tft_isnumeric(const char *str)"
		]
	],
	"philo/utils/ft_get_timestamp_ms.c":[
		"philosophers.h",
		[
			"t_stamp\tft_get_timestamp_ms(void)"
		]
	],
	"philo/utils/ft_atol.c":[
		"philosophers.h",
		[
			"long int\tft_atol(const char *str)"
		]
	],
	"philo/utils/ft_strlen.c":[
		"philosophers.h",
		[
			"int\tft_strlen(const char *str)"
		]
	],
	"philo/utils/ft_error.c":[
		"philosophers.h",
		[
			"int\tft_putstr_strderr(const char *msg)",
			"int\terror_parse(int ret_code)",
			"int\terror_init2(int return_code)",
			"int\terror_init(int return_code)",
			"int\terror_life(int return_code)"
		]
	]
}
```

## requirements.txt

> to output installed package to requirements.txt
`pip freeze`
