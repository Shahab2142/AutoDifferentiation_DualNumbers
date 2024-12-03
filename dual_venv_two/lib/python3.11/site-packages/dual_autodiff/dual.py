import math

class Dual:
    """
    A class to represent dual numbers and perform automatic differentiation.

    A dual number is represented as `x + yε`, where `x` is the real part,
    `y` is the dual part, and `ε` is an infinitesimal unit satisfying `ε^2 = 0`.

    This implementation allows basic arithmetic, comparison, and mathematical
    operations, enabling automatic differentiation.

    Attributes:
        real (float): The real part of the dual number.
        dual (float): The dual part of the dual number.
    """

    def __init__(self, real, dual=0.0):
        """
        Initialize a Dual number.

        :param real: The real part of the dual number (float or int).
        :param dual: The dual part of the dual number (float or int), default is 0.0.
        :raises TypeError: If real or dual is not a number.
        :raises ValueError: If real or dual is NaN or Infinity.
        """
        if not isinstance(real, (int, float)) or not isinstance(dual, (int, float)):
            raise TypeError("Both real and dual parts must be numbers.")
        if math.isnan(real) or math.isnan(dual):
            raise ValueError("Real or dual part cannot be NaN.")
        if math.isinf(real) or math.isinf(dual):
            raise ValueError("Real or dual part cannot be Infinity.")
        self.real = real
        self.dual = dual

    def __repr__(self):
        """
        Provide an unambiguous string representation of the dual number.

        :return: A string in the form 'Dual(real, dual)'.
        """
        return f"Dual({self.real}, {self.dual})"

    def __str__(self):
        """
        Provide a readable string representation of the dual number.

        :return: A string in the form 'real + dualε'.
        """
        return f"{self.real} + {self.dual}ε"

    def __add__(self, other):
        """
        Add two dual numbers or a dual number and a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: A new Dual object representing the sum.
        """
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        elif isinstance(other, (int, float)):
            return Dual(self.real + other, self.dual)
        return NotImplemented

    def __radd__(self, other):
        """
        Add a scalar to a dual number (reversed operands).

        :param other: A scalar (int or float).
        :return: A new Dual object representing the sum.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Subtract another dual number or a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: A new Dual object representing the difference.
        """
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        elif isinstance(other, (int, float)):
            return Dual(self.real - other, self.dual)
        return NotImplemented

    def __rsub__(self, other):
        """
        Subtract a dual number from a scalar (reversed operands).

        :param other: A scalar (int or float).
        :return: A new Dual object representing the difference.
        """
        if isinstance(other, (int, float)):
            return Dual(other - self.real, -self.dual)
        return NotImplemented

    def __mul__(self, other):
        """
        Multiply two dual numbers or a dual number and a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: A new Dual object representing the product.
        """
        if isinstance(other, Dual):
            return Dual(
                self.real * other.real,
                self.real * other.dual + self.dual * other.real
            )
        elif isinstance(other, (int, float)):
            return Dual(self.real * other, self.dual * other)
        return NotImplemented

    def __rmul__(self, other):
        """
        Multiply a scalar by a dual number (reversed operands).

        :param other: A scalar (int or float).
        :return: A new Dual object representing the product.
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Divide a dual number by another dual number or a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: A new Dual object representing the quotient.
        :raises ZeroDivisionError: If dividing by zero in the real part.
        :raises ValueError: If the denominator contains NaN or Infinity.
        """
        if isinstance(other, Dual):
            if math.isnan(other.real) or math.isnan(other.dual):
                raise ValueError("Cannot divide by a dual number containing NaN.")
            if math.isinf(other.real) or math.isinf(other.dual):
                raise ValueError("Cannot divide by a dual number containing Infinity.")
            if other.real == 0:
                raise ZeroDivisionError("Division by zero in the real part.")
            real_part = self.real / other.real
            dual_part = (self.dual * other.real - self.real * other.dual) / (other.real ** 2)
            return Dual(real_part, dual_part)
        elif isinstance(other, (int, float)):
            if math.isnan(other):
                raise ValueError("Cannot divide by NaN.")
            if math.isinf(other):
                raise ValueError("Cannot divide by Infinity.")
            if other == 0:
                raise ZeroDivisionError("Division by zero.")
            return Dual(self.real / other, self.dual / other)
        return NotImplemented

    def __rtruediv__(self, other):
        """
        Divide a scalar by a dual number (reversed operands).

        :param other: A scalar (int or float).
        :return: A new Dual object representing the quotient.
        :raises ZeroDivisionError: If dividing by zero in the real part.
        :raises ValueError: If the numerator or denominator contains NaN or Infinity.
        """
        if math.isnan(self.real) or math.isnan(self.dual):
            raise ValueError("Cannot divide by a dual number containing NaN.")
        if math.isinf(self.real) or math.isinf(self.dual):
            raise ValueError("Cannot divide by a dual number containing Infinity.")
        if isinstance(other, (int, float)):
            if self.real == 0:
                raise ZeroDivisionError("Division by zero in the real part.")
            real_part = other / self.real
            dual_part = -other * self.dual / (self.real ** 2)
            return Dual(real_part, dual_part)
        return NotImplemented

    def __floordiv__(self, other):
        """
        Perform floor division between two dual numbers or a dual number and a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: A new Dual object representing the quotient with the real part floored.
        :raises ZeroDivisionError: If dividing by zero in the real part.
        """
        if isinstance(other, Dual):
            if other.real == 0:
                raise ZeroDivisionError("Division by zero in the real part.")
            real_part = math.floor(self.real / other.real)
            dual_part = (self.dual * other.real - self.real * other.dual) / (other.real ** 2)
            return Dual(real_part, dual_part)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero.")
            return Dual(math.floor(self.real / other), self.dual / other)
        return NotImplemented

    def __rfloordiv__(self, other):
        """
        Perform floor division between a scalar and a dual number (reversed operands).

        :param other: A scalar (int or float).
        :return: A new Dual object representing the quotient with the real part floored.
        :raises ZeroDivisionError: If dividing by zero in the real part.
        """
        if isinstance(other, (int, float)):
            if self.real == 0:
                raise ZeroDivisionError("Division by zero in the real part.")
            real_part = math.floor(other / self.real)
            dual_part = -other * self.dual / (self.real ** 2)
            return Dual(real_part, dual_part)
        return NotImplemented

    def __pow__(self, other):
        """
        Raise a dual number to the power of another dual number or a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: A new Dual object representing the result.
        :raises ValueError: If the base is non-positive and the exponent is not an integer.
        """
        if isinstance(other, Dual):
            if self.real <= 0:
                raise ValueError("Power undefined for non-positive real base with dual exponent.")
            real_part = self.real ** other.real
            dual_part = real_part * (
                other.real * self.dual / self.real +
                math.log(self.real) * other.dual
            )
            return Dual(real_part, dual_part)
        elif isinstance(other, (int, float)):
            if self.real < 0 and not isinstance(other, int):
                raise ValueError("Power undefined for non-integer exponent with negative base.")
            real_part = self.real ** other
            dual_part = 0 if self.real == 0 else other * (self.real ** (other - 1)) * self.dual
            return Dual(real_part, dual_part)
        return NotImplemented

    def __rpow__(self, other):
        """
        Raise a scalar to the power of a dual number (reversed operands).

        :param other: A scalar (int or float).
        :return: A new Dual object representing the result.
        :raises ValueError: If the base is non-positive.
        """
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("Power undefined for non-positive real base.")
            real_part = other ** self.real
            dual_part = real_part * math.log(other) * self.dual
            return Dual(real_part, dual_part)
        return NotImplemented

    def __neg__(self):
        """
        Negate the dual number.

        :return: A new Dual object with both parts negated.
        """
        return Dual(-self.real, -self.dual)

    def __pos__(self):
        """
        Return the positive value of the dual number.

        :return: The same Dual object.
        """
        return self

    def __eq__(self, other):
        """
        Check for equality between two dual numbers or a dual number and a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: True if equal, False otherwise.
        """
        if isinstance(other, Dual):
            return self.real == other.real and self.dual == other.dual
        elif isinstance(other, (int, float)):
            return self.real == other and self.dual == 0
        return NotImplemented

    def __ne__(self, other):
        """
        Check for inequality between two dual numbers or a dual number and a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: True if not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Check if a dual number is less than another dual number or a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: True if less, False otherwise.
        """
        if isinstance(other, Dual):
            return self.real < other.real
        elif isinstance(other, (int, float)):
            return self.real < other
        return NotImplemented

    def __le__(self, other):
        """
        Check if a dual number is less than or equal to another dual number or a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: True if less than or equal, False otherwise.
        """
        if isinstance(other, Dual):
            return self.real <= other.real
        elif isinstance(other, (int, float)):
            return self.real <= other
        return NotImplemented

    def __gt__(self, other):
        """
        Check if a dual number is greater than another dual number or a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: True if greater, False otherwise.
        """
        if isinstance(other, Dual):
            return self.real > other.real
        elif isinstance(other, (int, float)):
            return self.real > other
        return NotImplemented

    def __ge__(self, other):
        """
        Check if a dual number is greater than or equal to another dual number or a scalar.

        :param other: A Dual object or a scalar (int or float).
        :return: True if greater than or equal, False otherwise.
        """
        if isinstance(other, Dual):
            return self.real >= other.real
        elif isinstance(other, (int, float)):
            return self.real >= other
        return NotImplemented

    def exp(self):
        """
        Compute the exponential of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real part is infinite.
        """
        if math.isinf(self.real):
            raise ValueError("Exponential function undefined for infinite real part.")
        real_part = math.exp(self.real)
        dual_part = real_part * self.dual
        return Dual(real_part, dual_part)

    def log(self):
        """
        Compute the natural logarithm of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real part is non-positive, NaN, or infinite.
        """
        if self.real <= 0:
            raise ValueError("Logarithm undefined for non-positive real part.")
        real_part = math.log(self.real)
        dual_part = self.dual / self.real
        return Dual(real_part, dual_part)

    def sqrt(self):
        """
        Compute the square root of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real part is negative, NaN, or infinite.
        """
        if self.real < 0:
            raise ValueError("Square root undefined for negative real part.")
        real_part = math.sqrt(self.real)
        dual_part = self.dual / (2 * real_part)
        return Dual(real_part, dual_part)

    def sin(self):
        """
        Compute the sine of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real or dual part is NaN or infinite.
        """
        real_part = math.sin(self.real)
        dual_part = math.cos(self.real) * self.dual
        return Dual(real_part, dual_part)

    def cos(self):
        """
        Compute the cosine of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real or dual part is NaN or infinite.
        """
        real_part = math.cos(self.real)
        dual_part = -math.sin(self.real) * self.dual
        return Dual(real_part, dual_part)

    def tan(self):
        """
        Compute the tangent of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the cosine of the real part is zero, or if the real or dual part is NaN or infinite.
        """
        if math.cos(self.real) == 0:
            raise ValueError("Tangent undefined at odd multiples of π/2.")
        real_part = math.tan(self.real)
        dual_part = self.dual / (math.cos(self.real) ** 2)
        return Dual(real_part, dual_part)

    def sinh(self):
        """
        Compute the hyperbolic sine of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real or dual part is NaN.
        """
        real_part = math.sinh(self.real)
        dual_part = math.cosh(self.real) * self.dual
        return Dual(real_part, dual_part)

    def cosh(self):
        """
        Compute the hyperbolic cosine of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real or dual part is NaN.
        """
        real_part = math.cosh(self.real)
        dual_part = math.sinh(self.real) * self.dual
        return Dual(real_part, dual_part)

    def tanh(self):
        """
        Compute the hyperbolic tangent of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real or dual part is NaN or if |real| >= 1.
        """
        real_part = math.tanh(self.real)
        dual_part = self.dual / (math.cosh(self.real) ** 2)
        return Dual(real_part, dual_part)

    def asinh(self):
        """
        Compute the inverse hyperbolic sine of a dual number.

        :return: A new Dual object representing the result.
        """
        real_part = math.asinh(self.real)
        dual_part = self.dual / math.sqrt(self.real ** 2 + 1)
        return Dual(real_part, dual_part)

    def acosh(self):
        """
        Compute the inverse hyperbolic cosine of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If the real part is less than 1.
        """
        if self.real < 1:
            raise ValueError("acosh undefined for real part less than 1.")
        real_part = math.acosh(self.real)
        dual_part = self.dual / math.sqrt(self.real ** 2 - 1)
        return Dual(real_part, dual_part)

    def atanh(self):
        """
        Compute the inverse hyperbolic tangent of a dual number.

        :return: A new Dual object representing the result.
        :raises ValueError: If |real| >= 1.
        """
        if abs(self.real) >= 1:
            raise ValueError("atanh undefined for absolute real part >= 1.")
        real_part = math.atanh(self.real)
        dual_part = self.dual / (1 - self.real ** 2)
        return Dual(real_part, dual_part)

    def abs(self):
        """
        Compute the absolute value of a dual number.

        :return: A new Dual object representing the result.
        """
        return Dual(abs(self.real), self.dual if self.real >= 0 else -self.dual)

    def conjugate(self):
        """
        Compute the conjugate of a dual number (negates the dual part).

        :return: A new Dual object with the dual part negated.
        """
        return Dual(self.real, -self.dual)

    def to_dict(self):
        """
        Serialize the dual number into a dictionary.

        :return: A dictionary with 'real' and 'dual' as keys.
        """
        return {"real": self.real, "dual": self.dual}

    @classmethod
    def from_dict(cls, data):
        """
        Deserialize a dictionary into a dual number.

        :param data: A dictionary with 'real' and 'dual' keys.
        :return: A new Dual object created from the dictionary.
        """
        return cls(data["real"], data["dual"])

    def __round__(self, ndigits=0):
        """
        Round the real and dual parts to the given number of digits.

        :param ndigits: The number of decimal places to round to.
        :return: A new Dual object with rounded parts.
        """
        return Dual(round(self.real, ndigits), round(self.dual, ndigits))

    def floor(self):
        """
        Compute the floor of the real and dual parts.

        :return: A new Dual object with floored parts.
        """
        return Dual(math.floor(self.real), math.floor(self.dual))

    def ceil(self):
        """
        Compute the ceiling of the real and dual parts.

        :return: A new Dual object with ceiled parts.
        """
        return Dual(math.ceil(self.real), math.ceil(self.dual))

    def is_zero(self):
        """
        Check if the dual number is zero.

        :return: True if both real and dual parts are zero, False otherwise.
        """
        return self.real == 0 and self.dual == 0

    def is_positive(self):
        """
        Check if the dual number is positive based on the real part.

        :return: True if the real part is positive, False otherwise.
        """
        return self.real > 0

    def is_negative(self):
        """
        Check if the dual number is negative based on the real part.

        :return: True if the real part is negative, False otherwise.
        """
        return self.real < 0

def differentiate(func, x):
    """
    Compute the first derivative of a function using dual numbers.

    :param func: The function to differentiate.
    :param x: The point at which to compute the derivative.
    :return: The derivative of the function at x.
    """
    dual_x = Dual(x, 1)  # Convert x into a Dual number
    result = func(dual_x)  # Evaluate the function with the Dual number
    return result.dual  # Extract the derivative (dual part)
