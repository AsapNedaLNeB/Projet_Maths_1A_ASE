from math import *
import matplotlib.pyplot as plt
import numpy as np

#méthode de runge kutta mk4 :


# équation : thetapp + g/l*sin(theta) = 0 
# on fixe theta0 et theta_point0 : 
# analogie physique : revient à fixer position et vitesse initiale :

theta0 = 1
theta_point0 = 0.5 #rad/sec qu'on appelera omega0
omega0 = theta_point0 # vitesse initiale
g = 9.8 # m/sec^2
l = 0.5 # m

# discrétisation :
N = 10000

#choix du pas de calcul :
dt = 0.02 # secondes

temps = [float(i) *dt for i in range(0, 501)]
liste_theta = [theta0]
liste_omega = [omega0]

# initialisation de la solution théorique :
Theta_Theorique = [theta0]
dTheta_Theorique = [theta_point0]
ohmega = sqrt(g/l)


# calcul des k et j:
for ii in range(500):
    k1 = omega0*dt 
    j1 = -(g/l)*sin(theta0)*dt

    k2 = (omega0 + j1/2)*dt 
    j2 = -(g/l)*sin(theta0 + k1/2)*dt

    k3 = (omega0 + j2/2)*dt
    j3 = -(g/l)*sin(theta0 + k2/2)*dt

    k4 = (omega0 + j3)*dt
    j4 = -(g/l)*sin(theta0 + k3)*dt

    # calcul de theta1 et omega1 : 

    theta1 = theta0 + 1/6*(k1 + 2*k2 + 2*k3 + k4)
    omega1 = omega0 + 1/6*(j1 + 2*j2 + 2*j3 + j4)

    # calcul de la solution théorique
    Theta_Theorique.append(theta0*cos(ohmega*dt) + theta_point0/ohmega*sin(ohmega*dt))
    dTheta_Theorique.append(-ohmega*theta0*sin(ohmega*dt) + theta_point0*cos(ohmega*dt))

    

    liste_theta.append(theta1)
    liste_omega.append(omega0)

    theta0 = theta1
    omega0 = omega1

# calcul de l'erreur relative :
for i in range (len(liste_theta)): 
    erreur_moyenne_position = abs(liste_theta[i]-Theta_Theorique[i])
    #erreur_moyenne_vitesse  = abs(liste_omega[i]-dTheta_Theorique[i])

erreur_moyenne_position = erreur_moyenne_position/N
#erreur_moyenne_vitesse = erreur_moyenne_vitesse/N

print("erreur_moyenne_position: ",erreur_moyenne_position,"avec g="+str(g)+", l="+str(l)+"m, theta0= "+str(theta0)+"rad , dTheta0="+str(theta_point0)+"rad/s et N="+str(N))
#print("erreur_moyenne_vitesse : ",erreur_moyenne_vitesse,"avec g="+str(g)+", l="+str(l)+"m, theta0= "+str(theta0)+"rad , dTheta0="+str(theta_point0)+"rad/s et N="+str(N))


# test pour la vitesse angulaire :
t = np.zeros(N)
dTheta_Theorique = np.zeros(N)
dTheta_Theorique[0] = theta_point0
[t0,tf] = [0,10]
h = (tf-t0)/N 
for i in range (0,N-1):
    t[i+1] = t[i] + h
    dTheta_Theorique[i+1] = -ohmega*theta0 *np.sin(ohmega*t[i+1]) + theta_point0          *np.cos(ohmega*t[i+1])

plt.plot(temps,liste_theta,label = "courbe position")
plt.plot(temps,liste_omega, label = "courbe vitesse")
plt.plot(temps,Theta_Theorique, 'r--',label = "courbe théorique position")
plt.plot(t, dTheta_Theorique,'b--',label = "courbe théorique vitesse")
plt.legend()
plt.show()