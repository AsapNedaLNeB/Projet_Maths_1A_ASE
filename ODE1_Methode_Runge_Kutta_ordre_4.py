from math import *
import matplotlib.pyplot as plt

#méthode de runge kutta mk4 pour l'ordre 1 :


# équation : thetapp + g/l*sin(theta) = 0 
# on fixe theta0 et theta_point0 : 
# analogie physique : revient à fixer position et vitesse initiale :

var_K = 2 #rad/sec qu'on appelera omega0
const_y0 = 20 #valeur initiale
y0 = const_y0 # valeur initiale pour le calcul

#choix du pas de calcul :
dt = 0.02 # secondes

temps = [float(i) *dt for i in range(0, 1501)]
liste_y = [y0]

# implémentation de la solution théorique
Solution_Theorique = [y0]

# calcul des k :
for ii in range(1500):
    k1 = -var_K*y0 
    k2 = -var_K*(k1/2)*dt
    k3 = -var_K*(k2/2)*dt
    k4 = -var_K*k3*dt
    

    # calcul de y(n+1) : 

    y1 = y0 + 1/6*(k1 + 2*k2 + 2*k3 + k4)
    liste_y.append(y1)
    y0 = y1

    # calcul de la solution théorique :

    Solution_Theorique.append(y0*exp(-var_K*dt)) 



#calcul d'erreur : 
for i in range (len(liste_y)): 
    erreur_moyenne= abs (liste_y[i]- Solution_Theorique[i])
    erreur_moyenne = erreur_moyenne/(len(liste_y))

print("erreur_moyenne=",erreur_moyenne,"pour k=",str(var_K),"et y0="+ str(const_y0)) 


# affichage des courbes : 
plt.plot(temps,liste_y,label = "courbe position")
plt.plot(temps, Solution_Theorique, 'r--',label = "solution théorique")
plt.legend()
plt.show()