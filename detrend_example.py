import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

class detrend_example:
    def gen_data(self,ndata=100):
        x=np.linspace(1,ndata,100)
        y=0.5*x+np.random.randn(100)
        self.dt=pd.DataFrame({"x":x,"y":y})
    def detrend(self):
        newy=signal.detrend(self.dt['y'])
        self.dt['newy']=newy
    def plot(self,figname='./result.png'):
        fig=plt.figure()
        ax=fig.add_subplot(211)
        ax.plot(self.dt['x'],self.dt['y'])
        ax2=fig.add_subplot(212)
        ax2.plot(self.dt['x'],self.dt['newy'])
        plt.savefig(figname)
    def save_csv(self,csvname):
        self.dt.to_csv(csvname,sep=';',index=False)
