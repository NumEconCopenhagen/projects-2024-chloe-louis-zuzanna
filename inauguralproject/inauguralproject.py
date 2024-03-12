from types import SimpleNamespace

import numpy as np
import matplotlib.pyplot as plt

class inauguralprojectclass:

def omega1B(omega1A):
return 1 - omega1A

def omega2B(omega2A):
return 1 - omega2A

#preferences
alpha = 1/3
beta = 2/3

#endowment
omega1A = 0.8
omega2A = 0.3


#utility functions
def utility_A(x1A, x2A, alpha):
return x1A**alpha * x2A**(1-alpha)

def utility_B(x1B, x2B, beta):
return x1B**beta * x2B**(1-beta)

#demand functions
def demand_1A(p1, p2, omega1A, omega2A):
return alpha * ((p1 * omega1A + p2 * omega2A)/p1)

def demand_2A(p1, p2, omega1A, omega2A):
return (1-alpha)((p1 * omega1A + p2 * omega2A)/p2)

def demand_1B(p1, p2, omega1B, omega2B):
return beta((p1*omega1B + p2*omega2B)/p1)