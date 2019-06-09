import sys

import random
from math import *
import numpy as np
import sympy as sy
from math import sin, cos, sqrt
random.seed()
genes = list(np.arange(-10, 10, 0.0001))
#print "==========Poznate Vrijednosti========"
q1Initial = 0
q1tInitial = 0
q1Final = 1
q1tFinal = 0
q2Initial = 0
q2tInitial = 0
q2Final = 1
q2tFinal = 0

t1I = 0
t1F = 2
t2I = 0
t2F = 2



a1 = random.choice(genes)
print ("a1 = " + str(a1))
a2 = random.choice(genes)
print ("a2 = " + str(a2))

A1 = np.array([[t1I**3, t1I**2, t1I, 1], [3*t1I**2, 2*t1I, 1, 0],
               [t1F**3, t1F**2, t1F, 1], [3*t1F**2, 2*t1F, 1, 0]])
B1 = np.array([q1Initial - a1*t1I**4, q1tInitial - 4*a1*t1I **
               3, q1Final - a1*t1F**4, q1tFinal - 4*a1*t1F**3])
X1 = np.linalg.solve(A1, B1)
print ("X1  = ", X1)
b1 = X1[0]
c1 = X1[1]
d1 = X1[2]
e1 = X1[3]
print ("b1 = ", b1)
print ("c1 = ", c1)
print ("d1 = ", d1)
print ("e1 = ", e1)

A2 = np.array([[t2I**3, t2I**2, t2I, 1], [3*t2I**2, 2*t2I, 1, 0],
               [t2F**3, t2F**2, t2F, 1], [3*t2F**2, 2*t2F, 1, 0]])
B2 = np.array([q2Initial - a2*t2I**4, q2tInitial - 4*a2*t2I **
               3, q2Final - a2*t2F**4, q2tFinal - 4*a2*t2F**3])
X2 = np.linalg.solve(A2, B2)
print ("X2  = ", X2)
b2 = X2[0]
c2 = X2[1]
d2 = X2[2]
e2 = X2[3]
print ("b2 = ", b2)
print ("c2 = ", c2)
print ("d2 = ", d2)
print ("e2 = ", e2)

for t1 in np.arange(0,2,0.1):
    q1 = a1*t1**4+b1*t1**3+c1*t1**2+d1*t1+e1
    q2 = a2*t1**4+b2*t1**3+c2*t1**2+d2*t1+e2
    dq1 = 4*a1*t1**3+3*b1*t1**2+2*c1*t1+d1
    dq2 = 4*a2*t1**3+3*b2*t1**2+2*c2*t1+d2
    ddq1 = 12*a1*t1**2+6*b1*t1+2*c1
    ddq2 = 12*a2*t1**2+6*b2*t1+2*c2


    tau_1 = ddq1*(0.01*sin(q1)**2 + 0.01*cos(q1)**2 + 0.00333333333333333) + 0.001*dq1 - \
        0.981*cos(q1) - 3.924*cos(q1 + q2) + 0.01 - \
        0.009*2.71828182845905**(-abs(dq1)/1000)*np.sign(dq1)


    tau_2 = ddq1*(0.08*sin(q1 + q2)**2 + 0.08*cos(q1 + q2)**2 + 0.0266666666666667) + ddq2*(0.08*sin(q1 + q2)**2 + 0.08 * \
                                                                                            cos(q1 + q2)**2 + 0.0266666666666667) + 0.001*dq2 - 3.924*cos(q1 + q2) + 0.01 - 0.009*2.71828182845905**(-abs(dq2)/1000)*np.sign(dq2)

    tau_3 = ddq1*(0.64*sin(q1)**2 + 0.64*cos(q1)**2 + 0.213333333333333) + 0.001*dq1 - 15.696*cos(q1) - 22.0725*cos(q1 + q2) + 0.01 - 0.009*2.71828182845905**(-abs(dq1)/1000)*np.sign(dq1)

    tau_4 = ddq1*(1.0125*sin(q1 + q2)**2 + 1.0125*cos(q1 + q2)**2 + 0.3375) + ddq2*(1.0125*sin(q1 + q2)**2 +
                                                                                            1.0125*cos(q1 + q2)**2 + 0.3375) + 0.001*dq2 - 22.0725*cos(q1 + q2) + 0.01 - 0.009*2.71828182845905**(-abs(dq2)/1000)*np.sign(dq2)
    print("Fitness:", np.sqrt(tau_1**2+tau_2**2+tau_3**2+tau_4**2))
