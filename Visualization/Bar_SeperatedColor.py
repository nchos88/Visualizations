import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import cm
import matplotlib
#normalize item number values to colormap
norm = matplotlib.colors.Normalize(vmin=0, vmax=5)
rgba_color1 = cm.tab10(norm(0),bytes=True) 
rgba_color2 = cm.tab10(norm(1),bytes=True) 
rgba_color3 = cm.tab10(norm(2),bytes=True) 
rgba_color4 = cm.tab10(norm(3),bytes=True) 
rgba_color5 = cm.tab10(norm(4),bytes=True) 


s = pd.Series(
    [5, 4, 4, 1, 12],
    index = ["AK", "AX", "GA", "SQ", "WN"]
)

#Set descriptions:
plt.title("Total Delay Incident Caused by Carrier")
plt.ylabel('Delay Incident')
plt.xlabel('Carrier')

#Set tick colors:
ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='red')

#Plot the data:
my_colors = 'rgbkymc'  #red, green, blue, black, etc.
my_colors = [rgba_color1, rgba_color2 , rgba_color3 , rgba_color4 ,rgba_color5]  #red, green, blue, black, etc.

s.plot(
    
    kind='bar', 
    color=my_colors,
)

plt.show()
