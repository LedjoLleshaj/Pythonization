# Exercises - Study Notes

This directory contains various coding exercises to practice Python concepts.

## Repeated Sequences in String
A script that finds all repeated character sequences in a string of a minimum length and occurrence.

### Key Logic
- Uses nested loops to slide through the text and extract substrings.
- Uses a dictionary to count occurrences of each substring.
- Filters results based on criteria (min length, min occurrences).
- Uses `lambda` in the `sorted()` function for custom sorting (by length then count).

```python
# Custom sorting example
sorted_results = sorted(
    results.items(), 
    key=lambda x: (len(x[0]), x[1]), 
    reverse=True
)
```
筋
