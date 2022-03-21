# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

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

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

# for loop iterates on length of InfoDb
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