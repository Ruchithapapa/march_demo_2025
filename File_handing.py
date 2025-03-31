#Modes= 'r', 'w', 'a', 'r+', 'w+', 'a+'.
#using 'r' mode
file = open("basics.txt",mode='r')
read_data = file.read()
print(read_data)
file.close()


#using 'w' mode
file = open("new.txt",mode='w')
write_data = file.write("This is new file\nUsing 'w' mode to write the data in to the new.txt")
file.close()


#using 'a' mode
file = open ("new.txt",mode='a')
write_data=file.write("using append mode'a'\nadds the new data")
file.close()


#using 'r+' mode
file = open("basics.txt",mode = 'r+')
read_data = file.read()
write_data = file.write("using 'r+' mode")
print(read_data)
file.close()



#using 'w+' mode
file = open("new1.txt",mode='w+')
write_data = file.write("using 'w+' mode\nhere read, write, creating a new file and truncate all will possible")
file.seek(0)
read_data = file.read()
print(read_data)
file.close()


#using 'a+' mode
file = open("new2.txt",mode='a+')
write_data = file.write("\nHello everyone")
file.seek(0)
read_data=file_read()
print(read_data)
file.close()