import logging

logging.basicConfig(filename='log.log', level=logging.INFO)
logging.debug("hello")


def log_func(func):
    def inner_log_func(*args):
        logging.info("Running '{}' info with arguments".format(func.__name__, args))
        print(func(*args))

    return inner_log_func


def add(x, y): return x + y


def sub(x, y): return x - y


func_add_log = log_func(add)
logging.info(func_add_log)
func_sub_log = log_func(sub)

func_add_log(2,5)
func_sub_log(4,2)
