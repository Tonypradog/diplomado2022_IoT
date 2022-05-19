### Betavariate distribución de random y añadiendo un gráfico de sus valores ###

import random
import matplotlib.pyplot as plt
  
nums = []
low = 10
high = 100
mode = 20
  
for i in range(100):
    temp = random.betavariate(5, 10)
    nums.append(temp)
      
plt.plot(nums)
plt.show()