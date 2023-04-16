import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import *

nx=101
ny=101
nt=80
c=1

dx =2 / (nx-1)
dy= 2 / (ny-1)
dt=0.01

x=np.linspace(-1,1,nx)
y=np.linspace(-1,1,ny)
X,Y=np.meshgrid(x,y)

u=np.zeros((ny,nx))
u[int(ny/2),int(nx/2)]=1


for n in range(nt):
    un=u.copy()
    u[1:-1,1:-1]= (un[1:-1,1:-1]-c* dt / dx *(un[1:-1,1:-1]-un[1:-1,:-2]
                                           -c * dt/dy * (un[1:-1,1:-1]- un[:-2,1:-1])))
    u[0,:]=0
    u[ny-1,:]=0
    u[:,0]=0
    u[:,nx-1]=0
    
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot_surface(X,Y,u,cmap='coolwarm')
    ax.set_zlim(0,1)
    plt.show()
