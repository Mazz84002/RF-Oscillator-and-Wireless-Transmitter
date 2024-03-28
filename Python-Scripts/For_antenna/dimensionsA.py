import numpy as np
from scipy.integrate import quad
from scipy.special import j0  # Bessel function of the first kind, order 0

def cal():
    global k0, W, L

    f = 3.5 * 1e9  # Convert to Hz
    Er = 4.1
    h = 1 / 1000  # Convert to meters

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

    print('width =', W * 1000, 'mm')
    print('length =', L * 1000, 'mm')
    print('the inset feed point distance =', yo * 1000, 'mm')

if __name__ == '__main__':
    cal()
