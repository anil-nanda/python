# A decorator is a function that takes another function as argument and adds some kind of funtionality and returns another function without altering the source code of original

def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {} function".format(
            original_function.__name__))
        return original_function()
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)

decorated_display()


# below syntax is same as defining display1 = decorator_function(display1)


@decorator_function
def display1():
    print('display1 funtion ran')


display1()
