bubble_tea_flavors = [
    ["Taro", "Strawberry", "Honeydew"],
    ["Mango", "Lychee", "Passion Fruit"],
    ["Coffee", "Thai Tea", "Matcha"]
]

#index access
print(bubble_tea_flavors[0][1])
print(bubble_tea_flavors[1][2])
print()

print(bubble_tea_flavors)
print()

#looping
for flavor in bubble_tea_flavors:
    print(flavor)

print()
#looping with index
for index, flavor in enumerate(bubble_tea_flavors):
    print(index, flavor)

print()
#looping with index and subindex
for index, flavor in enumerate(bubble_tea_flavors):
    for subindex, subflavor in enumerate(flavor):
        print(index, subindex, subflavor)

print()