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
	"/home/pix/Documents/42/ft_helper/philosophers/philo/philosophers.c":[
		"philosophers.h",
		[
			"int\tmain(int argc, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/debug/debug.c":[
		"philosophers.h",
		[
			"void\tdebug_print_initial_config(t_main *config)",
			"void\tdebug_print_elapsed(t_stamp current_ts)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/dataset/parse.c":[
		"philosophers.h",
		[
			"int\tparse_is_empty(t_main *config, char **argv)",
			"int\tparse_is_numeric(t_main *config, char **argv)",
			"int\tparse_is_good_number(t_main *config, char **argv)",
			"int\tparse(t_main *config, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/dataset/free.c":[
		"philosophers.h",
		[
			"void\tfree_philos(t_main *config)",
			"void\tfree_forks(t_main *config)",
			"void\tdestroy_mutex(t_main *config)",
			"void\tfree_entry(t_main *config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/dataset/init.c":[
		"philosophers.h",
		[
			"void\tinit_config(t_main *config, char **argv)",
			"int\tinit_philos(t_main *config)",
			"int\tinit_forks(t_main *config)",
			"int\tinit_mutex(t_main *config)",
			"int\tinit_entry(t_main *config, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/utils.c":[
		"philosophers.h",
		[
			"void\tft_lock_both(t_main *config)",
			"void\tft_unlock_both(t_main *config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/sleep_ng.c":[
		"philosophers.h",
		[
			"void\tsleep_ng(t_philo *philo, t_stamp begin, t_stamp time_to_wait)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/solitary_life_manager.c":[
		"philosophers.h",
		[
			"void\t*solo_life(void *void_philo)",
			"int\tsolo_life_manager(t_main *config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/life_manager.c":[
		"philosophers.h",
		[
			"int\tcheck_all_good(t_philo *philo)",
			"void\tcycle_of_life(t_philo *philo)",
			"void\t*life(void *void_philo)",
			"int\tlife_manager(t_main *config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/say.c":[
		"philosophers.h",
		[
			"void\tsay(t_philo *philo, char *action)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/eat.c":[
		"philosophers.h",
		[
			"void\ttake_forks(t_philo *philo)",
			"void\teat(t_philo *philo)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/world/death.c":[
		"philosophers.h",
		[
			"void\tcheck_starving(t_philo *philo)",
			"void\tcheck_all_ate(t_philo *philo, int *nb_eat)",
			"void\t*death(void *void_config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_isnum.c":[
		"philosophers.h",
		[
			"int\tft_isnumeric(const char *str)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_get_timestamp_ms.c":[
		"philosophers.h",
		[
			"t_stamp\tft_get_timestamp_ms(void)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_atol.c":[
		"philosophers.h",
		[
			"long int\tft_atol(const char *str)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_strlen.c":[
		"philosophers.h",
		[
			"int\tft_strlen(const char *str)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo/utils/ft_error.c":[
		"philosophers.h",
		[
			"int\tft_putstr_strderr(const char *msg)",
			"int\terror_parse(int ret_code)",
			"int\terror_init2(int return_code)",
			"int\terror_init(int return_code)",
			"int\terror_life(int return_code)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/test/test1.c":[
		"None",
		[
			"void\tsay(char *msg, int id)",
			"int\tsafe_exit(int return_code)",
			"int\tchild_function(int id)",
			"void\tkill_all(pid_t *pid_table, int nb_philo)",
			"void\tmain_function(pid_t *pid_table, int nb_philo)",
			"int\tmain(int argc, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/test/test3.c":[
		"None",
		[
			"void\tfree_entry(t_test *test)",
			"void\tchild_process(t_test *test)",
			"void\tparent_process(t_test *test)",
			"void\tinit(t_test *test, int nb_child)",
			"int\tmain(int argc, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/test/test2.c":[
		"None",
		[
			"void\tsay(char *msg, int id)",
			"int\tsafe_exit(int return_code)",
			"int\tchild_function(int id)",
			"void\tmain_function(pid_t *pid_table, int nb_philo)",
			"int\tmain(int argc, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/philosophers_bonus.c":[
		"philosophers_bonus.h",
		[
			"int\tmain(int argc, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/debug/debug_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\tdebug_print_initial_config(t_main *config)",
			"void\tdebug_print_elapsed(t_stamp current_ts)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/dataset/parse_bonus.c":[
		"philosophers_bonus.h",
		[
			"int\tparse_is_empty(t_main *config, char **argv)",
			"int\tparse_is_numeric(t_main *config, char **argv)",
			"int\tparse_is_good_number(t_main *config, char **argv)",
			"int\tparse(t_main *config, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/dataset/init_bonus.c":[
		"philosophers_bonus.h",
		[
			"int\tinit_config(t_main *config, char **argv)",
			"int\tinit_philos(t_main *config)",
			"int\tcheck_semaphore_failed(t_main *config)",
			"int\tinit_semaphore(t_main *config)",
			"int\tinit_entry(t_main *config, char **argv)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/dataset/free_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\tfree_philos(t_main *config)",
			"void\tunlink_semaphore(void)",
			"void\tdestroy_semaphore(t_main *config)",
			"void\tfree_entry(t_main *config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/say_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\tsay(t_philo *philo, char *action)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/eat_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\ttake_forks(t_philo *philo)",
			"void\teat(t_philo *philo)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/utils.c":[
		"philosophers_bonus.h",
		[
			"void\tsay_dead(t_philo *philo)",
			"void\tdeath_check(t_philo *philo)",
			"void\tcheck_all_good(t_philo *philo)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/god_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\tkill_all(t_main *config)",
			"int\tcheck_all_ate(t_main *config, int philo_id)",
			"int\tcheck_pid_status(t_main *config)",
			"void\tstart_life(t_main *config)",
			"void\t*god(void *void_config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/life_manager_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\tcycle_of_life(t_philo *philo)",
			"void\tlife(t_philo *philo)",
			"int\tgod_manager(t_main *config)",
			"void\twait_for_all(t_main *config)",
			"int\tlife_manager(t_main *config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/death_bonus.c":[
		"philosophers_bonus.h",
		[
			"int\tcheck_starving(t_philo *philo)",
			"void\t*death(void *void_philo)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/sleep_ng_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\tsleep_ng(t_philo *philo, t_stamp begin, t_stamp time_to_wait)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/world/solitary_life_manager_bonus.c":[
		"philosophers_bonus.h",
		[
			"void\tsolo_life(t_philo *philo)",
			"int\tsolo_life_manager(t_main *config)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/utils/ft_get_timestamp_ms_bonus.c":[
		"philosophers_bonus.h",
		[
			"t_stamp\tft_get_timestamp_ms(void)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/utils/ft_isnum_bonus.c":[
		"philosophers_bonus.h",
		[
			"int\tft_isnumeric(const char *str)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/utils/ft_error_bonus.c":[
		"philosophers_bonus.h",
		[
			"int\tft_putstr_strderr(const char *msg)",
			"int\terror_parse(int ret_code)",
			"int\terror_init(int return_code)",
			"int\terror_life(int return_code)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/utils/ft_atol_bonus.c":[
		"philosophers_bonus.h",
		[
			"long int\tft_atol(const char *str)"
		]
	],
	"/home/pix/Documents/42/ft_helper/philosophers/philo_bonus/utils/ft_strlen_bonus.c":[
		"philosophers_bonus.h",
		[
			"int\tft_strlen(const char *str)"
		]
	]
}
```

## requirements.txt

> to output installed package to requirements.txt
`pip freeze`
