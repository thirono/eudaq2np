import numpy as np
from eudaq2np import data_np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    data = data_np("run071066.raw", "EUDRB")    
    print 'DATA:', data.dtype, data.shape    

    fig = plt.gcf()

    print np.unique(data['plane'])
    for i in range(6):
      plane = data[np.equal(data['plane'], i)]
      print 'plane ', i, plane.shape
      H, xedges, yedges = np.histogram2d(plane['x'].astype(int), plane['y'].astype(int), bins=(1152, 576))
 
      plt.subplot(2,3,i)
      plt.title('Plane '+str(i))
      plt.imshow(H, cmap=plt.cm.jet, interpolation='nearest')
      plt.colorbar()
      plt.clim(0,10)

    plt.show()
