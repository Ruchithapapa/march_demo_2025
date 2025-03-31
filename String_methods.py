#String: It is squence of characters.
# it is immutable data type. 
# it is represented text format to store the data.
# Creating strings
# the single quotes(') = 'Hello World"
# double quotes("") = "Python String" 
# triple quotes(''') = '''Triple quotes allow strings to span multiple lines'''

######INDEXING#######
#my_string = "python life"
###Positive index###
#print(my_string[0]) #p
#print(my_string[7]) #l
#print(my_string[10]) #e
######Negative index#####
#print(my_string[-1]) #e
#print(my_string[-7]) #o

#######Slicing####
#seq[s:s:s]
##P.I in forward direction
#print(my_string[1:6]) #python
#print(my_string[ : : ]) #python life
# N.I in forward direction
#my_string = "python life"
#print(my_string[-10:-5])  #ython 
# N.I in backward direction
#print(my_string[ : :-1]) #efil nothyp
#print(my_string[-1:-5:-1]) #efil


#####STRING METHODS####
#upper(): it's returns the original string with all alphabetic char converted to uppercase.
#my_string = "python life"
#uc = my_string.upper()
#print(uc)  #o/p: PYTHON LIFE

#sample = "welcome to PYTHON LIFE @8'O Clock"
#print(sample)
#uc = sample.upper()
#print(uc) #o/p: WELCOME TO PYTHON LIFE @8'O CLOCK

#lower():it's returns the lowercase alphabetic.
#sample = "welcome to PYTHON LIFE @8'O Clock"
#print(sample)
#uc = sample.lower()
#print(uc) #o/p: welcome to python life @8'o clock


#Strip(): remove spaces only at starting and ending
#print(len(my_string))
#print(my_str.strip()) #remove both side spaces.
#print(len(my_string.strip()))
#print(my_string.lstrip()) #remove left sides space
#print(len(my_string.lstrip()))
#print(my_str.rstrip()) #remove right side space
#print(len(my_str.rstrip()))


#Count(): returns no.of occurences of the specified sub-string.
#sentance = "This is a sample sentance"
#count_i = sentance.count('e')
#print(count_i) #O/p: 3


#split(): split the str list of sub str based on the specified separator.
#data = "pythonlife, kiran, 123456"
#data1 = data.split(',')
#print(data1) #o/p: ['pythonlife', ' kiran', ' 123456']

#Replace(): returns the str in old str to new str
#original_string = "python is fun!"
#modified_string = original_string.replace('fun', 'awesome')
#print(modified_string)       #o/p: python is awesome!

#Startswith() and endswith():
#----> returns the str strats with the specified prefix
#----> returns the str ends with the specified suffix
#filename = 'example txt'
#starts_with = filename.startswith("ex")
#ends_with = filename.endswith("txt")
#print(starts_with)
#print(ends_with)

#find() and indes():
#---> nees to pass char in arg. and result the index of the char.
#sentence = "This is a sentence"
#position_i = (sentence.find('i'))
#print(position_i) #o/p: 2 characters
#position_w = (sentence.find('w'))
#print(position_w) #here w is not present in entire str. so it result is -1

#----> need to pass char in arg. and result the index of the char
#sentence = "This is a sentence"
#position_a = (sentence.index('a'))
#print(position_a) #o/p: 8position
#position_w = (sentence.index('w'))
#print(position_w) #o/p: ere w is not present in entire str. so it reslt is error

#Capitalize(): first letter of the entire str will capitalize.
#text = "python life"
#capitalized_text = text.capitalize()
#print(capitalized_text) #o/p: Python life

#title(): first letter of the entire str eill capitalize.
#my_string = "welcome to pythonlife"
#print(my_string.title())  #o/p:Welcome To Pythonlife


#indigit():  it checks entire str is consist of only numbers, and it's print the boolen value
#if we have special char like @,%,+ print as false
#my_string = "12348679"
#print(my_string.isdigit()) #o/p: True
#my_string = "1234 8679"
#print(my_string.isdigit()) #o/p: false because it find the special char like space

#isalpha(): returns if all char in the str are alphabetic
#my_string = "pythonlife"
#print(my_string.isalpha()) #o/p: True


#join(): joins the sub str of the list into single str
#word_list = ['Hello', 'world']
#joined_string = ' '.join(word_list)
#print(joined_string) #o/p: Hello world






##########CODING EXERCISE###########
#1. You are given a string sentence. print the characters at even indices.
sentence = "python is amazing"
final_output =[]
for i in range(len(sentence)):
    if i%2 ==0:
        final_output.append(sentence[i])
print("".join(final_output))        #o/p: pto saaig

#2. You are given a string s. Check if the string contains only digits.
s = "12345"
print(s.isdigit())   #o/p: True



#3. You are given a string s. Print the string in reverse order.
s = "python is amazing"
print(s[-1:-18:-1])   #o/p: gnizama si nohtyp


#4. You are given a string s. Capitalize the first letter of each word in the string
#and print thr modified string.
s="python programming is fun"
print(s.title())   #o/p: Python Programming Is Fun
