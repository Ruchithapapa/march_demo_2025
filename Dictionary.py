#1. Write python code to add a new key-value pair to the following dictionary.
my_dict = {'name' : 'python', 'age' : 25}
print(my_dict)


#2. Write python code to access and print the value associated with the key 'price' in
#the following dictionay.
product_info = {'name':'laptop', 'brand':'bell', 'price':1200}
print(product_info['price'])


#3. Write python code to print all keys present in the following dictionary.
my_dict = {'name':'python', 'age':25, 'city':'Rajahmundry'}
print(my_dict.keys())

#4. Write python code to remove the keys-value pair with the 'city' from the following
#dictionary.
my_dict = {'name':'python', 'age':30, 'city':'Bhimavaram'}
print(my_dict.pop('city'))
print(my_dict)



#5. Write python code to print all the values present in the following dictionary.
my_dict={'name':'python', 'age':25, 'city':'tanuku'}
print(my_dict.values())



#Write a python script that updates a dictionary with a new key-value pair.
dict_1={'name':'raj', 'age':27, 'village':'kamareddy'}
dict_1.update({'pin no':503111})
print(dict_1)


#Write a python script that accesses and prints the value associated with a specific key
#in a dictionary.
dict1={'name':'raj', 'age':27, 'village':'kamareddy', 'wife':'ruchitha'}
print(dict1.get('wife'))


#Write a pyhton script that removes a key-value pair from the dictionary.
dict1={'name':'raj', 'age':27, 'village':'kamareddy', 'wife':'ruchitha'}
print(dict1.pop('age'))
print(dict1)


#Write a python script that prints all the keys present in a dictionary.
dict1={'name':'raj', 'age':27, 'village':'kamareddy', 'wife':'ruchitha', 'state':'Telangana'}
print(dict1.keys())



#Write a python script that prints all the values present in a dictionary.
dict1={'name':'raj', 'age':27, 'village':'kamareddy', 'wife':'ruchitha', 'state':'Telangana'}
print(dict1.values())
