# namedtuples are a quick way to create a class and instantiate it
# with a few attributes
import collections

Book = collections.namedtuple("Book", ["title", "author"]) # or i can use a string with spaces to divide the attributes

animal_farm = Book("Animal Farm", "George Orwell")

gatsby = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald")

print(animal_farm[0])
print(gatsby[1])
print(animal_farm.title)
print(gatsby.author)