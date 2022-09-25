alphabet= "abcdefghijklmnopqrstuvwxyz"
print(alphabet[::2]) # acegikmoqsuwy prints every second letter
print(alphabet[1::2]) # bdfhjlnprtvxz prints every second letter starting at index 1
print(alphabet[::3]) # adgjmpsvy prints every third letter
print(alphabet[::4]) # aeimquy prints every fourth letter
print(alphabet[::-2]) # zyxvtrpnjlhfdb prints every second letter in reverse order
print(alphabet[::-1]) # zyxwvutsrqponmlkjihgfedcba prints the alphabet in reverse order

def first_three_characters(str):
    return str[:3]

def last_five_characters(str):
    return str[-5:]

def is_palindrome(str):
    return str == str[::-1]