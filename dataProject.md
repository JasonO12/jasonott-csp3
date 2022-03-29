{% include navbar.html %}


# Data Structures Project

## Replit

{% include replitembed.html %}

## Week 2

### GitHub

- [Fibonacci Issue](https://github.com/JasonO12/jasonott-csp3/issues/5)
- [InfoDB Issue](https://github.com/JasonO12/jasonott-csp3/issues/6)

### Code

#### File Organization

![image](https://user-images.githubusercontent.com/89180255/160300894-7763e0d7-2467-4f80-b493-5e158030674e.png)
- Image showing file organization on Replit for each week's work and imports in the menu.

``` python
main_menu = [
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu

math_sub_menu = [
    ["Swap", swap.test_swapNum],
    ["Fibonacci", fibonacci.fibonacci_tester],
    ["Factorials", factorial.recur_tester],
    ["IMP GCD", impgcd.gcd]
]

data_sub_menu = [
    ["Lists", listsandloops.tester],
]

visual_sub_menu = [
    ["Keypad", keypad.format_tester],
    ["Tree", tree.treefunc],
    ["Pattern", pattern.patternfunc]
]

oop_sub_menu = [
    ["OOP Palindrome", ooppalindrome.pali_tester],
    ["OOP Fibonacci", oopfib.fib_tester],
    ["OOP Factorial", oopfact.fact_tester],
    ["OOP GCD", oopgcd.gcd_tester]
]
```

#### Factorial Function w/ Classes

``` python
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
  ```
  
#### Greatest Common Denominator (Imperative and OOP format)

``` python 
# Function to find the GCD of two Numbers
def findgcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def gcd():
    a = int(input(" Enter the First Value for GCD: "))
    b = int(input(" Enter the Second Value for GCD: "))
    gcd = findgcd(a, b)
    print("\n GCD of {0} and {1} is: {2}".format(a, b, gcd))
    print()
```
``` python
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
```

#### Palindrome OOP (progress)

``` python
# import re


# class Palindrome:
#     # palindrome initializer method
#     def __init__(self, candidate):
#         # input values
#         self._candidate = candidate  # input string
#         self._length = len(candidate)  # input length
#         # analysis values
#         self._is_a_palindrome = False  # initialize status
#         self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  # alpha numeric characters
#         self._analysis = []  # array of tests
#         self._tests = 0  # counter of tests performed
#         # evaluate for palindrome
#         self.is_palindrome()

#     # palindrome tester method
#     def is_palindrome(self):
#         c = self._az09
#         # Run loop from 0 to len/2 of string (middle is exit point)
#         tests = int(len(c) / 2)
#         for i in range(0, tests):
#             front = c[i];
#             back = c[len(c) - i - 1]
#             if front.lower() == back.lower():
#                 self.logger(front, back, True)
#                 self._tests += 1
#             else:
#                 self.logger(front, back, False)
#                 return
#         self._is_a_palindrome = True
#         return

#     # palindrome logging
#     def logger(self, front, back, result):
#         self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

#     # getters follow
#     @property
#     def candidate(self):
#         return self._candidate

#     @property
#     def tests(self):
#         return self._tests

#     @property
#     def isPalindrome(self):
#         return self._is_a_palindrome

#     @property
#     def analysis(self):
#         return self._analysis

def pali_tester():
  # pali = Palindrome()
  # pali("uhefgsrbkjehiebihqet")
  print('\u001b[31;1mNot Currently Working\u001b[37;1m')
  ```


## Week 1

### GitHub

- [Fibonacci Issue](https://github.com/JasonO12/jasonott-csp3/issues/5)
- [InfoDB Issue](https://github.com/JasonO12/jasonott-csp3/issues/6)

### Code

#### InfoDB Lists

``` python
InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Jason",  
               "LastName": "Ott",  
               "Age": "16",     
               "Schools":["Del Sur Elementary","Monterey Ridge Elementary","Oak Valley Middle","Del Norte High"]  
              })  

InfoDb.append({  
               "FirstName": "Lucas",  
               "LastName": "Ho",  
               "Age": "16",     
               "Schools":["Monterey Ridge Elementary","Oak Valley Middle","Del Norte High"]  
              })

InfoDb.append({  
               "FirstName": "Everitt",  
               "LastName": "Cheng",  
               "Age": "16",     
               "Schools":["PS203", "Black Mountain Middle","Oak Valley Middle","Del Norte High"]  
              })

InfoDb.append({  
               "FirstName": "Daniel",  
               "LastName": "Tsivkovski",  
               "Age": "17",     
               "Schools":["Stone Ranch Elementary","Oak Valley Middle","Del Norte High"]    
              })


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Attended Schools: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Schools"]))  # join allows printing a string list with separator
    print()
```

#### InfoDB Loops

``` python 
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

  
# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input


def tester():
    print("For loop: \n" + "-------------------")
    for_loop()
    print("While loop: \n" + "-------------------")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop \n" + "-------------------")
    recursive_loop(0)  # requires initial index to start recursion
```
 
#### Fibonacci

``` python
def fibonacci(n):
  # sets the first two values in the fibonacci sequence to remove errors
  a = 1
  print(a)
  b = 1
  print(b)
  i = 2
   # starts the loop to display each value in the fibonacci sequence for n
  while i < n:
    # introduces k variable to act as a temp
    k = b
    b = a + b
    a = k
    print(b)

    # iterates each integer until n
    i += 1
  return

def fibonacci_tester():
  n = int(input("Enter Value for Fibonoacci: "))
  fibonacci(n)
  # runs the function
  
  ```

## Week 0

### GitHub

- [Pattern Issue](https://github.com/JasonO12/jasonott-csp3/issues/1)
- [Menu Issue](https://github.com/JasonO12/jasonott-csp3/issues/3)
- [Tree Issue](https://github.com/JasonO12/jasonott-csp3/issues/2)

### Code

<!-- #### Swap Code
``` python
def swapNum(num1, num2):
    if int(num1) > int(num2):
        temp = num1
        num1 = num2
        num2 = temp
    return(num1, num2)

def test_swapNum():
    num1 = input("Input age 1: ")
    num2 = input("Input age 2: ")
    num1, num2 = swapNum(num1, num2)
    print("Swapped:", num1, num2)
``` -->
#### Pattern Code
``` python
def pattern_print(position):
    print(ANSI_HOME_CURSOR)
    sp = " " * position
    print(AMOGUS_COLOR)
    print(sp + "    .-----.   ")
    print(sp + "  /|    ___|  ")
    print(sp + " | |   (____) ")
    print(sp + " | |       |  ")
    print(sp + "  \|       |  ")
    print(sp + "   |  .-.  |  ")
    print(sp + "   |  | |  |  ")
    print(sp + "   |__| |__|  ")
    print(NON_COLOR)

  
# Pattern function, interface into this file
def patternfunc():

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate candle moving
    for position in range(start, distance, step):
        pattern_print(position)  # call to function with parameter
        time.sleep(.1)
```
#### Tree Code
``` python 
def build_tree(height):
  i = 1
  while i <= height:
    print(" " * (height - i) + "X " * i)
    i = i + 1
  print(" " * (height - 3) + "|   |\n" + " " * (height - 3) + "L...⅃")
    

def treefunc():
  height = int(input("Enter height: "))
  build_tree(height)
```
<!-- #### Keypad Code
``` python
def format(matrix):
    rows = len(matrix)
    for x in range(rows):
        columns = len(matrix[x])
        for i in range(columns):
            print(matrix[x][i], end=' ')
        print()


def format_tester():
    matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
    format(matrix)
    matrix2 = [ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ]
    format(matrix2)
``` -->
#### Menus Code
``` python
main_menu = [
    ["Swap", swap.test_swapNum],
    ["Keypad", keypad.format_tester],
    ["Tree", tree.treefunc]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
patterns_sub_menu = [
    ["Pattern", pattern.patternfunc],
]


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Pattern", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()


def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again
```


