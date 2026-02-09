# Modules - Study Notes

## Intro to Modules
A module is a Python file (`.py`) containing definitions (functions, classes, variables) that can be imported and used in other scripts.

## Importing Modules
- `import module`: Imports the entire module. Access attributes using dot notation (`module.func()`).
- `from module import func`: Imports a specific attribute. Use it directly without the module name.
- `from module import *`: Imports everything (Not recommended due to possible name collisions).
- `import module as alias`: Assigns a shorthand name to the module.

## The `if __name__ == "__main__":` Block
This block ensures that specific code only runs when the script is executed directly, not when it is imported as a module elsewhere.

```python
if __name__ == "__main__":
    print("Executing script directly")
```

## Private Attributes
By convention, names starting with an underscore (e.g., `_private_var`) are intended to be internal to the module and are not imported when using `from module import *`.

## The Standard Library
Python comes with many pre-installed modules.
- **`math`**: Math constants (`pi`, `e`) and functions (`sqrt`, `sin`, `factorial`).
- **`string`**: Predefined string constants (`ascii_letters`, `digits`, `punctuation`).
- **`sys`**: System-specific parameters and functions (like `argv`).

## The `dir()` Function
Use `dir(module)` to see all available attributes and functions within an imported module.
