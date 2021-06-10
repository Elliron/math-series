
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
  The function will iterate
  The function will return the nth value
  """

  a = 2
  b = 1

  if (n==0) :
    return a
  
  for i in range(2, n + 1) :
    c = a + b
    a = b
    b = c

  return b