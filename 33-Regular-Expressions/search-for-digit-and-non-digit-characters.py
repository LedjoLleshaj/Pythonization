import re

# digits
pattern = re.compile(r"\d")  # \d means any digit [0-9]
print(
    pattern.findall("I went to him at 11 A.M. on 4th July 1886")
)  # ['1', '1', '4', '1', '8', '8', '6']

pattern = re.compile(r"\D")  # \D means any non-digit opposite of \d
print(
    pattern.findall("I went to him at 11 A.M. on 4th July 1886")
)  # ['I', ' ', 'w', 'e', 'n', 't', ' ', 't', 'o', ' ', 'h', 'i', 'm', ' ', 'a', 't', ' ', ' ', 'A', '.', 'M', '.', ' ', 'o', 'n', ' ', 't', 'h', ' ', 'J', 'u', 'l', 'y', ' ', ' ']


# word characters alphanumeric and underscore
pattern = re.compile(
    r"\w"
)  # \w means any word character [a-zA-Z0-9_] underscore is also included
print(
    pattern.findall("I went to him at 11 A.M. on 4th July 1886")
)  # ['I', 'w', 'e', 'n', 't', 't', 'o', 'h', 'i', 'm', 'a', 't', '1', '1', 'A', 'M', 'o', 'n', '4', 't', 'h', 'J', 'u', 'l', 'y', '1', '8', '8', '6']

pattern = re.compile(r"\W")  # \W means any non-word character opposite of \w
print(
    pattern.findall("I went to him at 11 A.M. on 4th July 1886")
)  # list of whitespaces and dots


# whitespace characters
pattern = re.compile(r"\s")  # \s means any whitespace character
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))

pattern = re.compile(r"\S")  # \S means any non-whitespace character
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))


# word boundaries
# \b means word boundary (start or end of word)

# to find all words starting with we
pattern = re.compile(r"\bwe")
print(pattern.findall("we are the world we are the children"))

# to find all words ending with nt
pattern = re.compile(r"nt\b")
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))


# meta characters. The Dot (.) Character
# . means any character except newline

pattern = re.compile(r"J..y")  # number of dots matters
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))
# sometimes we might want to match a dot character
# to match a dot character we need to escape it by using (r"\.")


# meta characters. The Square brackets [ ] Character
# [abc] means either a or b or c anywhere in the string
# order doesn't matter
pattern = re.compile(r"[abc]")
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))
# if we want to do the opposite of [abc] we can use [^abc]
# [^abc] means anything except a or b or c
pattern = re.compile(r"[^abc]")
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))


# Range of characters
pattern = re.compile(r"[a-l]")  # any character between a to l
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))

# Number of matches using curly brackets
# {x} means x number of occurrences
# {x,} means x or more occurrences
# {x,y} means x to y occurrences
pattern = re.compile(r"\d{2}")  # 2 digits
print(
    pattern.findall("I went to him at 11 A.M. on 4th July 1886")
)  # ['11', '18', '86']

pattern = re.compile(r"\d{3,}")  # 3+ digits
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))  # ['1886']


# Combining whitespaces and number of matches
pattern = re.compile(r"\s{3,}")  # 3+ whitespaces
print(pattern.findall("I went to him at 11 A.M.   on 4th July 1886"))

# Combining digits and number of matches
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")  # 3 digits - 3 digits - 4 digits
print(pattern.findall("My number is 123-456-7890 i repeat 123-456-7890"))

# Combining digits and number of matches
pattern = re.compile(r"\d{3}\s{1,}\d{3}\s{1,}\d{4}")
print(pattern.findall("My number is 123    456 7890 i repeat 123 456    7890"))

# alternative to one or more whitespaces is \s+
# however with the + we lose precision of the exact number
pattern = re.compile(r"\d{3}\s+\d{3}\s+\d{4}")
print(pattern.findall("My number is 123    456 7890 i repeat 123 456    7890"))


# Using OR logic in regular expressions
# we can use | to match either of the two expressions
pattern = re.compile(r"man|woman")
print(pattern.findall("I am a man"))

pattern = re.compile(r"\d{3,}(\s+|-)\d{3,}(\s+|-)\d{4}")
print(pattern.findall("My number is 123    456 7890 ,i repeat 123-456   7890"))
