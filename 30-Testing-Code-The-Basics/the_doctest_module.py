def sum_of_list(numbers):
    """Returns the sum of all the numbers in the list.

    >>> sum_of_list([1, 2, 3])
    6
    >>> sum_of_list([1.1, 2.2, 3.3])
    6.6
    >>> sum_of_list([1, 2, 3, 4])
    10
    """
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()
