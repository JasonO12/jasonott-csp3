def fibonacci(n):
  # sets the first two values in the fibonacci sequence to remove errors
  a = 1
  print(a)
  b = 1
  print(b)
  i = 2
   # starts the loop to display each value in the fibonacci sequence for n
  while i < n:
    # introduces k variable to act as a temp
    k = b
    b = a + b
    a = k
    print(b)

    # iterates each integer until n
    i += 1
  return

def fibonacci_tester():
  n = int(input("Enter Value for Fibonoacci: "))
  fibonacci(n)
  # runs the function
  


