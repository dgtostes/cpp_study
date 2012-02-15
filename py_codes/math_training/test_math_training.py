#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes

import unittest
from math_training import Adiction, Operation

class test_(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Adiction(100,2,1)._soma(20, 10),30)
        
    def test_2(self):
        self.assertEqual(Adiction(80,3,2)._soma(25, 3),28)
       
      
if __name__ == "__main__":
    unittest.main()
