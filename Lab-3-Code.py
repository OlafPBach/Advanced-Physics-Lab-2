import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Lab-2/main/Lab-3-Annual_Surface_Temperature_Change.csv"
data = pd.read_csv(path, quotechar='"', skipinitialspace=True)

NpData = data.to_numpy()

USTempData = (NpData[214,10:])

Years = np.arange(1961, 2022, 1).tolist()

fig, ax = plt.subplots()
ax.plot(Years,USTempData)
ax.set_xlabel('Year')
ax.set_ylabel('Change of Average Temperature')
ax.set_title('The Effects of Climate Change on Average Temperature')
plt.show()
