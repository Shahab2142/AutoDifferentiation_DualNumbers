Modules
=======

The `dual_autodiff` package contains the following modules, designed to simplify the computation of derivatives using dual numbers.

dual_autodiff.dual Module
-------------------------

The `dual_autodiff.dual` module provides the core `Dual` class, which implements dual number arithmetic and supports mathematical functions for automatic differentiation.

Features of dual_autodiff.dual
------------------------------

1. **Dual Number Representation**
    - A dual number is represented as:
      ```
      x = real + dual * ε
      ```
      where `ε² = 0`.

2. **Supported Arithmetic Operations**
    - **Addition** (`+`)
    - **Subtraction** (`-`)
    - **Multiplication** (`*`)
    - **Division** (`/`)
    - **Power** (`**`)

3. **Supported Mathematical Functions**
    - **Trigonometric Functions:** `sin`, `cos`, `tan`
    - **Hyperbolic Functions:** `sinh`, `cosh`, `tanh`
    - **Exponential and Logarithmic Functions:** `exp`, `log`
    - **Square Root:** `sqrt`
    - **Inverse Hyperbolic Functions:** `asinh`, `acosh`, `atanh`

4. **Error Handling**
    - Includes robust error handling for:
        - Division by zero.
        - Logarithms of non-positive numbers.
        - Unsupported operand types or invalid inputs.

API Reference
-------------

Below is the API reference for the `Dual` class, including all available methods and attributes.

.. autoclass:: dual_autodiff.dual.Dual
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:
