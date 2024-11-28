# Tests for Dual Class

This folder contains the unit tests for the `Dual` class, which is implemented as part of the `dual_autodiff` module. The `Dual` class represents dual numbers and provides support for arithmetic, comparison, and mathematical operations, enabling automatic differentiation.

## Structure

- `test_dual.py`: The main test suite for the `Dual` class, implemented using Python's `unittest` framework.
- `__init__.py`: Marks the `tests` directory as a Python package.


## Running the Tests

To run the tests, ensure you have Python installed and the `dual_autodiff` module accessible in your Python environment. Then, you can execute the test suite using the following command:

python -m unittest test_dual.py

## Test Coverage

The test suite covers the following features of the Dual class:

Initialization and error handling
Arithmetic operations (addition, subtraction, multiplication, division, floor division, and exponentiation)
Comparison operations (equality, inequality, greater than, less than, etc.)
Mathematical functions (e.g., sine, cosine, exponential, logarithm, square root)
Hyperbolic functions and their inverses
Rounding, floor, and ceiling operations
Serialization and deserialization