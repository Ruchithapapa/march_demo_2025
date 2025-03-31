#Write a python function square.all(numbers) that takes a list of numbers as input and returns a
#new list containing tha square of each number in the input list. Use the map() function with a
#lambda func to implement this.
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda i:i**2,list_1)
print(list(result))


#Write a python func filter.positive(numbers) that takes a list of numbers as list and returns a
# new list containing only the positive numbers from the input list. Use the filter() func with a
# lambda func to implement this.
list_1 = [-7, -4, 2, 8, -25, 61, 12, -13, 15]
result=filter(lambda a:a>0,list_1)
print(list(result))


#Write a python function calculate_factorial(n) that calculates the factorial of a given number n.
# Use the reduce() func with an appropriate lambda func to implement this.
from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
print(factorial(5))


#Write a python func count_vowels(string) that takes a string as input and returns the count of
#vowels (a, e, i, o,u) in the input string. use the reduce() func with an appropriate lambda func
#to implement this,
def count_vowels(string):
    from functools import reduce
    return reduce(lambda count,char:count + (1 if char in string2 else 0), string,0)
string = input("enter your string : ")
string2="aeiouAEIOU"
print(f"the no.of vowels in {string} is {count_vowels(string)}")