### Lab 2: RC Circuit Simulation
### Modify program for discharging capacitor:
### Change R and C values to observe effects on time constant T = RC.
### Discuss how this relates to real-world circuits.


import numpy as np
import matplotlib.pyplot as plt

R = 1000
C = 1e-6
V = 5

t = np.linspace(0, 0.01, 1000)
Vc = V * (1 - np.exp(-t / (R*C)))

plt.plot (t, Vc)
plt.xlabel("Time (s)")
plt.ylabel ("Voltage (V)")
plt. title ("RC Charging Curve")
plt . show ()

# Modified code for discharging capacitor
import numpy as np
import matplotlib.pyplot as plt

R = 2000  # Changed resistance
C = 2e-6  # Changed capacitance
V0 = 5  # Initial voltage
t = np.linspace(0, 0.02, 1000)
Vc_discharge = V0 * np.exp(-t / (R * C))

plt.subplot(2, 1, 1)
plt.plot(t, Vc_discharge)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC Discharging Curve")
plt.show()
