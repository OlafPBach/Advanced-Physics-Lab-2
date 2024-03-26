import pandas as pd
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Lab-2/main/Lab-4-Trials.csv"
data = pd.read_csv(path, quotechar='"', skipinitialspace=True)

NpData = data.to_numpy()

Trial1 = (NpData[1:5,1])
Trial2 = (NpData[1:5,2])
Trial3 = (NpData[1:5,3])
Trial4 = (NpData[1:5,4])


Aperature = [2,1,0.75,0.5]
SqrAperature = [i**2 for i in Aperature]

print(SqrAperature)

#Raw
fig, ax = plt.subplots()
ax.plot(Aperature,Trial1,color='red')
ax.plot(Aperature,Trial2,color='gold')
ax.plot(Aperature,Trial3,color='green')
ax.plot(Aperature,Trial4,color='blue')
ax.set_xlabel('Aperature Size (mm)')
ax.set_ylabel('Voltage (V)')
ax.set_title('Intensity as a function of Aperature Diameter')
plt.show()

#Raw Squared
fig, ax = plt.subplots()
ax.plot(SqrAperature,Trial1,color='red')
ax.plot(SqrAperature,Trial2,color='gold')
ax.plot(SqrAperature,Trial3,color='green')
ax.plot(SqrAperature,Trial4,color='blue')
ax.set_xlabel('Aperature Size Squared (mm^2)')
ax.set_ylabel('Voltage (V)')
ax.set_title('Intensity as a function of Aperature Diameter Squared')
plt.show()

#normalized with theory
fig, ax = plt.subplots()
ax.plot([4,0],[1,0],color='black')
ax.plot(SqrAperature,Trial1/NpData[1,1],color='red')
ax.plot(SqrAperature,Trial2/NpData[1,2],color='gold')
ax.plot(SqrAperature,Trial3/NpData[1,3],color='green')
ax.plot(SqrAperature,Trial4/NpData[1,4],color='blue')
ax.set_xlabel('Aperature Size Squared (mm^2)')
ax.set_ylabel('Voltage (V)')
ax.set_title('Intensity as a function of Area Squared Normalized')
plt.show()