# name, adjective, noun
mad_libs = "{} laughed at the {} {}."

print (mad_libs.format("Bob", "funny", "cat")) # Bob laughed at the funny cat.
print (mad_libs.format("Alice", "sad", "dog")) # Alice laughed at the sad dog.
# print (mad_libs.format("not","enough")) # Traceback (most recent call last):

mad_libs = "{0} laughed at the {1} {2}."
print (mad_libs.format("Bob", "funny", "cat")) # Bob laughed at the funny cat.

mad_libs = "{name} laughed at the {adjective} {noun}."
print (mad_libs.format(name="Bob", adjective="funny", noun="cat")) # Bob laughed at the funny cat.
print(mad_libs.format(noun="dog", name="Alice", adjective="sad")) # Alice laughed at the sad dog.
