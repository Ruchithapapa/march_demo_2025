#1. Vowel Checker:
#Write a python program that takes a character as input and checks whether it is a vowel or not.
#use the if-else statement.
vowels = ('a','e','i','o','u')
character = input("enter the string" )
#here string is vowels
if character in vowels:
  print(f"{character} is a vowel" )
else:
  print(f"{character} is not a vowel" ) 




#2. Age group classification
#Write a program that an age as input and classifies the person into one of the following age groups.
age=int(input("enter the age"))
if age>0 and age<=12:
  print("person is child" )
elif age<=17:
  print("person is teenager" ) 
elif age<=64:
  print("person is adult" )
else:
  print("person is senior" )


#4. Leap year checker
#Create a program that checks whether a given year is a leap year or not. A leap year is divisible
#by 4, but not by 100 unless it is diviaible by 400.
year=int(input("enter year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not leap year") 
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




#5. Calculator:
#Build a simple calculator prigram that takes two numbers and an operator (+,_,*,/) as input and
#performs the corresponding operation.
if opr=='+':
      print(f"the firstvalue is{ num_1} and second value is {num_2} its sum is {sum}")
elif opr=='-':
      difference=num_1-num_2
      print(f" the first value is{ num_1} and second value is {num_2} its difference is {difference}")
elif opr=='*':
      multiplication=num_1*num_2
      print(f"the first value is{ num_1} and second value is {num_2} its multiplication is {multiplication}")
elif opr=='/':
      division=num_1/num_2
else:
    print("given operator is invalid") 




#6.Short hand it:
# Rewrite the following code using the short-hand if statement.
num=int(input("enter the number"))
print(f"{num} is even") if num%2==0 else print(f"{num} is odd")




#7. Discount Calculator
orginal_amount=int(input("enter the amount"))
discount_percent=int(input("enter the discount percent"))
discount_amount=orginal_amount+(discount_percent/100)
after_discount=orginal_amount-discount_amount
print(f"the orginal price is {orginal_amount} its discount percentage is {discount_percent} then after discount price is")



#8. BMI Calculator
weight=float(input("enter the weight in kilograms"))
height=float(input("enter the height in meters"))
BMI=weight/(height**2)
print(f"the weight of a body is {weight} and height is {height} then body mass index of a body is {BMI}")