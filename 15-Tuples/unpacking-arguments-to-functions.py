def accept_stuff(*args):
    print(args)
    print(type(args))

# by using the asterisk, we can pass in any number of arguments
accept_stuff(1)
accept_stuff(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
accept_stuff(1, 2, 3)

def my_max(*nums):
    # greatest = nums[0]
    # for num in nums:
    #     if num > greatest:
    #         greatest = num
    # return greatest
    # or
    return max(nums)

print(my_max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(my_max(1, 2, 3))


def product(a, b):
    return a * b

print(product(2, 3))
#print(product(2, 3, 4)) # TypeError: product() takes 2 positional arguments but 3 were given
numbers = [3, 3]
print(product(*numbers))

numbers = (3, 4)
print(product(*numbers))

