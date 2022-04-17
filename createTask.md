{% include navbar.html %}

# Create Task Outline

## Plan

My plan is to make a marbles game where a player plays against a computer. The player and the computer will each select a number of marbles 1-10, and they will then each guess if the other selected an even or odd number of marbles. If the player is right, they get a point displayed on a scoreboard at the top of the page. The same applies for the computer. The past inputs for number of marbles for both the player and computer are also listed at the top of the page using lists that get values appended to them.

## Runtime

Type '1' in this menu to view my create task program.

{% include replitembed.html %}

## Written Response

#### 3a i.

- The overall purpose of the program is to create a game where a player will face a computer. A player will input a number of marbles, and the computer will also select a number of marbles. The player will then guess if the computer chose an odd or even number of marbles, as will the computer. If the player is right, they get a point, and if the computer is right, it gets a point. The scoreboard is displayed at the top of the page, as are lists of past inputs from the player and computer. 

#### 3a ii.

- 

#### 3a iii. 

- 

#### 3b i.

- Lists are defined and empty, and after the player and computer input a number of marbles, the input is added to their respective list:

``` python
ppastList = []
cpastList = []

ppastList.append(choice)
cpastList.append(cvalue)
```

#### 3b ii.
 
- Items in the lists being used:

``` python
# function that lists past player inputs at the top banner.
def ppast(n):
  iteration = range(n)
  for n in iteration:
    print(ppastList[n], end=", ")

# function that lists past computer inputs at the top banner.
def cpast():
  print("Computer's Past Inputs:")
  for item in cpastList:
    print(item, end=", ")
```
 
#### 3b iii.

- The names of the lists in this response are ```ppastList``` and ```cpastList``` (player past input list and computer past input list).

#### 3b iv.

- The data that is appended to these lists are the past guesses of the player and the computer, and they aree added after each round. Each item in the list represents a previous marble input from the player/computer. 

#### 3b v.

- These lists are essential for the displaying of the past inputs from the player and the computer after each round of the game. The list is necessary to print out all of the inputs from players, and since the player and computer will choose a variety of different numbers, the best way to store the numbers would be by appending them to an empty list. Without the use of these lists, the player would have to keep track of past inputs manually or not at all, or the code may be potentially rewritten using conditionals. The use of lists in this scenario will prove to be the most effective.

#### 3c i.

- Function for past player inputs.

``` python
# function that lists past player inputs at the top banner.
def ppast(n):
  iteration = range(n)
  for n in iteration:
    print(ppastList[n], end=", ")
```

#### 3c ii.

-  Calls the ```ppast``` function after displaying the scoreboard at the top of the page.

``` python
  print("=" * 30, "\nYour Score:", len(pscoreList), "\nComputer's Score:", len(cscoreList))
  print("=" * 30)
  print("Your Past Inputs (Full):")
  ppast(n)
  print("", "\nYour Past Inputs (Shortened):")
  ppast(round(n / 2))
```

#### 3c iii.

- The procedure uses ```n``` as a way to analyze the length of ```ppastList```, and this is done to print out the items in the list that represent the past inputs of the player.

#### 3c iv.

- First, the variable ```n``` is assigned to the length of ```ppastList```, the list containing the past inputs of players. Then, ```iteration``` is set as the range of n, and then a for loop is run: for n in iteration, print ```n``` values of ```ppastList```. The numbers in the list are separaed by commas when printed for a more visually appealing look.

#### 3d i.

- First call:

``` python
print("Your Past Inputs (Full):")
  ppast(n)
```

- Second call:

``` python
print("", "\nYour Past Inputs (Shortened):")
  ppast(round(n / 2))
```

#### 3d ii.

- In the first call, the condition being tested is just ```ppast(n)```, where the parameter is ```n```. ```n``` represents the length of ```ppastList```, so this call will display the full list of past inputs. In the second call, the condition being tested is ```ppast(round(n / 2))```, where the parameter is ```round(n / 2)```. Since ```n``` will not always be even, ```n / 2``` will not always yield a whole number, so the round function is necessary. This call will display a list of player inputs that is roughly half as long as normal.

#### 3d iii.

- The result of the first call is the whole list of past inputs from the player being printed at the top of the page, on a single line and separated by commas. The result of the second call is the same list of past player inputs but only about half as long, as the parameter shortens the length. This is also printed out on a single line separated by commas, and is displayed at the top of the page under the full list of past player inputs.


