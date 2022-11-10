animals = ["cat", "dog", "fish", "bird"]

long_words = [animal for animal in animals if len(animal) > 3]
print(long_words)
long_words = list(filter(is_long_animal, animals))
print(long_words)

def is_long_animal(animal):
    return len(animal) > 3
