# ft_helper

Helper to make life easier, and effiency btw

## TODO

1. make things modulable
	- like for philosophers, two folder, two makefile, two src_folder
2. make class for everything

## TIPS

> 40 function in philo folder

> 17 c files

> better view of data https://jsonformatter.curiousconcept.com

> `\cp -r ../ft_helper ./scripts && ./scripts/ft_helper`

> current data

```json
{
	"/home/pix/Documents/42/ft_helper/philosophers/philo/dataset/free.c":[
		"void\tfree_philos(t_main *config)",
		"void\tfree_forks(t_main *config)",
		"void\tdestroy_mutex(t_main *config)",
		"void\tfree_entry(t_main *config)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/dataset/init.c":[
		"void\tinit_config(t_main *config, char **argv)",
		"int\tinit_philos(t_main *config)",
		"int\tinit_forks(t_main *config)",
		"int\tinit_mutex(t_main *config)",
		"int\tinit_entry(t_main *config, char **argv)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/dataset/parse.c":[
		"int\tparse_is_empty(t_main *config, char **argv)",
		"int\tparse_is_numeric(t_main *config, char **argv)",
		"int\tparse_is_good_number(t_main *config, char **argv)",
		"int\tparse(t_main *config, char **argv)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/debug/debug.c":[
		"void\tdebug_print_initial_config(t_main *config)",
		"void\tdebug_print_elapsed(t_stamp current_ts)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/file.c":[

	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/philosophers.c":[
		"int\tmain(int argc, char **argv)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_atol.c":[
		"long int\tft_atol(const char *str)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_error.c":[
		"int\tft_putstr_strderr(const char *msg)",
		"int\terror_parse(int ret_code)",
		"int\terror_init2(int return_code)",
		"int\terror_init(int return_code)",
		"int\terror_life(int return_code)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_get_timestamp_ms.c":[
		"t_stamp\tft_get_timestamp_ms(void)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_isnum.c":[
		"int\tft_isnumeric(const char *str)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_strlen.c":[
		"size_t\tft_strlen(const char *str)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/death.c":[
		"void\tcheck_starving(t_philo *philo)",
		"void\tcheck_all_ate(t_philo *philo, int *nb_eat)",
		"void\t*death(void *void_config)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/eat.c":[
		"void\ttake_forks(t_philo *philo)",
		"void\teat(t_philo *philo)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/life_manager.c":[
		"int\tcheck_all_good(t_philo *philo)",
		"void\tcycle_of_life(t_philo *philo)",
		"void\t*life(void *void_philo)",
		"int\tlife_manager(t_main *config)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/say.c":[
		"void\tsay(t_philo *philo, char *action)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/sleep_ng.c":[
		"void\tsleep_ng(t_philo *philo, t_stamp begin, t_stamp time_to_wait)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/solitary_life_manager.c":[
		"void\t*solo_life(void *void_philo)",
		"int\tsolo_life_manager(t_main *config)"
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/utils.c":[
		"void\tft_lock_both(t_main *config)",
		"void\tft_unlock_both(t_main *config)"
	]
}
```

## requirements.txt

> to output installed package to requirements.txt
`pip freeze`
