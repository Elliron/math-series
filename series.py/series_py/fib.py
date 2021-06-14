
def fibonacci(n):
  """
  The function will be a fibonacci sequence
  The function will have one parameter called n
  The function will do a recursive call
  The function will return the nth value.

  0 + 1 1 2 3 5 8
  """
  
  if n < 0:
    print("Incorrect")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


    # recursive(5)
    # 5 + 4 + 3 + 2 + 1 + 0

    # return 5+ recursive(5-1)
    #return 4+ recursive(4-1)


def lucas(n):
  """
  The function will be a lucas sequence
  The function will have one parameter called n
  The function will be recursive
  The function will return the nth value
  """
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else: 
    return lucas(n-1) + lucas(n-2)


  # Lucas Iteration
  # a = 2
  # b = 1

  # if (n == 0) :
  #   return a
  
  # for i in range(2, n + 1) :
  #   c = a + b
  #   a = b
  #   b = c

  # return b

def sum_series(n, a = 0, b = 1):
  """
  The function will determine which sequence to run
  The function with have one required parameter and two optional ones
  The required parameter will determine the element in the series to print
  The optional parameters will default to 0 and 1.
  The optional parameters will determine the first two values.
  Calling the function with no optional paramaters will produce fibonacci.
  Calling the function with optional parameters will produce values from the lucas series.
  """
  if n == 0:
    return a
  elif n == 1:
    return b
  else:
    return sum_series(n-1, a, b) + sum_series(n-2, a, b)