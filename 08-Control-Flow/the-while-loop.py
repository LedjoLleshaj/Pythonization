# count = 0

# while count < 5:
#     print(count)
#     count += 1
 
# print(count) # 5


invalid_number = True

while invalid_number:
    number = input("Enter a number between 1 and 10: ")
    if number.isdigit() and 1 <= int(number) <= 10:
        invalid_number = False
        print(f"Well done! Number {number} is great.")
    else:
        print("Invalid number.Try again!")