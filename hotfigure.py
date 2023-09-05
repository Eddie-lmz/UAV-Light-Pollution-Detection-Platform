import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

file_location = "MARK2.xlsx"
data = pd.read_excel(file_location)
mark = 100
vegetables =data.values[0:mark,1]
farmers = data.values[0:mark:,2]
lightdata =  data.values[0:mark*mark:,0]
harvest = np.zeros((mark,mark))
j = 0
for i in range(mark):
    harvest[i] = lightdata[j:j+mark]
    j = j+mark

plt.xticks(np.arange(len(farmers)), labels=farmers,
                     rotation=45, rotation_mode="anchor", ha="right")
plt.yticks(np.arange(len(vegetables)), labels=vegetables)
plt.title("Harvest of local farmers (in tons/year)")

plt.imshow(harvest)
plt.colorbar()
plt.tight_layout()
plt.show()
