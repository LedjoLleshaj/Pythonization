class Book():
    def __init__(self, title, author ,price = 14.99): # pricehas now a default value if its not spicified on book instanciation
        self.title = title
        self.author = author
        self.price = price

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", 19.99)

atlas = Book(author = "Ayn Rand", title = "Atlas Shrugged") # we can also specify the attributes in any order