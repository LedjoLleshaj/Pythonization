str = "Python"
print(str[-1]) # n
print(str[-2]) # o
print(str[-3]) # h
print(str[-4]) # t
print(str[-5]) # y
print(str[-6]) # P
# print(str[-7]) # IndexError: string index out of range
print(type(str[-1])) # <class 'str'>
str[-1] = "p" # TypeError: 'str' object does not support item assignment
