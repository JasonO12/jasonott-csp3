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
  

guessList = ["Odd", "Even"]
pscoreList = []
cscoreList = []



def aiguessfunc():
  global aiguess
  aiguess = random.randint(1,2)


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



def gamefunc():
  os.system("clear")
  
  print("=" * 30, "\nYour Score:", len(pscoreList), "\nComputer's Score:", len(cscoreList))
  print("=" * 30)
  rowTest()
  
  print("...")
  time.sleep(0.75)
  
  print("The Computer has selected a number of marbles.")
  
  print("...")
  time.sleep(0.75)
  
  guess = input("Do you think the computer chose an even or odd number of numbers?").lower()
  
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
    pscoreList.append(value)
  else:
    print("You Guessed Incorrectly!")

  print("...")
  time.sleep(0.75)
  
  # computer guess function same as player guess function
  if aiguess == 1:
    print("The Computer's guess was:", guessList[0])
  else:
    print("The Computer's guess was:", guessList[1])


  # this determines if computer guessed right or not.
  if aiguess == 1 and choice % 2 != 0 or aiguess == 2 and choice % 2 == 0:
    print("The Computer Guessed Correctly!")
    # adds the number to the defined list if you guess right, so the length of that list can be analyzed to determine your score.
    cscoreList.append(value)
  else:
    print("The Computer Guessed Incorrectly!")

  print("...")
  time.sleep(0.75)

  endfunc()


if __name__ == "__main__":
    gamefunc()

# find potential while loops