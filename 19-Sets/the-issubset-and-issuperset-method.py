a = {1,2,4}
b = {1,2,3,4,5}
print(a.issubset(b)) # True because b contains all items in a
print(b.issuperset(a))

# we can also use the < and > operators 
# to check if a set is a subset or superset of another set
print( a < b ) # True
print( b > a ) # True

