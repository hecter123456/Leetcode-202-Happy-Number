import unittest
import math

class unitest(unittest.TestCase):
    def testNone(self):
        Input = 0
        Output = False
        self.assertEqual(Solution().isHappy(Input),Output)
    def testSample(self):
        Input = 19
        Output = True
        self.assertEqual(Solution().isHappy(Input),Output)

class Solution():
    def isHappy(self, n):
        if n == 4 or n == 0:
            return False
        if n == 1:
            return True
        k = 0
        while n != 0:
            k += int(math.pow((n%10),2))
            n = int(n / 10)
        return self.isHappy(k)

if __name__ == '__main__':
    unittest.main()
