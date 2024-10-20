def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    # Having () at the end of func executes the function
    return inner_func()


def outer_func1(msg):
    message = msg

    def inner_func1(name):
        print(message+' '+name)

    # Having () at the end of func executes the function
    return inner_func1


msg1 = outer_func1('Hi')
msg1('anil')

msg2 = outer_func1('Hello')
msg2('anil')
