#function that has two parameters and returns the first parameter repeated the number of times of the second parameter
def word_multiplier(word: str, times: int) -> str:
    return word * times

print(word_multiplier("Hello", 5))
print(word_multiplier("Hello", "5")) # TypeError: can't multiply sequence by non-int of type 'str'