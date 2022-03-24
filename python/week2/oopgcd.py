class GCD:
  def __init__(self):
        self.gcdSeq = []
  # Factorial of a number using recursion
  def __call__(self, a, b):
      if a == 0:
          return a
      while b != 0:
        if a > b:
          a = a - b
        else:
            b = b - a
      return a # self.gcdSeq[a]

  

def gcd_tester():
  a = 342
  b = 114
  gcd_of = GCD()
  print("GCD of", a, "and", b, "is", gcd_of(a, b))
  