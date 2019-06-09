import numpy as np
from sympy import *

q1 = Symbol('q1')
q2 = Symbol('q2')

T_0_1 = [[cos(q1), -sin(q1), 0, 0.8*cos(q1)],
         [sin(q1), cos(q1), 0, 0.8*sin(q1)],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]

T_1_2 = [[cos(q2), -sin(q2), 0, 0.9*cos(q2)],
         [sin(q2), cos(q2), 0, 0.9*sin(q2)],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]

T_0_2 = [[cos(q1 + q2), -sin(q1 + q2),  0,  0.8*cos(q1) + 0.9*cos(q1 + q2)], 
         [sin(q1 + q2), cos(q1 + q2),   0,  0.8*sin(q1) + 0.9*sin(q1 + q2)], 
         [0,            0,              1,  0], 
         [0,            0,              0,  1]]

#print("T_0_2 = ", T_0_2)
#print("T_0_2(1,4) = ", T_0_2[0][3])
