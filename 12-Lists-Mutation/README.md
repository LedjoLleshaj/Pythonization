# Lists: Mutation - Study Notes

## Adding Elements
- `append(value)`: Adds an element to the end.
- `extend(iterable)`: Adds all elements from another iterable (list, tuple, etc.) to the end.
- `insert(index, value)`: Inserts an element at a specific index.

```python
nums = [1, 2]
nums.append(3)      # [1, 2, 3]
nums.extend([4, 5]) # [1, 2, 3, 4, 5]
nums.insert(0, 0)   # [0, 1, 2, 3, 4, 5]
```

## Removing Elements
- `pop()`: Removes and returns the last element.
- `pop(index)`: Removes and returns element at index.
- `remove(value)`: Removes the first occurrence of a value. Raises `ValueError` if not found.
- `clear()`: Removes all elements.
- `del list[index]`: Deletes an element or slice using the `del` keyword.

## Sorting and Ordering
- `sort()`: Sorts the list in-place (ascending by default). Use `reverse=True` for descending.
- `reverse()`: Reverses the elements in-place.

> [!TIP]
> Use `.sort()` when you want to modify the original list. Use the built-in `sorted(list)` if you want a *new* sorted list without changing the original.

## Multiple Assignment (Recap)
You can assign new values to a slice:
```python
fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["blueberry", "blackberry"]
# fruits is now ["apple", "blueberry", "blackberry", "cherry"]
```
