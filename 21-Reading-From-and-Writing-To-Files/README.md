# Reading From and Writing To Files - Study Notes

## The `with` Statement (Recommended)
The `with` statement creates a context manager that automatically closes the file after the block finishes, even if an error occurs.

```python
with open("filename.txt", "r") as file:
    content = file.read()
```

## File Modes
- `"r"`: **Read** (default). Opens for reading; error if file doesn't exist.
- `"w"`: **Write**. Opens for writing; creates file if missing, **overwrites** if it exists.
- `"a"`: **Append**. Opens for writing; creates file if missing, **adds to the end** if it exists.

## Reading Methods
- `file.read()`: Reads the entire file as a single string.
- **Line-by-line**: Iterate directly over the file object for memory efficiency.
  ```python
  with open("file.txt") as file:
      for line in file:
          print(line.rstrip()) # rstrip() removes the newline character
  ```

## Writing Methods
- `file.write("text")`: Writes the string to the file. Note that it does not add newlines automatically.
