# an object is iterable if it can be used in a for loop
# the for loop will iterate over the elements of the object (one at a time)
# until it reaches the end of the object

dinner = "Steak and Potatoes"

for letter in dinner:
    print(letter)

ingredients = ["Steak", "Potatoes", "Asparagus", "Broccoli", "Carrots"]

for ingredient in ingredients:
    print(ingredient)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0

for number in numbers:
    total = total + number

print(total)

