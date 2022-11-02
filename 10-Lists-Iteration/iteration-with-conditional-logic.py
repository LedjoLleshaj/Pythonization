values = [3,6,9,12,15,18,21,24]
other_values = [5,10,15,20,25,30]

def odds_sum(values):
    total = 0

    for value in values:
        if value % 2 == 1:
            total = total + value

    return total

print(odds_sum(values))
print(odds_sum(other_values))

def greatest_number(values):
    greatest = 0

    for value in values:
        if value > greatest:
            greatest = value

    return greatest

print(greatest_number(values))
print(greatest_number(other_values))
