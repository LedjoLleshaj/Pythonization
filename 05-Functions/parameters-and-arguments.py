def party(text):
    print("I was passed a", text)

party("string")
party(2)
party(2.5)
# party() # This will cause a TypeError

def sum(a, b):
    print(a + b)

sum(2, 3)
sum(2.5, 3.5)
sum("2", "3")
# sum(2) # This will cause a TypeError