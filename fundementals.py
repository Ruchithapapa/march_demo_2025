#1. Write a python program that prints your Name 
print("Ruchitha")

#2. Create a python script with both single-line and multi-line comments explaining the propose of the script
#single line comment
age = 25
print(age)

#multi-line comments
num_1 = 20
num_2 = 25
result = num_1+num_2
print(result)


#3. Define a list containing three different data types
list = [25,3.5,"Raj"]
print(list)
print(type(list))
# Define a set containing employee id's
set = {1,2,3,"Ruchitha",5.7,1,1,3,3.5,"sahasya"}
print(set)
print(type(set))


#4. Concatenate two string and print the result
vegetable = "tomato"
animal = "lion"
result = (vegetable + animal)
print(result)
print(type(result))
#Repeat a string three times and display the output
employee_name = "sahasya"
print(employee_name)
print(type(employee_name))
#6. Declare two variables, one string an integer and the other a string. print their values.
int = 35
subject = "English"
print(int,subject)
print(type(int))
print(type(subject))
#7. Convert a float to an integer and print the result.
height = 5.2
print(height)
print(type(height))
print(id(height))



#float ----> integer
height = 5.2
print(height)
print(type(height))
int_conversion = int(height)
print(int_conversion)


#Convert an integer to a string and display.
num = 22
print(num)
print(type(num))


#integer -----> string
num= 22 
print(num)
str_conversion = str(num)
print(str_conversion)
print(type(str_conversion))

#8. Take the user's age as input and print a message using that input.
age = int(input("enter your age"))
print(age)