# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testIsoceles(self): 
        self.assertEqual(classifyTriangle(1,2,3),'Isoceles','3,4,5 is a Right triangle')

    def testScalene(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is a Scalene triangle')
        
    def testEquilateral(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIntegers(self):
        self.assertEqual(classifyTriangle(-1,-2,-3), 'InvalidInput', 'Some or all of the values are not integers')
        
    def testValidTriangleA(self):
        self.assertEqual(classifyTriangle(10,10,5), 'NotATriangle','This is not a triangle')
        
    def testValidTriangleB(self):
        self.assertEqual(classifyTriangle(0,10,0), 'InvalidInput','Some or all of the values are not valid inputs')
        
    def testValidTriangleC(self):
        self.assertEqual(classifyTriangle(300,500,250), 'InvalidInput','Some or all of the values are not valid inputs')

if __name__ == '__main__':
    print('Running unit tests...')
    unittest.main()

