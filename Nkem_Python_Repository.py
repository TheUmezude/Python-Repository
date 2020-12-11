"""
use triple apostrophes to indicate multi-line comments.
"""


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                           STRINGS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 'Strings' are more or less just an ordered and immutable array of characters.

# Important methods to use with strings
.capitalize() # this capitalizes the first letter in a string -- irrespective if there are multiple full-stops, ONLY the first letter would be capitalized
.casefold() # this makes the entire characters in the string lower-case **?
.count(string/character) # to count the number of times a particular string or character occurred in the string 
.endswith(string/character) # returns 'True' or 'False', depending on if the string ends with the character or string you passed into the method
.find(string/character, occurrence) # to find the index that a particular string or character occurred for the specified occurrence (like 2 for 2nd occurrence)
.lower() # to convert the characters in the string to lower-case
.upper() # to convert the characters in the string to upper-case
.islower() # returns 'True' if the characters in the string are lower-case, and 'False' if the characters in the string are not lower-case
.isupper() # returns 'True' if the characters in the string are upper-case, and 'False' if the characters in the string are not upper-case
.isalpha() # returns 'True' if the contents of the string are all alphabets and 'False' if they aren't -- Note that it identifies spaces and punctuations as non-alphabets
.isdigit() # returns 'True' if the contents of the string are integers and 'False' if they are not integers (floats are not integers)
.title() # Capitalizes the first letter of every word
.istitle() # returns 'True' if the first letter of every word of the string is upper-case, and 'False' if not.
.split(string/character) # returns a list of the words separated by the spaces from a string -- if a character or string is initialized, it returns splitting at that string word or character


#String Interpolations

#using the '.format' method
print ("The {q} {b} {f}".format(q = "quick", f = "fox", b = "brown"))

#Using the F-string method
q = quick
b = brown
f = fox
print(f"The {q} {b} {f})

# The '.format' method can also be used for float formatting, such as in example---
result = 100/777  # originally, that result would be: 0.1287001287001287
# However, if I wantto print to format the result (like rounding it up), and print to screen, I could use the '.format' method and specify width & precision. using format {value:width.precision f} Like so ---
print("The result was {r:1.3f}".format(r = result))
# Print out would be: 'The result was 0.129'
# Note, that the width indicates how much white spaces before and with the value, precision indicates how you want it rounded up.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                             COMPARISON OPERATORS
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
True and False ----> False
False and True ----> False
False and False ----> False
True and True ----> True

True or False ----> True
True or True ----> True
False or True ----> True
False or False ----> False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                            .TXT FILE MANIPULATION
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##Opening and reading files
with open('C:\\Users\\Admin\\Desktop\\email.txt') as myfile:
	myfile.seek(0) # To return the cursor to the beginning point of the file
    contents = myfile.readlines()
	print(contents)
	
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode ='r') as myfile:
    contents = myfile.readlines()
	print(contents)
############################


##Opening and overwriting files
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'w') as myfile:
    myfile.write('\nHello')
	
##Opening and adding to files
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'a') as myfile:
    myfile.write('\nInteresting')
	

##Opening and reading and writing to files
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'r+') as myfile:
    contents = myfile.readlines()
	
##Opening and overwriting and reading files
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'w+') as myfile:
    contents = myfile.readlines()
	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	
	
	
	
	
	
	
	
	
	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                 DICTIONARIES
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dictionaries are a method of holding a variety of data types, also - just like how lists and tuples do -   
# But dictionaries are different from tuples and lists, because the data is stored in an un-ordered manner.
# Tuples and lists store data in an ordered manner (like keeping socks in shelves in a cabinet), 
# but dictionaries store them in an un-ordered manner (like throwing socks anywhere in your room) - this makes them unable to be sorted 
# Dictionaries are hoever able to access the data they store by means of key-value pairs

# The dictionary syntax is also different from tuple and list syntax. They use curly braces and colons to separate the keys from the associated values
# Since dictionaries are unsorted, they are useful when you may need to retrieve data, without knowing the exact location of the data - you just call the key

# Create Dictionary
my_dictionary = {'key1': 'value1', 'key2': 'value2'}

# Print out dictionary to show how the computer recognizes them
print(my_dictionary)

# Get values out of the dictionary by passing keys
print(my_dictionary['key1'])
print(my_dictionary['key2'])

# Dictionaries are especially useful for instance when creating programs that store values of items in a store.

item_price = {'Apple': 2.99, 'Mango': 0.99, 'Orange': 0.49}
print(item_price['Apple']) ---- print(item_price['Mango']) ----- print(item_price['Orange'])

# You can also assign a new key into your dictionary on the go by doing something like
item_price['Lemon'] = 0.25
print(item_price)

# Grabbing the keys out
print(item_price.keys())   #Note that the keys in a dictionary must always be a string!
# Grabbing the values
print(item_price.values())
# Grabbing the items
print(item_price.items())

