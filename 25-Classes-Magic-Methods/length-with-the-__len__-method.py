import collections

Book = collections.namedtuple('Book', 'title author pages')
animal_farm = Book('Animal Farm', 'George Orwell', 112)
gatsby = Book('The Great Gatsby', 'F. Scott Fitzgerald', 180)
print(len(animal_farm)) # 3 - the number of fields in the namedtuple

class Library():
    def __init__(self, *books):
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library(animal_farm,gatsby)
print(len(l1)) # 2 - the number of books in the library
l2 = Library(animal_farm)
print(len(l2)) # 1 - the number of books in the library

    
