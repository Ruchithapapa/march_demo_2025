#The process is a program (set of instructions) in execution
#process cannot share the memory
#A process is an independent program that runs in its own mwmory space.
#It has its own memory, variables, and resource.
# One process cannot directly access data of another process


#Thread:
#Thread is light-weight processes
#Thread can be used to perform complicates tasks in the background without interrupting the main program
#thread can share the memory


# run(): is the entry point for a thread.
# start(): method starts a thread by calling the run method.
# join([time]): waits threads to terminate.
#isAline(): method checks whether a thread is still executing.
#getName(): method returns the name of a thread.



#import time
#def square(numbers):
#    print("squares")
#    for i in numbers:
#        time.sleep(0.2)
#        print(i*i)


#list_1 = [1, 2, 3, 4, 5]
#time_1 = time.time()
#square(list_1)
#print(time.time()-time_1)
#def cube(numbers):
#    print("cubes")
#    for i in numbers:
#        print(i*i*i)
#time_1 = time.time()
#print(time_1)
#square(list_1)
#cube(list_1)
#print(time.time()-time_1)        


import time
def square(numbers):
    print("squares")
    for i in numbers:
        time.sleep(0.2)
        print(i*i)
def cube(numbers):
    print("cubes")
    for i in numbers:
        time.sleep(0.2)
        print(i*i*i)
time_1 = time.time()
print(time_1)
list_1 = [1, 2, 3, 4, 5]
square(list_1)
cube(list_1)
print(time.time()-time_1)


import threading
import time
def square(numbers):
    print("squares")
    for i in numbers:
        time.sleep(0.2)
        print(f"square{i*i}")
def cube(numbers):
    print("cubes")
    for i in numbers:
        time.sleep(0.2)
        print(f" cubes {i*i*i}")
it = time.time()
list_1 = [1,2,3,4,5]
t1 = threading.Thread(target=square,args=(list_1,))
t2 = threading.Thread(target=cube,args=(list_1))
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time()-it)