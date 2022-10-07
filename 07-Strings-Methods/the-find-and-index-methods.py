browser = "Mozilla Firefox"
print(browser.find("Firefox"))
print(browser.find("r")) # returns the first occurence
print(browser.find("y")) # -1 if not found

print(browser.index("y")) # ValueError if not found

print(browser.find("Firefox", 0)) # start at index 0
print(browser.find("Firefox", 1)) # start at index 1

