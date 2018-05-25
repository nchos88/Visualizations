from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib
cmap = matplotlib.cm.get_cmap('tab20c')
plt.style.use("seaborn-whitegrid")
matplotlib.rcParams['figure.figsize'] = (8.0, 3.0)
#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

norm = matplotlib.colors.Normalize(vmin=0, vmax=3)


rgba = cmap(norm(0))
rgba1 = cmap(norm(1))
rgba2 = cmap(norm(2))



fig, ax = plt.subplots()
plt.title('Number of Episode with Action-Count below 2500 ( Higher is Better ) ')
plt.barh([1,2],[1067,101,82])
plt.yticks([1,2,3], ['SWARL-CA','SWARL','Q-Learning'])


ax.get_children()[0].set_color(rgba) 
ax.get_children()[1].set_color(rgba1) 
ax.get_children()[2].set_color(rgba2) 
plt.show()

