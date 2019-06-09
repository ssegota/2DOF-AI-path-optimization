import scipy
import numpy as np
from sympy import *


#1
import kinematika.kinematicsR1 as k1


q1 = Symbol('q1')
q2 = Symbol('q2')
"""
dq1 = Symbol('q1\'')
ddq1 = Symbol('q1\'\'')
dq2 = Symbol('q2\'')
ddq2 = Symbol('q2\'\'')
"""
dq1 = Symbol('dq1')
ddq1 = Symbol('ddq1')
dq2 = Symbol('dq2')
ddq2 = Symbol('ddq2')

a1 = Symbol('a1')
m1 = Symbol('m1')
d1 = Symbol('d1')
f1 = Symbol('f1')

a2 = Symbol('a2')
m2 = Symbol('m2')
d2 = Symbol('d2')
f2 = Symbol('f2')
           # bv     bs     bd
b_coefs_1 = [0.001, 0.001, 0.01, 1000]
b_coefs_2 = [0.001, 0.001, 0.01, 1000]

g0 = Symbol('g0')
q_ = (q1, q2)
dq_ = (dq1, dq2)
ddq_ = (ddq1, ddq2)
#2
n=2
i = 1
T_0_0 = np.eye(4)
D = np.zeros(3)

#3.1
dc1 = np.array([-(a1/2), 0, 0, 0]).reshape(-1,1)

#4.1
#tenzor inercije
D1 = np.array([[d1**2+f1**2, 0, 0],
               [0, a1**2+d1**2, 0],
               [0, 0, a1**2+f1**2]])

D1 = np.multiply(m1/12, D1)

#5.1
i3 = np.array([0, 0, 1]).reshape(-1, 1)

R_0_0 = np.eye(3)

z0 = np.dot(R_0_0,i3)

#matrica složene homogene transformacije
H1 = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0]])

c1 = np.dot(H1, np.dot(k1.T_0_1, dc1))

R_0_1 = k1.T_0_1[:3,:3]


#D_1_q = np.dot(R_0_1, np.dot(D1, R_0_1.transpose()))
D_1_q = R_0_1.dot(D1).dot(R_0_1.transpose())

#jacobian

A_1_q = np.hstack((np.array(diff(c1,q1)).reshape(3,1), np.zeros((3, 1))))
B_1_q = np.hstack((z0, np.zeros((3, 1))))

J_1_q = np.vstack((A_1_q, B_1_q))

D_1_q = np.multiply(A_1_q.transpose(), m1).dot(A_1_q) + B_1_q.transpose().dot(D_1_q).dot(B_1_q)

#print("D_1_q = ", D_1_q)

#5.2

z1 = R_0_1.dot(i3)
dc2 = np.array([-(a2/2), 0, 0, 0]).reshape(-1, 1)
c2 = H1.dot(k1.T_0_2).dot(dc2)

R_0_2 = k1.T_0_2[:3, :3]

D2 = np.array([[d2**2+f2**2, 0, 0],
               [0, a2**2+d2**2, 0],
               [0, 0, a2**2+f2**2]])

D2 = np.multiply(m2/12, D2)

D_2_q = R_0_2.dot(D2).dot(R_0_2.transpose())

A_2_q = np.hstack((np.array(diff(c2, q1)).reshape(3, 1),
                   np.array(diff(c2, q2)).reshape(3, 1)))
B_2_q = np.hstack((z0, z1))

J_2_q = np.vstack((A_2_q, B_2_q))

D_2_q = np.multiply(A_2_q.transpose(), m2).dot(A_2_q) +  B_2_q.transpose().dot(D_2_q).dot(B_2_q)

#1/2
D_q = D_1_q + D_2_q

C_1_q = np.zeros((2,2))

for k in range(2):
    for j in range(2):
        C_1_q[k][j] = diff(D_q[0][j], q_[k]) - (1/2)*diff(D_q[k][j], q_[0])

#gravitacija
h_1_q = g0*m1*A_1_q[1][0]+g0*m2*A_2_q[1][0]
#trenje

#####q__ --> q dvoderivirano
b_1 = b_coefs_1[0]*dq1 + (b_coefs_1[2] + (b_coefs_1[1]-b_coefs_1[2])*np.e**(-np.abs(dq1)/b_coefs_1[3]))#*np.sign(dq1)
#jednadžba

D_1_SUM = 0
for j in range(n):
    D_1_SUM+=D_1_q[0][j]*ddq_[j]

C_1_SUM = 0
for k in range(2):
    for j in range(n): 
        C_1_sum = C_1_q[k][j]*dq_[k]*dq_[j]

tau_1 = D_1_SUM +C_1_SUM + h_1_q + b_1
#2/2
C_2_q = np.zeros((2, 2))

for k in range(2):
    for j in range(2):
        C_2_q[k][j] = diff(D_q[1][j], q_[k]) - (1/2)*diff(D_q[k][j], q_[1])

#gravitacija
h_2_q = g0*m1*A_1_q[1][1]+g0*m2*A_2_q[1][1]
#trenje
b_2 = b_coefs_2[0]*dq2 + (b_coefs_2[2] + (b_coefs_2[1] -
                                          b_coefs_2[2])*np.e**(-np.abs(dq2)/b_coefs_2[3]))#*np.sign(dq2)
#jednadžba
D_2_SUM = 0
for j in range(n):
    D_2_SUM += D_2_q[0][j]*ddq_[j]

C_2_SUM = 0
for k in range(2):
    for j in range(n):
        C_2_sum = C_2_q[k][j]*dq_[k]*dq_[j]

tau_2 = D_2_SUM + C_2_SUM + h_2_q + b_2

#ubacivanje vrijednosti poznatih


print("tau_1 = ", tau_1.subs([(a1, 0.8), (a2, 0.9), (m1, 4.0), (m2, 5.0), (g0, 9.81), (d1, 0.0), (f1, 0.0)]))
print("tau_2 = ", tau_2.subs([(a1, 0.8), (a2, 0.9), (m1, 4.0), (m2, 5.0), (g0, 9.81), (d2, 0.0), (f2, 0.0)]))
