"""
Projet Maths 1A ASE Mai 2024 

Resolution de l'equation du deuxieme ordre (E) par la méthode d'Euler :
Cette méthode donne une approximation numérique du résultat 

(E): ddTheta + (g/l)*sin(Theta)  avec Theta(0) = y0 et dTheta(0) =dTheta0
On peut poser dTheta(x) = F(dT(x),Theta(x),x) = -(g/l)*sin(Theta)
"""

# Import
import numpy as np
import matplotlib.pyplot as plt

# Constantes : 
g = 9.8 # m/s**2
l = 0.5  # m
ohmega = np.sqrt(g/l)
Theta0 = 1 #rad
dTheta0 = 0.5 #rad/s

# Paramétres d'étude : 
[t0,tf] = [0,15] #Interval d'étude en seconde
N = 100000        #Discretisation
h = (tf-t0)/N     #Le pas d'étude


# La suite de solution discrétisé de (E) à °(h**2) prés: 
t = np.zeros(N)
Theta = np.zeros(N)
dTheta = np.zeros(N)
Theta_Theorique = np.zeros(N)
dTheta_Theorique = np.zeros(N)

t[0]  = t0
Theta[0]  = Theta0
dTheta[0] = dTheta0
Theta_Theorique[0]  = Theta0
dTheta_Theorique[0] = dTheta0



# Generation des points
for i in range (0,N-1):

    t[i+1] = t[i] + h
    Theta[i+1] = Theta[i] +h*dTheta[i]
    dTheta[i+1] = dTheta[i] - h*(g/l)*np.sin(Theta[i])

    Theta_Theorique[i+1]  =  Theta0        *np.cos(ohmega*t[i+1]) + dTheta0/ohmega   *np.sin(ohmega*t[i+1])
    dTheta_Theorique[i+1] = -ohmega*Theta0 *np.sin(ohmega*t[i+1]) + dTheta0          *np.cos(ohmega*t[i+1])

# Calcul erreur : 
for i in range (1,N): 
    erreur_moyenne_position = abs(Theta[i]-Theta_Theorique[i])
    erreur_moyenne_vitesse  = abs(dTheta[i]-dTheta_Theorique[i])

#Presence d'un déphasage qui va décupler l'erreur si l'interval de temps est grand
erreur_moyenne_position = erreur_moyenne_position/N
erreur_moyenne_vitesse = erreur_moyenne_vitesse/N
print("erreur_moyenne_position: ",erreur_moyenne_position,"sur",tf-t0,"s avec g="+str(g)+", l="+str(l)+"m, theta0= "+str(Theta0)+"rad , dTheta0="+str(dTheta0)+"rad/s et N="+str(N))
print("erreur_moyenne_vitesse : ",erreur_moyenne_vitesse,"sur",tf-t0,"s avec g="+str(g)+", l="+str(l)+"m, theta0= "+str(Theta0)+"rad , dTheta0="+str(dTheta0)+"rad/s et N="+str(N))
#Erreur déduite pas tres exploitable 

# Affichage
plt.close()

plt.figure(2)
plt.title("Position angulaire du pendule simple au cours du temps")
plt.xlabel("t [s]")
plt.ylabel("Theta")
plt.plot(t,Theta)
plt.plot(t,Theta_Theorique)
plt.legend(["Solution avec Euler d'ordre 2","Solution Théorique"])


plt.figure(3)
plt.title("Vitesse angulaire du pendule simple au cours du temps")
plt.xlabel("t [s]")
plt.ylabel("dTheta")
plt.plot(t,dTheta)
plt.plot(t,dTheta_Theorique)
plt.legend(["Solution avec Euler d'ordre 2","Solution Théorique"])

plt.show()