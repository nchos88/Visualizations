import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
import numpy as np

#region color
from matplotlib import cm
import matplotlib
cmap = matplotlib.cm.get_cmap('tab10')
norm = matplotlib.colors.Normalize(vmin=0, vmax=3)
rgba = cmap(norm(0))
rgba1 = cmap(norm(1))

def autolabel(ax,rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.97*height,
                '%d' % int(height),
                ha='center', va='bottom')

#endregion

f , ax = plt.subplots(1,2,figsize=(10,6))

N =4
ind = np.arange(N)
width = 0.8
opacity = 0.7

temp = [ 0, 100 , 78 , 0 ]
time = [ 0 , 166 , 132 , 0]

ind1=[1]
time1 = [166]
temp1 = [100]
ind2=[2]
time2 = [132]
temp2 = [78]

rect11 = ax[0].bar(ind1 , time1 , alpha = opacity , width = width , label='4.4 GHz') 
rect12 = ax[0].bar(ind2 , time2 , alpha = opacity ,width = width , label='4.9 GHz') 
ax[0].get_children()[0].set_color(rgba) 
ax[0].get_children()[1].set_color(rgba1)
ax[0].set_ybound( 100 , 170)
ax[0].set_xticks(ind) # position and number of ticks
ax[0].set_xticklabels(["","Before","After",""])
ax[0].set_title("Task Time ( Lower is better)")
ax[0].set_ylabel(" Time ( ms )")
ax[0].legend()
autolabel(ax[0],rect11)
autolabel(ax[0],rect12)

rect21 = ax[1].bar(ind1 , temp1 , alpha = opacity , width = width , label='4.4 GHz') 
rect22 = ax[1].bar(ind2 , temp2 , alpha = opacity ,width = width , label='4.9 GHz') 
ax[1].get_children()[0].set_color(rgba) 
ax[1].get_children()[1].set_color(rgba1)
ax[1].set_ybound( 110 , 50)
ax[1].set_xticks(ind) # position and number of ticks
ax[1].set_xticklabels(["","Before","After",""])
ax[1].set_title("Average Temperature ( Lower is better)")
ax[1].set_ylabel("Temperature( C )")
ax[1].legend()
autolabel(ax[1],rect21)
autolabel(ax[1],rect22)
plt.show()

#https://matplotlib.org/2.1.1/gallery/statistics/barchart_demo.html
#https://matplotlib.org/api/axes_api.html

