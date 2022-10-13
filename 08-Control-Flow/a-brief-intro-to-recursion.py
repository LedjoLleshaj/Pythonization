def count_down_from_iterative(number):
    while number > 0:
        print(number)
        number -= 1
    print("Blastoff!")

def count_down_from(num):
    if num == 0:
        print("Blastoff!")
    else:
        print(num)
        count_down_from(num - 1)

count_down_from_iterative(5)
count_down_from(5) 
