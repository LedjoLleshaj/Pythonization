import random

characters = [
    "Warrior",
    "Mage",
    "Rogue",
    "Priest",
    "Paladin",
    "Shaman",
    "Druid",
    "Hunter",
    "Warlock",
]
print(characters)
random.shuffle(characters)
print(characters)

clone = characters[:]
print(clone)
random.shuffle(clone)
print(clone)
