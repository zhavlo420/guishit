import numpy as np
import matplotlib.pyplot as plt


trials=10000
p=0.5

results=np.random.binomial(1,p,trials)
ravg=np.cumsum(results)/(np.arange(trials)+1)
fig,ax=plt.subplots()
ax.plot(ravg)
ax.axhline(p,color="green", linestyle="--")
ax.set_xlabel("no of trials")
ax.set_ylabel("error prob")
ax.set_title("monte carlo distribution")
plt.show()
