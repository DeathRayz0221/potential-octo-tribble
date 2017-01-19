# -*- coding: utf-8 -*-
"""
COMP 1012 SECTION A03
INSTRUCTOR: Janjic
ASSIGNMENT: Assignment 2
AUTHOR      Edison Guillermo
VERSION     2016-Jan-7
PURPOSE:    To calculate complex equations
"""

import math

expTotal,sinTotal,cosTotal = 0, 0, 0 # current sum
sign = 1 # sign integer (- or +)
denominator = 1 # denominator
count = 0
term = 1
c1=0
xx = 1
cosTerm,sinTerm = 0,0
print("INVESTIGATION OF COMPLEX INFINITE SERIES")
print("\nPart A: exp, cos and sin series for real value 1")
print("using convergence criterion of 1e-20")
print("%4s %17s %13s %17s %20s" %("count","exp terms","sign",
                                 "cos terms" , "sin terms"))
print("-"*80)
while abs(term) > 10e-20:
    sign = (-1) ** (count//2)
    term = xx**count / denominator
    expTotal += term
    count += 1
    useForCos = term * (count % 2)
    useForSin = term * ((count+1) % 2)
    cosTotal += useForCos
    sinTotal += useForSin
    print("%2d %25s %6d" %(count, term, sign))
    print (useForSin * ("%22.17f" % (term * sign)))
    denominator *= count
    c1 = 0
    sign *= -1
print(expTotal)