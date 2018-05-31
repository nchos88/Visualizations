
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
color = cm.inferno_r(np.linspace(.4,.8, 6))

pd.DataFrame()

frequencies = [[0.7780,0.9367,0.9973,0.9982,0.9993,0.9997]]   # bring some raw data


x_labels = ['Fixed Physical Model', 'Applied Physical Model', 'Simple DNN Model', 'Simple Random Forest', 'Complex Random Forest', 'Optimized Model']
freq_series = pd.DataFrame(frequencies , columns = x_labels)# in my original code I create a series and run on that, so for consistency I create a series from the list.

colors = ['xkcd:sea blue', 'g', 'yellow', 'k', 'maroon' , 'black']

# now to plot the figure...
plt.figure(figsize=(8, 8))
ax = freq_series.iloc[0].plot(color=colors,kind='bar')
plt.axhline(0, color='k')
ax.set_title("Performance Compare")
ax.set_xlabel("Model Name")
ax.set_ylabel("Correlation Score")
ax.set_xticklabels(x_labels)

rects = ax.patches

# For each bar: Place a label
for rect in rects:
    # Get X and Y placement of label from rect
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2

    # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    va = 'bottom'

    # If value of bar is negative: Place label below bar
    if y_value < 0:
        # Invert space to place label below
        space *= -1
        # Vertically align label at top
        va = 'top'

    # Use Y value as label and format number with one decimal place
    label = "{:.4f}".format(y_value)

    # Create annotation
    plt.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(0, space),          # Vertically shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        ha='center',                # Horizontally center label
        va=va)                      # Vertically align label differently for
                                  # positive and negative values.


plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
y_pos = np.arange(len(x_labels))
plt.xticks(y_pos, x_labels , rotation = 45 )
plt.ylim((0.7 , 1.05))
plt.show()


