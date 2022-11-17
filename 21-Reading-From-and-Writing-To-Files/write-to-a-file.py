file_name = "write-to-a-file.txt"
with open(file_name, "w") as file:
    file.write("Hello World!") # if the file does not exist, it will be created 
    file.write("You are awesome!") # but if it does exist, it will be overwritten

