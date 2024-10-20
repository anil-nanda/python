from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper_func(*args, **kwargs):
        logging.info('Ran with args: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper_func


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in: {} secs'.format(orig_func.__name__, t2))
        return result
    return wrapper


# below statement is same as display=my_timer(my_logger(display))

@my_logger
@my_timer
def display(name, age):
    print("display ran for {} {}".format(name, age))


display('anil', 23)
