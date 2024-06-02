
"""
Projet Maths 1A ASE Mai 2024 

Resolution de l'equation du premier ordre (E) par la méthode d'Euler :
Cette méthode donne une approximation numérique du résultat 

(E): dy + k*y = 0  avec y(0) = y0
On peut poser dy(x) = F(y(x),x) = -k*y(x) 
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Constantes :
k = 2
y0 =20

# Paramétres d'étude : 
[x0,xf] = [0,10] #Interval d'étude
N = 1000         #Discretisation
h = (xf-x0)/N    #Le pas d'étude


# La suite de solution (y) discrétisé de (E) à °(h**2) prés: 
x = np.zeros(N) # L'abscisse de la discretisation 
y = np.zeros(N)
Solution_Theorique = np.zeros(N)

x[0] = x0
y[0] = y0
Solution_Theorique[0] = y0

# Generation des points :
for i in range (0,N-1):
    x[i+1] = x[i] + h
    y[i+1] = (1-h*k)*y[i]  # y(x[i+1]) = y(x[i]) +h*F(y(x[i]),x[i])
    Solution_Theorique[i+1]= y0*np.exp(-k*x[i+1])


# Affichage :
plt.close()
plt.figure(1)
plt.title("dy+"+str(k)+"*y=0")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.plot(x,Solution_Theorique)
plt.legend(["Solution avec Euler d'ordre 1","Solution Théorique"])
plt.show()