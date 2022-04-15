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

- Lists are defined and empty, and after the player and computer input a number of marbles, the input is added to their respective list:

``` python
ppastList = []
cpastList = []

ppastList.append(choice)
cpastList.append(value)
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

- The names of the lists in this response are ppastList and cpastList (player past input list and computer past input list).

#### 3b iv.

- The data that is appended to these lists are the past guesses of the player and the computer, and they aree added after each round. Each item in the list represents a previous marble input from the player/computer. 

#### 3b v.

- These lists are essential for the displaying of the past inputs from the player and the computer after each round of the game. The list is necessary to print out all of the inputs from players, and since the player and computer will choose a variety of different numbers, the best way to store the numbers would be by appending them to an empty list. Without the use of these lists, the player would have to keep track of past inputs manually or not at all, or the code may be potentially rewritten using conditionals. The use of lists in this scenario will prove to be the most effective.

#### 3c i.

- Function that ends the round.

``` python
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
```

#### 3c ii.

- endfunc() is called at the end of gamefunc(), the main game. 

``` python
  print("...")
  time.sleep(0.75)

  ppastList.append(choice)
  cpastList.append(value)

  endfunc()
```

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


