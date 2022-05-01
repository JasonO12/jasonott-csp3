{% include navbar.html %}

# Create Task Outline

## Plan

My plan is to make a program that allows users to search for terms in a list, add terms to a list, and display the whole list if they dedsire. There will be a defined list that contains multiple sports, and the user can interact with this list after bring prompted by the computer. 

## Runtime

Type '1' in this menu to view my create task program.

{% include replitembed.html %}

## Video - [Link](https://www.youtube.com/watch?v=6kwxaIS7nes)

{% include createtaskvid.html %}

## Written Response

#### 3a i.

- The overall purpose of the program is to create am environment where a user can interact with a list that contains various names of sports in it. The user can add items to the list, display the hole list, or search for a term in the list. They can also decide to clear the data they previously added if they wish. The user interface contains a section at the top of the screen that outlines the basic idea of the program, as well as directions for how to use it.

#### 3a ii.

- The video shows the program running differently based on different user inputs. The user is able to add items, display, and search for items in the list. The video also shows the termination of the program, clearing the data. 

#### 3a iii. 

- The inputs displayed in the video are the user typing 'all', 'add' + item they want to add, 'search' + term they want to search for, and 'clear'. The output for 'all' is the printed list, the output for 'search' is a prompt asking what they want to search for and then responding with yes or no depending if the item is in the list or not, and the output for 'add' is a prompt asking what term the uer wants to add. The output for 'clear' is the termination of the system.

#### 3b i.

``` python
# Preset list of sports
sportList = ["Baseball", "Basketball", "Football", "Soccer", "Hockey", "Tennis"]
```

#### 3b ii.

``` python
# Parameter that prints out the whole list
  if input1 == 'all':
    for item in sportList:
      print(item, end=", ")
```

``` python      
# Loops through the list, searching for the term that the user had just inputted. If the term is somewhere in the list, True is returned. 
    for i in range(len(sportList)):
      list = sportList[i]
      if list.lower() == term:
        found = True
    # Gives the user feedback
    if found == True:
      print("Yes, this item is in the list.")
    else:
      print("No, this item is not in the list.")
```
 
#### 3b iii.

- The name of the list in this response is ```sportList```

#### 3b iv.

- The data that is in the list represents various names of sports, and any other items that the user may decide to add to the list. These terms are in place so that a user can interact with them through searching for a sport, or adding more sports to the list. 

#### 3b v.

- This list is essential for the overall functionality of the program. Using the list, users are easily able to work with the data that it contains. For example, adding items to the list is easy using the ```.append``` function, and containing the data in a list allows the user to easily search for a term: the program simply has to iterate through the list, identifying if the inputted term is there or not. Without using lists, users would not be able to search for a term as there would be no place for the program to search. With no list, users would manually have to keep track of the listed sports, and search for terms manually.

#### 3c i.

- Function for past player inputs.

``` python
# Main function that does seperate things based on user input 
def userResponseFunc(input1):
  # Parameter that prints out the whole list
  if input1 == 'all':
    for item in sportList:
      print(item, end=", ")
    print(" ")
  # Parameter that runs the search function for a user to search for a specific term in the list
  elif input1 == 'search':
    found = False
    term = input("Which term do you want to search for? ").lower()
    # Loops through the list, searching for the term that the user had just inputted. If the term is somewhere in the list, True is returned. 
    for i in range(len(sportList)):
      list = sportList[i]
      if list.lower() == term:
        found = True
    # Gives the user feedback
    if found == True:
      print("Yes, this item is in the list.")
    else:
      print("No, this item is not in the list.")
  # Parameter that allows the user to add their own terms to the list
  elif input1 == 'add':
    addition = input("What do you want to add to the list? ")
    sportList.append(addition)
    print(addition + " has been added to the list.")
  # Parameter that clears the data and kills the process, removing all appended terms. Exits the system.
  elif input1 == 'clear':
    print("Clearing Data...")
    time.sleep(1)
    sys.exit()
  # If the user did not input a valid word, then they are prompted again.
  else:
    print("Invalid input.")
```

#### 3c ii.

``` python
 def runtime():
  input1 = input("\nWhat would you like to do? ").lower()
  print("=" * 60)
  userResponseFunc(input1)
  print("=" * 60)
  
  runtime()
```

#### 3c iii.

- The procedure analyzes the text input that the user gives after being showsn a list of valid words that they can input, and what each input will allow them to do. Depending on the input, the procedure will show the full list of sports, allow a user to add items to the list, allow the user to search for a term in the list, or clear the data and terminate the process.

#### 3c iv.

- First, if the user typed 'all' when prompted, the procedure will use a for loop to print out every item in ```sportList```, each item separated by a comma. Then, if the user typed 'search' when prompted, the procedure will run a basic search function. In this search function, the variable ```found``` is set to False, and the user is asked what term they would like to search for. Then, the items in ```sportList``` are looped through, and if an item in the list matches the term the user wanted to search for, the variable ```found``` is set to true. If not, ```found``` remains False. If ```found``` is True, then the procedure tells the user that the item is in the list, and if ```found``` is False, the procedure tells the user that the item is not in the list. Then, if the user typed 'add' when prompted, the procedure asks the user what they want to add to the list and adds it. Finally

#### 3d i.

- First call:


- Second call:



#### 3d ii.

- 

#### 3d iii.

- 


