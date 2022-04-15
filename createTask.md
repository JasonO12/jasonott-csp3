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
```
 
#### 3b iii.

- 

#### 3b iv.

- 

#### 3b v.

- 

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


