import os
import sys

def odd_even():
  try:

    number = int(input('Enter a numero:'))
    if number % 2 == 0:
      print('Number is even')
    else:
      print('Number is odd')


  except(ValueError):
    print('Not a number broseph')

  if __name__ == '__main__':
    odd_even()
    os.execv(__file__, sys.argv)