import matplotlib.pyplot as plt
import numpy as np

def love_s(i,a,b,c):
    s=np.array(np.sqrt(a-np.power((abs(i)-b),c)))
    return s

def love_t(i,a,b,c):
    t=-a*np.sqrt(b-c*abs(i))
    return t

if __name__=='__main__':
    i=np.linspace(-2,2,100)
    x=love_s(i,1,1,2)
    y=love_t(i,2,1,0.5)

    plt.plot(i,x,'--',color='r')
    plt.fill(i,x,color='r')
    plt.plot(i,y,'--',color='r')
    plt.fill(i,y,color='r')
    plt.title('emmmmm')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()