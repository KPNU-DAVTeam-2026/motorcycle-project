import unittest
from src.token_logic import TokenCalculator

class TestTokenCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = TokenCalculator(cost_per_token=0.01)

    def test_calculate_tokens(self):
        text = "Hello world"
        self.assertEqual(self.calculator.calculate_tokens(text), 2)
        
        text = "This is a test message."
        self.assertEqual(self.calculator.calculate_tokens(text), 5)

    def test_spend_credits_success(self):
        class MockUser:
            def __init__(self, credits):
                self.credits = credits

        user = MockUser(100.0)
        # 10 tokens * 0.01 = 0.1 cost
        success = self.calculator.spend_credits(user, 10)
        self.assertTrue(success)
        self.assertAlmostEqual(user.credits, 99.9)

    def test_spend_credits_failure(self):
        class MockUser:
            def __init__(self, credits):
                self.credits = credits

        user = MockUser(0.05)
        # 10 tokens * 0.01 = 0.1 cost
        success = self.calculator.spend_credits(user, 10)
        self.assertFalse(success)
        self.assertEqual(user.credits, 0.05)

if __name__ == "__main__":
    unittest.main()
