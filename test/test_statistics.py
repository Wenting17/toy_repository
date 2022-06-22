import unittest
from toy_repository.statistics import maximum, minimum

class TestStatistics(unittest.TestCase):
    
    def test_maximum(self):
        number = 5
        output = maximum(number)
        true = 0.5625919433373465
        
        self.assertEqual(output, true)
        
    def test_minimum(self):
        number = 5
        output = minimum(number)
        true =-0.8454361447111014
        
        self.assertEqual(output, true)

if __name__ == "__main__":
    unittest.main()