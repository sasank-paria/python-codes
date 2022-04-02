import os
# add new line or paragraph
file1 = open("C:\\Users\SHASHANK\Documents\python notes harry\9. Chapter 9\poems.txt","a")
file1.write("\n up above the sky ")
file1.close()
# "w" is a overwrite which formats the entire file

# print the content of the file
file1 =open("C:\\Users\SHASHANK\Documents\python notes harry\9. Chapter 9\poems.txt")
print(file1.read())
file1.close()

#create a new file

file2=open("newfile.txt","a")
file2.write("its a new file created !")
file2.close()

# delete of  existing file
os.remove("newfile.txt")

if os.path.exists("newfile.txt"):
                               os.remove("newfile.txt")
else:
     print("file doesnt exist")

# also we can delete empty folders

