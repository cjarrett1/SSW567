'''
Created on Sep 1, 2019

@author: Craig Jarrett
SSW-567-WS
HW01
'''
import unittest
from HW_Jarrett.HW01_Jarrett import classifyTriangle


class ClassifyTriangleTest(unittest.TestCase):
    def test_Equilateral(self):
        result = classifyTriangle(1, 1, 1)
        self.assertEquals(result, 'Equilateral triangle')
 
    def test_Isoceles(self):
        result = classifyTriangle(1, 1, 2)
        self.assertEquals(result, 'Isosceles triangle')
 
    def test_Scalene(self):
        result = classifyTriangle(3, 4, 5)
        self.assertEquals(result, 'Scalene triangle')
        
    def test_inputs(self):
        result = classifyTriangle(-3, 4.5, -5)
        self.assertEquals(result, 'Some or all of the values are not integers')
 
if __name__ == '__main__':
    unittest.main()
    