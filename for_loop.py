#!/usr/bin/python

def main():
    string1 = 'abc'
    string2 = 'A \
               B \
               C'
    print string2
    for value in string1:
        print value
#        print value,
    lst = [1,2,3,4]
    print '\n'
    for item in lst:
        print item

if __name__ == '__main__':
    main()
