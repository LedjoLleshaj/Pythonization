import re  # imports the regular expression module

pattern = re.compile(r"flower")  # creates a regex object
print(type(pattern))

print(pattern.search("I like flowers"))  # searches for the pattern in the string
print(pattern.search("I like candy"))


match = pattern.search("flower is my favorite")
print(type(match))

if match:
    print(match.group())  # returns the string that matched the pattern
    print(match.start())  # returns the index of the start of the match
    print(match.span())  # returns the index of the end of the match
