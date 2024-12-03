import unittest
import math
from dual_autodiff import Dual

class TestDual(unittest.TestCase):
    """
    Unit tests for the Dual class to ensure correct behavior of all operations
    and methods, including arithmetic, comparison, and mathematical functions.
    """

    def test_initialization(self):
        """
        Test the initialization of Dual objects.

        Ensure that:
        - Real and dual parts are correctly assigned.
        - Type errors are raised for invalid input types.
        - Value errors are raised for NaN and infinity values.
        """
        self.assertEqual(Dual(5, 3).real, 5)
        self.assertEqual(Dual(5, 3).dual, 3)
        self.assertRaises(TypeError, Dual, "5", 3)
        self.assertRaises(TypeError, Dual, 5, "3")
        self.assertRaises(ValueError, Dual, math.nan, 3)
        self.assertRaises(ValueError, Dual, 5, math.nan)
        self.assertRaises(ValueError, Dual, math.inf, 3)
        self.assertRaises(ValueError, Dual, 5, math.inf)

    def test_repr_str(self):
        """
        Test string representation of Dual objects.

        Ensure that:
        - __repr__ produces the expected unambiguous string.
        - __str__ produces the expected human-readable string.
        """
        self.assertEqual(repr(Dual(5, 3)), "Dual(5, 3)")
        self.assertEqual(str(Dual(5, 3)), "5 + 3ε")

    def test_addition(self):
        """
        Test addition operations with Dual objects and scalars.

        Ensure that:
        - Dual + Dual returns the correct Dual object.
        - Dual + scalar returns the correct Dual object.
        - Scalar + Dual returns the correct Dual object.
        """
        self.assertEqual(Dual(5, 3) + Dual(2, 4), Dual(7, 7))
        self.assertEqual(Dual(5, 3) + 2, Dual(7, 3))
        self.assertEqual(2 + Dual(5, 3), Dual(7, 3))

    def test_subtraction(self):
        """
        Test subtraction operations with Dual objects and scalars.

        Ensure that:
        - Dual - Dual returns the correct Dual object.
        - Dual - scalar returns the correct Dual object.
        - Scalar - Dual returns the correct Dual object.
        """
        self.assertEqual(Dual(5, 3) - Dual(2, 4), Dual(3, -1))
        self.assertEqual(Dual(5, 3) - 2, Dual(3, 3))
        self.assertEqual(7 - Dual(5, 3), Dual(2, -3))

    def test_negation(self):
        """
        Test negation of Dual objects.

        Ensure that:
        - -Dual returns a Dual object with negated real and dual parts.
        """
        self.assertEqual(-Dual(5, 3), Dual(-5, -3))

    def test_multiplication(self):
        """
        Test multiplication operations with Dual objects and scalars.

        Ensure that:
        - Dual * Dual returns the correct Dual object.
        - Dual * scalar returns the correct Dual object.
        - Scalar * Dual returns the correct Dual object.
        """
        self.assertEqual(Dual(5, 3) * Dual(2, 4), Dual(10, 26))
        self.assertEqual(Dual(5, 3) * 2, Dual(10, 6))
        self.assertEqual(2 * Dual(5, 3), Dual(10, 6))

    def test_division(self):
        """
        Test division operations with Dual objects and scalars.

        Ensure that:
        - Dual / Dual returns the correct Dual object.
        - Dual / scalar returns the correct Dual object.
        - Scalar / Dual returns the correct Dual object.
        - Division by zero raises a ZeroDivisionError.
        """
        self.assertEqual(Dual(10, 5) / Dual(2, 1), Dual(5, 0))
        self.assertEqual(Dual(10, 5) / 2, Dual(5, 2.5))
        self.assertEqual(20 / Dual(5, 2), Dual(4, -1.6))
        self.assertRaises(ZeroDivisionError, Dual(10, 5).__truediv__, Dual(0, 1))
        self.assertRaises(ZeroDivisionError, Dual(10, 5).__truediv__, 0)

    def test_floordiv(self):
        """
        Test floor division operations with Dual objects and scalars.

        Ensure that:
        - Dual // Dual returns the correct Dual object with floored real part.
        - Dual // scalar returns the correct Dual object with floored real part.
        - Scalar // Dual returns the correct Dual object with floored real part.
        - Division by zero raises a ZeroDivisionError.
        """
        self.assertEqual(Dual(10, 5) // Dual(2, 1), Dual(5, 0))
        self.assertEqual(Dual(10, 5) // 2, Dual(5, 2.5))
        self.assertEqual(20 // Dual(5, 2), Dual(4, -1.6))
        self.assertRaises(ZeroDivisionError, lambda: Dual(10, 5) // 0)

    def test_power(self):
        """
        Test exponentiation with Dual objects and scalars.

        Ensure that:
        - Dual ** scalar returns the correct Dual object.
        - Dual ** Dual correctly raises a Dual object to the power of another.
        """
        self.assertAlmostEqual((Dual(2, 1) ** 0.5).real, math.sqrt(2), places=7)
        self.assertAlmostEqual((Dual(2, 1) ** 0.5).dual, 0.5 / math.sqrt(2), places=7)

    def test_comparison_operations(self):
        """
        Test comparison operations with Dual objects and scalars.

        Ensure that:
        - ==, !=, <, <=, >, >= behave as expected for Dual objects and scalars.
        """
        self.assertTrue(Dual(5, 3) == Dual(5, 3))
        self.assertTrue(Dual(5, 3) != Dual(5, 4))
        self.assertTrue(Dual(5, 3) > Dual(4, 2))
        self.assertTrue(Dual(5, 3) >= Dual(5, 3))
        self.assertTrue(Dual(5, 3) < Dual(6, 4))
        self.assertTrue(Dual(5, 3) <= Dual(5, 3))

    def test_math_functions(self):
        """
        Test mathematical functions on Dual objects.

        Ensure that:
        - sin, sqrt, exp, and log produce correct results.
        - sqrt raises ValueError for negative real parts.
        """
        self.assertAlmostEqual(Dual(math.pi / 2, 1).sin().real, 1, places=7)
        self.assertAlmostEqual(Dual(math.pi / 2, 1).sin().dual, 0, places=7)
        self.assertAlmostEqual(Dual(4, 2).sqrt().real, 2, places=7)
        self.assertAlmostEqual(Dual(4, 2).sqrt().dual, 0.5, places=7)
        self.assertRaises(ValueError, Dual(-1, 1).sqrt)
        self.assertEqual(Dual(0, 1).exp(), Dual(1, 1))
        self.assertEqual(Dual(1, 0).log(), Dual(0, 0))
        self.assertEqual(Dual(4, 2).log(), Dual(math.log(4), 0.5))

    def test_hyperbolic_functions(self):
        """
        Test hyperbolic functions on Dual objects.

        Ensure that:
        - sinh, cosh, and tanh produce correct results.
        """
        self.assertEqual(Dual(0, 1).sinh(), Dual(0, 1))
        self.assertEqual(Dual(0, 1).cosh(), Dual(1, 0))
        self.assertEqual(Dual(0, 1).tanh(), Dual(0, 1))

    def test_inverse_hyperbolic_functions(self):
        """
        Test inverse hyperbolic functions on Dual objects.

        Ensure that:
        - asinh, acosh, and atanh produce correct results.
        - ValueError is raised for invalid input to atanh and acosh.
        """
        self.assertRaises(ValueError, Dual(1.5, 0).atanh)
        self.assertRaises(ValueError, Dual(-1.5, 0).atanh)
        self.assertAlmostEqual(Dual(0.5, 1).atanh().real, math.atanh(0.5), places=7)
        self.assertAlmostEqual(Dual(0.5, 1).atanh().dual, 1 / (1 - 0.5 ** 2), places=7)

    def test_error_handling(self):
        """
        Test error handling for invalid inputs.

        Ensure that:
        - ValueError is raised for NaN values.
        - ZeroDivisionError is raised for division by zero.
        """
        self.assertRaises(ValueError, Dual, math.nan, 1)
        self.assertRaises(ValueError, Dual, 1, math.nan)
        self.assertRaises(ZeroDivisionError, lambda: Dual(5, 1) / Dual(0, 0))
        self.assertRaises(ValueError, Dual(-1, 1).sqrt)
        self.assertRaises(ValueError, Dual(-1, 1).log)

    def test_round_floor_ceil(self):
        """
        Test rounding, floor, and ceiling functions.

        Ensure that:
        - round, floor, and ceil produce the correct results for real and dual parts.
        """
        self.assertEqual(round(Dual(5.5, 3.2)), Dual(6, 3))
        self.assertEqual(Dual(5.5, 3.2).floor(), Dual(5, 3))
        self.assertEqual(Dual(5.5, 3.2).ceil(), Dual(6, 4))

    def test_serialization(self):
        """
        Test serialization and deserialization of Dual objects.

        Ensure that:
        - Dual objects can be serialized into a dictionary.
        - Dual objects can be deserialized from a dictionary.
        """
        dual = Dual(5, 3)
        serialized = dual.to_dict()
        self.assertEqual(serialized, {"real": 5, "dual": 3})
        deserialized = Dual.from_dict(serialized)
        self.assertEqual(dual, deserialized)


if __name__ == "__main__":
    unittest.main()
