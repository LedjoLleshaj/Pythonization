numbers = [ 4 ,7,2,0,9]
print ( sorted (numbers))
print ( sorted (numbers, reverse = True )) 
# sorted() returns a new list, leaving the original list unchanged
#if we actually want to sort the list, we can use the sort() method
numbers.sort()
print (numbers)

# we want to print a dictionary in a sorted order based on the key or value 
# we can use the sorted() function to do this

wheel_count = { "car": 4 , "motorcycle": 2 , "truck": 6 , "van": 4 }
print ( sorted (wheel_count))
print ( sorted (wheel_count, reverse = True ))
print ( sorted (wheel_count.items()))
print ( sorted (wheel_count.items(), reverse = True ))
