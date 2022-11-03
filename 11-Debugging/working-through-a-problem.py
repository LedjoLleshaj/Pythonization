#debug console is a console where i can run commands during the debugging
#this can be useful to check the value of the variables


values = [1,2,3,4,5]

# multiply the nummber with index -1

# 1 * 0-1  -1
# 2 * 1-1   0
# 3 * 2-1   3
# 4 * 3-1   8
# 5 * 4-1  15
#==============
#          25

def multiply_element_by_one_less_than_index(numbers):
    total = 0

    for index,el in enumerate(numbers):
        total += el * (index-1)

    return total

print(multiply_element_by_one_less_than_index(values))