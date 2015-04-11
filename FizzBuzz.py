import sys

if len(sys.argv) == 1:

  input = raw_input("What is the upper limit of your FizzBuzz? ")
  count = 1
  
  try:
    int(input)

    print('Fizz Buzz counting up to ' + str(input) + '.')

    while count <= int(input):
      if count % 3 == 0 and count % 5 == 0:
        print('Fizz Buzz')
      elif count % 3 == 0:
        print('Fizz')
      elif count % 5 == 0:
        print('Buzz')
      else:
        print(count)

      count += 1      
      
  except ValueError:
    print('Please provide an integer value.')
      
elif len(sys.argv) == 2:
  
  try:
    input = int(sys.argv[1])
    count = 1

    print('Fizz Buzz counting up to ' + str(input) + '.')

    while count <= int(input):
      if count % 3 == 0 and count % 5 == 0:
        print('Fizz Buzz')
      elif count % 3 == 0:
        print('Fizz')
      elif count % 5 == 0:
        print('Buzz')
      else:
        print(count)

      count += 1
  except ValueError:
    print 'Please supply an integer value as an argument.'
    
elif len(sys.argv) > 2:

  print('Please only input one argument!')