dual_autodiff Package
=====================

The `dual_autodiff` package provides tools for forward-mode automatic differentiation using dual numbers. This package is ideal for educational, scientific, and computational mathematics applications, offering an efficient and intuitive approach to derivative computation.

Dual Class Overview
-------------------

The `Dual` class is the core of the `dual_autodiff` package. It allows forward-mode automatic differentiation by representing dual numbers in the form:

    x = real + dual * ε

where `ε² = 0`. This representation enables efficient computation of both function values and their derivatives simultaneously.

Attributes
----------

- **real (float)**: Represents the real part of the dual number.
- **dual (float)**: Represents the dual part, which propagates the derivative.

Key Advantages
--------------

1. **Simplifies Derivative Computation**  
   Automatically computes derivatives of complex mathematical functions without requiring symbolic differentiation or numerical approximations.

2. **Utility Function for Derivatives**  
   The `differentiate` function provides a direct and efficient interface for computing derivatives of scalar functions.

3. **Lightweight and Standalone**  
   Relies only on Python’s built-in `math` library, ensuring ease of installation and high portability.

4. **Robust Error Handling**  
   Includes detailed checks for common errors, such as division by zero or invalid logarithmic inputs.

5. **Intuitive API**  
   Provides a clean and user-friendly interface for defining and evaluating mathematical expressions.

Supported Features
------------------

Arithmetic Operations
~~~~~~~~~~~~~~~~~~~~~

The `Dual` class supports the following arithmetic operations:

- **Addition** (`+`): Combines the real and dual parts of two dual numbers.
- **Subtraction** (`-`): Subtracts the real and dual parts of two dual numbers.
- **Multiplication** (`*`): Applies the product rule for derivatives.
- **Division** (`/`): Applies the quotient rule, with robust error handling for division by zero.
- **Floor Division** (`//`): Computes the floored quotient of two dual numbers.
- **Power** (`**`): Computes powers of dual numbers, including fractional and scalar exponents.

Mathematical Functions
~~~~~~~~~~~~~~~~~~~~~~

The `Dual` class includes comprehensive support for mathematical functions.

Trigonometric Functions
^^^^^^^^^^^^^^^^^^^^^^^^

- **sin()**: Computes the sine of a dual number.
- **cos()**: Computes the cosine of a dual number.
- **tan()**: Computes the tangent of a dual number (with error handling for undefined values).

Hyperbolic Functions
^^^^^^^^^^^^^^^^^^^^^

- **sinh()**: Computes the hyperbolic sine.
- **cosh()**: Computes the hyperbolic cosine.
- **tanh()**: Computes the hyperbolic tangent.

Exponential and Logarithmic Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **exp()**: Computes the exponential of a dual number.
- **log()**: Computes the natural logarithm, with error handling for non-positive real parts.

Square Root
^^^^^^^^^^^

- **sqrt()**: Computes the square root of a dual number, with error handling for negative real parts.

Inverse Hyperbolic Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **asinh()**: Computes the inverse hyperbolic sine.
- **acosh()**: Computes the inverse hyperbolic cosine, with error handling for inputs less than 1.
- **atanh()**: Computes the inverse hyperbolic tangent, with error handling for inputs outside `(-1, 1)`.

Error Handling
--------------
The `Dual` class includes robust error handling to ensure safe and reliable computations. Common errors handled include:

- **Division by Zero**: Raises a `ZeroDivisionError` for division by zero.
- **Logarithm of Non-Positive Numbers**: Raises a `ValueError` for invalid logarithmic inputs.
- **Unsupported Operations**: Ensures invalid operand types raise a `TypeError`.

Detailed Examples
-----------------

Basic Arithmetic with Dual Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from dual_autodiff.dual import Dual

   # Initialize dual numbers
   x = Dual(3, 1)  # Represents real = 3, dual = 1
   y = Dual(2, 0.5)  # Represents real = 2, dual = 0.5

   # Perform basic arithmetic
   z_add = x + y  # Addition
   z_sub = x - y  # Subtraction
   z_mul = x * y  # Multiplication
   z_div = x / y  # Division
   z_pow = x**2   # Power

   print("Addition:", z_add)
   print("Subtraction:", z_sub)
   print("Multiplication:", z_mul)
   print("Division:", z_div)
   print("Power:", z_pow)

Derivatives of Mathematical Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `dual_autodiff` package simplifies derivative computation using two approaches:

**Using the Dual Class Directly**:

.. code-block:: python

   from dual_autodiff.dual import Dual

   # Define a function f(x)
   def f(x):
       return x.sin() + x.exp()

   # Initialize a dual number
   x = Dual(2, 1)  # Represents real = 2, dual = 1

   # Compute the function value and its derivative
   result = f(x)

   print("Value of f(x):", result.real)
   print("Derivative of f(x):", result.dual)

**Using the differentiate Utility**:

.. code-block:: python

   from dual_autodiff.dual import differentiate

   # Define a function f(x)
   def f(x):
       return x.sin() + x.exp()

   # Compute the derivative at x = 2
   df_dx = differentiate(f, 2)

   print("Derivative of f(x) at x=2:", df_dx)

Composite Functions
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from dual_autodiff.dual import Dual

   # Define a composite function g(x)
   def g(x):
       return (x**2).sin() + x.sqrt()

   # Compute the derivative using differentiate
   from dual_autodiff.dual import differentiate
   dg_dx = differentiate(g, 3)

   print("Derivative of g(x) at x=3:", dg_dx)

Advanced Mathematical Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from dual_autodiff.dual import Dual

   # Initialize a dual number
   x = Dual(0.5, 1)

   # Evaluate advanced functions
   z_asinh = x.asinh()
   z_acosh = Dual(2, 1).acosh()
   z_atanh = x.atanh()

   print("asinh(x):", z_asinh.real, "Derivative:", z_asinh.dual)
   print("acosh(x):", z_acosh.real, "Derivative:", z_acosh.dual)
   print("atanh(x):", z_atanh.real, "Derivative:", z_atanh.dual)

Using Utility Functions
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from dual_autodiff.dual import Dual

   # Initialize a dual number
   x = Dual(-3, 1)

   # Compute the absolute value and conjugate
   z_abs = x.abs()
   z_conj = x.conjugate()

   print("Absolute value:", z_abs)
   print("Conjugate:", z_conj)

Handling Errors Gracefully
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from dual_autodiff.dual import Dual

   # Division by zero
   try:
       z = Dual(3, 1) / Dual(0, 0)
   except ZeroDivisionError as e:
       print(f"Error: {e}")

   # Logarithm of a non-positive number
   try:
       z = Dual(-1, 1).log()
   except ValueError as e:
       print(f"Error: {e}")


Best Practices
--------------

1. **Initialize Dual Numbers Correctly**  
   Ensure that the `dual` part is set to `1` for derivative computations with respect to a single variable.

2. **Handle Errors Gracefully**  
   Use `try`-`except` blocks to catch and handle errors like division by zero or invalid logarithm inputs.

3. **Leverage Composite Functions**  
   Combine `Dual` objects effectively to compute derivatives of complex expressions.

Educational Purposes
~~~~~~~~~~~~~~~~~~~~
- Demonstrate the principles of automatic differentiation.
- Teach numerical methods and calculus concepts.

Scientific Computing
~~~~~~~~~~~~~~~~~~~~
- Derivative-based optimization.
- Sensitivity analysis in physics and engineering.

Mathematical Research
~~~~~~~~~~~~~~~~~~~~~
- Explore properties of mathematical functions with automatic differentiation.
