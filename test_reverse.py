# Write a function which accepts a natural number and returns another natural number that represents input’s reverse.
# Please supply unit tests for the solution.
# Examples of input and output values:
# +-----------+-----------+
# | Input     | Output    |
# +-----------+-----------+
# | 123       | 321       |
# | 456951782 | 287159654 |
# | 7777      | 7777      |
# | 24000000  | 42        |
# +----------+------------+
# Assume our data type can handle numbers of arbitrary length and don’t worry about overflows.
# Obviously there is a simple solution like output = int(str(input)[::-1]) but here I ask not to use character
# representation and work only with numbers.
# Extra task. Propose how to generalize this task to floating point numbers. Think not only about how to reverse a number
# but also what user expects from this routine (e.g. should 12.345 result in 21.543 or 543.21 or any other variant).
import unittest
from parameterized import parameterized
from ReverseNumbers import Reverser as rev


class TestMyMethod(unittest.TestCase):

    @parameterized.expand([
        (123, 321),
        (456951782, 287159654),
        (7777, 7777),
        (24000000, 42)
    ])
    def test_prove_its_working(self, input, expected):

        expected_num = expected
        self.assertEqual(rev.reverse_number(self, input), expected_num)

    @parameterized.expand([
        (12.345, 543.21),
        (1.2, 2.1),
        (33.44, 44.33),
        (12312312.1, 1.21321321)
    ])
    def test_prove_floats_work_fine_too(self, my_num, expected_num):
        self.assertEqual(rev.reverse_float_number(self, my_num), expected_num)