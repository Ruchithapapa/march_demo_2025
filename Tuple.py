#1. Create a Tuple
#Write a program that creates a tuple containing three elements your name, your age, and your
#favorite color. Then print the tuple.
my_details = ("raj", 27, "blue")
print(my_details)


#2. Access tuple elements.
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days[2])


#3. Tuple Concatenation.
odd_tuples = (1,3,5)
even_tuples = (2,4,6)
tuples = odd_tuples+even_tuples
print(tuples)


#4. Tuple Unpacking.
rectangle = (12,3)
length,width=rectangle
rectangle_area = length*width
print("area : ",rectangle_area)


#5. Check if an element exists.
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(9 in tuple)
print(14 in tuple)


#6. Supermarket bill purchase
items = [("apple", 99), ("banana", 99), ("milk", 49)]
total = float(0)
print("item     price")
print("-"*15)
for i,j in items:
    print(i,j)
    total+=j
print("-"*15)
print("Total: ",total)    