import unittest
from gradescope_utils.autograder_utils.decorators import weight
from calculator import Calculator


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(2)
    def test_eval_add(self):
        """Test evaluating 1 + 1"""
        val = self.calc.eval("1 + 1")
        self.assertEqual(val, 2)

    @weight(2)
    def test_eval_sub(self):
        """Test evaluating 2 - 1"""
        val = self.calc.eval("2 - 1")
        self.assertEqual(val, 1)

    @weight(2)
    def test_eval_mul(self):
        """Test evaluating 4 * 8"""
        val = self.calc.eval("4 * 8")
        self.assertEqual(val, 32)

    @weight(2)
    def test_eval_div(self):
        """Test evaluating 8/4"""
        val = self.calc.eval("8 / 4")
        self.assertEqual(val, 2)

    @weight(2)
    def test_eval_whitespace(self):
        """Test evaluating 1+1 (no whitespace)"""
        val = self.calc.eval("1+1")
        self.assertEqual(val, 2)

    @weight(2)
    def test_eval_parens(self):
        """Test evaluating (1+1)*4"""
        val = self.calc.eval("(1 + 1) * 4")
        self.assertEqual(val, 8)

    @weight(2)
    def test_eval_precedence(self):
        """Test evaluating 1 + 1 * 8"""
        val = self.calc.eval("1 + 1 * 8")
        self.assertEqual(val, 9)

    @weight(2)
    def test_eval_mul_div(self):
        "Test evaluating 8 / 4 * 2"
        val = self.calc.eval("8 / 4 * 2")
        self.assertEqual(val, 4)
