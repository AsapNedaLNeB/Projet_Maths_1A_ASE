from math import *
#méthode de runge kutta mk4 :


# équation : thetapp + g/l*sin(theta) = 0 
# on fixe theta0 et theta_point0 : 
# analogie physique : revient à fixer position et vitesse initiale :

theta0 = 0
theta_point0 = 2 #rad/sec qu'on appelera omega0
omega0 = theta_point0 # vitesse initiale
g = 9.81 # m/sec^2
l = 1 # m

#choix du pas de calcul :
dt = 0.02 # secondes

# calcul des k et j:

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

print(k1,k2,k3,k4)
print(j1,j2,j3,j4)
print(theta1,omega1)