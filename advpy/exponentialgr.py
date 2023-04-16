
import numpy as np
import matplotlib.pyplot as plt

#formula n=n0*e^(r*t)
#r=growth rate,t=time,n=initial point
def exp(t,r,n0):
    return n0*np.exp(r*t)

r=0.03
n0=100
t=np.linspace(0,10,100)

n=exp(t,r,n0)

plt.plot(t,n)
plt.xlabel('time')
plt.ylabel('HIV DEATHS')
plt.title('exponential growth')
plt.show()