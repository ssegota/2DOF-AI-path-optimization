import numpy as np
from sympy import *

q1 = Symbol('q1')
q2 = Symbol('q2')
a2 = Symbol('a1')

T_0_1 = numpy.array([[cos(q1), -sin(q1), 0, 0.2*cos(q1)],
                     [sin(q1), cos(q1), 0, 0.2*sin(q1)],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

T_1_2 = numpy.array([[cos(q2), -sin(q2), 0, 0.4*cos(q2)],
                     [sin(q2), cos(q2), 0, 0.4*sin(q2)],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

T_0_2 = numpy.array([[cos(q1 + q2), -sin(q1 + q2),  0,  0.2*cos(q1) + 0.4*cos(q1 + q2)], 
                    [sin(q1 + q2), cos(q1 + q2),   0,  0.2*sin(q1) + 0.4*sin(q1 + q2)], 
                    [0,            0,              1,  0], 
                    [0,            0,              0,  1]])

#print("T_0_2 = ", T_0_2)
#print("T_0_2(1,4) = ", T_0_2[0][3])
