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
MUTATION_CHANCE = 1.0 #mutation between 0 and 100 percent
if MUTATION_CHANCE > 100:
        MUTATION_CHANCE=100.0
if MUTATION_CHANCE<0:
        MUTATION_CHANCE=0.0

NOTE="GA - avg. recomb."
print("PARAMETERS\n")
print(NOTE)
print("Generations: ", GENERATIONS)
print("Population size: ", POPULATION_SIZE)
print("Mutation chance: ", MUTATION_CHANCE)
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
    #sort
    
    #for x in genes:
    #    print(x.fitness)
    #store best
    
    #delete worse half of survivors
    del genes[-floor(len(genes)/2):]
    
    #refill the population
    for i in range(POPULATION_SIZE-len(genes)):
        (geneA,geneB) = random.sample(genes,2)
        #print("A", geneA.a1, geneA.a2)
        #print("B",geneB.a1, geneB.a2)
        g = Gene()
        g.setParameters(a1=(geneA.a1+geneB.a1)/2, a2=(geneA.a2+geneB.a2)/2)
        #random mutation
        if random.random() < MUTATION_CHANCE/100:
                #print("RANDOM MUTATION")
                g.setParameters(a1=random.choice(populationValues),a2=random.choice(populationValues))
        genes.append(g)

    genes.sort(key=lambda x: x.fitness, reverse=False)
    best_fit.append(genes[0].fitness)
DELTA = best_fit[0]-best_fit[GENERATIONS-1]

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
