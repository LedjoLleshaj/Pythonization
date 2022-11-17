disney_characters = {
    "Mickey Mouse",
    "Donald Duck",
    "Goofy"
}
disney_characters.add("Minnie Mouse")
# disney_characters.add(["Minnie Mouse"]) # TypeError: unhashable type: 'list'
print(disney_characters)

disney_update = {
    "Mickey Mouse",
    "Donald Duck",
    "Superman",
    "Batman"
}
disney_characters.update(disney_update)
print(disney_characters)

