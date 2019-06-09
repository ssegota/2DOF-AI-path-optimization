import numpy as np
from sympy import *

q1 = Symbol('q1')
q2 = Symbol('q2')
a1 = Symbol('a1')
a2 = Symbol('a2')

T_0_1 = np.array([[cos(q1), -sin(q1), 0, 0.2*cos(q1)],
                  [sin(q1), cos(q1), 0, 0.2*sin(q1)],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

T_1_2 = np.array([[cos(q2), -sin(q2), 0, 0.4*cos(q2)],
                  [sin(q2), cos(q2), 0, 0.4*sin(q2)],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

T_0_2 = np.array([[cos(q1 + q2), -sin(q1 + q2),  0,  0.2*cos(q1) + 0.4*cos(q1 + q2)],
                  [sin(q1 + q2), cos(q1 + q2),   0,  0.2*sin(q1) + 0.4*sin(q1 + q2)],
                  [0,            0,              1,  0],
                  [0,            0,              0,  1]])


#print("T_0_2 = ", T_0_2)
#print("T_0_2(1,4) = ", T_0_2[0][3])

#inverse
w1 = Symbol('w1')
w2 = Symbol('w2')


"""
q2_inv = np.arccos((w1**2+w2**2-a1**2-a2**2)/(2*a1*a2))

q1_inv_a = (a1+a2*cos(q2))*w2-w1*a2*sin(q2)
q1_inv_b = (a1+a2*cos(q2))*w1+w2*a2*sin(q2)
q1_inv = np.arctan(np.array([q1_inv_a],np.array([q1_inv_b])))

"""