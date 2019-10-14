#!/usr/bin/python

import sys

def main():
  name = sys.argv[1]
  if name == 'Tinku':
     print 'Alert'
     name = name+'!!!'
  elif name == 'Pinku':
     name = name+' $$$'
  else:
     name = name+ '???'

  print 'Hello '+name 

  empty_string = 'abc'
  if empty_string:   #If statement will be True if the variable is not null or 0 or empty or False
     print 'Not empty'

if __name__ == '__main__':
    main()
