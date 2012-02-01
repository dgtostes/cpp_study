#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes

import unittest
import datetime
from analise_extrato_bb import *

class test_pd(unittest.TestCase):
   def test_1(self):
      self.assertEqual(process_date('12-08-1981'),datetime.date(1981, 12, 8))
      
   def test_2(self):
      self.assertEqual(process_date('11/15/1982'),datetime.date(1982, 11, 15))
      
   def test_3(self):
      self.assertEqual(process_date('09/11/2001'),datetime.date(2001, 9, 11))       
      
if __name__ == "__main__":
	unittest.main()

