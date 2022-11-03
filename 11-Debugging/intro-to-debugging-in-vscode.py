#debuggin is the process of finding and fixing errors in a program
#while debugging, you can see the value of variables at any point in the program
#you can also see the value of variables at any point in the program
#this way you can see if the value of a variable is what you expect it to be

#to debug a program, you need to set breakpoints
#breakpoints are places in the program where you want to pause the program
#and inspect the values of variables

#to set a breakpoint, click on the left side of the line number
#to remove a breakpoint, click on the red dot next to the line number

#step over moves to the next line inside the scope
#it will not go deeper inside functions
#unless we have a breakpoint inside that function

#step into enters inside the function
#while step out will finish the fucntion and step out


print ("Hello World")

def do_fun_stuff():
    
    a =20
    print ("I am doing fun stuff")
    a = 25

    return a

final = do_fun_stuff()
print (final)
