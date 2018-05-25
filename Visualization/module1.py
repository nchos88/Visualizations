import matplotlib.pyplot as plt
import pandas as pd
data = pd.DataFrame({'name' : ['a','b','c'],'value' : [1,2,3], 
                     'c' : ['b','r','b']})
data.plot('name','value',color=['r', 'g', 'b'],kind='bar')
plt.show()