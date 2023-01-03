import re

pattern = re.compile(r"flower")

# match will match only the beginning of the string
match = print(pattern.match("flower is my favorite"))

if match:
    print(match.group())
    print(match.start())
    print(match.span())
