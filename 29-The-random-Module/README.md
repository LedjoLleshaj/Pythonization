# The `random` Module - Study Notes

The `random` module provides tools for generating pseudo-random numbers and making random selections.

## Random Numbers
- **`random.random()`**: Returns a random float between 0.0 and 1.0.
- **`random.randint(a, b)`**: Returns a random integer between `a` and `b` (both inclusive).
- **`random.randrange(start, stop, step)`**: Returns a randomly selected element from `range(start, stop, step)`.

## Selections from Sequences
- **`random.choice(sequence)`**: Returns a single random element from a non-empty sequence (like a list or string).
- **`random.sample(sequence, k)`**: Returns a list of `k` unique elements chosen from the sequence.

## Shuffling
- **`random.shuffle(list)`**: Shuffles the elements of a list **in-place**.
  ```python
  cards = ["Ace", "King", "Queen"]
  random.shuffle(cards)
  ```
