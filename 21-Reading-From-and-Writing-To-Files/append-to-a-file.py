#keep what is already in the file and add to it

with open("My_appended_file.txt", "a") as file:
    file.write("Hello World!") # if the file does not exist, it will be created 
    file.write("You are awesome!") # but if it does exist, it will be appended to
