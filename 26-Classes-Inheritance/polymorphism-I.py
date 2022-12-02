class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __len__(self):
        return self.height


values = [
    [1, 2, 3],
    (4, 5, 6, 7),
    {"a": 8, "b": 9, "c": 10},
    Person("John", 180),
]
for value in values:
    print(len(value))
