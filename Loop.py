#1.write a python program that calculates and prints the sum of the squares of numbers from 1 to 5
#using a
sum_of_squares=0
sum=0
for i in range(1,6):
    squares=i*i
    sum_of_squares+=squares
print(f"sum of squares from 1 to 5 is {sum_of_squares}")




#Multiplication table.
table=int(input("enter the table number: "))
for i in range(1,11):
    print(f"{table}*{i}={i*table}")
    
    
    
    


#using for loop to find the sum of all even numbers bwtween 1 to 10.
sum_of_even=0
for i in range(0,11):
    if i%2==0:
      sum_of_even +=i
print(f"sum of squares of even numbers between 1 to 10{sum_of_even}")




#sum of all number
sum_of_numbers=0
num_1=int(input("enter the nth number"))
for i in range(1,num_1):
    sum_of_numbers +=i
print(f"sum of n all number is {sum_of_numbers} ")




#display numbers from a list using loop.
list_1=['3','5','1','4','9']
for i in list_1:
    print(i)


#display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)



#write a program to display all prime number within a range.
num_1=int(input("enter the 1st number:"))
num_2=int(input("enter the 2nd number:"))
for i in range(num_1,num_2+1):
   if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(f"{i} is a prime number") 
