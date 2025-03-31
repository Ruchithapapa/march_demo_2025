##############OBJECT_ORIENTED PROGRAMMING#####
#----> oop's is based on the concept of "objects."
#----> The object contains both data and code.
#Type of OOP's
#1. Class
#2. Object
#3. Inheritance
#4. polymorphism
#5. Encapsulation
#6. Abstraction
####OOP's Terminology###
#1. Attribute also known as data member or variables.
#2. Behaviour also known as member function or method.

############# Class ###############
#---> Class is defined with keyword class
#---> It is a user_defined data structure that binds members and methods into a single unit.
#---> Class is a blueprint or code template for object creation.
#Examples: Mercedes, BMW, Toyota etc.
#syntax: class classname()
class details():
    user_name="raj"
    id=1234
    def user_info(self):
        print(f"this is basic info funactionality")

########### Object #############
#---> An object is simpy a collection of data(variables) and methods(functions).
#---> The object is the instance of class. The process of creating an object can be called instantiation.
#---> There is no memory allocation until we create its object. 
#---> The objector instance contains real data or information.
# Example: chair, bike, marker, pen, table, car etc.
# Syntax: objname = classname()
obj=details()
print(obj.user_name)
print(obj.id)
obj.user_info()


########### class and object ############
class mobile_phone:
    brand_name = "samsung"
    color = "white"
    storage = "120gb"
    def calling(self,mobile_name):
        print("making a phone call.....!",mobile_name)
    def browsing(self,mobile_name):
        print("you are browsing....",mobile_name)
    def gaming(self,mobile_name):
        print("you are playing games",mobile_name)

samsung = mobile_phone()
samsung.calling("samsung")
samsung.browsing("samsung")
samsung.gaming("samsung")


###########  ___init____ ############
#---> __init__ method in oops is nothing but a special fumction.
#---> special function are the function that are used to enrich the class.
#---> these can be easily identified as they double underscores on either side.
#---> __inti_- method is used to constructor in other programming languages.
# Syntax: __init__(self,attribute1,attributes2,.....attributesn)
#self.attr1 = attr1
#self.attr2 = attr2
#.
#.
#.
#self,attrn = attrn

#---> Inheritance allows us to define a class that inherits all the methods and properties from another class
#--> parent class is the class being inherited from, also called base class.
#--> child class is th class that inherits from another class, also called derived class.

#1. Single inheritance
#2. Multilevel inheritance
#3. Hierarchical inheritance
#4. Multiple inheritance

class mobile_phone():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def make_call(self,number):
        print(f"calling{number} from {self.brand} and {self.model}")
    def send_message(self,number,message):
        print(f"sending{message} to {number} from {self.brand} and {self.model}")
obj = mobile_phone("apple", "apple15s") 
obj.make_call(12345)
obj.send_message("24689","hello everyone")


###### 1. Single Inheritance ######
#upgrading with smart phone
class mobile_phone():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def make_call(self,number):
        print(f"calling {number} from {self.brand} and {self.model}")
    def send_message(self,number,message):
        print(f" sending {message} to {number} {self.brand} {self.model}")
class smart_phone(mobile_phone):
    def browsing(self):
        print(f"browsing internet on {self.brand} {self.model}")
    def app (self,appname):
        print(f"using {appname} app on {self.brand} {self.model}") 
apple = smart_phone("apple","iphone15")
apple.make_call(123456)
apple.send_message(123456,"hello")
apple.browsing()
apple.app("instagram")


########## 2. Multilevel Inheritance #########
class grandfather():
    def output(self):
        print('this is gf class')
class father(grandfather):
    def outputf(self):
        print('this is father class')
class child(father):
    def outputc(self):
        print('this is child class')
obj = child()
obj.output()
obj.outputf()
obj.outputc()


######### 3. Hierarchical Inheritance #########
class a():
    def output(self):
        print('this is parent class')
class b(a):
    def output1(self):
        print('this is child1 class')
class c(a):
    def output2(self):
        print('this is child2 class')
obj = b()
obj.output()
obj.output1()
obj = c()
obj.output()
obj.output2()   


########## 4. Multiple Inheritance ##########
class parent1():
    def father(self):
        print("this is father class")
class parent2():
    def mother(self):
        print("this is mother class")
class child(parent1,parent2):
    def child(self):
        print("this is child class")
obj=child() 
obj.father()
obj.mother()          





############# Polymorphism ############
#---> implementing something in diff.forms.
#---> th literal meaing of polymorphism is the condition of occurence in different forms.
#--> TWO TYPES
#---> 1. Overloading.   * method overloading   * operator overloading
#---> 2. Method overriding.

# Operator OL:
#1+2=3 added
#"hi"+"world"="hi world"

#Method OL:
#--> method name shold be some arguments must be different, in the terms of length ot type of argument.
#class calculator():
#    def add(self,a,b)
#        print(a,b)
#obj=calculator()
#obj.add(10,10)

#----> This method not overloading in this code, So using default parameters to achieve.
class calculator():
    def add(self,a=None, b=None):
        print(a,b)
    def add(self,a=None, b=None, c=None):
        print(a,b,c)
obj=calculator()
obj.add(10,10,10)
obj.add(10,10)

# Method overriding:
#---> method name should be same, arguments should be also same.
class father():
    def details(self,a):
        print("this is base class",a)
class child(father):
    def details(self, a):
        print("this is child class",a)
        super().details("200cr")  # super(): to access the parent(base) function
obj=child()
obj.details("100cr")  


############# ENCAPSULATION #############
#---> maechanism of wrapping the data and code acting on the data(method) together as a single unit.
#Type if access modifiers:
# Public: access to outside world.
# protected: access to derived class(inherit class only)
# Private: not accessible to outside.
#--> if you want to give any protection, mostly keep private data or protected in base class.


### PUBILC
class gfather():
    def __init__(self,a):
        self.a = a
        print(a)
    def sample(self):
        print(self.a)
class father(gfather):
    def display(self):
        print(self,a)
obj=father("100cr")
obj.display()
obj.sample()   

### PROTECTED: symbol'_'
class gfather():
    def __init__(self,a):
        self._a = a
        print(a)
    def sample(self):
        print(self._a)
class father(gfather):
    def display(self):
        print(self._a)
obj=father("200cr")
obj.display()
obj.sample()

### PRIVATE: symbol "__"
#class gfther():
#   def __init__(self,a):
#       self.__a = a
#        print(a)
#    def sample(self):
#        print(self.__a)
#class father(gfather):
#    def display(self):
#        print(self.__a)
#obj = father("150cr")
#obj.display()
#obj.sample()



############## 6. Data abstraction ###########
#---> Hiding the implementation and hiding the code(unnecessary part) and showing the essential part
# 1. abstract class: class which contains abstract methods.
# 2. abstract method.
# 3. concrete class.

#abstract method: the method which is having only declaration but not the definition/implementation/declaration(hiding)
# object cannot create here.

# Concrete class: class which does not have abstract method.
# object can create only to concrete class only
# to create abstract classes, you can use the abc module(abstract base class)

from abc import ABC, abstractmethod
class abstract_demo(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def display2(self):
        pass
class demo(abstract_demo):
    def display(self):
        print("implementing in derived class")
    def display2(self):
        print("implementing in derived class display2")
obj=demo()
obj.display()
obj.display2()                



    

                





        