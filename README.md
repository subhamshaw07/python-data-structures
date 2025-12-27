# python-data-structures
Implementation of core data structures like Arrays, Linked Lists, and Trees in Python.

# Python Data Structures
A collection of fundamental data structures implemented in Python. This repository demonstrates my understanding of Computer Science theory and Python syntax.

## Contents

### 1. Array Operations (`array_operations.py`)
* **Description:** A script demonstrating the core operations of a dynamic array (List).
* **Key Concepts:**
    * **Insertion/Deletion:** Handling dynamic resizing and safe removal.
    * **Traversal:** Using `enumerate()` for index-value pairs.
    * **Search:** Using the `in` keyword for efficient linear search.
    * **Input Handling:** Using `f-strings` for user-friendly prompts.

## Tech Stack
* **Language:** Python 3.x
* **Focus:** Data Structures & Algorithms (DSA), Efficient Coding Practices
### 2. Matrix Analyzer & Magic Square Validator (`magic square check.py`)
* **Description:** A script that performs structural analysis on 2D Arrays (Matrices). It calculates directional sums and validates if the grid represents a "Magic Square" (where all rows, columns, and diagonals sum to the same value).
* **Key Algorithms:**
    * **Column Operations:** Uses the advanced `zip(*matrix)` technique to transpose rows into columns for efficient vertical summation.
    * **Diagonal Traversal:** Implements logic to traverse both the Primary Diagonal (`index [i][i]`) and the Secondary Diagonal (`index [i][n-1-i]`) in a single pass.
    * **Validation Logic:** Uses Python's `all()` function to compare all calculated sums against a target value.
* **Concepts Covered:** 2D Array Traversal, Matrix Transposition, List Comprehensions, Boolean Logic.
