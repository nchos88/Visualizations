import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn-whitegrid")


objects = ('Fixed Physical Model', 'Applied Physical Model', 'Simple DNN Model', 'Simple Random Forest', 'Complex Random Forest', 'Optimized Model')
y_pos = np.arange(len(objects))
performance = [0.7780,0.9367,0.9973,0.9982,0.9993,0.9997]

xlbl = "Correlation"
title = ""

def Horizontal():
    plt.barh(y_pos, performance, align='center', alpha=1 , color = "xkcd:sea blue")
    plt.yticks(y_pos, objects)
    plt.xlabel(xlbl)
    plt.title('Programming language usage')
 
def Vertical():
    plt.bar(y_pos, performance,width = 0.5, align='center', alpha=1 , color = "xkcd:metallic blue")
    plt.xticks(y_pos, objects , rotation = 45 )
    plt.ylabel(xlbl)
    plt.title(title)
    plt.ylim((0.5 , 1.0))
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

if __name__ == "__main__":
    Vertical()
    plt.show()
