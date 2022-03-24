class Factorial:
  def __init__(self):
        self.factSeq = [1, 1]
  # Factorial of a number using recursion
  def __call__(self, n):
      if n == 1 or n == 0:
          return self.factSeq[n]
      else:
        fact_num = n * self(n-1)
        self.factSeq.append(fact_num)
      return self.factSeq[n]
  

def fact_tester():
  fact_of = Factorial()
  print(" 10 factorial is", fact_of(10))
  