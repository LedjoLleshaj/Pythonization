# count = 0

# while count < 5:
#     print(count)
#     count += 1
 
# print(count) # 5

# invalid_number = True

# while invalid_number:
#     number = input("Enter a number between 1 and 10: ")
#     if number.isdigit() and 1 <= int(number) <= 10:
#         invalid_number = False
#         print(f"Well done! Number {number} is great.")
#     else:
#         print("Invalid number.Try again!")

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    else:
        print(number)

number = input("Enter a number: ")
count = 1
while count <= int(number): 
    fizz_buzz(count)
    count += 1