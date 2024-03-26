import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Lab-2/main/Lab-3-Annual_Surface_Temperature_Change.csv"
data = np.genfromtxt(path, delimiter=',',dtype='U2',invalid_raise = False)

print(data)