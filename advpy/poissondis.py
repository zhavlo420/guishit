import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

i=2#no of events per interval

dist=poisson(i)

k=3
print((dist.pmf(k)))
print(dist.rvs(size=10))

fig,ax=plt.subplots()
x=np.arange(0,11)
pmf=dist.pmf(x)
ax.bar(x,pmf)
ax.set_xticks(x)
ax.set_title('poisson prob distribution')
plt.show()