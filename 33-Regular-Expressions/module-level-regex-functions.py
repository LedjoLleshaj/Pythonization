import re

print(re.search(r"aza", "plaza"))  # <re.Match object; span=(2, 5), match='aza'>

print(re.match(r"aza", "aza"))  # <re.Match object; span=(0, 3), match='aza'>

print(re.findall(r"aza", "plaza"))  # ['aza']

for match in re.finditer(r"aza", "plaza"):
    print(match)  # <re.Match object; span=(2, 5), match='aza'>
