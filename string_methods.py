#!/usr/bin/python


def main():
    name = 'Abc'
    print(name.lower())
    print(name.upper())
    print(name.isalpha())

    if name.isalpha():
        print(name+' contains only alphabets')
    else:
        print(name+' contains non alphabets')

# Check whether a string is digit or not

    digits = '1234a'
    print(digits.isdigit())

# Join method

    lst = ['1', '2', '3', '4']
    b = '-'
    print(b.join(lst))

# Center aligns the given string

    a = 'abc'
    print(a.center(5, '-'))

# Split a given string with specified delimiter

    a = 'aaa.bbb.ccc'
    print(a.split('.'))

# Check whether given string is blank or not

    a = ' '
    a.isspace()

# Check whether a string starts or ends with a another string

    a = 'ABC'
    print(a.startswith('A'))
    print(a.endswith('d'))


# find a substring

    a = 'abcd'
    print(a.find('c'))

# Replace a particular string

    a = 'abcdc'
    print(a.replace('c', 'e'))


if __name__ == '__main__':
    main()
