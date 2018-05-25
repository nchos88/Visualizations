from matplotlib import pyplot as plt


from matplotlib import cm
import matplotlib
#normalize item number values to colormap
cmap = matplotlib.cm.get_cmap('tab10')


norm = matplotlib.colors.Normalize(vmin=0, vmax=3)


rgba = cmap(norm(0))
rgba1 = cmap(norm(1))
rgba2 = cmap(norm(2))
rgba3 = cmap(norm(3))


fig, ax = plt.subplots()

plt.bar([1,2,3,4],[1,2,3,4])
plt.xticks([1,2,3,4], ('Bill', 'Fred', 'Mary', 'Sue'))
ax.get_children()[0].set_color(rgba) 
ax.get_children()[1].set_color(rgba1) 
ax.get_children()[2].set_color(rgba2) 
ax.get_children()[3].set_color(rgba3) 
plt.show()
