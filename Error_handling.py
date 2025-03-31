#1. VALUE ERROR.
#try: Entering alphabet values valuerror will occur
try:
    num_1 = int(input("enter the number1 :"))
    num_2 = int(input("enter the number2 :"))
except ValueError as e:
    print(f"valueerror :{e}")
else:
    print(num_1**num_2)

#2.TYPE ERROR
try:
    num = 10
    text = "Hello" 
    print(num+text)
except TypeError as e:
    print(f"typeerror :{e}")


#3. FILE NOT FOUND
try:
    file = open("numpy.py",mode='r') 
except FileNotFoundError as e:
    print("FileNotFoundError :{e}")


#4. Zero Division Error
try:
    num_1 = int(input("enter the number :"))
    num_2 = int(input("enter the number2 :"))
    print(num_1/num_2)
except ZeroDivisionError as e:
    print("ZeroDivisionError :{e}")


#5. Index Error
list = [99,88,77,66,55,44,33]
try:
    print(list[8]) 
except IndexError as e:
    print(f"IndexError :{e}")
else:
    print(list[6])


#6. Key Error
my_dict = {'name':'python', 'age':30, 'city':'Bhimavaram'}
try:
    print(my_dict.pop('id'))
except KeyError as e:
    print(f"KeyError :{e}")    


#7. AttributeError
try:
    class car:
        def __init__(self,brand):
            self.brand = brand
    my_car = car("Toyota")
    print(my_car.colour)
except AttributeError as e:
    print(f"AttributeError: {e}")


#8. Overflow Error
try:
    value = 2**1000000
    float_number = float(value)
except OverflowError as e:
    print(f"OverflowError: {e}")


#9. IO Error
try:
    file = open("python.py",'r')
except IOError as e:
    print(f"IOError: {e}")


#10. Run time Error
my_list = [10,20,30,40,50,60,70,80,90]
print(my_list)
try:
    print(my_list[9])
except:
    print("some error occured")
else:           #if try block executes then else block will also executes
    print(my_list[7])
finally:            #if try block executes or not, even though finally block executes
    print("Regardless execution") 



#11. Execption
try:
    num_1 = int(input("enter the number1 :"))
    num_2 = int(input("enter the number2 :"))
    print(num_1/num_2)
except Exception as e:
    print(f"Exception: {e}")      

      
      