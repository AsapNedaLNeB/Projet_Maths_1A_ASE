"""
Projet Maths 1A ASE Mai 2024 

Resolution de l'equation du deuxieme ordre (E) par la méthode d'Euler :
Cette méthode donne une approximation numérique du résultat 

(E): ddT + (g/l)*sin(T)  avec T(0) = y0 et dT(0) =dT0
On peut poser dT(x) = F(dT(x),T(x),x) = -(g/l)*sin(T)
"""

import numpy as np
import matplotlib.pyplot as plt

# Constantes :
 
g = 9,8 # m/s**2
l = 20  # m
T0 = 20 #rad
dT0 = 8 #rad/s

# Paramétres d'étude : 

[x0,xf] = [0,10] #Interval d'étude
N = 1000         #Discretisation
h = (xf-x0)/N    #Pas d'étude

# L'erreur commise est en °(h**2)

# La suite de solution discrétisé à °(h**2) prés: 

T = np.zeros(N)
dT = np.zeros(N)
x = np.zeros(N)
T[0]  = T0
dT[0] = dT0
x[0]  = x0

for i in range (0,N-1):
    x[i+1] = x[i] + h
   

plt.close()
plt.figure(2)
plt.title("")
plt.xlabel("x")
plt.ylabel("")
plt.plot(x)
plt.show()