# Practice using abstraction by writing a program and sharing the file.
from abc import ABC,abstractmethod
class science(ABC):
    @abstractmethod
    def subject(self,subject):
        print(f"What is the meaning of physics:{subject} ")
class science2(science):
    def subject(self,subject):
        print(f"What is the meaning of biology:{subject} ")
class science3(science):
    def subject(self,subject):
        print(f"What is the meaning of chemistry:{subject} ") 
obj1 = science2()
obj1.subject(10)
obj2 = science3()
obj2.subject(10)
              


        
