# Lists: Iteration - Study Notes

## The `for` Loop
Used to iterate over elements of any iterable (lists, strings, ranges, etc.).

```python
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
```

## The `range()` Function
Generates a sequence of integers.
- `range(stop)`: 0 to stop-1.
- `range(start, stop)`: start to stop-1.
- `range(start, stop, step)`: increments by step.

```python
for i in range(0, 10, 2):
    print(i) # 0, 2, 4, 6, 8
```

## The `enumerate()` Function
Returns both the **index** and the **value** during iteration.

```python
for index, value in enumerate(fruits):
    print(f"Index {index} has {value}")
```

## Loop Control Keywords
- `break`: Terminate the loop prematurely.
- `continue`: Skip the rest of the current iteration and move to the next.

## Iterating in Reverse
- `reversed(list)`: Returns a reverse iterator (more memory efficient than slicing).
- `list[::-1]`: Returns a new reversed list.

## Command Line Arguments
Use `sys.argv` (from the `sys` module) to access arguments passed to the script. `sys.argv[0]` is the script name.
