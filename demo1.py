import os
import detrend_example

if(__name__=="__main__"):
    ####### interface #######
    workdir="./"
    ndata=100
    csvname='result.csv'
    figname='result.png'
    ####### interface #######
    os.chdir(workdir)
    tmp=detrend_example.detrend_example()
    tmp.gen_data(ndata)
    tmp.detrend()
    tmp.plot(figname)
    tmp.save_csv(csvname)
