from math import *
import matplotlib.pyplot as plt

#méthode de runge kutta mk4 :


# équation : thetapp + g/l*sin(theta) = 0 
# on fixe theta0 et theta_point0 : 
# analogie physique : revient à fixer position et vitesse initiale :

theta0 = 1
theta_point0 = 0.5 #rad/sec qu'on appelera omega0
omega0 = theta_point0 # vitesse initiale
g = 9.8 # m/sec^2
l = 0.5 # m

#choix du pas de calcul :
dt = 0.02 # secondes

temps = [float(i) *dt for i in range(0, 1501)]
liste_theta = [theta0]
liste_omega = [omega0]

# calcul des k et j:
for ii in range(1500):
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

    liste_theta.append(theta1)
    liste_omega.append(omega0)

    theta0 = theta1
    omega0 = omega1

plt.plot(temps,liste_theta,label = "courbe position")
plt.plot(temps,liste_omega, label = "courbe vitesse")
plt.legend()
plt.show()