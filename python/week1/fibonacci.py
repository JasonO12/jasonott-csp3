def fibonacci(n):
  a = 1
  print(a)
  b = 1
  print(b)
  i = 2
  while i < n:
    k = b
    b = a + b
    a = k
    print(b)
    
    i += 1
  return

def fibonacci_tester():
  n = int(input("Enter Value for Fibonoacci: "))
  fibonacci(n)
  


