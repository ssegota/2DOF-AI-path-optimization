from matplotlib import pyplot as plt
from fitness import *
import sys

import random
from math import *
import numpy as np
import sympy as sy
from math import sin, cos, sqrt, floor
random.seed()

CONDITION = True

POPULATION_SIZE = 20


NOTE = "Simulated Annealing - linear"
print("PARAMETERS\n")
print(NOTE)


print("\n")


def genPopulation(geneList):
    for i in range(POPULATION_SIZE):
        g = Gene()
        geneList.append(g)


genes = []
best_fit = []

#generate the beginning population
genPopulation(genes)

#starting temp
t0 = 100.0
k = 0
tk = t0
cooling_factor=0.8

while tk>0:

    print(int(100-((tk)/t0)*100), "%", "DONE", end="\r")
    #genes[:] = []


    for n in range(len(genes)):
        #generate a random neighbour
        g = Gene()
        x=genes[n]
        #if it's better set it as new
        difference = g.fitness - x.fitness
        if difference < 0:
            genes[n]=g
        else:
            if random.random() < (1-exp(difference/tk)):
                genes[n] = g


    #sort
    genes.sort(key=lambda x: x.fitness, reverse=False)
    #for x in genes:
    #    print(x.fitness)
    #store best
    best_fit.append(genes[0].fitness)
    k += 1
    tk-=k*cooling_factor

DELTA = best_fit[0]-best_fit[len(best_fit)-1]

#PLOTTING

plt.figure()
plt.title("Change of q1 and q2, "+NOTE)
plt.plot(genes[0].q1)
plt.plot(genes[0].q2)
plt.scatter(np.arange(0, len(genes[0].q1)), genes[0].q1, label="q1")
plt.scatter(np.arange(0, len(genes[0].q2)), genes[0].q2, label="q2")
plt.xlabel("Time [s]")
plt.ylabel("Joint angle [rad]")
plt.legend(loc="upper left")
plt.show()

plt.figure()
plt.title("Change of torques, "+NOTE)
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
plt.title(NOTE+"\nPopulation = "+str(POPULATION_SIZE) +
          ", $\\Delta = $" + str(DELTA)[0:4])

plt.xlabel("Iteration")
plt.ylabel("Fitness")
plt.plot(
    best_fit, label="$\sum \sqrt{\\tau_1^2+\\tau_2^2+\\tau_3^2+\\tau_4^2}$")
plt.legend(loc='upper right')

plt.show()
