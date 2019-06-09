import sys

import random
from math import *
import numpy as np
import sympy as sy
from math import sin, cos, sqrt
random.seed()
from fitness import *
from matplotlib import pyplot as plt

CONDITION = True
GENERATIONS = 20
POPULATION_SIZE = 20

def genPopulation(geneList):
    for i in range(POPULATION_SIZE):
        g = Gene()
        geneList.append(g)

genes = []
best_fit = []

for i in range(GENERATIONS):
    
    print(int(((i+1)/GENERATIONS)*100), "%", "DONE", end="\r")
    genes[:] = []
    genPopulation(genes)
    #for k in genes:
    #    print(k.fitness)
    genes.sort(key=lambda x: x.fitness, reverse=False)
    if i == 0:
        k = 0
        best_fit.append(genes[0].fitness)
        continue
    else:
        k = i-1
    
    if genes[0].fitness < best_fit[k]:
        best_fit.append(genes[0].fitness)
    else:
        best_fit.append(best_fit[k])


DELTA = best_fit[0]-best_fit[GENERATIONS-1]

#PLOTTING
plt.figure()
plt.title("Change of q1 and q2")
plt.plot(genes[0].q1)
plt.plot(genes[0].q2)
plt.scatter(np.arange(0, len(genes[0].q1)), genes[0].q1, label="q1")
plt.scatter(np.arange(0, len(genes[0].q2)), genes[0].q2, label="q2")
plt.xlabel("Time [s]")
plt.ylabel("Joint angle [rad]")
plt.legend(loc="upper left")
plt.show()

plt.figure()
plt.title("Change of torques")
plt.plot(genes[0].tau1)
plt.plot(genes[0].tau2)
plt.plot(genes[0].tau3)
plt.plot(genes[0].tau4)
plt.scatter(np.arange(0, len(genes[0].q1)), genes[0].tau1, label="$\\tau_1$")
plt.scatter(np.arange(0, len(genes[0].q1)), genes[0].tau2, label="$\\tau_2$")
plt.scatter(np.arange(0, len(genes[0].q1)), genes[0].tau3, label="$\\tau_3$")
plt.scatter(np.arange(0, len(genes[0].q1)), genes[0].tau4, label="$\\tau_4$")
plt.xlabel("Time [s]")
plt.ylabel("Joint Torque [Nm]")
plt.legend(loc="upper left")
plt.show()

plt.figure()
plt.title("Random search\nPopulation = "+str(POPULATION_SIZE)+ ", $\\Delta = $" + str(DELTA)[0:4])

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.plot(best_fit, label="$\sum \sqrt{\\tau_1^2+\\tau_2^2+\\tau_3^2+\\tau_4^2}$")
plt.legend(loc='upper right')

plt.show()
