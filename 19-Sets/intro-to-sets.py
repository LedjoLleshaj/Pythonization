# a set is an unordered collection of UNIQUE immutable elements
# we can construct them by using the set() function
x = set()
print(x)
# a set can be also created by using curly braces {}
y = {1, 2, 3, 4, 5, 5, 3, 2, 1}
print(y)
print(type(y))
print(type(x))
lottery_numbers = { (1,2,3), (4,5), (2,3,4,5) }

print(type(lottery_numbers))

#test = {[1,2], [3,4], [5,6]} # this will not work because lists are mutable and cannot be used in sets

for num in y:
    print(num)

for lottery in lottery_numbers:
    for num in lottery:
        print(num)

# set comprehension is also possible however in this case we actualy lose some of the values since they have the squares equal
squares = { number **2 for number in [-5 ,-4, -3, -2, -1, 0, 1, 2, 3, 4, 5] }
print(squares)

