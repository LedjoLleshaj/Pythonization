number = 0.123456789

print(format(number, "f")) # 0.123457 - default is 6 decimal places
print(format(number, ".2f")) # 0.12 - 2 decimal places

print(f"{number:.2f}") # 0.12
print(f"{number:.3f}") # 0.123

print(format(number, "%")) # 12.35% 
print(format(number, ".2%")) # 12.35% - 2 decimal places

