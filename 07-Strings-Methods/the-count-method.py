word = "quarantine"
print(word.count("q")) # 1 - the letter q appears once
print(word.count("a")) # 2 - the letter a appears twice

# The count method is case sensitive
print(word.count("Q")) # 0 - the letter Q does not appear
print(word.count("qu")) # 1 - the substring qu appears once

