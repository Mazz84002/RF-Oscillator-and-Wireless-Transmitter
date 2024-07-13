import numpy as np
from scipy.integrate import quad
from scipy.special import j0  # Bessel function of the first kind, order 0
import matplotlib.pyplot as plt

def cal():
    global k0, W, L

    f = 3.5 * 1e9  # Convert to Hz
    Er = 4.3
    h = 2 / 1000  # Convert to meters

    c = 3e8  # Speed of light
    k0 = 2 * np.pi * f / c  # Wave number
    Rin = 50  # Required input impedance of the antenna

    # Calculating width and length of the patch
    W = (c / (2 * f)) * ((2 / (Er + 1))**0.5)
    Er_eff = (Er + 1) / 2 + ((Er - 1) / 2) * (1 / np.sqrt(1 + (12 * (h / W))))
    L_eff = c / (2 * f * np.sqrt(Er_eff))
    a1 = (Er_eff + 0.3) * ((W / h) + 0.264)
    a2 = (Er_eff - 0.258) * ((W / h) + 0.8)
    delta_L = (0.412 * (a1 / a2)) * h
    L = L_eff - 2 * delta_L

    # Calculating the distance of the inset feed point
    t = np.linspace(0, np.pi, 100)  # Use np.linspace for better accuracy

    def g1(t):
        global k0, W
        return ((np.sin(k0 * W * 0.5 * np.cos(t)) / np.cos(t))**2 * np.sin(t)**3)

    def g12(t):
        global k0, W, L
        return ((np.sin(k0 * W * 0.5 * np.cos(t)) / np.cos(t))**2 * np.sin(t)**3) * j0(k0 * L * np.sin(t))

    I1 = quad(g1, 0, np.pi)[0]
    G1 = I1 / (120 * np.pi**2)
    I12 = quad(g12, 0, np.pi)[0]
    G12 = I12 / (120 * np.pi**2)
    yo = (L / np.pi) * np.arccos(np.sqrt(2 * Rin * (G1 + G12)))

    with open('outputA.txt', 'w') as file:
        file.write('width = ' + str(W * 1000) + ' mm\n')
        file.write('length = ' + str(L * 1000) + ' mm\n')
        file.write('the inset feed point distance = ' + str(yo * 1000) + ' mm\n\n')

        lambda_eff = c/f*np.sqrt(Er_eff)
        file.write('lambda_eff = ' + str(lambda_eff) + '\n')
        file.write('width of ground plane > ' + str(((lambda_eff/4)*2 + W)*1000) + ' mm\n')
        file.write('length of ground plane > ' + str(((lambda_eff/4)*2 + L)*1000) + ' mm\n\n')

    # Calculating the 50 ohm transmission line (symbolic solution required)
    Z0 = 50
    a = 1.393 - (120 * np.pi / (Z0 * np.sqrt(Er)))
    # Solve for the width of the 50 ohm line using sympy.solve
    W50 = np.linspace(2.5e-3, 3e-3, 100000)
    # Define the equation
    equation = W50/h + 2/3 * np.log(W50/h + 1.444) + a

    # Plotting
    plt.figure()
    fig, ax = plt.subplots()
    plt.plot(W50, equation)
    ax.axhline(y=0, color='red')
    plt.grid()
    plt.savefig('plotA.png')

    Z_feed = 50
    B_feed = 377*np.pi/(2*Z_feed*np.sqrt(Er))
    W_by_h_feed = (2/np.pi)*(B_feed-1-np.log(2*B_feed-1) + (Er-1)/(2*Er) * (np.log(B_feed-1)+0.39-0.61/Er))

    with open('outputA.txt', 'a') as file:
        closest_index = np.argmin(np.abs(equation))
        W50_val = W50[closest_index]
        file.write('width of the 50 Ohms line = ' + str(W_by_h_feed*h*1000) + ' mm\n')
    
    print('width =', W * 1000, 'mm')
    print('length =', L * 1000, 'mm')
    print('\n')
    print('the inset feed point distance =', yo * 1000, 'mm')
    print('\n')
    print('lambda_eff =', lambda_eff)
    print('width of ground plane >', ((lambda_eff/4)*2 + W)*1000, 'mm')
    print('length of ground plane >', ((lambda_eff/4)*2 + L)*1000, 'mm')
    print('\n')
    print("W/h =", W_by_h_feed)
    print('width of the 50 Ohms line =', W_by_h_feed*h * 1000, 'mm')

if __name__ == '__main__':
    cal()
