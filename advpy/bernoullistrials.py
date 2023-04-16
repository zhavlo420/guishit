import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt


p=0.3

dist=bernoulli(p)

print(dist.pmf(1))
print(dist.rvs(size=10))

fig,ax=plt.subplots()
x=[0,1]
pmf=[dist.pmf(0),dist.pmf(1)]
ax.bar(x,pmf)
ax.set_xticks(x)
ax.set_xticklabels(['0','1'])
ax.set_title('bernoullis dis')
plt.show()