# Dictionaries can also hold lists within them, or even other dictionaries 
item_price = ['Apple':{'Mexican': 1.99, 'Canadian': 2.29}, 'Orange': [0.26, 0.44, 0.89]}
print(item_price['Apple']['Canadian'])
print(item_price['Orange'][0]


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	
	
	
	
	
	
	
	
	
	
	
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                  LIST, TUPLE and SET MANIPULATION
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Here, I am using a for-loop to iterate through a list and print out a string with the value from the list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numbers in mylist:
    value = 0 + numbers
    if value == 1:
        notation = str(value) + 'st'
    elif value == 2:
        notation = str(value) + 'nd'
    elif value == 3:
        notation = str(value) + 'rd'
    else:
        notation = str(value) + 'th'
    print(('I came into your house on the ') + notation + (' day'))




#Separating even from odd numbers in a list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numbers in mylist:
    value = numbers % 2
    if value == 0:
        print(f'This is an even number: {numbers}')
    else:
        print(f'This is an odd number: {numbers}')


# Lists can be concatenated by adding them together with a '+' sign -- For example:
ListA = [1,2,3,4]
ListB = [9,8,7,6]
List_ADD = ListA + ListB
print(List_ADD) 
# List_ADD would be = [1,2,3,4,9,8,7,6]


# Important methods to use with lists
.append() # to add one new item to end of list
.pop(index) # to remove an item from end of list or indicated index
.extend(list) # to add the contents of one list into a new list 
.clear() # to remove all the items in a list
.count(item) # to count the number of times a given item occured in a list
.index(index) # to determine the item at a particular index in the list
.reverse() # to reverse the arrangement of items in a list
.remove(item) # to remove the first occurrence of an item in a list
.copy() # to return the contents of a list as an assignment to a new list variable
.insert(index, value) # to insert a value into a particular index location in a list 


# Important methods to use with sets
.add() # to add one new item to end of set
.pop(index) # to remove an item from the beginning of the set or indicated index
.clear() # to remove all the items in a set
.copy() # to return the contents of a set as an assignment to a new set variable
myset.intersection(another_set) # To return only the contents that are in both 'myset' and 'another_set'
myset.intersection_update(another_set) # To overwrite the contents of 'myset' with the elements that are both in 'myset' and 'another_set'
myset.union(another_set) # To unify the contents in 'myset' with the contents in 'another_set' and return the aggregate
myset.difference(another_set) # To return the elements in 'myset' that are not in 'another_set'
myset.difference_update(another_set) # To overwrite the contents of 'myset' with elements that are in 'myset' but are not in 'another_set'
myset.issubset(another_set) # Returns 'True' if 'myset' is a subset of 'another_set' or 'False' if 'myset' is not a subset of 'another_set'
myset.issuperset(another_set) # Returns 'True' if 'myset' has all the elements of 'another_set' or 'False' if 'myset' does not have all the elements of 'another_set'
myset.isdisjoint(another_set) # Returns 'True' if 'myset' and 'another_set' have no elements in common, otherwise it returns 'False'
myset.update(another_set) # Adds the elements in 'another_set' which aren not in 'myset' 




#Tupule unpacking - to print out 2, 4, 6, 11.
list_tuple = [(1,2), (3,4), (5,6), (10,11)]

for (a,b) in list_tuple:
    print(b)
	
	
#When using looping functions like for and while loops, the following are important to keep in mind
#break: Breaks out of the current closest enclosing loop.
#continue: Goes to the top of the closest enclosing loop.
#pass: Does nothing at all. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Examples are shown below:

name = 'Irfan'

for letter in name:
    if letter == 'f':
        pass   ########### If 'pass' is used, the name prints out as normal
		break ########### If 'break' is used, the print function only prints out 'Ir' because it breaks at f
		continue ######## If 'continue' is used, the print function prints out 'Iran', because it skips the 'f' since it is continuing.
    print(f'The letter here looks like this {letter}')



#When using a for-loop and you intend to break out without giving a list initialization;
for num in range(20):   ## Also can be written as for num in range(0,20)
    print(num)
	
for num in range(6,20,2): ## For num falling between numbers 6 and 20, and with a stepwise of 2 ##
    print(num)
	
	
#Importing functions from libraries in Python.
from random import shuffle # Here, the 'shuffle' function is being imported from the 'random' library
from random import randint # Here, the 'randint' function is being imported from the 'random' library
#The 'random library has the shuffle and randint(i.e random integer) functions

#Flattening out a for-loop -- List comprehension
newlist = [letters for letters in 'Avadakedavra']
newlist = [num**2 for num in range(0,20) if num%2 == 0] #Find the numbers in a range from 0 to 20, pick out only the even numbers, square them and append the newlist with the squares
newlist = [num if num%2 == 0 else 'Odd' for num in results]

#nested for-loop
newlist = []

for x in [2, 4, 6]:
	for y in [1, 10, 100]:
		newlist.append(x*y)
		
		
#More Tuple unpacking examples. Here we would use a function to iterate through a list containing tuples and perform data analysis for 'Most Valuable Employee'
def employee_check(new_list):
    max_hours = 0
    employee = ''
    
    for (name,hours) in new_list:
        if (hours > max_hours):
            max_hours = hours
            employee = name
            
        else:
            pass
            
    return (employee,max_hours)

work_hours = [('Abby',100), ('Billy',400), ('Cassie',200)]
award = employee_check(work_hours)

for a,b in award:
    print(f'The most valuable employee is {a}, and he/she worked {b} hours.') #'a' should become the name of the person with the most hours and 'b' should become the number of worked hours.
	
	
	
#Joining lists together
mylist = [a, b, c, d, e]
print('%'.join(mylist))
# The output would be the elements of the list joined with the value between the quotations that is;
a%b%c%d%e

#Write a program that returns the sum of numbers in an array, except ignore sections of numbers starting with a 6 and extending up until a 9 (every 6 would be followed by at-least one 9. Return 0 for no numbers.
def avoiding_6to9(mylist):
    total = 0
    add = True
    
    for num in mylist:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
                
    return total
	
		
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#              FUNCTION DEEP-DIVE
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Prime number finder function
def count_primes(num = 1): # Note that I am passing in a default value for num, just in-case it is called and the user doesn't pass in a value -- Good practice
     # Check for 0 or 1 in input
    if num < 2:
        return 0
    # We are looking for prime numbers that equal 2 or greater
    
    #create an array for storing prime numbers
    primes = [2] #Your choice to initialize it with 2 to make it easier
    
    x = 3 #initialize the count number. Starting from 3 because 2 is in array
    
    while x <= num:
        #check if x is prime
        
        for y in range (3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
            
    print(primes)
	


#A crude way to create a function that would be flexible for whichever number of parameters are passed into it would be like:
def AdditionFunction(a,b=0,c=0,d=0,e=0):
    #Here, the function must at-least get one argument passed in, whereas, it can sum up about 5 parameters. If only two arguments are passed in, it just sums the two with the other arguments initialized as 0. 
	result = sum((a,b,c,d,e))
	return result
	
#A much better way to do it would be as:
def AdditionFunction(*args): # A tuple would be returned
	result = sum((args))
	return result
	
# *args and **kwargs are interesting way to ensure versatility of a function. While *args allows operations to be done for any number of arguments, **kwargs allows passing in of unlimited mapings and creates a sort of dictionary out of them. For example;
def NewFunction(**kwargs): # A dictionary would be returned
	if 'fruit' in kwargs:
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here.')
		
#We can call the function, now;
NewFunction(fruit = 'Apple', vegetable = 'Tomatoes')

# Additional stuff----------------------------------------------
def user_choice():
    choice = 'WRONG!!'
    acceptable_range = range(0, 11)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter an number (0-10): ')

        if choice.isdigit() == False:
            print('Sorry, that is not a digit!')

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False

    return int(choice)

result = user_choice()
print(result)	

# Simple coin toss using the 'randint' function from the 'random' library
from random import randint
def choose_first():
    flip = randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


#------------------------------------- DECORATORS ---------------------------------------------
# When you create a function in Python, you can 'assign' that function to another variable, such that the variable inherits the behavior of the function
# Example:
def say_hi():
	return "Hi, there!"
	
greet = say_hi
# Now, when 'greet' is executed, it returns "Hi, there!", even if the 'say_hi' function is deleted.


# You can also generally define functions inside other functions, such as:
def hello():
    print("The hello() function has been executed.")
    
    def greet(): # The greet() function is being defined inside the hello() function -- Nested
        return "\tThis is the greet() function inside hello()"
    
    def welcome(): # The welcome() function is being defined inside the hello() function -- Nested
        return "\t\tThis is the welcome() function inside hello(), as well."
    
    print(greet()) # The greet() function is being executed 
    print(welcome()) # The welcome() function is being executed
# Here, when the 'hello()' function is executed, the execution of the 'greet()' and 'welcome()' functions are also printed to screen.
# Note that the greet() and welcome() functions cannot be called outside the hello() function for executing.
# You could also decide to return one of the nested functions for a specific condition, as so:

def hello(name = "Nkem"): #This is very interesting.
    print("The hello() function has been executed.")
    
    def greet():
        return "\tThis is the greet() function inside hello()"
    
    def welcome():
        return "\t\tThis is the welcome() function inside hello(), as well."
    
    if name == "Nkem":
        return welcome
    else:
        return greet

# If the hello() function is called for execution and assigned to a variable, such as:
my_func = hello("Bobby") # Depending on the value in 'name', when my_func is printed out, one of the functions execution would be printed out
print(my_func())


# Functions can also be passed in as arguments for other functions to execute. Such as in;
def hello(): # This is a simple function being defined here 
    return "Hi, Bobby!"
	
def function_executor(a_function): # This is a function that takes in another function as an argument
    print("Just chilling here.")
    print(a_function()) # The function taken in as an argument is being executed here
	
	
	
# Another decorator example
def func_needs_decorator():
	return "I want to be decorated!"


def new_decorator(my_func): # A function called 'new_decorator' is created to take a function in as an argument
    
    def decorating_guy(): # A function 'decorating_guy' is defined inside the 'new_decorator' function -- acting like a wrapper
        print("Hello, I am the decorating guy. See decorated function argument below.") 
        
        print(my_func()) 
		# The function 'my_func' is a function passed in as an argument, and by executing it here, what it returns becomes a part of the bigger function 'inside_new'
        
        print("Decoration complete. See decorated function argument above.")
        
    return decorating_guy() # this returns the wrapped version of 'my_func', as wrapped by 'inside_new' -- ensure to put execution brackets!
	# now, when the function 'new_decorator' is executed, 'inside_new' is created and executed.
	
# Executing: Can be done in two ways
# Way 1
new_decorator(func_needs_decorator) # This passes the 'func_needs_decorator' function as an argument into the 'new_decorator' function

# Way 2
@new_decorator # Python automatically assigns whatever function that comes next as an argument into the function 'new_decorator'.
def func_needs_decorator():
	return "I want to be decorated" # by doing this, Python automatically passes the function 'func_needs_decorator' into the 'new_decorator' function as an argument.
	
	
	
#------------------------------------- GENERATORS ---------------------------------------------
# Generators are an efficient way to perform particular operations without taking up so much space in memory. For example:
# If I wanted to write a function that finds the square of numbers within a range given, I would do soemthing like:

def find_squares(value):

	squares_result = [] # I would initialize a list to hold the values of the squares that I find
	
	for items in range(value):
		squares_result.append(items**2)
	return squares_result # By doing this, I am returning a list of the squares. You can now imagine how much memory would be exhausted if 'value' is maybe 10,000,0000
	
# A better way to go about this is to create a generator similar to the range() function that doesnt need to store anything in memory. Such as:
def square_generator(value):
	for items in range(value):
		yield items**2              # The 'yield' keyword identifies the function as a generator function.
		
# Now, if I need information from the generator, I could instead do something like:
list(square_generator(15)) # To type-cast the result of the 'square_generator' function into a list and store in memory, or;

for items in square_generator(15): # To avoid storing in memory and just get the values needed.
	print(items) # or
	
result = square_generator(15) # Making result a generator object for the created generator
print(next(result)) # To only print out the values one-by-one, as needed.
	
	
	
# Creating a generator for a Fibonacci sequence:
def create_fibonacci(value):
    a = 0
    b = 1
    
    for items in range(value):
        yield a
        a,b = b, a+b
		

# Creating a generator that yields random numbers between a low and high initialized value:
import random

def yield_random(low,high):
    for items in range(high+1):
        yield random.choice(range(low,high+1))
		
randomized = yield_random(1,9)
print(next(randomized))

# ------------- Generator comprehension --------------
my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 2)  # gencomp, here, is a type of generator object.
for items in gencomp:
    print(items)


# Useful information. You can some items iterable items. Such as strings.
s = "Hello"
s_iter = iter(s)
print(next(s_iter)) # Should print 'H'
print(next(s_iter)) # Should print 'e'
print(next(s_iter)) # Should print 'l'
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







	




	

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                          LAMBDA, MAP AND FILTER FUNCTIONS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------- MAP ------------------------------------------
#Mapping helps to link an established function to an established set of data without complicating the function
# Example: we define a function called splicer, we define a set of data, then request a tuple to be formed by mapping the function to the data parameters
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Babe'
    else:
        return mystring[1]

new_string = ['Lion', 'Tiger', 'Goose', 'Antelope', 'Duck']

print(tuple(map(splicer,new_string))) #Here, a tuple would be iteratively created based on the operations defined in the function and on the established data 
new_tuple = tuple(map(splicer,new_string))  # The iteratively created tuple can be assigned to a tuple variable.


#another way:
for n in map(splicer,new_string):
	print(n)  #This still performs the operation, but doesn't create a list or tuple out of the results



#----------------------------- FILTER -------------------------------------------------------
#Filters act like maps, in that they apply a function operation on a set of data values, however, they return based on bolean -- Such as in the example below
def check_even(number):
	return number % 2 == 0 #This would return 'True' if the number sent into the function is even, and 'False' if the number sent into the function is odd

mynumbers = [1,2,3,4,5,6,7,8,9] #Establishing the data set or parameters

print(list(filter(check_even,mynumbers))) #This prints out a list containing only the values that returned 'True' from the function 'check_even'

#another way:
for n in filter(check_even,mynumbers):
	print(n)   #This performs the filtering operation and prints out the even numbers that return 'True', but not in a list or tuple form.
	


#---------------------------- LAMBDA ------------------------------------------------------
# Lambda functions help to reduce the general length of functions -- Example
# Consider a function defined as:
def times2(variable1):
	return variable1 * 2       # This function takes in a variable, and returns the variable multiplied by 2
# Rewriting in a Lambda expression would look like:
lambda variable1 : variable1 * 2
# This 'lambda' function would do exactl the same thing as the prior defined function. Its results can be assigned to a sort of function
times2 = lambda variable1 : variable1 * 2     # Now, 'times2' is a function that takes in a variable, performs the multiplication operation and returns the result.
# The result of 'times2' for any particular value can be returned to a variable -- such as:
result = times2(4)


#### Lambda expressions would preferably be used alongside things 'Maps' and 'Filters' -- Such as:
# For maps
my_list = [1,2,3,4,5] # A list is initialized with numbers
squared_list = list(map(lambda num : num ** 2, my_list)) # Here, a new list called 'squared_list' is created as the square of the numbers initialized in 'my_list'
# The entire function that would have done the same is made rather cleaner and on a single line.

# For filters
number_list = [20,21,22,23,24,25,26,27,28] # A list is initialized with numbers
even_numbers = tuple(filter(lambda num : num%2 == 0, number_list)) # Here, I am using the 'filter' and 'lambda' functions to create a tuple of even numbers from the original list
print(even_numbers)
# The created tuple is assigned to even_numbers
# Another example
my_string = 'ThE TruTH Of The BoOk' # A string -- essentially an iterable array of characters is created
capital_letters = list(filter(lambda letter : letter.isupper(), my_string)) # Here, I am creating a new list using the 'filter' & 'lambda' functions to find the letters that are uppercase
print(capital_letters)

# It is important to note that 'filter' and 'map' functions require that an iterable item be sent in
 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

		
		
		
		



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                 CLASSES
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Classes are an important aspect of 'Object Oriented Programming (OOP)'
# A sample class is shown below with its attributes, and a way to relate a variable under the class to the attributes is also shown:

class GroupMates(): # Class names should be written with 'Camel' casing
    # Defining a CLASS OBJECT ATTRIBUTE
    # supposedly to be constant for any instance of the class
    animal = 'human'
    
    def __init__(self, name, nationality, personality):
        
        # Attributes
        # We take in the argument
        # The argument is assigned to self.(the attribute name)
        self.name = name
        self.nationality = nationality
        self.personality = personality
    
    # Method: functions inside of a class -------- You can have more than one method for a single class definition.
    def usual_statement(self,date): # 'date' here, is an external variable that is inputted by the user
        print(f'I want to get the job! - {self.name}, {date}') # External variables can also be used in performing operations, and not just printing out.

mate1 = GroupMates('Irfan', 'Pakistani', 'nice') #Here, we are letting python know that 'mate1' is an instance of the class 'GroupMates', then we pass parameters

print(f'My groupmate, {mate1.name}, is a {mate1.nationality} by nationality, and he is {mate1.personality}')
# Result: My groupmate, Irfan, is a Pakistani by nationality, and he is nice




# You could also, when creating a class, add a check to ensure that the intended data type is passed in. For instance:
class Dog():
    
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
        # I expect the argument for spots to be boolean (either 'True' or 'False'), hence, I am adding a check 'if' statement
        if type(self.spots) != bool:
            raise NotImplementedError('The third parameter needs to be true or false!') 
            #If the argument passed in for 'spots' is not a boolean, an error would be raised




# Class to calculate the area of a circle
class CircleArea():
    Pi = 3.142   # May be referenced within the class as self.Pi or even CircleArea.Pi since it is a class-based object attribute
    
    def __init__(self, radius = 1):
        self.radius = radius
		self.circumference = self.radius * 2 * self.pi  # Note, here, I am defining an attribute that has nothing to do with user input. This allows increased dexterity
    def get_area(self):
        return self.Pi * self.radius * self.radius

# Utilizing the class call
circle1 = CircleArea(4) 
print(circle1.get_area()) #You use the '()' because here, 'get_area' is a method, and can execute an action.
print(circle1.circumference)  #You don't use '()' because 'circumference' is just an attribute and has nothing to execute.



##### There is a way to establish inheritance of methods from one class into another class. For example:
# Create first class
class Animal():

	def __init__(self): # Here we are not passing in an attribute
		print('Animal Created!')
	
	def who_am_i(self):
		print('I am an animal.')
		
	def eat(self):
		print('I am eating...')

# Now we create another class which is supposed to inherit from the first class
# In this class that inherits from the previous class, several other methods can be added 
# Or methods from the previous class can be overwritten by naming methods in this new class with the same name as the class they are inheriting from 
class Cat():

	def __init__(self):
		Animal.__init__(self) # With this, the previous class which was defined, 'Animal', is linked to this new class called dog, so that its attributes can be used
		print('Cat created!') # When this prints, 'Animal Created' and 'Cat created' would both print out.
		
	def me(self): # Here, I am also creating a new method and linking the the method from class 'Animal' called 'who_am_i'.
#	I may also decide to override the 'who_am_i' method by naming this method in the Cat class the exact name as what is in the animal class, i.e: 'who_am_i'
		Animal.who_am_i(self)
		print('A cat, to be precise.')


#----------------------------------- POLYMORPHISM -----------------------------------
##### Polymorphism can be used to iterate through a set of classes. For instance;
class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says WOOFF!'

class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says Meow!'

mydog = Dog('Bob')
mycat = Cat('Stace')
# Iterating through the classes... 
for pet in (mydog, mycat):
    print(type(pet))
    print(pet.speak()) # This is possible because both the instances of the class have a method called 'speak' in their respective classes.
#---------------------------------------	
# The print statements return:
<class '__main__.Dog'>
Bob says WOOFF!
<class '__main__.Cat'>
Stace says Meow!
#---------------------------------------
# It could also be done by creating a function that takes in the class variables and gets the return value
def pet_speak(pet): #In this instance, you would pass in either 'mydog' or 'mycat'
	print(pet.speak())
	
	
#------------------------------ ABSTRACT CLASSES AND INHERITANCE --------------------------------------------------------------
class Animal(): # Here, the 'Animal' class is serving as a base class, and doesn't expect to be instantiated by a call. I
   # The 'Animal' class is only here for the sake of other classes that inherit from it. 
    def __init__(self, name):
        self.name = name
        
    def speak(self): #This is only existing as an abstract method.
        raise NotImplementedError("Subclass needs to implement this abstract method") 
		
class Dog(Animal): # Here, I am passing in the class called 'Animal', so I can use from its method
	
	def speak(self): # Notice I didn't need to call the '__init__', because it has already been called in the class I am inheriting from
		return self.name + ' says woof!!!'
# When creating an instance of this 'Dog' class, the argument 'name' should be passed in, since the 'Dog' class is inheriting the '__init__' method from the Animal # class. For example, in creating an instance, I would say: mydog = Dog('Jessie'), even though I didn't declare an '__init__' that takes the name argument.



#To use normal python functions like 'len', 'print', etc. with a class instance, special methods (Dunder methods) have to be applied. FOr example:
class Book():
    
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages
        
    def __str__(self): #The method '__str__' is a special method allowing any instance of the class 'Book' to return customized information when 'print()' is called 
        return f"The book titled, \'{self.title}\', was written by {self.author}. It has {self.pages} pages."
		
	def __len__(self): #The method '__len__' is a special method allowing any instance of the class 'Book' to return information when 'len()' is called
		return self.pages #Note that 'len()' only recognizes integers, so an error would occur if you return a string.
		
	def __del__(self): #The method '__del__' is a special method allowing customizable information to show when an instance of a class is being deleted with 'del'
		print('A Book object has just been deleted!')




# A bank account class for withdrawing and depositing.
class BankAccount():
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        if type(balance) != int and type(balance) != float:
            print("You need to enter a valid number.")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Hello, you have just added {amount} dollars to your account.")
        print(f"Your current account balance is {self.balance}.")
    
    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Sorry, you do not have sufficient money in your account.")
        else:
            self.balance = self.balance - amount
            print("Dispensing...")
            print(f"Now, your current account balance is {self.balance}")
            
    def __str__(self):
        return f"An account belonging to {self.owner} has been created with {self.balance} dollars."

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                        MAKING PERSONAL MODULES AND PACKAGES/LIBRARIES
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Just like we are able to use libraries or packages made by third-parties, we can also make our own modules and packages/libraries
# If I have two python scripts open, lets say 'script 1' = 'main.py' and 'script 2' = 'function_script.py',
# I can import functions from 'function_script.py' to 'main.py' in two ways:
# --- Way 1 --- in 'main.py'
from function_script import function1
print(function1())

# --- Way 2 --- in 'main.py'
import function_script
print(function_script.function1())  # ------- Remember to go to the Udemy lecture on making packages, if that ever becomes important for you


# '__name__' and '__main__' -- Unlike in other languages (including C++), where you have to declare a particular script as main (int main():),
# In Python, whichever script you are running is assigned by Python as main. But to be sure, you could do the below to confirm
if __name__ == '__main__':
	print('This particular script is running through command line and not being imported.')
else:
	print('This particular script is being imported')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	
	






#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                      ERRORS AND EXCEPTIONS HANDLING
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
# 'Error handling' is a way to allow a script which is being executed to continue running even if it encountered an input/logic error
# Without 'Error handling' procedures, entire scripts would be stopped when the program comes across something it is unable to understand
# 'Error handling' uses 3 key words:
# try - The block of code to be attempted... May lead to an error.
# except - The block of code to execute, in-case there is an error in the 'try' block.
# finally - Final block of code to be executed, regardless of an error.
try:
    result = 20 + '2' # -- Adding an integer to a string would cause an error, so with this 'try-except-else' statement, 
	# when the error is realized, the except statement is run, also, if there is no error, the try runs and the 'else' statement runs as well.

except: #Note that you can except for specific errors, such as -- except TypeError: -- You can also have more than one except error 
    print("Hey, looks like we aren't adding in the proper way.")
else:
    print("Addition is looking good, so far.")

# This is an example of a 'try-except-finally' error. Here, the code block in 'finally' would always run, no matter what. The excepts would run if any of their errors is raised.
try:
    f = open('C:\\Users\\Admin\\Desktop\\testfile.txt','w')
    f.write("Write a test line")
    f.close()
except TypeError:
    print("Sorry, there was a type error.")
except OSError:
    print("Sorry, there was an OS error.")
finally:
    print("I am running fine")
	
# Another example
def ask_for_int():
    
    while True:
        try:
            result = int(input("Please enter an integer value: "))
        except:
            print("Whoops! Looks like you didn't enter an integer.")
			continue
        else:
            print("Thanks")
            break
        finally:
            print("Yeah, I'm just chilling back here.")
	
# You can reference https://docs.python.org/3/tutorial/errors.html for more information on different types of errors.
# Just my opinion, though, but it seems that error handling is how passcode entries are managed.







#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                 ADDITIONAL STUFF
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Pylint is an opensource bug and quality checker for Python code.
# Unittest is an inbuilt library in python that allows you to test the behavior of written programs.

#NoteToSelf, you can initialize an array or tuple in Python by defining a variable name and assigning it to a range. For example:
Variable1 = list(range(0, 100)) # With this, Variable1, has become a list with pockets from 0 to 100

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                          MODULES IN PYTHON
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from collections import Counter # This can be used to count number of ocurrences of values in an array -- including strings (Since strings are essentially character arrays)
mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3]
print(Counter(mylist)) # This would show the number of times each value occurred
print(Counter(mylist)[1]) # You could also do it this way if you are only interested in the occurrence of one value
# It could also be used to count number of occurrences of words in a sentence
my_sentence = "How many how words can be seen in this many words sentence"
print(Counter(my_sentence.lower().split()))
# You can assign the contents of your count to a separate variable and perform operations on it. Such as:
count_variable = Counter(my_sentence.lower().split())

