# Project: Texas Hold'em Poker - Study Notes

This project implements a Texas Hold'em Poker game using Object-Oriented Programming (OOP) and Test-Driven Development (TDD).

## Core Architecture
- **`Card`**: Represents a single playing card with a `rank` and a `suit`.
- **`Deck`**: A collection of 52 `Card` objects. Supports shuffling and dealing.
- **`Player`**: Represents a participant with a `name` and a `Hand`.
- **`Hand`**: Collection of cards held by a player. Responsible for determining the best poker hand from available cards.
- **`GameRound`**: Manages the flow of a single round of poker (shuffling, dealing, determining the winner).
- **`Validators`**: A set of classes/methods used to check for specific poker hands (e.g., Flush, Straight, Full House).

## Test-Driven Development (TDD)
The project follows the **Red-Green-Refactor** cycle:
1. **Red**: Write a failing test that defines a small piece of desired functionality.
2. **Green**: Write the simplest code to make the test pass.
3. **Refactor**: Clean up the code while ensuring the tests still pass.

## Key OOP Concepts Used
- **Composition**: A `Deck` *has* many `Cards`. A `Player` *has* a `Hand`.
- **Encapsulation**: Using properties and protected attributes to manage state safely.
- **Magic Methods**:
  - `__str__` and `__repr__`: For descriptive object output.
  - `__eq__`, `__gt__`: To compare card ranks and determine winning players/hands.
  - `__len__`: To check the number of cards in a deck or hand.
- **Inheritance**: (If applicable) base validator classes for different hand types.
筋
