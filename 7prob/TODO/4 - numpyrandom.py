#### Numpy random distribución de EXPONENCIAL ####

import numpy as np 
import matplotlib.pyplot as plt 
  
gfg = np.random.exponential(101.123, 10000) 
gfg1 = np.random.exponential(gfg, 10000) 
  
count, bins, ignored = plt.hist(gfg1, 14, density = True) 
plt.show()