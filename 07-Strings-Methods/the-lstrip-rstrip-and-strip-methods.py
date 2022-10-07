empty_space = "     Hello World     "
print(empty_space)
print(empty_space.lstrip()) #removes all leading whitespace
print(empty_space.rstrip()) #removes all trailing whitespace
print(empty_space.strip()) #removes all leading and trailing whitespace
 
link = "https://www.google.com"
print(link.lstrip("https://")) #removes all leading characters
print(link.rstrip(".com")) #removes all trailing characters
print(link.strip("https://.com")) #removes all leading and trailing characters
