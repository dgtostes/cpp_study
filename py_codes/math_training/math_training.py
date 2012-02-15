#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes
import random

class Operation(object):
    '''
    class to abstract terms of operations. the init
    gets the first and second terms of the operation and 
    the operator simbol '+', '-', 'x', '/'.
    whith this information the class give us the result 
    of the operation
    '''
    def __init__(self, 
                 first_term,
                 second_term,
                 operator):
        self.operator = operator
        self.first_term = first_term
        self.second_term = second_term
        self.result = self._result()        
          
    def _result(self):
        if self.operator == "+":
            return self.first_term + self.second_term
        elif self.operator == "-":
            return self.first_term - self.second_term
        elif self.operator == "x":
            return self.first_term*self.second_term
        elif self.operator == "/":
            return (self.first_term / self.second_term,
                    self.first_term % self.second_term)
        
    
    def _expose(self):
        if self.operator != "/":
            print "%s %s %s = %s" % (self.first_term,
                                 self.operator, 
                                 self.second_term, 
                                 self.result)
        else:
            if self.result[1] > 0:
                print "%s %s %s = %s  -- mod %s" % (self.first_term,
                                 self.operator, 
                                 self.second_term, 
                                 self.result[0],
                                 self.result[1])
            else:
                print "%s %s %s = %s" % (self.first_term,
                                 self.operator, 
                                 self.second_term, 
                                 self.result[0])

class Trainning(object):
    def __init__(self, 
                 first_term_alg_qty,
                 second_term_alg_qty):
        self.first_term_alg_qty = first_term_alg_qty
        self.second_term_alg_qty = second_term_alg_qty
    
    def _get_operation_terms(self):
        def get_range_tuple(qty_alg):
            min_limit = int("1"+"0"*(qty_alg-1))
            max_limit = int("9"*qty_alg)
            return (min_limit, max_limit)
        
        first_ran_t = get_range_tuple(self.first_term_alg_qty)
        second_ran_t = get_range_tuple(self.second_term_alg_qty)
                
        first_term = random.randint(first_ran_t[0], first_ran_t[1])
        second_term = random.randint(second_ran_t[0], second_ran_t[1])
        
        return {'first_term':first_term,
                'second_term':second_term}    
                 
            
if __name__ == "__main__":
    for i in range(0,10):
        #Operation(3,1,"/")._expose()
        terms_dic = Trainning(3,1)._get_operation_terms()
        Operation(terms_dic['first_term'],terms_dic['second_term'],"+")._expose()
