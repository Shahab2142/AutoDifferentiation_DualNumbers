Modules
=======

The `dual_autodiff` package contains the following modules, designed to simplify the computation of derivatives using dual numbers.

dual_autodiff.dual Module
-------------------------

The `dual_autodiff.dual` module provides the core `Dual` class, which implements dual number arithmetic and supports mathematical functions for automatic differentiation. It also includes the `differentiate` utility function for easy derivative computation.

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

4. **Derivative Computation**
    - **Manual Differentiation with Dual Numbers:**  
      Directly use the `Dual` class by initializing a dual number with a real part and a dual part (e.g., `Dual(2, 1)`). The derivative is automatically propagated and stored in the dual part during function evaluation. This method provides transparency and control, making it suitable for educational purposes or fine-grained operations.
      
    - **Automatic Differentiation with the `differentiate` Function:**  
      Use the `differentiate` utility for a streamlined approach to compute derivatives. Simply define the scalar function and specify the point of differentiation. The function handles the initialization of dual numbers internally, offering a convenient and clean interface, particularly for complex or user-defined functions.


5. **Error Handling**
    - Includes robust error handling for:
        - Division by zero.
        - Logarithms of non-positive numbers.
        - Unsupported operand types or invalid inputs.

API Reference
-------------

Below is the API reference for the `Dual` class and `differentiate` function, including all available methods and attributes.

.. autoclass:: dual_autodiff.dual.Dual
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autofunction:: dual_autodiff.dual.differentiate
