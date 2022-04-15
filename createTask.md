{% include navbar.html %}

# Create Task Outline

## Plan

My plan is to make a marbles game where a player plays against a computer. The player and the computer will each select a number of marbles 1-10, and they will then each guess if the other selected an even or odd number of marbles. If the player is right, they get a point displayed on a scoreboard at the top of the page. The same applies for the computer. The past inputs for number of marbles for both the player and computer are also listed at the top of the page using lists that get values appended to them.

## Runtime

Type '1' in this menu to view my create task program.

{% include replitembed.html %}

## Written Response

#### 3a i.

- The overall purpose of the program is to create a game where a player will face a computer. A player will input a number of marbles, and the computer will also select a number of marbles. The player will then guess if the computer chose an odd or even number of marbles, as will the computer. If the player is right, they get a point, and if the computer is right, it gets a point. The scoreboard is displayed at the top of the page, as is a list of past inputs from the player and computer. 

#### 3a ii.

- 

#### 3a iii. 

- 

#### 3b i.

- Lists are defined and empty, and if the player/computer is right, their guess is added to their respective list:

``` python
pscoreList = []
cscoreList = []

if guess == 'odd' and value % 2 != 0 or guess == 'even' and value % 2 == 0:
    print("You Guessed Correctly!")
    # adds the number to the defined list if you guess right, so the length of that list can be analyzed to determine your score.
    pscoreList.append(choice)
  else:
    print("You Guessed Incorrectly!")

if aiguess == 1 and choice % 2 != 0 or aiguess == 2 and choice % 2 == 0:
    print("The Computer Guessed Correctly!")
    # adds the number to the defined list if you guess right, so the length of that list can be analyzed to determine your score.
    cscoreList.append(value)
  else:
    print("The Computer Guessed Incorrectly!")
```

#### 3b ii.
 
- Items in the lists being used:

``` python
# runs the game.
def gamefunc():
  os.system("clear")
  
  print("=" * 30, "\nYour Score:", len(pscoreList), "\nComputer's Score:", len(cscoreList))
```
 
#### 3b iii.

- The names of the lists in this response are pscoreList and cscoreList, representing the player's score list and the computer's score list.

#### 3b iv.

- The data that is appended to these lists are the past guesses of the player and the computer, but they are only appended when a point is awarded. Each item in the list represents a point for the player/computer.

#### 3b v.

- These lists are essential for the tallying of the points for the player and the computer after each round of the game. As the score is determined by analyzing the length of each list, the game would cease to have a working scoreboard without them, and would therefore be less interesting. Without the use of these lists, the player would have to keep score manually or not at all, or the code may be potentially rewritten using conditionals. 

#### 3c i.

- 

#### 3c ii.

- 

#### 3c iii.

- 

#### 3c iv.

- 

#### 3d i.

- 

#### 3d ii.

- 

#### 3d iii.

- 


