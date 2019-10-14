#!/usr/bin/python

def repeat(string,exclaim):
    result = string+string+string
    if exclaim:
        result = result+' !!!'
    return result

def main():
    output = repeat('Yahoo',False)
    print output


if __name__ == '__main__':
    main()
