#1. Write pyhton code to find and print the intersection of the following two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)


#2. Write python code to find and print the union of the following two sets.
set1={1, 2, 3, 4, 5}
set2={4, 5, 6, 7, 8}
set3=set1.union(set2)
print(set3)


#3. Write python code to find and print the elements present in set1 but not in set2.
set1={1, 2, 3, 4, 5}
set2={4, 5, 6, 7, 8}
set3=set1.difference(set2)
print(set3)


#4. Write python code to find and print the symmetric diference of the following two sets.
set1={1, 2, 3, 4, 5}
set2={4, 5, 6, 7, 8}
set3=set1.symmetric_difference(set2)
print(set3)


#5. Write python code to check if the element 3 is present in the set my_set
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)


#Write a python script that finds and prints the intersection of two sets.
set1={1, 3, 5, 7, 9}
set2={5, 9, 2, 4, 6}
set3=set1.intersection(set2)
print(set3)


#Write a python script that finds and prints the union of two sets.
set1={1, 3, 5, 7, 9}
set2={5, 9, 2, 4, 6}
set3=set1.union(set2)
print(set3)


#Write a python script that finds and prints the difference between two sets.
set1={1, 3, 5, 7, 9}
set2={5, 9, 2, 4, 6}
set3=set1.difference(set2)
print(set3)


#Write a python script that finds and prints the symmetric difference between two sets.
set1={1, 3, 5, 7, 9}
set2={5, 9, 2, 4, 6}
set3=set1.symmetric_difference(set2)
print(set3)