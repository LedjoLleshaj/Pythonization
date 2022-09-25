print("This will \nbegin on a \nnew line")

print("This will \tput a tab \t\t\tbetween these words")

print("This will \\allow a backslash in the string")

print("This will \"allow quotes\" in the string")

print("This will \'allow single quotes\' in the string")

print("This will \blremove the character before it")

raw = r"This will not \nbegin on a \nnew line" # Raw string
print(raw)

print("This will not begin on a new line","This will not begin on a new line",\
    "But this print is in two lines", sep="--")
