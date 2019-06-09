import scipy
import numpy as np
from sympy import *


#1
import kinematika.kinematicsR1 as k1

q1 = Symbol('q1')
q2 = Symbol('q2')

q1d = Symbol('q1\'\'')
print(diff(cos(q1)))
a1 = Symbol('a1')
m1 = Symbol('m1')
d1 = Symbol('d1')
f1 = Symbol('f1')

a2 = Symbol('a2')
m2 = Symbol('m2')
d2 = Symbol('d2')
f2 = Symbol('f2')

g0 = Symbol('g0')


#2
i = 1
T_0_0 = np.eye(4)
D = np.zeros(3)
i3 = np.array([0, 0, 1]).reshape(-1, 1)
R_0_0 = np.eye(3)

H1 = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0]])

n = 2 #DOF



dc1 = np.array([-(a1/2), 0, 0, 0]).reshape(-1, 1)
D1 = np.array([[d1**2+f1**2, 0, 0],
               [0, a1**2+d1**2, 0],
               [0, 0, a1**2+f1**2]])

D1 = np.multiply(m1/12, D1)
dc2 = np.array([-(a2/2), 0, 0, 0]).reshape(-1, 1)
D2 = np.array([[d2**2+f2**2, 0, 0],
               [0, a2**2+d2**2, 0],
               [0, 0, a2**2+f2**2]])

D2 = np.multiply(m2/12, D2)

#ulaz
q_ = (q1, q2)
T_ = [k1.T_0_1, k1.T_1_2]
D_ = [D1, D2]
dc_ = [dc1, dc2]

#izlaz

z_ = np.zeros(n)
c_ = np.zeros(n)
Aq = np.zeros(n)
Bq = np.zeros(n)
Jq = np.zeros(n)
R0_ = np.zeros(n+1)
Dq_ = np.zeros(n)

R0_[0] = R_0_0

while i <= n:
    m = i-1
    z[m] = R0_[m].dot(i3)
    c_[m] = H1.dot(T_[m]).dot(dc_[m])
