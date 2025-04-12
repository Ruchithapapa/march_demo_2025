#'{----------}'
#---> function is a block of code. Which only runs when it is called.
#--> in python, function is a block of organized. resuable code that perferms a specific task or set of task.
#--> function allow you break down your code into smaller modular pieces and making it more reable, maintainable and reusble.
#--> to define a function def.
# Syntax:
# def funcname():
      #block of code
      #block of code
#statements '''function call'''
#-->to call the created cuntion, we use function call.
#def great():
#function Name
#     print("hello, welcome to pythonlife") block of code
#     num_1 = 10   #  block of code
#     num_2 = 20   #  block of code
#     print(num_1+num_2)  #  block of code
#great()
#list_1()

##### WAY1 ####
#def details():
#   user_name = "Raj"   #here user_name is variable. and raj is value.
#   id = 12345   #in  function we call variables as parameters and values are arguments.
#   print(f"username is {user_name} and id is {id}")
#details()


#### WAY2 ####
#def details(user_name,id):
#    print(f"username is {user_name} and id is {id}")
#details("raj", 2468)

#''' parameters and arguments'''
#--> parameters are variables that are used in a function definition.
#--> arguments are values passed to function during the function call.
#--> parameters receive values from arguments.
# Syntax:
# def multiply(x,y):    here parameters count = arguments coumt.
#    print(x*y)
#    return x*y
#multiply(3,4)


#''' return '''
#--> used to exist a function and return a value to the function.
#def my_func(x,y):
#   return(x-y)  # only once return is used in one func, once the return is used, we cannot excute any statments.
#   print(x+y)   # here unable to excute.
#obj = my_func(10,5)  #storing the return value into an variable called obj.
#print(obj*4)     #after storing we can perform operations.


#'''### default parameters ####'''
#-->fewer arguments wont accept the function. to over come. we can use default parameters.
#def sub(a=None,b+None,c=None):
#    print(a,b,c)
#sub(2,3,4)
#sub(2,4)
#sub(2,3)
#-->in form filling. if user did not fill with data. in that place we used the None.
#
#def power(base,exponent=2):
#    return(base**exponent)
# print(power(3))   here expo default value
# print(power(3,1))


#'''##### orbitary arguments ####'''
#-->function can accept a variable with n no. of arguments by using
#--> *argu(syntax)   resilt will be in tuple format.
#here * means all
#def details(*a):
#    print(a)
#details("vasu", "raj", "chinna")


#'''#### keyword arguments####'''
#-->keyword arguments are passed to function with a keyword and vlue, allowing for more explicit parameter passing.
# def sample(**a):
#     print(a)
# sample(vasu=2344, raj=5372)    o/p will be dict format

#'''#### variable ####'''#-->two types:
#-->1. local variables-->present inside the function(this variable is declared only to particular one function)
#2. global variables-->present outside the function(a variable declared outside of all functions and accessiable throughtout the program, including inside functions)

# 1. local variable:
#def greet():
    #name = "raj"
    #dept = "frontend"
   # print(name)
  #  print(dept)
 #   print(name*2) #local variables can perform operations only inside the function.
#greet()

#2. global variables:
#balance = 1000
#def credit(amount):
#    print(amount)
#   print(balance*3) #here the value is taken from global variables
#credit(500)
#credit(balance)

#balance = 1000
#def credit(amount=0):
#   global balance  #her we have to use "global" to perform below operations.
#    balance += amount
#    print(balance) here the value is taken from global variable
#credit()


#'''##### key points ####'''
#-->local variables are limited to the function scope.
#-->global variables are accessible throughtout the program but can only be modified inside a function if declared as 'global'

#-->collections of function-- modules.(every python file is module)
#-->are used to organize code into reusable units.
#-->three types:
#1. user defined
#2. built_in
#3. third party

#def add(a,b):
#    print(a+b)
#def sub(a,b):
#    print(a-b)
#def mul(a,b):
#    print(a*b)
#def expo(a,b):
#   print(a**b)
#add(5,5)  #here if any mistake happend in one of the function, we can check to corresponding function
# only. It wont disturb to other functions.
#sub(4,6)
#mul(3,4)
#expo(2,3)


#'''## 1. USER DEFINED ####'''
# IMPORT FROM SOME OTHER MODULE CREATE BY USER.
# Syntax: import modulename
# import conditional.age
# modulename.funcname()

# import sample  #the py files present in same working directory, then we can import.
# sample.sub(3,4)
#sample.expo(2,3)
# if the module is present in another folder, by using path, we can import. We can discuss in file handling
# from sample import *           # * is all.
#add(35,10)         #here no need to call module again. directly we can perform actions
#these are user define modules.

#'''#### 3. third party####'''
# first module has to install into the system and next import

