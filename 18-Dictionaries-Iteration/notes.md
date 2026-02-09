# Dictionaries: Iteration - Study Notes

## Iterating Over Dictionaries
You can iterate directly over a dictionary (which defaults to its keys) or use specific methods.

- **Keys**: `for key in d.keys():`
- **Values**: `for value in d.values():`
- **Items** (Recommended): `for key, value in d.items():`

```python
stats = {"hp": 10, "mp": 5}
for stat, val in stats.items():
    print(f"{stat}: {val}")
```

## Dictionary Comprehensions
A concise way to create dictionaries from iterables.
**Syntax**: `{key_expr: val_expr for item in iterable if condition}`

```python
langs = ["Python", "Ruby"]
lengths = {l: len(l) for l in langs} # {'Python': 6, 'Ruby': 4}

# Inverting a dictionary
inverted = {v: k for k, v in lengths.items()}
```

## Keyword Arguments (`**kwargs`)
The `**` prefix in parameters gathers extra keyword arguments into a **dictionary**.

```python
def collect(**kwargs):
    print(kwargs)

collect(a=1, b=2) # kwargs is {'a': 1, 'b': 2}
```

## Unpacking Dictionary Arguments
Use `**` to pass dictionary keys/values as keyword arguments to a function.
```python
params = {"feet": 5, "inches": 11}
def height(feet, inches): ...
height(**params)
```

## Sorting
`sorted(d)` returns a sorted list of keys. To sort by items, use `sorted(d.items())`.
