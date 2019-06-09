import numpy as np
from sympy import *

q1 = Symbol('q1')
q2 = Symbol('q2')
a1 = Symbol('a1')
a2 = Symbol('a2')

q1_ = 0.25
d1 = 0
a1_ = 0.8
alpha_1 = 0

q2_ = 0.3
d2 = 0
a2_ = 0.9
alpha_2 = 0

T_0_1 = np.array([[cos(q1), -cos(alpha_1)*sin(q1),  sin(alpha_1)*sin(q1),   a1*cos(q1)],
                  [sin(q1), cos(alpha_1)*cos(q1),   -sin(alpha_1)*cos(q1),  a1*sin(q1)],
                  [0,       sin(alpha_1),           cos(alpha_1),           d1],
                  [0,       0,                      0,                      1]])


T_1_2 = np.array([[cos(q2), -cos(alpha_2)*sin(q2),  sin(alpha_2)*sin(q2),   a2*cos(q2)],
                  [sin(q2), cos(alpha_2)*cos(q2),   -sin(alpha_2)*cos(q2),  a2*sin(q2)],
                  [0,       sin(alpha_2),           cos(alpha_2),           d2],
                  [0,       0,                      0,                      1]])

print("T_0_1 = ", T_0_1)
print("T_1_2 = ", T_1_2)
T_0_2 = simplify(np.dot(T_0_1, T_1_2))
print(T_0_2)
T_0_2 = T_0_2.subs([(a1, a1_),(a2, a2_)])
print(T_0_2)
