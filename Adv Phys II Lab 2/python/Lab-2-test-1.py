import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Lab-2/main/Lab-2-Test-1.csv"
data = np.genfromtxt(path, delimiter=',', names =True,invalid_raise = False)
val1 = data['Test1']
val2 = data['Test2']
time = data['Time1']

start = next(x for x, val in enumerate(val2)
                                  if val > .25)
end = next(x for x, val in enumerate(val1)
                                  if val > 0.04)
print("The time difference is",round((time[end-1]-time[start-1])*10**4,3),"E-4 s")
      
fig, ax = plt.subplots()
ax.plot(time*10**3,val1, color='blue')
ax.plot(time*10**3,val2-0.05, color='red')
ax.plot(time[end-1]*10**3,0,"o",color='black')
ax.plot(time[start-1]*10**3,0,"o",color='black')
ax.set_xlim(-0.2,.8)
ax.set_ylim(-1,4)
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Amplitude (V)')
ax.set_title('Test 1')
print(time[start+2])

plt.show()