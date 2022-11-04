action_start = ["Norris", "Chuck", "Bruce", "Arnold", "Steven"]

# The pop() method removes the last item in a list when no index is specified.
# The pop() method returns the removed item.
# The pop() method has one parameter:
# 1. index - the index of the element to be removed. If the index is not specified, the last item will be removed.
# If the index is greater than the length of the list, an IndexError will be raised.
# If the index is a negative number, the last item will be removed.

action_start.pop()
print(action_start) # ['Norris', 'Chuck', 'Bruce', 'Arnold']

print(action_start.pop(1)) # Chuck
print(action_start) # ['Norris', 'Bruce', 'Arnold']

action_start.pop(-1)
print(action_start) # ['Norris', 'Bruce']

