import unittest
from main import *


class TestMain(unittest.TestCase):

   def test_monthly_payment(self):
       result = monthly_payment(50000, 3, 5)
       self.assertEqual(result, ((50000+(50000*3/100*5))/60))

if __name__ == '__main__':
    unittest.main()