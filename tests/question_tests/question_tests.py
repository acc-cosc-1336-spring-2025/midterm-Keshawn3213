import unittest
from src.question_1.use_local_variable import use_local_variable

class TestUseLocalVariable(unittest.TestCase):
    def test_local_variable_does_not_affect_external(self):
        num = 100
        use_local_variable(num)
        # Check that `num` is still 100 after function call
        self.assertEqual(num, 100)

if __name__ == '__main__':
    unittest.main()
import unittest
from src.question_2.get_sum_of_evens import get_sum_of_evens

class TestGetSumOfEvens(unittest.TestCase):
    def test_values(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)

if __name__ == '__main__':
    unittest.main()
    
import unittest
from src.question_3.get_bonus_pay_amount import get_bonus_pay_amount

class TestGetBonusPayAmount(unittest.TestCase):
    def test_bonus_values(self):
        self.assertEqual(get_bonus_pay_amount(-1), "Invalid arguments")
        self.assertEqual(get_bonus_pay_amount(200), 10)       # 5% of 200
        self.assertEqual(get_bonus_pay_amount(600), 36)       # 6% of 600
        self.assertEqual(get_bonus_pay_amount(1000), 70)      # 7% of 1000
        self.assertEqual(get_bonus_pay_amount(1500), 120)     # 8% of 1500
        self.assertEqual(get_bonus_pay_amount(2000), "Invalid arguments")

if __name__ == '__main__':
    unittest.main()
