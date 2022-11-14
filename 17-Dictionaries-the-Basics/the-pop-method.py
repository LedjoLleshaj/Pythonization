years = [1991,2000,2007]
print(years.pop()) # 2007
print (years) # [1991,2000] wihtout 2007 since it was popped


release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007,
    "Rust": 2010
}
java_release = release_dates.pop("Java") # 1995
print(release_dates) # {'Python': 1991, 'Ruby': 1995, 'Go': 2007, 'Rust': 2010} without Java since it was popped

# second argument to pop() method is the default value to return if the key is not found
c_release = release_dates.pop("C", "Not Found") # "Not Found"


del release_dates["Python"] # deletes the key "Python" from the dictionary
print(release_dates) # {'Ruby': 1995, 'Go': 2007, 'Rust': 2010}
#del vs pop()
#del is a keyword and pop() is a method
#del is faster than pop() since it doesn't return the value
#del can be used to delete variables, lists, dictionaries, etc.
