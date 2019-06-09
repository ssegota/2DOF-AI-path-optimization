import random
import numpy as np
from math import sin,cos
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
genes = list(np.arange(-10, 10, 0.0001))

class Gene:

    a1 = 0.0
    a2 = 0.0

    b1 = 0.0
    b2 = 0.0
    c1 = 0.0
    c2 = 0.0
    d1 = 0.0
    d2 = 0.0
    e1 = 0.0
    e2 = 0.0

    q1 = []
    q2 = []
    dq1 = []
    dq2 = []
    ddq1 = []
    ddq2 = []

    tau1 = []
    tau2 = []
    tau3 = []
    tau4 = []

    fitness = 0.0

    def calcAllFromA(self):
        A1 = np.array([[t1I**3, t1I**2, t1I, 1], [3*t1I**2, 2*t1I, 1, 0],
                       [t1F**3, t1F**2, t1F, 1], [3*t1F**2, 2*t1F, 1, 0]])
        B1 = np.array([q1Initial - self.a1*t1I**4, q1tInitial - 4*self.a1*t1I **
                       3, q1Final - self.a1*t1F**4, q1tFinal - 4*self.a1*t1F**3])
        X1 = np.linalg.solve(A1, B1)

        self.b1 = X1[0]
        self.c1 = X1[1]
        self.d1 = X1[2]
        self.e1 = X1[3]


        A2 = np.array([[t2I**3, t2I**2, t2I, 1], [3*t2I**2, 2*t2I, 1, 0],
                    [t2F**3, t2F**2, t2F, 1], [3*t2F**2, 2*t2F, 1, 0]])
        B2 = np.array([q2Initial - self.a2*t2I**4, q2tInitial - 4*self.a2*t2I **
                       3, q2Final - self.a2*t2F**4, q2tFinal - 4*self.a2*t2F**3])
        X2 = np.linalg.solve(A2, B2)

        self.b2 = X2[0]
        self.c2 = X2[1]
        self.d2 = X2[2]
        self.e2 = X2[3]
    

    
    def calcTaus(self):

        for t1 in np.arange(0, 2, 0.1):
            q1=self.a1*t1**4+self.b1*t1**3+self.c1*t1**2+self.d1*t1+self.e1
            q2=self.a2*t1**4+self.b2*t1**3+self.c2*t1**2+self.d2*t1+self.e2
            dq1=4*self.a1*t1**3+3*self.b1*t1**2+2*self.c1*t1+self.d1
            dq2=4*self.a2*t1**3+3*self.b2*t1**2+2*self.c2*t1+self.d2
            ddq1=12*self.a1*t1**2+6*self.b1*t1+2*self.c1
            ddq2=12*self.a2*t1**2+6*self.b2*t1+2*self.c2

            self.q1.append(q1)
            self.q2.append(q2)
            self.dq1.append(dq1)
            self.dq2.append(dq2)
            self.ddq1.append(ddq1)
            self.ddq2.append(ddq2)

            tau_1 = ddq1*(0.01*sin(q1)**2 + 0.01*cos(q1)**2 + 0.00333333333333333) + 0.001*dq1 - \
                0.981*cos(q1) - 3.924*cos(q1 + q2) + 0.01 - \
                0.009*2.71828182845905**(-abs(dq1)/1000)*np.sign(dq1)
            self.tau1.append(tau_1)
            tau_2 = ddq1*(0.08*sin(q1 + q2)**2 + 0.08*cos(q1 + q2)**2 + 0.0266666666666667) + ddq2*(0.08*sin(q1 + q2)**2 + 0.08 *
                                                                                                    cos(q1 + q2)**2 + 0.0266666666666667) + 0.001*dq2 - 3.924*cos(q1 + q2) + 0.01 - 0.009*2.71828182845905**(-abs(dq2)/1000)*np.sign(dq2)
            self.tau2.append(tau_2)
            tau_3 = ddq1*(0.64*sin(q1)**2 + 0.64*cos(q1)**2 + 0.213333333333333) + 0.001*dq1 - 15.696 * \
                cos(q1) - 22.0725*cos(q1 + q2) + 0.01 - 0.009 * \
                2.71828182845905**(-abs(dq1)/1000)*np.sign(dq1)
            self.tau3.append(tau_3)
            tau_4 = ddq1*(1.0125*sin(q1 + q2)**2 + 1.0125*cos(q1 + q2)**2 + 0.3375) + ddq2*(1.0125*sin(q1 + q2)**2 +
                                                                                            1.0125*cos(q1 + q2)**2 + 0.3375) + 0.001*dq2 - 22.0725*cos(q1 + q2) + 0.01 - 0.009*2.71828182845905**(-abs(dq2)/1000)*np.sign(dq2)
            self.tau4.append(tau_4)
    

    def getFitness(self):
        torques = np.array([self.tau1, self.tau2, self.tau3, self.tau4]).reshape(20,4)
        
        self.fitness = np.sum(np.sqrt(np.sum(np.square(torques))))

    def __init__(self):
        #clear any stovaways
        self.q1[:] = []
        self.q2[:] = []
        self.dq1[:] = []
        self.dq2[:] = []
        self.ddq1[:] = []
        self.ddq2[:] = []
        self.tau1[:] = []
        self.tau2[:] = []
        self.tau3[:] = []
        self.tau4[:] = []

        self.a1 = random.choice(genes)
        self.a2 = random.choice(genes)

        self.calcAllFromA()
        self.calcTaus()
        self.getFitness()
