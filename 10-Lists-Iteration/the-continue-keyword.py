#continue makes the loop skip the rest of the code and go back to the top
#of the loop and continue with the next iteration

def sum_of_positive_numbers(values):
    total = 0
    for value in values:
        if value <= 0:
            continue
        total += value
    return total