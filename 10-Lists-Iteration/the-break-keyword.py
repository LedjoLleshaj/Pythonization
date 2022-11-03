print(3 in [1, 2, 3, 4, 5]) # True

#break keyword is used to break out of a loop
#can be used for efficiency if you know you don't need to continue
#the loop

def contains(values, target):
    found = False

    for value in values:
        if value == target:
            found = True
            break # we dont need to continue the loop becuase we found the target
        
    return found