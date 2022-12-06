# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_888(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("5 3 -"), 2)
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
        self.assertAlmostEqual(postfix_eval("5"), 5)

    def test_postfix_eval_999(self):
        self.assertNotEqual(postfix_eval('4'), 10)
        self.assertAlmostEqual(postfix_eval('5 6 3 + 7 3 * - 2 + * 6 /'), -8.3333333)
        self.assertAlmostEqual(postfix_eval('6 4 3 + 2 - * 6 /'), 5)
        self.assertAlmostEqual(postfix_eval('5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +'), 18)

    def test_postfix_eval_78(self):
        self.assertAlmostEqual(postfix_eval('5 4 >>'), 0)
        self.assertAlmostEqual(postfix_eval('5.0 4.0 +'), 9)
        self.assertAlmostEqual(postfix_eval('1 1 <<'), 2)

    def test_postfix_eval_02(self):
        with self.assertRaises(ValueError):
            postfix_eval('4 6 6 - /')

    def test_postfix_eval_03(self):
        try:
            postfix_eval("6 -")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("17.4 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("0 /")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_07(self):
        try:
            postfix_eval("4 **")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_08(self):
        try:
            postfix_eval("5 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_09(self):
        try:
            postfix_eval("6 >> *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_10(self):
        try:
            postfix_eval("6.2 5.8 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_11(self):
        try:
            postfix_eval("6 << *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_12(self):
        try:
            postfix_eval("100 + *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_13(self):
        try:
            postfix_eval("6.2 5.8 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_14(self):
        with tsort([]):

    def test_postfix_eval_15(self):
        try:
            postfix_eval('')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix(''), '')
        self.assertNotEqual(infix_to_postfix('80'), '90')
        self.assertEqual(infix_to_postfix('5 * ( 6 + 3 - 7 * 3 + 2 ) / 6'), '5 6 3 + 7 3 * - 2 + * 6 /')
        self.assertEqual(infix_to_postfix('5 * ( ( 3 + 4 ) * 4 ) + 2 / 4'), '5 3 4 + 4 * * 2 4 / +')

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix('4'), '4')
        self.assertEqual(prefix_to_postfix('* - 5 3 2'), '5 3 - 2 *')
        self.assertEqual(prefix_to_postfix(''), '')

    def test_postfix_eval_30(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02a(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_02b(self):
        try:
            postfix_eval('5 9 + 7 / lame +')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Invalid token')

    def test_postfix_eval_03a(self):
        try:
            postfix_eval("2 56 48 - 2 / + 6 * +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03b(self):
        try:
            postfix_eval("4 9 - +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04a(self):
        try:
            postfix_eval("2 20 * 2 / 3 4 + 3 2 ** + 6 - 15 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_04b(self):
        try:
            postfix_eval("7 9 - 3 ** 6")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval32(self):
        self.assertEqual(postfix_eval('2 56 48 - 2 / 3 + 6 * +'), 44)
        self.assertEqual(postfix_eval('6 2 / 6 +'), 9)
        self.assertEqual(postfix_eval('2 3 <<'), 16)
        self.assertEqual(postfix_eval('9 1 >>'), 4)
        self.assertEqual(postfix_eval('3 2 **'), 9)

    def test_postfix_eval40(self):
        self.assertEqual(postfix_eval('3 5 2 ** * 15 / 5 2 2 ** - -'), 4)
        self.assertAlmostEqual(postfix_eval('5.9 5.3 - 7.2 * 1.4 2 ** +'), 6.280000000000004)
        self.assertEqual(postfix_eval('2 20 * 2 / 3 4 + 3 2 ** * + 6 - 15 +'), 92)

    def test_postfix_eval30(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")

    def test_postfix_eval38(self):
        try:
            postfix_eval("7 7 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')

    def test_postfix_eval90(self):
        with self.assertRaises(ValueError):
            postfix_eval("6 3 3 - /")

        with self.assertRaises(ValueError):
            postfix_eval("0 6 6 - 8 ** /")

    def test_postfix_eval78(self):
        try:
            postfix_eval("6 9 / 3 << 1 **")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')

    def test_infix_to_postfix100(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("6 ** 9"), '6 9 **')
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), '5 6 3 + 7 3 * - 2 + * 6 /')

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3'), '3 4 2 * 1 5 - 2 3 ** ** / +')

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix('( ( 3 + 2 ) ** 2 + 3 ) - 9 + 3 ** 2'), '3 2 + 2 ** 3 + 9 - 3 2 ** +')

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix('2 * 20 / 2 + ( 3 + 4 ) * 3 ** 2 - 6 + 15'),
                         '2 20 * 2 / 3 4 + 3 2 ** * + 6 - 15 +')

    def test_infix_to_postfix_06(self):
        self.assertNotEqual(infix_to_postfix("78 + ( 30 - 5 ( 28 + 8 ) ) / 6"), "78 30 5 28 8 + * - 6 / +")

    def test_infix_to_postfix_07(self):
        self.assertNotEqual(infix_to_postfix("( 18 / 3 ) ** 2 + ( ( 13 + 7 ) * 5 ** 2)"),
                            "18 3 / 2 ** 13 7 + 5 2 ** * +")

    def test_infix_to_postfix_08(self):
        self.assertNotEqual(infix_to_postfix("8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1) - 3 )"),
                            "8 3 4 * + 6 2 – 2 6 3 / 1 - * + 3 - +")

    def test_infix_to_postfix_09(self):
        self.assertEqual(infix_to_postfix("( ( 4 + 8 * 3 ) )"), "4 8 3 * +")

    def test_prefix_to_postfix01(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix02(self):
        self.assertEqual(prefix_to_postfix("* / 122 9 + 1 2"), "122 9 / 1 2 + *")

    def test_prefix_to_postfix03(self):
        self.assertEqual(prefix_to_postfix("- * ** 9.2 2.8 + 25 / 10 5 13"), "9.2 2.8 ** 25 10 5 / + * 13 -")

    def test_infix_to_postfix78(self):
        self.assertEqual(infix_to_postfix("5 >> 9 + 1"), "5 9 >> 1 +")
        self.assertEqual(infix_to_postfix("5 << 9 + 1"), "5 9 << 1 +")
        self.assertEqual(infix_to_postfix("6 << 9 ** 2"), "6 9 << 2 **")

    def test_infix_to_postfix_56(self):
        self.assertEqual(infix_to_postfix('19 >> 9 ** 5'), '19 9 >> 5 **')
        self.assertEqual(infix_to_postfix('6 + 9 >> 9 ** 5'), '6 9 9 >> 5 ** +')
        self.assertEqual(infix_to_postfix('9 + 19 * 5 / ( 1 - 5 ) ** 2 ** 3'), '9 19 5 * 1 5 - 2 3 ** ** / +')


if __name__ == "__main__":
    unittest.main()
