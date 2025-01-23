# **Dual Autodiff**

Dual Autodiff is a Python package for forward-mode automatic differentiation using dual numbers. This package simplifies the computation of derivatives for mathematical functions, making it ideal for educational and scientific computing purposes.

---

## **Features**

- **Automatic Differentiation:** Simplifies forward-mode differentiation for scalar functions using dual numbers.
- **Dual Number Arithmetic:** Supports arithmetic operations (addition, subtraction, multiplication, division, floor division, and power).
- **Mathematical Functions:** Handles trigonometric (`sin`, `cos`, `tan`), hyperbolic (`sinh`, `cosh`, `tanh`), and exponential/logarithmic (`exp`, `log`, `sqrt`) functions.
- **Inverse Hyperbolic Functions:** Includes support for `asinh`, `acosh`, and `atanh`.
- **Error Handling:** Robust checks for division by zero, logarithms of non-positive numbers, invalid inputs, and more.
- **Comprehensive Tests:** Includes unit tests to ensure accuracy and robustness.

---
## **Installation**

### **1. Clone or Download the Repository**
Clone the repository or download the files from [GitLab](https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/assessments/c1_coursework1/sy475.git).

### **2. Install the Package**

Navigate to the project directory and run:

```bash
pip install .
```

### **3.  Install the Cythonized Version (Optional)**

```bash
python setup_cython.py build_ext --inplace
pip install .
```

---

## **Usage**

### **1. Initialize Dual Numbers**

Create dual numbers using the Dual class. A dual number has a real part and a dual part. For example:

```python
from dual_autodiff.dual import Dual

x = Dual(3.0, 1.0)  # Represents 3 + 1ε
```

### **2. Arithmetic Operations**

Perform arithmetic operations on dual numbers:

```python
x = Dual(3, 1)
y = Dual(2, 0.5)

z_add = x + y  # Dual(real=5, dual=1.5)
z_sub = x - y  # Dual(real=1, dual=0.5)
z_mul = x * y  # Dual(real=6, dual=3.5)
z_div = x / y  # Dual(real=1.5, dual=0.25)
z_pow = x**2   # Dual(real=9, dual=6)

```

### **3. Mathematical Functions**

Use built-in mathematical functions with dual numbers:

```python
x = Dual(3, 1)

# Trigonometric functions
z_sin = x.sin()  # Dual(real=sin(3), dual=cos(3))
z_cos = x.cos()  # Dual(real=cos(3), dual=-sin(3))
z_tan = x.tan()  # Dual(real=tan(3), dual=1/cos(3)^2)

# Exponential and logarithmic functions
z_exp = x.exp()  # Dual(real=exp(3), dual=exp(3))
z_log = x.log()  # Dual(real=log(3), dual=1/3)

# Square root
z_sqrt = x.sqrt()  # Dual(real=sqrt(3), dual=1/(2*sqrt(3)))

```

### **4. Hyperbolic and Inverse Hyperbolic Functions**

Work with hyperbolic and inverse hyperbolic functions:

```python
x = Dual(3, 1)

# Hyperbolic functions
z_sinh = x.sinh()  # Dual(real=sinh(3), dual=cosh(3))
z_cosh = x.cosh()  # Dual(real=cosh(3), dual=sinh(3))
z_tanh = x.tanh()  # Dual(real=tanh(3), dual=1/cosh(3)^2)

# Inverse hyperbolic functions
z_asinh = x.asinh()  # Dual(real=asinh(3), dual=1/sqrt(3^2+1))
z_acosh = x.acosh()  # Dual(real=acosh(3), dual=1/sqrt(3^2-1))
z_atanh = Dual(0.5, 1).atanh()  # Dual(real=atanh(0.5), dual=1/(1-0.5^2))

```

---

## **Examples of Specific Function Derivatives**

### **1. Derivative of $f(x) = \sin(x^2) + \exp(x)$:**

```python
from dual_autodiff.dual import differentiate

# Define the function
def f(x):
    return (x**2).sin() + x.exp()

# Compute the derivative at x = 3
df_dx = differentiate(f, 3)
print(df_dx)  # 2*x*cos(9) + exp(3), evaluated at x=3


```

### **2. Derivative of Composite Functions: $\sin(x) \cdot \exp(x)$ and $\cos(\exp(x))$:**

```python
from dual_autodiff.dual import differentiate

# Define the function
def f(x):
    return x.sin() * x.exp()

# Compute the derivative at x = 3
df_dx = differentiate(f, 3)
print(df_dx)  # exp(3)*cos(3) + sin(3)*exp(3)

# Define the function
def g(x):
    return x.exp().cos()

# Compute the derivative at x = 3
dg_dx = differentiate(g, 3)
print(dg_dx)  # -sin(exp(3)) * exp(3)
```

---

## **Error Handling**

### **1. Division by Zero:**

```python
try:
    z = Dual(3, 1) / Dual(0, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

### **2. Logarithm of a Non-Positive Number:**

try:
    z = Dual(-1, 1).log()
except ValueError as e:
    print(f"Error: {e}")

```

---

## **Documentation**

The online documentation is available on Read the Docs at the following link: https://dual-autodiff-sy475.readthedocs.io/en/latest/

To build the documentation locally, ensure you have Sphinx installed and run:

cd docs/docs
make html



---

## **Troubleshooting Installation**

If using the Cythonized version, make sure you have Cython installed (pip install cython).
Use Python version >= 3.9, as specified in the pyproject.toml.

---

## **Contributing**

This package was created as part of university coursework and is not open for public contributions. However, suggestions for improvement are welcome.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

