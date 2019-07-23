from main import *
import unittest


class TestMonthlyPayment(unittest.TestCase):

    def test_monthly_payment(self):
        self.assertEqual(monthly_payment(50000, 3, 5), 958.33)


if __name__ == '__main__':
    unittest.main()
