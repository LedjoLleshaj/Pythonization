employee_salary = {
    'John': 50000,
    'Jane': 60000,
    'Jack': 65000
}
print(employee_salary) # {'John': 50000, 'Jane': 60000, 'Jack': 65000}
extra_salary = {
    'John': 60000,
    'Smith': 20000,
}
print(extra_salary) # {'John': 60000, 'Smith': 20000}
employee_salary.update(extra_salary) # update the dictionary
print(employee_salary) # {'John': 60000, 'Jane': 60000, 'Jack': 65000, 'Smith': 20000}