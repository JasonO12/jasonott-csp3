import random
import time
import os

# function that has the player guess a number 1-10 each time the game is played. global choice can be referenced.
def rowTest():
  global choice
  choice = int(input("Enter Your Number of Marbles (1-10): ")) 
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

# defines player/computer lists for score and past guesses. values are added to the list after each round of the game.
pscoreList = []
cscoreList = []
ppastList = []
cpastList = []

# function for the computer's guessing of odd or even.
def aiguessfunc():
  global aiguess
  aiguess = random.randint(1,2)

# function for analyzing the players guess of odd or even. asks the player to try again if they type anything other than odd or even. 
def guessanalyze():
  global guess
  guess = input("Do you think the computer chose an even or odd number of numbers?").lower()
  if guess == 'odd' or guess == 'even':
    return
  else: 
    print("Please type either odd or even.")
    guessanalyze()

# function to end the round and clear the board.
def endfunc():
   end = input("Play again? (yes/no):").lower()
   if end == 'yes':
     gamefunc()
   elif end == 'no':
     os.system("clear")
     return
   else:
     print("Please type yes or no.")
     endfunc()

# function that lists past player guesses at the top banner.
def ppast():
  print("Your Past Inputs:")
  for item in ppastList:
    print(item, end=", ")

# function that lists past computer guesses at the top banner.
def cpast():
  print("Computer's Past Inputs:")
  for item in cpastList:
    print(item, end=", ")

# runs the game.
def gamefunc():
  os.system("clear")
  
  print("=" * 30, "\nYour Score:", len(pscoreList), "\nComputer's Score:", len(cscoreList))
  print("=" * 30)
  ppast()
  print("")
  cpast()
  print("")
  print("=" * 30)
  
  rowTest()
  
  print("...")
  time.sleep(0.75)
  
  print("The Computer has selected a number of marbles.")
  
  print("...")
  time.sleep(0.75)

  guessanalyze()
  
  print("...")
  time.sleep(0.75)
  
  print("The Computer has guessed even or odd.")
  aiguessfunc()
  
  print("...")
  time.sleep(0.75)

  # shows your marbles and the computers marbles visually, with the computers marbles being random each time the game is played.
  print("Here is the current playing field:")
  print("Your Marbles:        ", choice * "⦿ ", choice)
  print("Computer's Marbles:  ", aimarblefunc() * "⦿ ", value)

  print("...")
  time.sleep(1.5)

  if guess == 'odd':
    print("Your guess was: Odd")
  else:
    print("Your guess was: Even")


  # this determines if you guessed right or not.
  if guess == 'odd' and value % 2 != 0 or guess == 'even' and value % 2 == 0:
    print("You Guessed Correctly!")
    # adds the number to the defined list if you guess right, so the length of that list can be analyzed to determine your score.
    pscoreList.append(choice)
  else:
    print("You Guessed Incorrectly!")

  print("...")
  time.sleep(0.75)
  
  # computer guess function same as player guess function
  if aiguess == 1:
    print("The Computer's guess was: Odd")
  else:
    print("The Computer's guess was: Even")

  # this determines if computer guessed right or not.
  if aiguess == 1 and choice % 2 != 0 or aiguess == 2 and choice % 2 == 0:
    print("The Computer Guessed Correctly!")
    # adds the number to the defined list if you guess right, so the length of that list can be analyzed to determine your score.
    cscoreList.append(value)
  else:
    print("The Computer Guessed Incorrectly!")

  print("...")
  time.sleep(0.75)

  ppastList.append(choice)
  cpastList.append(value)

  endfunc()

if __name__ == "__main__":
    gamefunc()