sum(count_variable.values())                 # total of all counts
count_variable.clear()                       # reset all counts
list(count_variable)                         # list unique elements
set(count_variable)                          # convert to a set
dict(count_variable)                         # convert to a regular dictionary
count_variable.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
count_variable.most_common()[:-n-1:-1]       # n least common elements
count_variable += Counter()                  # remove zero and negative counts


from collections import defaultdict # This can be used to assign a default value to keys not present in a dictionary, in-order to avoid a potential 'key error' if they are called.
# Example below:
d = {'a':10} # Here a dictionary has been created with one actual key and one actual value
# now, if a key other than what exists in the dictionary is called, we would get a 'KeyError' with Python.
# To avoid such a scenario, we may first initialize the dictionary to be a default dictionary; Like
d = defaultdict(lambda: 2) # Now, I have assinged a default value of 2 to any non actual key element that is called in the dictionary.
# I can however still treat it as a normal dictionary by assigning keys and values 
d['real key'] = 100
# Now, if I call 'real key', I would get 100, if I call any other key that doesn't actually exist there, a default value of 2 would be assigned. And the dictionary length increases
# Note, if you assign a dictionary as a default dictionary, and you go ahead to assign it as a real dictionary, again, the new would overwrite the old.


from collections import namedtuple # Kinda like a class that allows you access tuple contents with named mapping instead of just index locations -- Not too interesting 




