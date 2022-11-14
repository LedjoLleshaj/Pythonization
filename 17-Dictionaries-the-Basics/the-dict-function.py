print(list("abc")) # ['a', 'b', 'c']
print(dict()) # {} because dicts() function returns an empty dictionary
# important that lists are with only two elements
#that will serve as key and value for the dictionary
employee_title = [
    ["John", "Manager"],
    ["Jane", "CEO"],
    ["Jack", "CTO"],
    ["Jill", "CFO"]
]

print(dict(employee_title))