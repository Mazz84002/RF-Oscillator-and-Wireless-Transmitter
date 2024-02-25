import numpy as np
import matplotlib.pyplot as plt

f = 3.5e9

T = 1/f
Tstep = T/10
Tstop = T*1000

print("f = ", f)
print("T = ", T)
print("Tstep = ", Tstep)
print("Tstop = ", Tstop)

LCT = np.square(1/(2*np.pi*f))

L = np.linspace(10e-10, 10e-6, 10000)
CT = LCT/L
C1 = CT*2

Ctankv = 0
Lv = 1e-9
CTv = LCT/Lv - Ctankv
C1v = CTv*2

print("for L = 1n, C1 = ", C1v)

plt.figure()
plt.loglog(L, C1)
plt.ylabel("C1/C2")
plt.xlabel("L")
plt.grid()
plt.show()