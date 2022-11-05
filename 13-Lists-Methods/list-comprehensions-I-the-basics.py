numbers = [3, 4, 5, 6, 7]

# old way vs using list comprehension
# old way

squares = []
for num in numbers:
    squares.append(num ** 2)

print(squares)

# list comprehension
squares = [num ** 2 for num in numbers]
print(squares)

# list comprehension is more readable and less code and it is formed
# by using the square brackets and the for loop inside the brackets 
# and then the expression that you want to apply to each element in the list

rivers = ['nile', 'amazon', 'mississippi', 'yangtze', 'ganges']
print([len(river) for river in rivers])

expressions = ["lol", "rofl", "lmao"]
print([expression.upper() for expression in expressions])
print([len(exp) for exp in expressions])