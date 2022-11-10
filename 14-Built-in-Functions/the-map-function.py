numbers = [1, 2, 3, 4, 5]
cubes = [number **3 for number in numbers]
print(cubes)
def cube(number):
    return number ** 3
cubes = list(map(cube, numbers))
print(cubes)
animals = ["cat", "dog", "fish", "bird"]
animals_upper = list(map(str.upper, animals))
print(animals_upper)