#'''### 2. built_in ###'''
#import from some other module, but they are in built_in in python.
# there are few module: to operate particular module right click on module name select go to definition
# '1.math'
# provides mathematical functions like trigonomatric, logarithmic, exponential functions and more.
# from math import *    #here calling all functions present if math module.
#print(sqrt(16))          # squareroot
#print(pi)     #no need to use modulence. as we are import from the module.
#print(int(pow(2,3)))      #o/p: 8... (2 power 3)
#print(ceil(3,4))    # results as round up a number to the nearest highest integer.
#print(fabs(3.8))    # return the absolute value
#print(floor(2,9))   # results as round up a number to the smallest integer.
#print(radians(115)) # convert angle from degress to radians
#print(factorial(5)) # 5!=120
# '2. random'
# to generate pseudo numbers.
#from random import *
# numbers =[1,2,3,4,5]   #works only on mutable datatypes like list.
# shuffle(numbers)
# print(numbers) 
# print(randint(0,5))         # include starting and ending 
# print(choice(['apple','banana','cherry']))      #randomly choose from the list
#'3.datetime'   #-->provide date and time
# from datetime import *
# now = datetime.now()
# print(now)                # here why we are storing in variable now and using to print.
#'4. os '        #-->returns to current working directory
# import os
# print(os.getcwd())
#'5. sys'
# import sys
# print("Before exiting...")
# sys.exit("Exiting the script now!")  # Exit with a message. once we use exit we cannot print any statment 
# print("This will not be printed.") 
# print("Python Version:", sys.version)
# print("Version Info:", sys.version_info)            #version and version_info used to extract the python version and info of what we are using.
# print("Default Recursion Limit:", sys.getrecursionlimit())
# sys.setrecursionlimit(2000)                     # here we are updating the recursion limit to 2000
# print("New Recursion Limit:", sys.getrecursionlimit())
# print("OS Platform:", sys.platform)         #"win32" → Windows(platform)

# Function	                Description
# sys.argv	                Get command-line arguments
# sys.exit()	            Exit the script
# sys.version	            Get Python version
# sys.setrecursionlimit(n)	Change recursion limit
# sys.stdout              	Redirect standard output
# sys.platform            	Get operating system name
# sys.maxsize               Get max integer size




#''' ############## quiz ########## '''
# 1. purpose of using functions in python:
# ->to organize code into logical blocks.
# ->to improve code readability and maintainability.
# ->to enable code reuse.
# 2. "def" key is used to define a function in python.
# 3.valid way to call a function named "my_function" with no arguments:
# my_function()
# 4. scope of a variable defined inside a function in python
# local scope


#'''######## task ###########'''
#'task1:'# add function:
# def add(a=0,b=0):
#     a = int(input("enter the first number :"))
#     b = int(input("enter the second number :"))
#     print(a+b)
# add()
#'task2:' #square function:
# def square(a=0):
#     a = int(input("enter the number :"))
#     print(a*a)
# square()
#'task3:' #factorial function:
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# num = int(input("Enter a positive integer: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"Factorial of {num} is {factorial(num)}")
#'task4:' # maximum function:
# def maximum(numbers):
#     if not numbers:  # Check if the list is empty
#         return None
#     return max(numbers)
# nums = [10, 25, 89, 65, 32]
# print(f"Maximum value: {maximum(nums)}")  
#'task5:' #reverse function:
# def reverse(s):
#     return s[::-1]  # Using slicing to reverse the string
# s = input("Enter a string: ")
# print("Reversed string:", reverse(s))
#'task6:' #check prime function: """Returns True if n is a prime number, otherwise False."""
# def is_prime(n):
#     if n < 2:
#         return False  # Prime numbers start from 2

#     for i in range(2, int(n ** 0.5) + 1): 
#         if n % i == 0:
#             return False  # Found a divisor, not prime

#     return True  # No divisors found, prime number
# num = int(input("Enter a positive integer: "))
# print(f"Is {num} a prime number? {is_prime(num)}")
#'task7:' # fibonacci function:     """Returns the nth Fibonacci number using recursion."""
# def fibonacci(n):
#     if n <= 0:
#         return
#     elif n == 1:
#         return 0  # First Fibonacci number is 0
#     elif n == 2:
#         return 1  # Second Fibonacci number is 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# num = int(input("Enter a positive integer: "))
# print(f"The {num}th Fibonacci number is {fibonacci(num)}")
#'task8:' # palindrome function:
# A palindrome is a word, phrase, or sequence that reads the same forward and backward, 
# e.g., "madam", "racecar", "level", etc.
# def is_palindrome(s):
#     """Returns True if s is a palindrome, otherwise False."""
#     s = s.lower().replace(" ", "")  # Convert to lowercase & remove spaces
#     return s == s[::-1]  # Compare with its reverse
# word = input("Enter a string: ")
# print(f"Is '{word}' a palindrome? {is_palindrome(word)}")
#'task9:'  # sum of squares function:      """Returns the sum of squares of the given list of numbers."""
# def sum_of_squares(numbers):
#     return sum(num ** 2 for num in numbers)
# nums = list(map(int, input("Enter numbers separated by spaces: ").replace(',', ' ').split()))
# print(f"Sum of squares: {sum_of_squares(nums)}")
#'task9:'       # avg functions:        #    """Returns the average of a list of numbers."""
def average(numbers):
    if not numbers:
        return "List is empty! Cannot calculate average."
    return sum(numbers) / len(numbers)
user_input = input("Enter numbers separated by spaces or commas: ")
numbers = list(map(float, user_input.replace(',', ' ').split()))
print("Average:", average(numbers))



