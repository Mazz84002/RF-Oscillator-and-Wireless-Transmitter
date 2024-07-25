# %%
import numpy as np

# %%
Vp = 1.26
Vrms = Vp/(np.sqrt(2))

I = (5.93)*1e-3
Vcc = 7*2

# %%
Pin = Vcc*I
Pout = (Vrms**2)/50

eta = Pout/Pin*100
print(eta)

# %%
Vp = 161e-3
Vrms = Vp/(np.sqrt(2))

I = (1.5 + 1.8)*1e-3
Vcc = 5*2

# %%
Pin = Vcc*I
Pout = (Vrms**2)/50

eta = Pout/Pin*100
print(eta)


