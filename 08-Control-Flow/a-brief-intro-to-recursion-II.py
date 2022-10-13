def reverse_iterative(s):
    count = len(s)
    result = ""
    while count > 0:
        result += s[count-1]
        count -= 1
    return result

reversed = reverse_iterative("hello")
print(f"The reverse of 'hello' is {reversed}.") # olleh

def reverse_recursive(s):
    print(s)
    if len(s) == 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

reversed = reverse_recursive("hello")
print(f"The reverse of 'hello' is {reversed}.") # olleh

def factorial(val):
    if val == 1:
        return val
    else :
        return factorial(val-1) * val

print(factorial(5)) 