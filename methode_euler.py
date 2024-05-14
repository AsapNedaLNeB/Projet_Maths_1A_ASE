
# Approximation de la solution de l'equation du pendule simple

#Conditions initial :
Theta_init = 10
Theta_point_init = 5
nbr_iteration = 100

# Grandeurs Physique caractéristique du système
l = 1 #m
g = 9,81 #m/s**2

Theta = [0 for i in range(nbr_iteration)]
Theta_point = [0 for i in range(nbr_iteration)]

# Equations : 
# (1) Theta_point_point + g/l * sin(Theta) = 0
Theta[0] = Theta_init
Theta_point[0] = Theta_point_init

# Resolution de (1) par la méthode d'Euler :

