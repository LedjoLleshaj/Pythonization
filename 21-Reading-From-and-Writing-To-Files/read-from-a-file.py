# file = open('cupcakes.txt','r') # open the file in read mode (default)

# file.close() # close the file
#this is not the best way to open and close a file.
# best practice is to use the with statement

with open('cupcakes.txt','r') as file: # noow we don't need to close the file
    print("File opened")
    content = file.read()
    print(content)
print("File closed") # with statement closes the file automatically after the block

filename = input("Write the file name: ")
with open(filename,'r') as file:
    print("File opened")
    content = file.read()
    print(content)
print("File closed")

