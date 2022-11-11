a = 3
a = 10
a = "hello"
a = 3.14
# variables are just names for objects in memory
# when you assign a new value to a variable, the old value is lost
# and the variable is now pointing to a new object in memory
# the old object is no longer referenced by any variable
# and is eligible for garbage collection
# garbage collection is the process of reclaiming memory
# that is no longer referenced by any variable
# the garbage collector is run automatically by the Python interpreter
# when it detects that an object is no longer referenced by any variable
# the garbage collector will reclaim the memory used by that object
# and make it available for other objects to use


# however you can also force the garbage collector to run
# by importing the gc module and calling the gc.collect() function
# this is useful if you want to free up memory immediately
# and you know that you are done using an object
# but you don't want to wait for the garbage collector to run

a = [1, 2, 3]

a = [4,3,2,1]
 