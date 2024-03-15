import numpy as np
import matplotlib.pyplot as plt
import sys
import ast
from tabulate import tabulate
import pandas as pd

def read_second_column(filename):
    data = pd.read_csv(filename, delimiter='\t')
    data[['re(V(v1))', 'im(V(v1))']] = data['V(v1)'].str.split(',', expand=True)
    Z_out_osc = np.array(data['re(V(v1))'], dtype=complex) + 1j*np.array(data["im(V(v1))"], dtype=complex)
    return Z_out_osc


def findQ(R_high, R_low):
    return np.sqrt(R_high/R_low -1)

def findXparallel(Q, R_high):
    return R_high/Q

def findXseries(Q, R_low):
    return Q*R_low

def findLC_ld_side(Xparallel, Xseries, f0):
    C = 1/(2*np.pi*f0*Xseries)
    L = Xparallel/(2*np.pi*f0)
    return L, C

def findLC_src_side(Xparallel, Xseries, f0):
    C = 1/(2*np.pi*f0*Xparallel)
    L = Xseries/(2*np.pi*f0)
    return L, C


def ll(x, y):
    return x*y/(x+y)

def plotResponse(f, x, title):
    plt.figure()
    plt.plot(f, np.real(x))
    plt.plot(f, np.imag(x))
    plt.xlabel('f')
    plt.ylabel(title)
    plt.grid()

def plotImpedance(w, L_src, L_ld, C_src, C_ld, Z_load):
    #impedance = (1j*w*L_src) + ll(1/(1j*w*C_com), 1j*w*L_ld+Z_load)
    impedance = 1j*w*L_src + ll(
        1/(1j*w*C_src), ll(
            1j*w*L_ld, 1/(1j*w*C_ld) + Z_load
        )
    )
    plt.figure()
    plt.plot(w/(2*np.pi), impedance)
    plt.xlabel('f')
    plt.ylabel('impedance seen by oscillator')
    plt.grid()
    return max(impedance)

def displayStats(f0, 
                 Z_out_osc,
                 Z_load,
                 Z_center,
                 Q_src,
                 Xparalle_src,
                 Xseries_src,
                 L_src,
                 C_src,
                 Q_ld,
                 Xparalle_ld,
                 Xseries_ld,
                 L_ld,
                 C_ld, 
                 C_com,
                 max_imp):
    # Creating a table
    table = [
        ["Variable", "Value"],
        ["f0", f0],
        ["Z_out_osc", Z_out_osc],
        ["Z_load", Z_load],
        ["Z_center", Z_center],
        ["Q_src", Q_src],
        ["Xparalle_src", Xparalle_src],
        ["Xseries_src", Xseries_src],
        ["L_src", L_src],
        ["C_src", C_src],
        ["Q_ld", Q_ld],
        ["Xparalle_ld", Xparalle_ld],
        ["Xseries_ld", Xseries_ld],
        ["L_ld", L_ld],
        ["C_ld", C_ld],
        ["C_com", C_com],
        ["L_com", ll(L_src, L_ld)],
        ["max_imp", max_imp]
    ]
    # Printing the table
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))


def main():
    args = sys.argv

    f0 = 3.5e9                                                                  # operating freq
    f = np.linspace(3e9, 4e9, 100000)                                           # f array for plots
    Z_out_osc = read_second_column("Input-Impedance.txt")                       # the load impedance at the output of oscillator for f = 3.5 Ghz
    Z_out_osc_0 = 110                                # oscillator output impedance at 3.5 GHz
    Z_load = 50                                                                 # the actual load impedance

    Z_center = 111                                           # must be larger than both Z_load and Z_out_osc

    # At the source side
    Q_src = findQ(R_high=Z_center, R_low=Z_out_osc_0)
    Xparalle_src = findXparallel(Q=Q_src, R_high=Z_center)
    Xseries_src = findXseries(Q=Q_src, R_low=Z_out_osc_0)
    L_src, C_src = findLC_src_side(Xparallel=Xparalle_src, Xseries=Xseries_src, f0=f0)

    # At the load side
    Q_ld = findQ(R_high=Z_center, R_low=Z_load)
    Xparalle_ld = findXparallel(Q=Q_ld, R_high=Z_center)
    Xseries_ld = findXseries(Q=Q_ld, R_low=Z_load)
    L_ld, C_ld = findLC_ld_side(Xparallel=Xparalle_ld, Xseries=Xseries_ld, f0=f0)


    # values at source that are freq dependent
    plotResponse(f, Z_out_osc, "Z_out_osc")
    
    max_imp = plotImpedance(w=2*np.pi*f,L_src=L_src, L_ld=L_ld, C_src=C_src, C_ld=C_ld, Z_load=Z_load)

    displayStats(f0, 
                 Z_out_osc_0,
                 Z_load,
                 Z_center,
                 Q_src,
                 Xparalle_src,
                 Xseries_src,
                 L_src,
                 C_src,
                 Q_ld,
                 Xparalle_ld,
                 Xseries_ld,
                 L_ld,
                 C_ld, 
                 C_src+C_ld,
                 max_imp)

    plt.show()



if __name__ == "__main__":
    main()