import numpy as np

L = 10e-9
C1 = 1e-9
C2 = 1e-9

CT = C1*C2/(C1+C2)

f = 1/(2*np.pi*np.sqrt(L*CT))
T = 1/f
Tstep = T/10

Tstop = T*1000

print("f = ", f)
print("T = ", T)
print("Tstep = ", Tstep)
print("Tstop = ", Tstop)