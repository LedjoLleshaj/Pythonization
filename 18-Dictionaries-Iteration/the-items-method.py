# the order of the items is not guaranteed

college_courses = {
    "Math": "Godel",
    "Physics": "Einstein",
    "Chemistry": "Curie"
}

for course,professor in college_courses.items():
    print(f"{course}: {professor}.")

# it is preferable to use the items() method to iterate over a dictionary
# the items() method returns a list of tuples
# each tuple contains a key and a value that can be used to access the dictionary

# when we don't need the key or the value 
# # we can use the _ (underscore) as a placeholder for the variable name
# 
for _,professor in college_courses.items():
    print(f"{professor} teaches a course.")