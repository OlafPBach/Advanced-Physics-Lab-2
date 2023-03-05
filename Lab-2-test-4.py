import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Lab-2/main/Lab-2-Test-4.csv"
data = np.genfromtxt(path, delimiter=',', names =True,invalid_raise = False)
val1 = data['Test1']
time = data['Time1']



fig, ax = plt.subplots()
ax.plot(time*10**3,val1, color='blue')
ax.plot(0.48,3.1,"o",color='black')
ax.plot(0.86,6.3,"o",color='black')
ax.plot(1.21,9.15,"o",color='black')
ax.plot(1.58,11.5,"o",color='black')
ax.set_xlim(0,2)
ax.set_ylim(-1,13)
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Amplitude (V)')
ax.set_title('Test 3')

plt.show()