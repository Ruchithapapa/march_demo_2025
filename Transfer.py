#Problem 1: Using break in a While loop
#Write a python program that takes a list of numbers as input numbers = [25, 30, 20, 40, 15, 
# 25] and prints the sum of the numbers. However, if the sum exceeds 100, stop adding
# numbers and print "sum exceeded 100".
number=[25, 30, 20, 40, 15, 25]
sum=0
for i in number:
    sum+=i
    if sum>100:
        print("sum exceeded 100")
        break
if sum<100:
    print("total sum{sum}")    



#Problem2: Using continue in a for loop
#Write a python script that uses a for loop to iterate through numbers from 1 to 600 print
#only the odd numbers, skipping the even onces using the continue statement.
for i in range(1,601,2):
    if i%2==0:
        continue
    print(i)



#Problem3: Using pass in conditional statements
# Write a python script that checks if a number is even or odd. If the number is even,
# print'even', if odd, do nothing (use the pass statement).
num=int(input("enter the number:"))
if num%2==0:
    print(f"it is an even")
else:
    pass        



#Problem4: Combining Transfer statements
#Write a python script that iterates through a list words. If the word is "break," exit
#the loop using the break statement, if the word is "skip," skip the rest of the code for
#the current iteration using the continus statement, for any other word, print the word
name=["sahasya", "bhanu", "raj","vinya","bhavishya"]
for i in name:
    if i=="bhavishya":
       break
    elif i=="bhanu":
        continue
    else:
        print(i)    