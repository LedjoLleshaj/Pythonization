#in keyword is used to check if a value is in a list
#not in keyword is used to check if a value is not in a list
#both return a boolean value
#both can be used with any data type

print("fast" in "breakfast")
print("fast" in "lunch")

meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)
print("dinner" in meals)
print("snack" in meals)

print()

test_score = [99.0 , 88.0 , 77.0 , 66.0 , 55.0]

print(99.0 in test_score) #True
print(99 in test_score) #true because 99 is the same as 99.

print()

print(99.0 not in test_score) #False

if 99.0 in test_score:
    print("The student passed the test.")