import os  # This is very important, as it allows you to get the current working directory or list all files in a directory -- plus a WHOLE LOT MORE!!!!!

os.getcwd()      # This reports back the current working directory
os.listdir()     # This reports back a list of everything in a directory -- You can put in the name of the particular directory you want it to report on
os.listdir('Desktop\\Free-time')     # Here, the directory opens up 'Desktop', then looks for the folder called 'Free-time' and reports a list of its contents
os.walk('Desktop\\Adele')     # Also interesting -- for getting information of the folders, sub_folders and files and more in a path


import shutil    # This allows you to move files around within your computer -- it can be called independently. without first importing 'os'
shutil.move('Desktop\\Free-time\\Doyinsola.docx', 'Desktop')    # Here, I am using Python to tell the computer to locate the 'Doyinsola.docx' file in 'Free-time', in 'Desktop', cut the file,
# and move the file to 'Desktop' -- in-other words, first item is the item you want to move. Second item is the location you want it to go to.

# To move a file to your current working directory, though, you would need to first import 'os' if you want to do it the easier way -- Example:
import os
import shutil
shutil.move('Desktop\\Free-time\\Doyinsola.docx', os.getcwd()) # Now you are moving the file to your current working directory without needing to write out its path.


# To delete files:
os.unlink('Desktop\\Free-time\\Doyinsola - Copy.docx') # For deleting files at the provided path --- HIGH RISK
os.rmdir('Desktop\\Free-time\\new_folder') # For deleting a folder at the provided path, folder should be empty, though --- HIGH RISK
shutil.rmtree('Desktop\\sample_folder') # This would remove all files and folders contained in the path. --- VERY HIGH RISK
# A lower risk method:
import send2trash
send2trash.send2trash('Desktop\\Free-time\\Doyinsola - Copy.docx') # This sends the file or folder in the path to the recycle bin. --- LOW RISK




