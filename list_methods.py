#Reverse list:
#Write python code to reverse the code of elements in the given list my_list.
#print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
print(my_list[-1:-7:-1])



#Common elements:
#Given two lists list1 and list2, find and print the common elements between them.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [x for x in list1 if x in list2]
print(common)



#Unique elements.
#Create a new list unique_list containing only the unique elements from the given list 
#original_list. Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list=[]
for val in original_list:
    if val not in unique_list:
        unique_list.append(val)
print(unique_list) 




#Remove Duplicates:
#Remove duplicate elements from the given list duplicate_list and print the list without 
#duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
dup_remove_list=[]
for x in duplicated_list:
    if x not in dup_remove_list:
        dup_remove_list.append(x)
print(dup_remove_list)          



#list concatenation
names=["raj", "sahasya", "sadhvin", "vinya"]
id=[2, 3, 5, 8]
concat=names+id
print(concat)


#List repetition.
emp_names=["vasu", "laxmi", "padma", "bhagya"]
repetition=emp_names*3
print(repetition)



#List Removal
list=[1, 2, 5, 6, 8, 9]
even_index_remove=[]
i=0
for i in range(1,len(list)):
    if i%2 !=0:
       even_index_remove.append(list[i])
print(even_index_remove)     



#list insertion
fruits_price=[23,60,82,76]
fruits_price.insert(0,10)
fruits_price.insert(1,11)
fruits_price.insert(2,12)
print(fruits_price)



#Square Numbers.
#Create a list of squares of numbers from 1 to 10.
print([i*i for i in range(1,11) ])



#Even Numbers.
#Generate a list of even numbers from 1 to 20.
print([i for i in range(1,21) if i%2==0])


#words Lengths.
#given a list of words, create a list containing the lengths of each words.
words=["apple", "banana", "cherry", "date"]
len_words=[]
for i in words:
    len_words.append(len(i))
print(f"the words length of each element in words list is{len_words}")    
