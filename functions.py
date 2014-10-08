# -*- coding: utf-8 -*-
"""
Super mathematical functions
"""

def myfunction(x):
  """
  A powerful function tha computes :math:`y = x^2`
  
  :param x: the x value
  :type x: float
  :rtype: float
  
  >>> x = 5
  >>> y = myfunction(x)
  >>> y
  25
  >>> print " AMAZING !!
    File "<stdin>", line 1
      print " AMAZING !!
                       ^
  SyntaxError: EOL while scanning string literal
  >>> print "AMAZING !!"

  .. note::
 
   This function will get me the Fields medal ! (at least)
  
  .. image::  images/rabbit.jpg  
  """
  return x**2   # A comment 
  """
  haha !!! caché !
  """
x = 5
y = myfunction(x)  