# --------------- The 'random', 'math' and 'datetime' modules are very important libraries for particular operations in Python.
import random
import math
import datetime

# The 'Python Debugger' allows you to pause your code, mid-script, in-order to determine where an error exists in a code --
import pdb    # Importing the 'Python Debugger' library

# Code block
x = [1,2,3]
y = 2
z = 5

pdb.set_trace()  # Putting this here would pause the code at this line, before running the next line where an error would occur
# Better still, set the trace before all the results (But AFTER all the vairable definitions)...
# Typing 'q' into the dialog box for 'pdb' would allow you to quit the debugger.

result_1 = y + z
result_2 = x + z  # This would obviously cause an error becouse you can't add an integer to a list


# The 'time' library which is built into Python allows for a number of very interesting operations. It is imported as shown;
import time 
# Operations in the 'time' library can be used to determine how efficient a written code is. This is done by taking the time before and after the code starts to run, and finding the difference.

# Current time at execution of code
start_time = time.time()
# Code block to be run
print("Hello World!")
# Current time after execution of code
end_time = time.time()
# Time it took for the entire process
elapsed_time = end_time - start_time 
print(elapsed_time) # The time gotten here is in seconds from a start time several tens of years ago. You can conver that to readable time with:
readable_time = time.ctime(elapsed_time)
print(readable_time)

