import re

pattern = re.compile(r"flower")

sentence = "There are a lot of flowers in the flower field"

matches = pattern.findall(sentence)
print(matches)

for match in pattern.finditer(sentence):
    print(match.span())
