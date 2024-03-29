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
GENERATIONS = 20
POPULATION_SIZE = 20
MUTATION_CHANCE = 1.0  # mutation between 0 and 100 percent
if MUTATION_CHANCE > 100:
        MUTATION_CHANCE = 100.0
if MUTATION_CHANCE < 0:
        MUTATION_CHANCE = 0.0

CROSSOVER_CHANCE = 80.0
if CROSSOVER_CHANCE > 100:
        CROSSOVER_CHANCE = 100.0
if CROSSOVER_CHANCE < 0:
        CROSSOVER_CHANCE = 0.0

F=1.2 #Fe[0,2]
if F>2.0:
        F=2.0
if F<0.0:
        F=0.0
NOTE = "Differential Evolution"
print("PARAMETERS\n")
print(NOTE)
print("Generations: ", GENERATIONS)
print("Population size: ", POPULATION_SIZE)
print("Mutation chance: ", MUTATION_CHANCE)
print("Crossover chance: ", CROSSOVER_CHANCE)
print("\n")


def genPopulation(geneList):
    for i in range(POPULATION_SIZE):
        g = Gene()
        geneList.append(g)


genes = []
best_fit = []

#generate the beginning population
genPopulation(genes)


for i in range(GENERATIONS):

    print(int(((i+1)/GENERATIONS)*100), "%", "DONE", end="\r")
    #genes[:] = []
    
    #for x in genes:
    #    print(x.fitness)

    #delete worse half of survivors
    for n in range(len(genes)):
        x = genes[n]
        (a,b,c) = random.sample(genes, 3)
        g = Gene()
        g.setParameters(a1=a.a1+F*(b.a1-c.a1),a2=a.a2+F*(b.a2-c.a2))
        if g.fitness < x.fitness:
                genes[n] = g

    #sort
    genes.sort(key=lambda x: x.fitness, reverse=False)
    #store best
    best_fit.append(genes[0].fitness)
    
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

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.plot(
    best_fit, label="$\sum \sqrt{\\tau_1^2+\\tau_2^2+\\tau_3^2+\\tau_4^2}$")
plt.legend(loc='upper right')

plt.show()