# A more precise way to check the efficiency of your code is with the 'timeit' module
import timeit # You can read up on how best to make use of this. -- Also make use of the documentation from Jose.


#-------------------------------------- Zipping and unzipping files with Python
# zipping
import zipfile
compressed_file = zipfile.ZipFile('compressed.zip', 'w') # Create the zip file in a manipulable way
compressed_file.write('first_file.txt', compress_type = zipfile.ZIP_DEFLATED) # Compressing the first file into the zip file -- Note that the zip file is still open.
compressed_file.write('second_file.txt', compress_type = zipfile.ZIP_DEFLATED) # Compressing the second file into the zip file -- Note that the zip file is still open.
compressed_file.write('third_file.txt', compress_type = zipfile.ZIP_DEFLATED) # Compressing the third file into the zip file -- Note that the zip file is still open.
compressed_file.close() # To close the zip file

# unzipping
zipped_file = zipfile.ZIP_DEFLATED('compressed.zip', 'r')
zipped_file.extractall('unzipped_content') # This would extract all the files in the zipped folder/file, 'compressed.zip' and put them into the folder, 'unzipped_content'.

# NOTE: With the shell utility library, you can point out an entire folder of contents and zip -- unlike zipping files one by one 
# zipping
import shutil
dir_to_zip = 'C:\\Desktop\\unzipped_content' # We are specifying the directory containing the folder that we would like to compress.
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip) # Sending the command to zip the contents in the file-path variable, 'dir_to_zip' into 'output_filename'.
# unzipping
shutil.unpack_archive('example.zip', 'final_unzip', 'zip') # Here, we are specifying the file path of the sipped file, asking for it to be unzipped into 'final_unzip' and specifying the file type.
# If you want to unzip to your current location, you can leave the destination folder name as an empty string. 'shutil' would automatically create an 'extracted_content' folder in same location.



#---------------------------------------------- Regular Expressions ----------------------------------------------------------
# 'Regular Expressions (REGEX)' allow you to search out particular patterns from bulk text -- SUch as finding things that look like phone numbers, emails or specific items in general text
# To use 'Regular Expressions' we have to import the respective library in Python

#--------- Example Set 1 -- When we know what exactly the item we are looking for looks like
import re     # Importing the 'Regular Expresisons' library

sample_text = "The truth of the book of countered shadows to be issued to the seeker by the mother confessor. A mother is a very important figure in a home."  # Just a sample text that we are to find stuff in
pattern = 'mother'    # Assuming we are to find the particular item in the 'sample_text', one way of doing that is saying

if pattern in sample_text:
	print(pattern)    # This looks for the first occurence of the item text you are looking to find in the 'sample_text', and allows you to perform operations. It can also be used in for-loops
	
# However, if you wan to use the 'REGEX' way, we could say

re.search(pattern, sample_text) # This finds the first occurrence of the specified item in the given sample text.
matchA = re.search(pattern, sample_text)  # This assigns the first occurrence of the searched out item properties to 'match1'. 'match1' essentially becomes an instance of the 're' class.
matchA.span() # Returns the index location span where the first occurence of the item occured in the string character array
matchA.start() # Returns the index position where the first occurrence of the searched-out item began
matchA.end() # Returns the index position where the first occurrence of the searched-out item ends
matchA.group() # Returns the item value you were searching for, in this case, 'mother'

# If you want to for-instance, find all the times the particular item occurred, you can use:
matchB = re.findall(pattern,sample_text) # This finds all the occurrences of the item in the sample_text, and organizes them as a list.
print(matchB)
# In this case, match2 is not an instance of the 're' class. It is more like a generated list.

# If you for-instance, want to loop through the occurrences -- This will especially come in handy when searching for phone numbers -- You can do:
for items in re.finditer(pattern, sample_text):
	print(items.group())

	
#--------- Example Set 2 -- When we do not know what exactly the item we are looking for looks like -- Finding a phone number
# \d = A digit ---- Example: file_\d\d ---- for: file_25
# \w = Alphanumeric ---- Example: \w-\w\w\w ---- for: A-b_1
# \s = White space ---- Example: a\sb\sc ---- for: a b c
# \D = Non-digit ---- Example: \D\D\D ---- for: ABC
# \W = Non-alphanumeric ---- Example: \W\W\W\W\W ---- for: *-+=)
# \S = Non-whitespace ---- Example: \S\S\S\S ---- for: Yoyo

