import random

print(random.choice(["Me", "Myself", "I"]))
print(random.choice("Python"))

lottery_numbers = [random.randint(1, 50) for i in range(50)]
print(lottery_numbers)

print(random.sample(lottery_numbers, 1))
print(random.sample(lottery_numbers, 5))
