from sympy import *
import sys
sys.path.append('../')

import kinematika.kinematicsR1 as kin

from simpy import *

q1 = Symbol('q1')
q2 = Symbol('q2')

import numpy as np
from scipy.special import zeta
#set initial values
#1.
n = 2
g_0 = 9.81

T_0_0 = np.eye(4)
f_tool = np.array([0, 0, 0]).reshape(-1,1)
v_0 = np.array([0, 0, 0]).reshape(-1, 1)

dv_0dt = np.array([0, g_0, 0]).reshape(-1, 1)
n_tool = np.array([0, 0, 0]).reshape(-1, 1)

omega_0 = np.array([0, 0, 0]).reshape(-1, 1)
domega_0dt = np.array([0, 0, 0]).reshape(-1, 1)

k = 1

omega_1 = omega_0 + zeta(cos(q1), 1)*n_tool
print(omega_1)

while k<=n:



    k+=1
