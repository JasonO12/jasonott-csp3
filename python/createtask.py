import random
import time

# function that has the player guess a number 1-10 each time the game is played. global choice can be referenced.
def rowTest():
  global choice
  choice = int(input("Enter Your Number of Marbles: ")) 
  if 0 < choice <= 10:
    return(choice)
  else:
    print("=" * 20)
    print("Must choose a number of marbles 1-10")
    print("=" * 20)
    rowTest()
    
# function that has the computer randomly guess a number each time the game is played. global value can be referenced.
def aimarblefunc():
  global value
  value = random.randint(1, 10)
  return(value)
  

guessList = ["Odd", "Even"]
scoreList = []


def gamefunc():
  print("=" * 20)
  rowTest()
  
  print("...")
  time.sleep(0.75)
  
  print("The Computer has selected.")
  
  print("...")
  time.sleep(0.75)
  
  guess = input("Will you guess odd or even?").lower()
  
  print("...")
  time.sleep(0.75)
  
  print("The Computer has guessed.")
  
  print("...")
  time.sleep(0.75)

  # shows your marbles and the computers marbles visually, with the computers marbles being random each time the game is played.
  print("Here is the current playing field:")
  print("Your Marbles:        ", choice * "⦿ ", choice)
  print("Computer's Marbles:  ", aimarblefunc() * "⦿ ", value)

  print("...")
  time.sleep(1.5)

  # restates the players original guess
  if guess == 'odd':
    print("Your guess was:", guessList[0])
  elif guess == 'even':
    print("Your guess was:", guessList[1])
  else:
    print("Please type either odd or even.")

  # this determines if you guessed right or not.
  if guess == 'odd' and value % 2 != 0 or guess == 'even' and value % 2 == 0:
    print("You Guessed Correctly!")
    # adds the number to the defined list if you guess right, so the length of that list can be analyzed to determine your score.
    scoreList.append(value)
  else:
    print("You Guessed Incorrectly!")


if __name__ == "__main__":
    gamefunc()

# find potential while loops
# implement scoring system at the top
# make a banner that displays score that doesnt go away
# find out how to clear the game