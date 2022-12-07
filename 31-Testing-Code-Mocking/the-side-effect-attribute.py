from unittest.mock import Mock
from random import randint


def generate_number():
    return randint(1, 10)  # [1; 10]


call_me_maybe = Mock(side_effect=generate_number)

print(call_me_maybe())
print(call_me_maybe())
print(call_me_maybe())

three_item_list = Mock()
three_item_list.pop.side_effect = [1, 2, 3, IndexError("No more items!")]

print(three_item_list.pop())
print(three_item_list.pop())
print(three_item_list.pop())
# print(three_item_list.pop()) # IndexError: No more items!

# mock = Mock(side_effect=NameError("NameError!"))
# print(mock())