# When the exact item is unknown, but the pattern is known -- for instance, the pattern of a phone number is '\d\d\d-\d\d\d-\d\d\d\d', where '\d' represents a digit.
# Consider the sample:
import re
phone_list = "The gardener's phone number is 438-929-3629. His boss phone number is 514-323-4477. Call Asap" # In this sample, there are two phone numbers we intedn to search out.
pattern = r"\d\d\d-\d\d\d-\d\d\d\d"  # Specify the pattern with a preceding 'r' so that Python does'nt see it as escape sequences.
pattern = r"\d{3}-\d{3}-\d{4}"  # The pattern may also be specified in this way where the value in the curly braces indicates the number of occurrences of the pattern (quantifier)
match1 = re.search(pattern, phone_list) # This uses the pattern to search out the first phone-number and assign it as an instance to match1 for further operations
print(match1.group()) # This prints the retrieved phone number to the screen.

# Scenarios may occur when you would want a portion of the data you just found -- For instance, the area code of a phone number. To do that, we use the 'compile' method as below:
pattern_split = re.compile(r"(\d{3})-(\d{3})-(\d{4})") # The use of the 'compile' method with parenthesis separated by dashes shows that we want to group the data into smaller subsections
match2 = re.search(pattern_split, phone_list) # The 'search' method is called with 'pattern_split' which uses the 'compile' method.
print(match2.group(1)) # This prints out '438' from the example input text-- note that indexing begins with '1', and not '0', here
print(match2.group(2)) # This prints out '929' from the example input text 
print(match2.group(3)) # This prints out '3629' from the example input text 
print(match2.group()) # Note that no index location was passed into 'group()'. This prints out the entire phone number as normal: '438-929-3629'

# To find all the numbers and print them out, we can do as such:
for items in re.finditer(pattern,phone_list):
    print(items.group())
	

	
# --- Quantifier deep-dive:
# + : Occurs one or more times ---- For example: Version \w-\w+ --- for: Version A-b1_1
# {3} : Occurs exactly 3 times ---- For example: \D{3} --- for: abc
# {2,4} : Occurs 2 to 4 times ---- For example: \d{2,4} --- for: 123
# {3,} : Occurs 3 or more times ---- For example: \w{3,} --- for: jbfudfbeu
# * : Occurs zero or more times ---- For example: ABC* --- for: AAACC
# ? : Once or none ---- For example: plurals? --- for: plural ---- 's' occurs once or none at all.

#--------- Example Set 3 -- When we do not know what exactly the item we are looking for looks like -- Finding an email
import re
# I'd put a sample text containing an email address that I would like to find:
email_string = "Hello, Nkem. Really nice hearing from you, recently. Please when you find the time, send me an email at sledgeunited@icloud.com. Thank you."
print(email_string)
pattern1 = r"\w{2,}@\w{2,}.\w{1,}" # Pattern, here, is a sequence of alphanumeric characters containing 2 or more words before an '@' sign, 2 or more words after '@' and 1 or more words after '.'

for items in re.finditer(pattern1, email_string):
    print(f"The email, {items.group()} was found in the text.")
 
 
#------- Additional stuff -------------------
find_text = re.search(r'boy|girl', 'The girl clapped and danced all day long') # This searches the text for any match for either 'boy' or 'girl'. A list is made from this.

find_text = re.findall(r'.op', 'The mop was put on top of the table to open the dance.') # This searches for any word that has 'op' in it and extracts it till the end of 'op' based on the number of dots before 'op'. These dots are called wild-cards. A list is made from this.

find_text = re.findall(r'[^\d]', 'There are 3 numbers inside 567, and 2 in 43') # This removes the digits (\d) from the text and extracts all other characters (including white spaces) to make a list of them.
# To get a list of the actual strings (instead of characters), and without the numbers, it couls be done as:
find_text = re.findall(r'[^\d]+', 'There are 3 numbers inside 567, and 2 in 43')
# More examples:
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
pattern = r'[^\W]+' # Now we are trying to remove non-alphanumeric characters, but keep the strings
clean = re.findall(pattern, test_phrase)
print(clean) # A print-out of list containing only the words is gotten.



#--------------------- Web-scraping with Python -------------------------------------
import requests  # Library that allows page source information of webpages to be accessed.
import bs4  # Beautiful soup library that allows information to be extracted from the webpage

result = requests.get("http://example.com") # Assigning the variable, 'result' with the information gotten from the requests.get() method. The variable thus takes in all the class attributes.
print(result.text) # Prints out the page source information from the accessed webpage

