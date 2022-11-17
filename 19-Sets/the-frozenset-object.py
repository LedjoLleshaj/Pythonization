mr_freeze = frozenset(['Mr. Freeze', 'Penguin', 'Riddler'])
print(mr_freeze)
# frozenset function returns a frozenset object, which is an immutable set
# methods like add, remove, discard, pop, clear, update, intersection_update,
# difference_update, symmetric_difference_update, and intersection do not work on frozensets


# Use case
# A frozenset can be used as a key in a dictionary
# A frozenset is hashable, so it can be used as a key in a dictionary
# A set is not hashable, so it cannot be used as a key in a dictionary

regular_set = {1,2,3}
# print({regular_set: 'Hello'}) # TypeError: unhashable type: 'set'
print({mr_freeze: 'Hello'}) # {frozenset({'Riddler', 'Mr. Freeze', 'Penguin'}): 'Hello'}