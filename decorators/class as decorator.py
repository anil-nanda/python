class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(
            self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display(name, age):
    print('displat function ran with args {} {}'.format(name, age))


display('anil', 23)
