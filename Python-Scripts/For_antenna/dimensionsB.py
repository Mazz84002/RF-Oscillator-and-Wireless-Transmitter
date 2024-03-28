import numpy as np
import sympy as sp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def cal():
    global a, d

    f = 3.5 * 1e9  # Convert to Hz
    Er = 4.1
    h = 1 / 1000  # Convert to meters

    c = 3e8  # Speed of light

    # Calculating Width and Length of the Patch
    W = (c / (2 * f)) * ((2 / (Er + 1))**0.5)
    Er_eff = (Er + 1) / 2 + ((Er - 1) / 2) * (1 / np.sqrt(1 + (12 * (h / W))))
    L_eff = c / (2 * f * np.sqrt(Er_eff))
    a1 = (Er_eff + 0.3) * ((W / h) + 0.264)
    a2 = (Er_eff - 0.258) * ((W / h) + 0.8)
    delta_L = (0.412 * (a1 / a2)) * h
    L = L_eff - 2 * delta_L

    print('Width of the patch =', W * 1000, 'mm')
    print('Length of the patch =', L * 1000, 'mm')

    # Calculating the input impedance of the patch
    Zo = 90 * Er**2 * (L / W)**2 / (Er - 1)

    # Calculating the strip transition line
    Zt = np.sqrt(50 * Zo)
    a3 = np.exp(Zt * np.sqrt(Er) / 60)
    p = -4 * h * a3
    q = 32 * h**2
    Wt1 = - (p / 2) + np.sqrt((p / 2)**2 - q)
    Wt2 = - (p / 2) - np.sqrt((p / 2)**2 - q)  # Width of the transition line
    Er_t = (Er + 1) / 2 + ((Er - 1) / 2) * (1 / np.sqrt(1 + (12 * (h / Wt2))))
    L_t = (c / f) / (4 * np.sqrt(Er_t))  # Length of transition line

    print('Width of the transition line =', Wt2 * 1000, 'mm')
    print('Length of transition line =', L_t * 1000, 'mm')

    # Calculating the 50 ohm transmission line (symbolic solution required)
    Z0 = 50
    a = 1.393 - (120 * np.pi / (Z0 * np.sqrt(Er)))
    # Solve for the width of the 50 ohm line using sympy.solve
    W50 = np.linspace(1e-3, 2e-3, 100000)
    # Define the equation
    equation = W50/h + 2/3 * np.log(W50/h + 1.444) + a
    #fig, ax = plt.subplots()
    #plt.plot(W50, equation)
    #ax.axhline(y=0, color='red')
    #plt.grid()

    closest_index = np.argmin(np.abs(equation))

    W50_val = W50[closest_index]

    L50 = (L/np.pi) * np.arccos(np.sqrt(Z0/Zt))

    print('Width of the 50 Ohms line =', W50_val * 1000, 'mm')
    print('Length of 50 Ohms line =', L50 * 1000, 'mm')
    #plt.show()

if __name__ == '__main__':
    cal()