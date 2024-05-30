"""
Projet Maths 1A ASE Mai 2024 

Resolution de l'equation du deuxieme ordre (E) par la méthode d'Euler :
Cette méthode donne une approximation numérique du résultat 

(E): ddTheta + (g/l)*sin(Theta)  avec Theta(0) = y0 et dTheta(0) =dTheta0
On peut poser dTheta(x) = F(dT(x),Theta(x),x) = -(g/l)*sin(Theta)
"""

import numpy as np
import matplotlib.pyplot as plt

# Constantes :
 
g = 9.8 # m/s**2
l = 20  # m
Theta0 = 0 #rad
dTheta0 = 5 #rad/s

# Paramétres d'étude : 

[t0,tf] = [0,100] #Interval d'étude
N = 1000         #Discretisation
h = (tf-t0)/N    #Pas d'étude

# L'erreur commise est en °(h**2)

# La suite de solution discrétisé à °(h**2) prés: 

Theta = np.zeros(N)
dTheta = np.zeros(N)
t = np.zeros(N)
Theta[0]  = Theta0
dTheta[0] = dTheta0
t[0]  = t0

for i in range (0,N-1):
    t[i+1] = t[i] + h
    Theta[i+1] = Theta[i] +h*dTheta[i]
    dTheta[i+1] = dTheta[i] - h*(g/l)*np.sin(Theta[i])
   

plt.close()
plt.figure(2)
plt.title("Position angulaire du pendule simple au cour du temps")
plt.xlabel("t")
plt.plot(t,Theta)
plt.ylabel("Theta")

plt.figure(3)
plt.title("Vitesse angulaire du pendule simple au cours du temps")
plt.xlabel("t")
plt.plot(t,dTheta)
plt.ylabel("dTheta")

plt.show()