soup = bs4.BeautifulSoup(result.text, "lxml") # Using the methods in the 'bs4' library, the source code gotten from requests can be passed in its text attribute with the '.BeautifulSoup()' method
print(soup) # Prints out the source-code in a cleaned up way by 'beautiful soup'. 
# NOTE: Now that the entire source code has been passed into the 'beautiful soup' class, we can extract specific items.
print(soup.select('title')) # The 'select' method from the library, is used to print out the title of the webpage -- It prints it out along with the list view, and HTML information
# Note that beautiful soup automatically creates a list of the items it extracts, in-case there are more than one.
print(soup.select('p')) # To print out the items from within a paragraph -- It prints it out along with the list view, and HTML information
print(soup.select('p')[0] # To print out paragraph contents -- without list view, but with HTML information
Paragraph_content = print(soup.select('p')[0].getText()) # To assign the contents of the paragraph as a string to the 'Paragraph_content' variable -- without list view and the HTML information
print(Paragraph_content)


soup.getText('title') # Can be used to get all the HTML and CSS components associated with the tag sent in.
soup.select('div') # To grab all elements that have the 'div' tag
soup.select('#some_id') # To grab elements containing the id = 'some_id'
soup.select('.some_class') # To grab Elements containing the class = 'some_class'
soup.select('div_span') # To grab any elements named span within a div element
soup.select('div> span') # To grab any elements named span directly within a div element, with nothing in between
soup.clear() # To remove all the page source information from the variable.


# Scraping Example 1: Scraping the table of contents & paragraph information from a wikipedia page
import requests
import bs4

page_4_scrape = "https://en.wikipedia.org/wiki/Michael_Jackson" # Initializing the web address for the page to be scraped
contents = requests.get(page_4_scrape)
soup = bs4.BeautifulSoup(contents.text, "lxml")
# To scrape out the Table of contents
soup.select(".toctext") # The 'table of contents' are contained in the class name 'toctext'. hence'.toctext'. 
for items in range(0, len(soup.select(".toctext"))): # I am looping through the entire 'table of contents' number entries.
	print(soup.select(".toctext")[items].getText()) # I am printing out all the 'table of contents' entries. 'items' here ranges from 1 to the length of the 'table of contents'
	
# To scrape out the paragraph information
soup.select("p") # Paragraph contents are contained within the <p> key in HTML 
for items in range(0, len(soup.select("p"))):
    print(soup.select("p")[items].getText())




#-------------------------- Unicodes for emojis -----------------------------------------
# Note that modules have to first be installed
print("U+1F600") # For: grinning face
print("U+1F603") # For: grinning face with big eyes
print("U+1F604") # For: grinning face with smiling eyes
print("U+1F601") # For: beaming face with smiling eyes
print("U+1F606") # For: grinning squinting face
print("U+1F605") # For: grinning face with sweat
print("U+1F923") # For: rolling on the floor laughing
print("U+1F602") # For: face with tears of joy
print("U+1F642") # For: slightly smiling face
print("U+1F643") # For: upside-down face
print("U+1F609") # For: winking face
print("U+1F60A") # For: smiling face with smiling eyes
print("U+1F607") # For: smiling face with halo
print("U+1F970") # For: smiling face with 3 hearts
print("U+1F60D") # For: smiling face with heart-eyes
print("U+1F929") # For: star-struck
print("U+1F618") # For: face blowing a kiss
print("U+1F617") # For: kissing face
print("U+263A") # For: smiling face
print("U+1F61A") # For: kissing face with closed eyes
print("U+1F619") # For: kissing face with smiling eyes
print("U+1F60B") # For: face savoring food
print("U+1F61B") # For: face with tongue
print("U+1F61C") # For: winking face with tongue
print("U+1F92A") # For: zany face
print("U+1F61D") # For: squinting face with tongue
print("U+1F911") # For: money-mouth face
print("U+1F917") # For: hugging face
print("U+1F92D") # For: face with hand over mouth
print("U+1F92B") # For: shushing face
print("U+1F914") # For: thinking face
print("U+1F910") # For: zipper-mouth face
print("U+1F928") # For: face with raised eyebrow
print("U+1F610") # For: neutral face
print("U+1F611") # For: expressionless face
print("U+1F636") # For: face without mouth
print("U+1F60F") # For: smirking face
print("U+1F612") # For: unamused face
print("U+1F644") # For: face with rolling eyes
print("U+1F62C") # For: grimacing face
print("U+1F925") # For: lying face
print("U+1F60C") # For: relieved face
print("U+1F614") # For: pensive face
print("U+1F62A") # For: sleepy face
print("U+1F924") # For: drooling face
print("U+1F634") # For: sleeping face
print("U+1F637") # For: face with medical mask
print("U+1F912") # For: face with thermometer
print("U+1F915") # For: face with head-bandage
print("U+1F922") # For: nauseated face

# outside Unicode:
import emoji 
   
print(emoji.emojize(":grinning_face_with_big_eyes:")) 
print(emoji.emojize(":winking_face_with_tongue:")) 
print(emoji.emojize(":zipper-mouth_face:")) 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------









#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#*************************************************************************************************************************************************************************************************
#                                                                             PYTHON FOR DATA-SCIENCE
#**************************************************************************************************************************************************************************************************


# The Numpy library is an important 'Linear ALgebra' library in Python. A lot of libraries depend on it and it has bindings to C libraries.
# There are several methods available for use with the Numpy library. These methods would be visited.
# You would notice that unlike lists, in Numpy arrays, values are not separated by a comma. They are just separated by spaces like in regular matrices.
# Arrays, like lists, can hold different data-types.

# ---------------------- Lists to Arrays --------------------
# Numpy arrays may be vectors or matrices
# A vector is a list of numbers which may be in one row or one column
# A matrix is an array of numbers which may exist in one or more rows and one or more columns
# Lists can be easily converted to arrays with the Numpy library
import numpy as np

matrix_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] # A 2D array defined in a single line list form
two_D_Array = np.array(matrix_list) # Using the Numpy library to rearrange the list in array form - Like a matrix
print(two_D_Array) # Prints out the matrix-like form of the 2D array -- Note that multiple array types can be worked with: 3D, 4D, etc. 

# ------------------------ Some Numpy functionalities ------------------------------
Numpy_range = np.arange(0,22,2) # Would create an array spanning from 0 to 22, with a step-size of 2. This array is assigned to 'Numpy_range' which becomes an instance of the numpy array


Evenly_spaced_array = np.linspace(4,20,5) # Would create an array of 5 numbers spaced out equally between 4 and 20


Matrix_of_zeros = np.zeros((4,6)) # Would create a matrix array of zero arranged in 4 rows and 6 columns. The array is assigned to 'Matrix_of_zeros'. If only one value is given, it would create a single row with columns equal to the initialized number. -- Interesting things can happen to created matrices by adding further initializations to the specified rows and columns


Matrix_of_ones = np.ones((4,6)) # Similar to the matrix of zeros, but this time, for ones.


Identity_matrix = np.eye(5) # Would create an 5x5 identity matrix -- You can force it to take two value initilizers **


Random_0_1 = np.random.rand(3,3) # Would create a 3x3 matrix of random numbers between 0 and 1 -- Notice the dimensions were passed right in, instead of via a tuple.


Gaussian_distribution = np.random.randn(5,6) # Random values in negative and positive for Gaussian curve created in a 5x6 matrix -- Notice the dimensions are also not passed in as tuples, here


Random_integers = np.random.randint(1,49,6) # Would create an 6 number array of random integers from 1 to 48.
Random_integers.max() # Returns the maximum value integer in the array
Random_integers.argmax() # This specifies the particular index location where the first instance of the maximum integer value exists in the array
Random_integers.min() # Returns the minimum value integer in the array
Random_integers.argmin() # This specifies the particular index location where the first instance of the minimum integer value exists in the array
Random_integers.mean() # Returns the average of the integer values in the array
Random_integers.sort() # Sorts out the array from minimum value to the maximum value -- Just like is done with lists
Random_integers.dtype # Attribute that returns the data type of the values in the array


# With Numpy, you can re-shape already existing arrays in different ways. Such as taking a 1D array and reshaping it to look as a 2D array, as shown:
range_val = np.arange(0,36) # I am creating a variable instance of the Numpy class and using the numpy range method to assign a range of values spanning 0 to 25 into it.
range_val.shape # An attribute that returns the current shape of the vector - in-terms of rows and columns
print(range_val)
range_val.reshape(6,6) # By calling the 're-shape' method, I am able to take the values stored in 'range_val' and reshape into a 6x6 matrix. 
range_val.shape # To return the current shape of the vector - in-terms of rows and columns
print(range_val)
# Note that, this would only work if the total values in the array equal the size of the matrix. for instance it would also work for a 12x3 matrice, since total size = 36












































