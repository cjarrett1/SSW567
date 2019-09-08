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
        self.assertEqual(classifyTriangle(3,4,5),'Right')
        
    def testIsoceles(self): 
        self.assertEqual(classifyTriangle(5,5,7),'Isoceles)

    def testScalene(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Scalene')
        
    def testEquilateral(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    
    def testIntegers(self):
        self.assertEqual(classifyTriangle(-1,-2,-3), 'InvalidInput')
        
    def testValidTriangleA(self):
        self.assertEqual(classifyTriangle(1,1,10), 'NotATriangle')
        
    def testValidTriangleB(self):
        self.assertEqual(classifyTriangle(0,10,0), 'InvalidInput')
        
    def testValidTriangleC(self):
        self.assertEqual(classifyTriangle(300,500,250), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests...')
    unittest.main()

