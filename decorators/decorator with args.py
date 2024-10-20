
def prefix_decorator(prefix):
    def decorator_function(original_function):
        # def wrapper_function():
        #     print("wrapper executed this before {} function".format(
        #         original_function.__name__))
        #     return original_function()
        def wrapper_function(*args, **kwargs):
            print(prefix, " wrapper executed this before {} function".format(
                original_function.__name__))
            return original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function

# If a funtion with arguments is decorated with a funtion which doesn't accept have will throw an error


@prefix_decorator('display-prefix')
def display(name, age):
    print('displaying funtion args {} {}'.format(name, age))


display('anil', 23)
