animals = ["cat", "dog", "fish", "bird"]


#for fiter function to work, it needs a function and a list
#filter function will return a list of elements that have verify the condition
#in this case, it will return a list of animals that are longer than 3 characters

long_words = [animal for animal in animals if len(animal) > 3]
print(long_words)
long_words = list(filter(is_long_animal, animals))
print(long_words)

def is_long_animal(animal):
    return len(animal) > 3
