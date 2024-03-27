import numpy as np
import matplotlib.pyplot as plt

def main():
    pass


def setup_params():
    fstart = 1e9
    fstop = 5e9
    fpoints = 500
    f = np.linspace(fstart, fstop, fpoints)
    RL = 1e3
    C1 = 100e-15
    Ct = C1
    Lmax = 1e-5
    return f, RL, C1, Ct, Lmax

def h_params(f, gm, r_pi, r0, Re, C1):
    h = np.zeros((2, 2, len(f)), dtype=complex)
    s = 1j*2*np.pi*f

def h2S(h):
    h11 = h[0, 0, :]
    h12 = h[0, 1, :]
    h21 = h[1, 0, :]
    h22 = h[1, 1, :]
    

def S_params_and_k(f, RL, C1, Ct, Lmax): 
    pass

if __name__ == main:
    main()