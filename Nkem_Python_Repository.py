Python_documentation = docs.python.org

'''
Docstring comment
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                           STRINGS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 'Strings' are more or less just an ordered and immutable array of characters.
# A string multiplied by a number would give several occurrences of said string together -- A sample is shown below:
mystring = 'z'
mystring = mystring * 10
print(mystring) # The print-out of this would be 10 z: zzzzzzzzzz
# NOTE also that you cannot concatenate strings with non-strings.

# Important methods to use with strings
.capitalize() # this capitalizes the first letter in a string -- irrespective if there are multiple full-stops, ONLY the first letter would be capitalized
.casefold() # this makes the entire characters in the string lower-case **? -- Used for caseless matching
.count(string/character) # to count the number of times a particular string or character occurred in the string 
.find(string/character) # Finds the index location for the first occurrence of the string or character.
.endswith(string/character) # returns 'True' or 'False', depending on if the string ends with the character or string you passed into the method
.startswith(string/character) # returns 'True' or 'False', depending on if the string starts with the character or string you passed into the method
.find(string/character, occurrence) # to find the index that a particular string or character occurred for the specified occurrence (like 2 for 2nd occurrence)
.lower() # to convert the characters in the string to lower-case
.upper() # to convert the characters in the string to upper-case
.islower() # returns 'True' if all the characters in the string are lower-case, and 'False' if the characters in the string are not lower-case
.isupper() # returns 'True' if the characters in the string are upper-case, and 'False' if the characters in the string are not upper-case
.isalpha() # returns 'True' if the contents of the string are all alphabets and 'False' if they aren't -- Note that it identifies spaces and punctuations as non-alphabets
.isdigit() # returns 'True' if the contents of the string are integers and 'False' if they are not integers (floats are not integers)
.isalnum() # returns 'True' if the contents of the string are alphanumeric
.isspace() # returns 'True' if all the characters in the string are white spaces.
.title() # Capitalizes the first letter of every word
.istitle() # returns 'True' if the first letter of every word of the string is upper-case, and 'False' if not.
.split(string/character) # returns a list of the words separated by the spaces from a string -- if a character or string is initialized, it returns splitting at that string word or character
.partition(string/character) # splits the string at only the first occurrence of the initialized string or character -- unlike split, it still returns the initialized character/string
s.center(20,'z') # To center the string 's' between 'z' characters and for a length of 20.


#String Interpolations

#using the '.format' method with indexing.
print ("The {0} {2} {1}".format("quick", "fox", "brown")) # Result: The quick brown fox

#using the '.format' method with keywords.
print ("The {q} {b} {f}".format(q = "quick", f = "fox", b = "brown")) # Result: The quick brown fox

#Using the F-string method
q = quick
b = brown
f = fox
print(f"The {q} {b} {f}")

# The '.format' method can also be used for float formatting, such as in example---
result = 100/777  # originally, that result would be: 0.1287001287001287
# However, if I wantto print to format the result (like rounding it up), and print to screen, I could use the '.format' method and specify width & precision. using format {value:width.precision f} Like so ---
print("The result was {r:1.3f}".format(r = result))
# Print out would be: 'The result was 0.129'
# Note, that the width (1) indicates how much white spaces before and with the value, precision (3)indicates how you want it rounded up.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                             BOOLEAN, COMPARISON AND LOGICAL OPERATORS
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
True and False ----> False
False and True ----> False
False and False ----> False
True and True ----> True

True or False ----> True
True or True ----> True
False or True ----> True
False or False ----> False

## Comparisons:
== # Check if equal
!= # Check if not equal
> # Check if greater than
< # Check if less than
>= # Check if greater than or equal to
<= # Check if lesser than or equal to

## Logical Operators:
and # The two conditions must be true, if not it returns false
or # At-least one of the conditions must be tru for it to return true
not # should not occur

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                            .TXT FILE MANIPULATION
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pwd # To print current working directory.

##Opening and reading files
with open('C:\\Users\\Admin\\Desktop\\email.txt') as myfile: # More functionality can be found with using SHIFT + TAB on Jupyter Notebook.
	myfile.seek(0) # To return the cursor to the beginning point of the file
	contents = myfile.read() # To read the entire file as a single line -- not the best
    contents = myfile.readlines() # contents becomes a list with each element equaling the first line from the text file.
print(contents)
	
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode ='r', encoding = 'utf-8') as myfile: #The encoding engine I added here is to allow python read non-English characters from the text file
    contents = myfile.readlines()
print(contents)
############################


##Opening and overwriting files -- Creates the file if the file initially doesn't exist.
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'w', encoding = 'utf-8') as myfile: #The encoding engine I added here is to allow python write non-English characters into the text file
    myfile.write('\nHello')
	
##Opening and adding to files
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'a', encoding = 'utf-8') as myfile: #The encoding engine I added here is to allow python append non-English characters into the text file
    myfile.write('\nInteresting')
	

##Opening and reading and writing to files
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'r+', encoding = 'utf-8') as myfile: #The encoding engine I added here is to allow python read/write non-English characters from/into the text file
    contents = myfile.readlines()
	
##Opening and overwriting and reading files -- Creates the file if the file initially doesn't exist
with open('C:\\Users\\Admin\\Desktop\\email.txt', mode = 'w+', encoding = 'utf-8') as myfile: #The encoding engine I added here is to allow python write/read non-English characters to/from the text file
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
# Existing key-value pairs may also be overriden in the same manner.

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

#NOTE that you can use 'Tuple unpacking' with dictionaries -- Sample shown below:
my_dict = {'k1':1, 'k2':2, 'k3':3}

for items in my_dict:
	print(items) # This prints out just the keys of the dictionary, whereas, if tuple unpacking (as shown below) is used:
	
for item1, item2 in my_dict.items():
	print(f"Key: {item1}") # Printing out from the keys
	print(f"Value: {item2}") # Printing out from the values
	
for items in my_dict.items():
	print(items) # Printing out the key-value pairs as individual tuples.
	
# Note that you can use the 'in' keyword to check if particular items exist in a dictionary.

# You can assign the keys, values or even items form a dictionary to an arbitrary variable. For instance:
key_variable = list(my_dict.keys())
value_variable = list(mydict.values())
nested_items = list(mydict.items())


# Dictionary comprehension example - Note that this is a big example, with concepts that would be discussed further down the line (like functions, lists, tuples):
users = [
    (0, "Bob", "bob123"),
    (1, "Rolf", "password"),
    (2, "Jose", "hbhefepass"),
    (3, "Michael", "forlive23")
] # A list with nested tuples containing information for users (ID number, name and password)

username_mapping = {item[1]: item for item in users} # Attempting to create a key-value pair for the user and user information from the nested list.
# Now, each tuple would be a value in the 'username_mapping' dictionary where the names (such as "Bob", "Rolf", etc.) would be the keys. For instance:
print(username_mapping['Rolf']) # This prints out the contents of the tuple where 'Rolf' is the name.
# You may then decide to write a function that takes in input for username and password, and checks to see if it exists in the database. Such as:
def sign_check(username, password, data):
    if username in data.keys() and password == data[username][2]:
        print(f"Welcome to your account, {username}")
    else:
        print(f"Sorry, I cannot recognize the username: {username}")
		
sign_name = input("Please enter your username: ")
sign_pass = input("Please enter your password: ")

sign_check(sign_name, sign_pass, username_mapping)
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


# Important information concerning tuples
x = 1,2,3 # Python seeing a comma or set of commas between values/items, automatically designates the variable as a type of tuple
x = (5,) # Even when defining a tuple with a single value, Python needs you to put a comma after the value so it doesn't designate it as a variable with brackets like BODMAS.
# Tuple methods 
.count(item) # to count the number of times a given item occured in a tuple -- if the item isn't there, it returns 0.
.index(item) # to determine the index of an item  for the first time it appears in the tuple.


# Important methods to use with lists
.append() # to add one new item to end of list
.pop(index) # to remove an item from end of list or indicated index
.extend(list) # to add the contents of one list into a new list 
.clear() # to remove all the items in a list
.count(item) # to count the number of times a given item occured in a list -- if the item isn't there, it returns 0.
.index(item) # to determine the index of an item  for the first time it appears in the list
.reverse() # to reverse the arrangement of items in a list
.remove(item) # to remove the first occurrence of an item in a list
.copy() # to return the contents of a list as an assignment to a new list variable
.insert(index, value) # to insert a value into a particular index location in a list
.sort() # To sort the contents of your list in place. 


## Sets are unordered collections of unique items.
# Note that elements in a set cannot be accessed by indexing, like lists and tuples.
# Important methods to use with sets
.add() # to add one new item to end of set
.pop(index) # to remove an item from the beginning of the set or indicated index
.clear() # to remove all the items in a set
.copy() # to return the contents of a set as an assignment to a new set variable -- future modification to the original set is not translated to the new set.
.discard(element) # To remove the initialized element from the set -- if not in set, nothing happens.
myset.intersection(another_set) # To return only the contents that are in both 'myset' and 'another_set'
myset.intersection_update(another_set) # To overwrite the contents of 'myset' with the elements that are both in 'myset' and 'another_set'
myset.union(another_set) # To unify the contents in 'myset' with the contents in 'another_set' and return the aggregate
myset.difference(another_set) # To return the elements in 'myset' that are not in 'another_set'
myset.difference_update(another_set) # To overwrite the contents of 'myset' with elements that are in 'myset' but are not in 'another_set'
myset.issubset(another_set) # Returns 'True' if 'myset' is a subset of 'another_set' or 'False' if 'myset' is not a subset of 'another_set'
myset.issuperset(another_set) # Returns 'True' if 'myset' has all the elements of 'another_set' or 'False' if 'myset' does not have all the elements of 'another_set'
myset.isdisjoint(another_set) # Returns 'True' if 'myset' and 'another_set' have no elements (null intersection) in common, otherwise it returns 'False'
myset.update(another_set) # Adds the elements in 'another_set' which are not in 'myset' 




#Tupule unpacking - to print out 2, 4, 6, 11.
list_tuple = [(1,2), (3,4), (5,6), (10,11)]

for (a,b) in list_tuple:
    print(b)
	
## NOTE: You can combine a while statement with an else statement for something to occur if the condition in while is not or no longer true.	
# When using looping functions like for and while loops, the following are important to keep in mind
# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Examples are shown below:

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
	
	
# Using the 'enumerate' function in Python:
word = 'abcde'
for item in enumerate(word):
	print(item) # The result would look like (0, 'a') -> (1, 'b') etc. -- It automatically prints the index, alongside with the item -- may come in handy.
	

# Using the 'zip' function in Python:
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']

for items in zip(mylist1, mylist2):
	print(items) # The result would look like: (1, 'a') -> (2, 'b') etc. -- It would only print for as long as the lists being zipped have same length -- would zip to the shortest list length.

new_list = list(zip(mylist1, mylist2)) # Creates a new list with the zipped lists.

	
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
# Functions use snail-casing
# When creating a function that takes in variables, if not specified, the function would only take in variables according to defined position. The alternative to this is using named arguments. For instance:
def sample_function(x,y):
	print(x+y)
	
sample_function(3,7) # When this executes, the 'sample_function' function would automatically assign the value: 3 to 'x', and the value: 7 to 'y' -- Here, arguments are taken in by position.
# You may decide that this is not what you intend to happen, and then instead of allowing the function to take in arguments positionally, you specify what arguments should be taken for where.
sample_function(y=3, x=7) # Now, when the function executes, the value: 3 would be assigned to 'y', and the value: 7 would be assigned to 'x'. 
# Note that the variable names for the arguments must be the same names indicated in the definition of the function.
	
## 'return' essentially breaks out of a function/loop --

# Interesting 2 functions to reverse an integer.
def twist(myinteger):
    mymodulus = 0
    my_reversed = 0
    
    while myinteger > 0:
        mymodulus = myinteger%10
        
        my_reversed = (my_reversed * 10)+mymodulus
        
        myinteger = int(myinteger/10)
        
    return my_reversed
# OR
def reverse_integer(my_integer):
    string_form = str(my_integer)
    reversed_string = string_form[::-1]
    reversed_integer = int(reversed_string)
    
    return reversed_integer



# Function to check anagram -- still needs work:
def check_anagram(string1, string2):
    string_list1 = []
    string_list2 = []
    check = True
    
    if len(string1) == len(string2):
        for items in string1:
            string_list1.append(items)
        
        for items in string2:
            string_list2.append(items)
        
        while check == True:
            if string_list1[0] in string_list2 and len(string_list1) != 0:
                var = string_list1.pop(0)
                index = string_list2.index(var)
                string_list2.pop(index)
                
                if string_list1[0] not in string_list2 and len(string_list1) != 0:
                    print("Not anagrams")
                    check = False
                
            else:
                check = False
                
        if len(string_list1) == 0 and len(string_list2) == 0:
            print("The words are anagrams")
        
    else:
        print("The words are not anagrams")
		
# OR -- better yet
def check_anagram(string1, string2):
    # Sort the string by extracting the characters and making a list out of them
    string1 = sorted(string1)
    string2 = sorted(string2)
    
    if len(string1) == len(string2):
        for items in range(0, len(string1)):
            if string1[items] != string2[items]:
                print("The words are not anagrams of each other.")
                return 
                break

        print("The words are definitely anagrams of each other.")
        
    else:
        print("The two words are not anagrams of each other.")
		
		
		

# Function 1 to sort an array -- Not the most processor efficient:
def sort_array(myarray):
    keep_count = 1
    
    while keep_count != (len(myarray)):
        for items in range(0, (len(myarray)-1)):
            if myarray[items] > myarray[items+1]:
                myarray[items], myarray[items+1] = myarray[items+1], myarray[items]
        
        keep_count += 1
            
    return myarray



# Function to find the smallest item in an array
def find_smallest(myarray):
    smallest = myarray[0]
    
    for item1 in range(0, len(myarray)):
        if myarray[item1] > smallest:
            continue
        for item2 in range(0, len(myarray)):
            if myarray[item1] <= myarray[item2]:
                smallest = myarray[item1]
                
    return smallest



# Function to reverse a list in-place -- i.e, no new memory allocation required.
def reverse_list(mylist):
    
    start_index = 0
    end_index = len(mylist)-1
    
    while end_index > start_index:
        mylist[start_index], mylist[end_index] = mylist[end_index], mylist[start_index]
        start_index += 1
        end_index -= 1
        
    return mylist



# Function to check for duplicates of elements within a list
def detect_duplicate(mylist):
    result = []
    
    for items in range(0, len(mylist)):
        for item2 in range(0, len(mylist)):
            if mylist[items] == mylist[item2] and items != item2:
                result.append(mylist[items])
                
    if len(result) != 0:
        result_set = set(result)
        for items in result_set:
            print(f"The program found a duplicate for: {items}")
        
    else:
        print("There are no duplicate items")




# Palindrome checker function -- NOTE that a palindrome is a word that looks exactly same when spelt backwards or forwards (e.g 'radar')
def check_palindrome(mystring):
    
    start_index = 0
    end_index = len(mystring)-1
    
    while end_index > start_index:
        if mystring[start_index] == mystring[end_index]:
            palindrome = True
            
        else:
            palindrome = False
            break
            
        start_index += 1
        end_index -= 1
        
    if palindrome == True:
        print(f"{mystring} is indeed a palindrome.")
        
    else:
        print(f"{mystring} is definitely not a palindrome")



# Prime number finder function
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
	

## ------------------------------------ ARGS and KWARGS ---------------------------------------------------------------------
# ARGS - Arguments
first, second, *others = [1,2,3,4,5,6,7,8,9,12,3,4]
print(first) # To print out the first item, i.e, 1
print(second) # To print out the second item, i.e, 2
print(others) # To make a list of all other items and print them, since the values going into the 'first' and 'second' variable has been achieved.

#A crude way to create a function that would be flexible for whichever number of parameters are passed into it would be like:
def AdditionFunction(a,b=0,c=0,d=0,e=0):
    #Here, the function must at-least get one argument passed in, whereas, it can sum up about 5 parameters. If only two arguments are passed in, it just sums the two with the other arguments initialized as 0. 
	result = sum((a,b,c,d,e))
	return result
	
#A much better way to do it would be as:
def AdditionFunction(*args): # A tuple would be returned
	result = sum((args))
	return result

# Example 1 -- Here, we would be creating a function to take in several parameters and an operator to use on the parameters.
# Note that the 'operator' variable must be a named variable when it is called.	
def apply(*args, operator):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        return multiply(args)
    else:
        return "I do not know what to do here."
# Calling the function:
print(apply(1,2,3,4,2,4,5, operator="+")) # Note how the operator was entered as a named variable, and the operation was entered as a string.

# Important to know: When passing '*args' as a parameter for a function;
# During execution: if '*args' is passed first, any other parameter following it must be named. if '*args' is passed last, other parameters need not be named.
	
	
	
# KWARGS - Key Word Arguments	
# *args and **kwargs are interesting way to ensure versatility of a function. While *args allows operations to be done for any number of arguments, **kwargs allows passing in of unlimited mapings and creates a sort of dictionary out of them. For example;
def NewFunction(**kwargs): # A dictionary would be returned
	if 'fruit' in kwargs:
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here.')
		
#We can call the function, now;
NewFunction(fruit = 'Apple', vegetable = 'Tomatoes')

# Additional stuff----------------------------------------------
## NOTE that functions relate to variables using the LEGB notation, where:
## L - Local (variables within the function itself)
## E - Enclosing (variables enclosed within a function that the function is enclosed within)
## G - Global (Variables outside the functions)
## B - Built-in (Python built-in variables)
## Note that you can change the value of a global variable from a function with the local same variable by declairng the keyword 'global' beside the variable
## For example:

x = 50

def func():
	global x # This tells Python that any change to the variable 'x', should be applied on the global variable 'x'
	print(f"For now, x is equal to {x}")
	
	x = 200 # Local reassignment of 'x'
	print(f"Now the value of 'x' is {x}")

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
# Lambda functions are nameless functions. They are also incapable of printing anything. All lambda functions can do is return values.
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

# Sample lambda function
lambda x,y : x+y # Lambda function to add two values together.
add = lambda x,y : x+y # Initializing the 'add' variable with the Lambda function/expression
add(3,5) # Calling the function on the arguments: 3 and 5. The sum is returned, here.


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
    
    def __init__(self, name, nationality, personality): # If there are no initializations in the '__init__' method, you may be able to get away with not defining it, as Pythin would do that.
        
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
		
	def __repr__(self): # To create an unambiguous representation of a class instance, so that you can use the information to maybe recreate the instance
		return f"<Book(Author: '{self.author}', Title: '{self.title}', Pages: {self.pages})>"
		
book_1 = Book("JK Rowling", "Harry Potter and the prisoner of Askaban", 700) # Creating a sample instance of the 'Book' class.
print(book_1) # This would print out the information in the '__str__' method. 
# However, if the '__str__' method was not created, the '__repr__' method would return information that may be used to recreate the instance of the class.




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
		
		
		
		
# @classmethod and @staticmethod
# Just as you can define methods to perform operations on instances with their objects and attributes, there also exists a method known as a 'class' method.
# A class method is essentially a method used by the class itself. 
# Also, there exists a method known as the 'static' method. 
# While inctance methods take in the instance and objects, class methods take in the class, static methods do not take in any arguments at all.

# For instance:

class Student():
    
    def __init__(self, name = "unnamed", ID = "Nil", grades = (0,0,0,0,0)):
        self.name = name
        self.ID = ID
        self.grades = grades
        self.university = "Concordia University"
        
        
    def avg_grades(self):
        total = 0
        for items in self.grades:
            total += items
            
        average = total/len(self.grades)
        return average
    
    def __del__(self):
        print(f"You have just deleted all information for {self.name}")
        
    @classmethod # Class method.
    def Student_method(cls): # In class methods, the class itself is passed in as an argument.
	# If you pass in the instance of the class, the 'class' method would be able to refer to the attributes, and methods of the instance.
        print("This is strictly for students of Concordia University.")
		
	@staticmethod # A static method. Static methods can be viewed as their own separate methods that exist within a class. It has no information about either the class or instance.
	def static_method1(): # Note that nothing is passed into the static method.
	# If you pass in the instance of the class, the 'static' method would be able to refer to the attributes, and methods of the instance.
		print("A static method has been called.")

# Calling the class method:
Student.Student_method()

# Calling the static method:
Student.static_method1()



# Consider this example:
# The @classmethod ***

class Store():
    
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })
        
    def stock_price(self):
        # To add all the item prices in the Store instance
        total = 0
        for items in self.items:
            total += items['price']
        return total
    
    @classmethod
    def franchise(cls, store):
        # To return another store, with the same name as the class arguments name, plus "- franchise"
        new_store = cls(store.name + "- franchise")
        return new_store
    
    @staticmethod
    def store_details(store):
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))
        # Returning a string representation of the class argument
        # It takes the format 'NAME, total stock price: TOTAL'
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
matchA = re.search(pattern, sample_text)  # This assigns the first occurrence of the searched out item properties to 'matchA'. 'matchA' essentially becomes an instance of the 're' class.
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
# Note that a code you may write to scrape information off a website may need to be updated even for the same website -- as website source code may change

import requests  # Library that allows page source information of webpages to be accessed.
import bs4  # Beautiful soup library that allows information to be extracted from the webpage

result = requests.get("http://example.com") # Assigning the variable, 'result' with the information gotten from the requests.get() method. The variable thus takes in all the class attributes.
print(result.text) # Prints out the page source information from the accessed webpage

soup = bs4.BeautifulSoup(result.text, "lxml") # Using the methods in the 'bs4' library, the source code gotten from requests can be passed in its text attribute with the '.BeautifulSoup()' method
# Note that 'lxml' is the engine used to decode the information being obtained from the 'result.text' method.
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




# Scraping Example 1: Scraping text items like - the table of contents & paragraph information from a wikipedia page
import requests
import bs4

page_4_scrape = "https://en.wikipedia.org/wiki/Michael_Jackson" # Initializing the web address for the page to be scraped - 'http' or 'https' associated with page must always be included.
contents = requests.get(page_4_scrape)
soup = bs4.BeautifulSoup(contents.text, "lxml")
# To scrape out the Table of contents
soup.select(".toctext") # The 'table of contents' are contained in the class name 'toctext'. hence'.toctext'. 
for items in range(0, len(soup.select(".toctext"))): # I am looping through the entire 'table of contents' number entries.
	# not that 'soup.select(".toctext")' returns a list of whatever items it finds.
	print(soup.select(".toctext")[items].getText()) # I am printing out all the 'table of contents' entries. 'items' here ranges from 1 to the length of the 'table of contents'
	
# To scrape out the paragraph information
soup.select("p") # Paragraph contents are contained within the <p> element in HTML 
for items in range(0, len(soup.select("p"))):
    print(soup.select("p")[items].getText())
	
	
	
	
# Scraping Example 2: Scraping images from a website (wikipedia page)
import requests
import bs4

page_4_scrape = "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)"
contents = requests.get(page_4_scrape)
soup = bs4.BeautifulSoup(contents.text, "lxml")
# It is important to know that images may be tagged using the 'img' keyword, but that may mean more than the target images being looked for. 
# It is rather preferable to use the class tag for the specific image being targetted. For instance:
for items in range(0, len(soup.select('.thumbimage'))): # The desired images in this webpage were contained in the 'thumbimage' class, hence, I specified the target with '.thumbinner'.
    print(soup.select('.thumbimage')[items]) # This would print out all the information concerning the images in the specified class, 'thumbinner'
    print("\n")
# One of the images from this webpage would look as:
# <img alt="" class="thumbimage" data-file-height="601" data-file-width="400" decoding="async" height="331" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/330px-Deep_Blue.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/b/be/Deep_Blue.jpg 2x" width="220"/>

# To specifically get to the image being targetted, the target. In this case, the content that 'src' equals to, we can assign the entire image to a variable and treat it like a dictionary.
image_01 = soup.select('.thumbimage')[0]
print(image_01['src']) # 'src' points to the URL for the image being targetted, and prints it out as a string.
# Print-out: '//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg'
complete_img_url = 'https:' + image_01['src'] # Assigning the 'https:' tagline to the image in-order to avoid errors.
image_file = requests.get(complete_img_url) # Requesting access to the image URL.
image_file.content # Binary information of the image

with open('C:\\Users\\Admin\\Desktop\\wikipedia_image.jpg', mode = 'wb') as myfile: # Creating the image on my desktop. 
    #NOTE: 'wb' - write binary is used to process the binary information of the image so it can be created. 
    myfile.write(image_file.content)




# Scraping Example 3: Scraping information from multiple pages of a website -- such as a website catalog of books for sale -- Here we know the total number of pages.

# In this example, one-star rated books from an entire book catalogue are analyzed and their titles are printed out.
import requests
import bs4

page_4_scrape = "https://books.toscrape.com/catalogue/page-{}.html" # For this example, a pro-scraping webpage with fake book catalogues that spans up to 50 pages is used.
# Each new catalogue page differs from the other by a number next to the hyphen after '...page'; as in '...page-1' for page 1, '...page-2' for page 2, etc.
product_list = []
page_no = 1
# Here we know the total number of pages is 50
while page_no < 51: # Since we know the total number of pages for the website, we increment 'page_no' from 1 to 50 (i.e less than 51)
    contents = requests.get(page_4_scrape.format(page_no)) # Here, we start initializing the information in each page to the contents variable -- going from page 1 up to 50
    soup = bs4.BeautifulSoup(contents.text, "lxml") # Here, we start decoding the information from the contents variable with 'Beautiful soup' -- going from page 1 up to 50
    for items in range(0, len(soup.select('.product_pod'))): 
        product_list.append(soup.select('.product_pod')[items]) # Here, we start appending decoded information under class 'product_pod' to the empty list 'product_list' -- from page 1 up to 50
		# Note that product_list contains all the HTML information of the books of interest.
        for items in product_list: # Looping through all the items now in the list 'product_list'
		# Note that now items would equal the individual instances of the 'soup.select('.product_pod')' method.
            if items.select('.star-rating.One'): # Here, we start checking if there is such a class named '.star-rating One' in the list called 'product_list'
                print(items.select('a')[1]['title']) # Here, we look through all the one star rated items, and extract the titles from them. 
				# 'a' is the HTML tag with information about the book image and title. 
                print("\n")
    page_no += 1 # With this, all the titles of the books with 1 star rating would be printed out.
	
# An important thing to note here is that items of type; 'bs4.element.Tag' can be treated as dictionaries, where information after a variable name with an equal sign can be extracted.




# Scraping Example 4: Scraping author information from a webpage of quotes: 'https://quotes.toscrape.com/' -- Here we do not know the total number of pages.
import requests
import bs4

count = 1 # The count variable is initialized with 1, since we expect the webpage to start counting from page 1
author_list = []
author_set = {}
search = True # We initialize the search variable to true, so that the code keeps scraping until search becomes false.

page_4_scrape = "https://quotes.toscrape.com/page/{}/" # Here we do not know the total number of pages associated with the website, but we know the pages differ from one another
# We use the curly braces and '.format()' method to allow the page to change; for page 1, {} is replaced by 1, for page 2, {} is replaced by 2, and on and on.

while search == True:
    contents = requests.get(page_4_scrape.format(str(count))) # Here, we start initializing the information in each page to the contents variable -- going from page 1 till we are forced to stop
    soup = bs4.BeautifulSoup(contents.text, "lxml") # Here, we start decoding the information from the contents variable with 'Beautiful soup' -- going from page 1 till we are forced to stop
    for items in range(0, len(soup.select('.author'))): # Author information is found in the 'author' class for each page.
        author_list.append(soup.select('.author')[items].getText()) # We append the author information for each page into the list, 'author_list'
        
    if 'No quotes found!' in contents.text: # On pages which exted beyond the available pages, in this example, we see the statement 'No quotes found!', so we use that to control the loop.
        search = False       
    else:
        search = True
        
    count = count + 1
    
author_set = set(author_list) # We make a set of all the author names found so that we can get out only the unique author information.
for item1 in author_set:
    print(item1)






#---------------------------------------------- Working with images in Python ----------------------------------------------------------
# The Pillow library is a fork of the PIL (Python Imaging Library) with easy to use function calls.
# Documentation for the library can be found here: pillow.readthe docs.io
from PIL import Image    # To use the 'pillow' library, you still have to call 'PIL' -- It can be called in this way.
photo1 = Image.open('C:\\Users\\Admin\\Desktop\\Random images\\1.jpg')
photo1.show() # This can be used to call the photo to be displayed.

photo2 = photo1.crop((530,100,1000,740)) # I am creating a new image, photo2, that is essentially a cropped version of the first impage, photo1.
photo1.paste(im=photo2, box=(0,0)) # I am pasting the new image, photo2, into the original image, photo1 with its 0,0 point coincident with the 0,0 point of photo1.
# Note that whatever changes you make would permanently affect the variable, allbeit not permanently affecting the original image.

# Image formats usually exist as 'RGBA' formats, where R = Red, G = Green, B = Blue and A = Transparency. 
# Each of these go from 0 to 255 with 0 meaning a complete absence (in case of R, G and B values), and 255 meaning complete presence (in case of R, G and B values)
# For A, i.e 'Alpha', 0 means complete transparency of the image, 255 means complete opacity of the image.

# Important attributes with images
.size # to show the size of the image in pixels
.filename # To get the file name of the image -- with the path
.format_description # To get the format of the image
.crop((left, upper, right, lower pixel)) # (x,y,width,height) -- To crop the photo accourding to the entered dimensions in pixel value -- imagine it moving clockwise
.resize((pixel_dimension1, pixel_dimension2)) # To stretch or squeeze the image to new dimensions
.rotate(degree) # To rotate the image to whatever degree value that was specified.
.putalpha(value) # To adjust the transparency level of the image from completely transparent 0 value to completely opaque 255 value.
.getpixel((dimension1,dimension2)) # Returns the pixel value at the specified point in an image.
.putpixel((dimension1, dimension2),(R_value,G_value,B_value,A_value)) # Allows you to adjust the RGB values of a photo at the indicated dimensions (x,y).
.save(file path) # Saves the image variable as a new image in the specified file-path or with the specified name.




#---------------------------------------------- Working with CSV in Python ----------------------------------------------------------
# .csv files, can be gotten out of regular spreadsheet files, like excel spreadsheet files, however, .csv would only contain the raw data from the spreadsheet.
# Things like images, formulas, etc., cannot be contained in a .csv file
# Pandas library allows for extensive data science applications, inclusive of .csv manipulation
# Openpyxl library is another module for manipulating excel related files and documents
# Google sheets Python API
import csv  # Library that allows you work with .csv files, asides the already aforementioned.

working_sheet = 'C:\\Users\\Admin\\Desktop\\Randoms\\Random SpreadSheets\\example.csv'  # Initializing the variable, 'working_sheet' with the file-path for the file we intend to work with.
contained_data = open(working_sheet, encoding='utf-8') # Initializing the variable, 'contained_data' to be the read value of the information in the file-path variable.
# Note that a peculiar encoding engine was chosen for this case, i.e 'utf-8'. Other encoding engines exist -- all dependent on the type of data you want to work with.
csv_data = csv.reader(contained_data) # Using the reader method in the csv library to make sense of the data and send the results into the variable, 'csv_data'
data_lines = list(csv_data) # Type casting the data in the 'csv_data' variable into a much easier manipulable list form.

# More cleanly put -- especially so you don't need to remember to close the file later on:
with open(working_sheet, encoding = 'utf-8') as myfile:
    csv_data = csv.reader(myfile)
    data_lines = list(csv_data)  # Now the list called 'data_lines' has all the information concerning the data that was mined with the csv library.
	
len(data_lines) # To give information concerning the length of rows in the .csv file.


# CSV Example 3: Reading a '.csv' file and entering the information into a '.txt' file -- The '.csv' file, here, has data arranged in 7 columns and 1000 rows:
import csv

working_sheet = 'C:\\Users\\Admin\\Desktop\\Randoms\\Random SpreadSheets\\example.csv' # Initializing the variable, 'working_sheet' with the file-path for the file we intend to work with.

with open(working_sheet, encoding = 'utf-8') as datafile: # Opening the '.csv' file with the 'utf-8' encoding to allow non-English text to be read.
    csv_data = csv.reader(datafile)
    data_lines = list(csv_data) # Creating a list of the data read from the '.csv' file
	
with open('C:\\Users\\Admin\\Desktop\\Randoms\\Random SpreadSheets\\example.txt', mode = 'w', encoding = 'utf-8') as myfile: 
# Opening the '.txt' file with the 'utf-8' encoding to allow non-English text to be written.
    for items in range(1, len(data_lines)): # Looping through the entire length of the list to extract information
        myfile.write(f'Currently decoding line: {items} \n')
        myfile.write(f'{data_lines[0][0]}: {data_lines[items][0]} \n') # Organizing by columns 
        myfile.write(f'{data_lines[0][1]}: {data_lines[items][1]} \n') # Organizing by columns
        myfile.write(f'{data_lines[0][2]}: {data_lines[items][2]} \n') # Organizing by columns
        myfile.write(f'{data_lines[0][3]}: {data_lines[items][3]} \n') # Organizing by columns
        myfile.write(f'{data_lines[0][4]}: {data_lines[items][4]} \n') # Organizing by columns
        myfile.write(f'{data_lines[0][5]}: {data_lines[items][5]} \n') # Organizing by columns
        myfile.write(f'{data_lines[0][6]}: {data_lines[items][6]} \n') # Organizing by columns
        myfile.write("\n\n")


# CSV Example 4: Writing to a '.csv' file directly from a list:
import csv

sheet_to_read = 'C:\\Users\\Admin\\Desktop\\Randoms\\Random SpreadSheets\\makeup_new.csv'

with open(sheet_to_read, mode= 'w', encoding = 'utf-8', newline='') as datafile:
    csv_data = csv.writer(datafile, delimiter=',') 
	# The 'delimiter' here, is just to let Python know how the items were separated in-order for Python to read the files -- Separations can be with anything, not just commas.
    csv_data.writerow(['a','b','c']) # In-case you just want to write a row at a time. May be useful, especially if parsing from a list
    csv_data.writerows([['1','2','3'],['4','5','6']]) # Always note that to indicate multiple rows, a 2-D array has to be passed in.
	
	
	

#---------------------------------------------- Working with PDFs in Python ----------------------------------------------------------
# Unlike '.csv' files, some PDF files are not readable by Python -- Unless with advanced ML methods.
# Unreadable PDF files include PDFs generated by scanning documents - Scanned documents are essentially like pictures.

# Reading into PDFs ------------------------------------------------------------------
import PyPDF2 # Import the library that allows for analysis of the PDF document

PDF_to_read = 'C:\\Users\\Admin\\Desktop\\Randoms\\Random PDFs\\Some_BrandNew_Doc.pdf' # Initializing the variable, 'PDF_to_read' with the file-path for the PDF we intend to work with.

with open(PDF_to_read, mode='rb') as myfile: # PDF files are read in binary form - just like images being scraped off a website. 
# There is also no encoding since it is being read in binary form.
    pdf_data = PyPDF2.PdfFileReader(myfile)
    print(pdf_data.numPages) # To determine the number of pages in the PDF -- returns the page number as an interger.
	
	page_one = pdf_data.getPage(0) # To read the items in the first page of the PDF file, we take the variable containing the PDF data and use the 'getPage()' method. 
	# 0 here indicates first page. So now, the data in page 1 is stored in the variable 'page_one'
    page_one_text = page_one.extractText()
	# The PDF page 1 data in the 'page_one' variable is extracted with the 'extractText()' method.
    print(page_one_text) # The extracted text from page 1 of the PDF is printed to screen.
	
# Overwriting PDFs ----------------------------------------------------------------------
import PyPDF2

PDF_to_read = 'C:\\Users\\Admin\\Desktop\\Randoms\\Random PDFs\\Some_BrandNew_Doc.pdf' # We would be taking the contents from the first page of this PDF document
PDF_to_write = 'C:\\Users\\Admin\\Desktop\\Randoms\\Random PDFs\\Some_New_Doc.pdf' # We would be replacing the contents of this entire PDF document

with open(PDF_to_read, mode='rb') as myfile: # Reading the contents of the first PDF
    pdf_data = PyPDF2.PdfFileReader(myfile) # Reading method is called off this instance

    first_page = pdf_data.getPage(0)

    write_pdf = PyPDF2.PdfFileWriter() # Writing method is called off this instance
    write_pdf.addPage(first_page)

    with open(PDF_to_write, mode='wb') as newfile: # Overwriting the contents of the first PDF
        write_pdf.write(newfile)







#---------------------------------------------- Sending emails with Python ----------------------------------------------------------
import smtplib  # In-built Python library called 'Simple Mail Transfer Protocol' that allows for emails to be sent through a Python script.
import getpass  # In-built Python library that hides things like passwords or text input that you want to hide

smtp_object = smtplib.SMTP('smtp.gmail.com',587) 
# Initialize a variable, 'smtp_object' that accesses the SMTP of the chosen mail (gmail in this case), port-number here is 587 -- some cases may have 465
smtp_object.ehlo() # The variable is now an instance of the SMTP class. The '.ehlo()' method is used to greet the server.
smtp_object.starttls() # The '.starttls()' method is used to start the encryption process for the intended email to be sent.

email = getpass.getpass("Please enter your email address: ") # Instead of using input(), I am using the 'getpass' library to take the email in a hidden manner.
password = getpass.getpass('Please enter your app password: ') # Instead of using input(), I am using the 'getpass' library to take the app password in a hidden manner.
# Note that 'app password' differs from 'email password' for gmail -- You get the app password after you enable 2 factor authentication 
smtp_object.login(email, password) # The 'login()' method takes in the email and app password and enters them into the server for verification.

sender_address = email # The email address sending the email
to_address = '12345@yahoo.com' # The email address the mail is being sent to
subject = input("Enter the subject of the email: ") # Take in the intended subject of the email
message = input("Enter the message: ") # Take in the intended body of the email
msg = "Subject: " +subject+"\n"+message # Concatenate them in this way -- the class being used would understand how to separate them.

smtp_object.sendmail(sender_address, to_address, msg)
smtp_object.quit() # Close the connection to the email server.




#--------------------------------------------------- EXTRAS ------------------------------------------------------
min(a_list) # returns the minimum value from the passed in list.
max(a_list) # returns the maximum value from the passed in list.
sum(a_list) # returns the sum of all the elements from the passed in list.
len(a_list) # returns the number of items in a list.

#------------ Numbers -------------------------------------------
hex(number) # To convert an integer into a hexadecimal format of the number -- output is in string format
bin(number) # To convert an integer into a binary format of the number -- output is in string format
pow(number1,number2) # Raise number1 to the power of number2 -- i.e number1**number2
pow(number1,number2,number2) # Raise number1 to the power of number2 and find the remainder when divided by number 3 -- i.e (number1**number2)%number3
abs(number) # Returns the absolute value of a number. i.e: -3 = 3, 3 = 3
round(number[, ndigits]) # Would round-up any given number to 0 decimal places, unless when specified as ndigits decimal places




#-------------------------- Unicodes for emojis -----------------------------------------
# Note that modules have to first be installed
print("\U0001F600") # For: grinning face
print("\U0001F603") # For: grinning face with big eyes
print("\U0001F604") # For: grinning face with smiling eyes
print("\U0001F601") # For: beaming face with smiling eyes
print("\U0001F606") # For: grinning squinting face
print("\U0001F605") # For: grinning face with sweat
print("\U0001F923") # For: rolling on the floor laughing
print("\U0001F602") # For: face with tears of joy
print("\U0001F642") # For: slightly smiling face
print("\U0001F643") # For: upside-down face
print("\U0001F609") # For: winking face
print("\U0001F60A") # For: smiling face with smiling eyes
print("\U0001F607") # For: smiling face with halo
print("\U0001F970") # For: smiling face with 3 hearts
print("\U0001F60D") # For: smiling face with heart-eyes
print("\U0001F929") # For: star-struck
print("\U0001F618") # For: face blowing a kiss
print("\U0001F617") # For: kissing face
print("\U000263A") # For: smiling face
print("\U0001F61A") # For: kissing face with closed eyes
print("\U0001F619") # For: kissing face with smiling eyes
print("\U0001F60B") # For: face savoring food
print("\U0001F61B") # For: face with tongue
print("\U0001F61C") # For: winking face with tongue
print("\U0001F92A") # For: zany face
print("\U0001F61D") # For: squinting face with tongue
print("\U0001F911") # For: money-mouth face
print("\U0001F917") # For: hugging face
print("\U0001F92D") # For: face with hand over mouth
print("\U0001F92B") # For: shushing face
print("\U0001F914") # For: thinking face
print("\U0001F910") # For: zipper-mouth face
print("\U0001F928") # For: face with raised eyebrow
print("\U0001F610") # For: neutral face
print("\U0001F611") # For: expressionless face
print("\U0001F636") # For: face without mouth
print("\U0001F60F") # For: smirking face
print("\U0001F612") # For: unamused face
print("\U0001F644") # For: face with rolling eyes
print("\U0001F62C") # For: grimacing face
print("\U0001F925") # For: lying face
print("\U0001F60C") # For: relieved face
print("\U0001F614") # For: pensive face
print("\U0001F62A") # For: sleepy face
print("\U0001F924") # For: drooling face
print("\U0001F634") # For: sleeping face
print("\U0001F637") # For: face with medical mask
print("\U0001F912") # For: face with thermometer
print("\U0001F915") # For: face with head-bandage
print("\U0001F922") # For: nauseated face

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












































