import unittest

from inventory.metrics import duration_text


class Behaviour(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(duration_text(*(5,)), '0:05')


if __name__ == "__main__":
    unittest.main()
