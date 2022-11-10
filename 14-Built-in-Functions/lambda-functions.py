metals = ["Gold", "Silver", "Platinum", "Palladium"]

# Using lambda function
#               
print(filter (lambda metal: len(metal) > 5, metals)) 
# lambda function is used to filter the list of metals
# which have length greater than 5
# they are consturcted using the lambda keyword
# lambda arguments: expression
# lambda function can take any number of arguments but only one expression
# the expression is evaluated and returned
# lambda functions can be used wherever function objects are required
# they are syntactically restricted to a single expression
# unlike normal functions, they can be used as an expression

print(map(lambda word: word.count("l"), metals))
# lambda function is used to map the list of metals
# and count the number of "l" in each word
print(map(lambda val: val.replace('s', '$'), metals))
