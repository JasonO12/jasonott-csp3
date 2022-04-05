def rowTest(choice):
  if 0 < choice <= 10:
    print("•" * (choice))
  else:
    print("=" * 20)
    print("Must choose a number of marbles 1-10")
    print("=" * 20)

def marblefunc():
  print("=" * 20)
  choice = int(input("Enter Number of Marbles: "))
  rowTest(choice)

