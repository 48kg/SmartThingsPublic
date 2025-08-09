import unittest
from time_board_game import Age

class TestAge(unittest.TestCase):
    def test_progress(self):
        age = Age('Test', ['Tech1'])
        age.progress()
        self.assertEqual(age.techs, ['Tech1'])
        # population should grow by at least 5%
        self.assertGreaterEqual(age.population, 105)

if __name__ == '__main__':
    unittest.main()
