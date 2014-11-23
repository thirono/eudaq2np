import numpy as np
from eudaq2np import data_np
import matplotlib.pyplot as plt

if __name__ == "__main__":

#    data = data_np("/home/silab/eudaq-1.4-dev/data/run000017.raw", "EPCB01") # a run with only espros data
    data = data_np("/home/silab/Downloads/run071060.raw", "EUDRB") # a run with mimosa data

    fig = plt.figure('Mimosa hitmaps', figsize=(8, 6))
    fig.patch.set_facecolor('white')
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

    # 0 mit 1,2,3,4,5
    corr_hist_01_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_01_y = np.zeros((576, 576), dtype=np.float)
    corr_hist_02_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_02_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_03_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_03_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_04_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_04_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_05_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_05_y = np.zeros((576, 576), dtype=np.float)   
    # 1 mit 2,3,4,5
    corr_hist_12_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_12_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_13_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_13_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_14_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_14_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_15_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_15_y = np.zeros((576, 576), dtype=np.float)   
    # 2 mit 3,4,5
    corr_hist_23_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_23_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_24_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_24_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_25_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_25_y = np.zeros((576, 576), dtype=np.float)   
    # 3 mit 4,5
    corr_hist_34_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_34_y = np.zeros((576, 576), dtype=np.float)   
    corr_hist_35_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_35_y = np.zeros((576, 576), dtype=np.float)   
    # 4 mit 5
    corr_hist_45_x = np.zeros((1152, 1152), dtype=np.float)    
    corr_hist_45_y = np.zeros((576, 576), dtype=np.float)
    
    print 'Data tluevent ', data['tluevent'].astype(int)

    # make all correlation plots of mimosas
    # get all trigger numbers 

    event_numbers = np.unique(data['tluevent'].astype(int))
    print 'event number = ', event_numbers, 'len = ', len(event_numbers)

    plane_0 = data[np.equal(data['plane'], 0)]
    plane_1 = data[np.equal(data['plane'], 1)]
    plane_2 = data[np.equal(data['plane'], 2)]
    plane_3 = data[np.equal(data['plane'], 3)]
    plane_4 = data[np.equal(data['plane'], 4)]
    plane_5 = data[np.equal(data['plane'], 5)]
   

#    for event in event_numbers:
    for event in event_numbers[0:100]:
#        print 'event plane 0', plane_0[np.equal(plane_0['tluevent'],event)]
        plane_0_x_values = plane_0[np.equal(plane_0['tluevent'],event)]['x']
        plane_0_y_values = plane_0[np.equal(plane_0['tluevent'],event)]['y']
        plane_1_x_values = plane_1[np.equal(plane_1['tluevent'],event)]['x']
        plane_1_y_values = plane_1[np.equal(plane_1['tluevent'],event)]['y']
        plane_2_x_values = plane_2[np.equal(plane_2['tluevent'],event)]['x']
        plane_2_y_values = plane_2[np.equal(plane_2['tluevent'],event)]['y']
        plane_3_x_values = plane_3[np.equal(plane_3['tluevent'],event)]['x']
        plane_3_y_values = plane_3[np.equal(plane_3['tluevent'],event)]['y']
        plane_4_x_values = plane_4[np.equal(plane_4['tluevent'],event)]['x']
        plane_4_y_values = plane_4[np.equal(plane_4['tluevent'],event)]['y']
        plane_5_x_values = plane_5[np.equal(plane_5['tluevent'],event)]['x']
        plane_5_y_values = plane_5[np.equal(plane_5['tluevent'],event)]['y']

#        print 'plane 0 x coordinates ', plane_0[np.equal(plane_0['tluevent'],event)]['x']
#        print 'plane 1 x coordinates ', plane_1[np.equal(plane_1['tluevent'],event)]['x']
        
        # plane 0 mit 1, 2,3,4,5
        for it_0 in range(0,len(plane_0_x_values)):
#            print 'it_0', it_0
            for it_1 in range(0,len(plane_1_x_values)):
#                print 'it_1', it_1
                corr_hist_01_x[plane_0_x_values[it_0]][plane_1_x_values[it_1]]+=1
                corr_hist_01_y[plane_0_y_values[it_0]][plane_1_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_2_x_values)):
                corr_hist_02_x[plane_0_x_values[it_0]][plane_2_x_values[it_1]]+=1
                corr_hist_02_y[plane_0_y_values[it_0]][plane_2_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_3_x_values)):
                corr_hist_03_x[plane_0_x_values[it_0]][plane_3_x_values[it_1]]+=1
                corr_hist_03_y[plane_0_y_values[it_0]][plane_3_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_4_x_values)):                
                corr_hist_04_x[plane_0_x_values[it_0]][plane_4_x_values[it_1]]+=1
                corr_hist_04_y[plane_0_y_values[it_0]][plane_4_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_5_x_values)):
                corr_hist_05_x[plane_0_x_values[it_0]][plane_5_x_values[it_1]]+=1
                corr_hist_05_y[plane_0_y_values[it_0]][plane_5_y_values[it_1]]+=1

        # plane 1 mit 2,3,4,5
        for it_0 in range(0,len(plane_1_x_values)):
#            print 'it_0', it_0
            for it_1 in range(0,len(plane_2_x_values)):
                corr_hist_12_x[plane_1_x_values[it_0]][plane_2_x_values[it_1]]+=1
                corr_hist_12_y[plane_1_y_values[it_0]][plane_2_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_3_x_values)):
                corr_hist_13_x[plane_1_x_values[it_0]][plane_3_x_values[it_1]]+=1
                corr_hist_13_y[plane_1_y_values[it_0]][plane_3_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_4_x_values)):
                corr_hist_14_x[plane_1_x_values[it_0]][plane_4_x_values[it_1]]+=1
                corr_hist_14_y[plane_1_y_values[it_0]][plane_4_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_5_x_values)):
                corr_hist_15_x[plane_1_x_values[it_0]][plane_5_x_values[it_1]]+=1
                corr_hist_15_y[plane_1_y_values[it_0]][plane_5_y_values[it_1]]+=1

        # plane 2 mit 3,4,5
        for it_0 in range(0,len(plane_2_x_values)):
#            print 'it_0', it_0
            for it_1 in range(0,len(plane_3_x_values)):
                corr_hist_23_x[plane_2_x_values[it_0]][plane_3_x_values[it_1]]+=1
                corr_hist_23_y[plane_2_y_values[it_0]][plane_3_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_4_x_values)):
                corr_hist_24_x[plane_2_x_values[it_0]][plane_4_x_values[it_1]]+=1
                corr_hist_24_y[plane_2_y_values[it_0]][plane_4_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_5_x_values)):
                corr_hist_25_x[plane_2_x_values[it_0]][plane_5_x_values[it_1]]+=1
                corr_hist_25_y[plane_2_y_values[it_0]][plane_5_y_values[it_1]]+=1
                
        # plane 3 mit 4,5
        for it_0 in range(0,len(plane_3_x_values)):
#            print 'it_0', it_0
            for it_1 in range(0,len(plane_4_x_values)):
                corr_hist_34_x[plane_3_x_values[it_0]][plane_4_x_values[it_1]]+=1
                corr_hist_34_y[plane_3_y_values[it_0]][plane_4_y_values[it_1]]+=1
            for it_1 in range(0,len(plane_5_x_values)):
                corr_hist_35_x[plane_3_x_values[it_0]][plane_5_x_values[it_1]]+=1
                corr_hist_35_y[plane_3_y_values[it_0]][plane_5_y_values[it_1]]+=1

        # plane 3 mit 4,5
        for it_0 in range(0,len(plane_4_x_values)):
#            print 'it_0', it_0
            for it_1 in range(0,len(plane_5_x_values)):                
                corr_hist_45_x[plane_4_x_values[it_0]][plane_5_x_values[it_1]]+=1
                corr_hist_45_y[plane_4_y_values[it_0]][plane_5_y_values[it_1]]+=1
    
    
    fig = plt.figure('Plane 0 Correlations', figsize=(15, 6))
    fig.patch.set_facecolor('white')
    plt.subplot(2,5,1)
    plt.title('0-1 x')
    plt.imshow(corr_hist_01_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,6)
    plt.title('0-1 y')
    plt.imshow(corr_hist_01_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,2)
    plt.title('0-2 x')
    plt.imshow(corr_hist_02_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,7)
    plt.title('0-2 y')
    plt.imshow(corr_hist_02_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,3)
    plt.title('0-3 x')
    plt.imshow(corr_hist_03_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,8)
    plt.title('0-3 y')
    plt.imshow(corr_hist_03_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,4)
    plt.title('0-4 x')
    plt.imshow(corr_hist_04_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,9)
    plt.title('0-4 y')
    plt.imshow(corr_hist_04_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,5)
    plt.title('0-5 x')
    plt.imshow(corr_hist_05_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,5,10)
    plt.title('0-5 y')
    plt.imshow(corr_hist_05_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.savefig('Plane_0_correlations.png')
    plt.show()


    fig = plt.figure('Plane 1 Correlations', figsize=(12, 6))
    fig.patch.set_facecolor('white')
    plt.subplot(2,4,1)
    plt.title('1-2 x')
    plt.imshow(corr_hist_12_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,4,5)
    plt.title('1-2 y')
    plt.imshow(corr_hist_12_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,4,2)
    plt.title('1-3 x')
    plt.imshow(corr_hist_13_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,4,6)
    plt.title('1-3 y')
    plt.imshow(corr_hist_13_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,4,3)
    plt.title('1-4 x')
    plt.imshow(corr_hist_14_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,4,7)
    plt.title('1-4 y')
    plt.imshow(corr_hist_14_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,4,4)
    plt.title('1-5 x')
    plt.imshow(corr_hist_15_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,4,8)
    plt.title('1-5 y')
    plt.imshow(corr_hist_15_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.savefig('Plane_1_correlations.png')
    plt.show()


    fig = plt.figure('Plane 2 Correlations', figsize=(9, 6))
    fig.patch.set_facecolor('white')
    plt.subplot(2,3,1)
    plt.title('2-3 x')
    plt.imshow(corr_hist_23_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,3,4)
    plt.title('2-3 y')
    plt.imshow(corr_hist_23_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,3,2)
    plt.title('2-4 x')
    plt.imshow(corr_hist_24_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,3,5)
    plt.title('2-4 y')
    plt.imshow(corr_hist_24_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,3,3)
    plt.title('2-5 x')
    plt.imshow(corr_hist_25_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,3,6)
    plt.title('2-5 y')
    plt.imshow(corr_hist_25_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.savefig('Plane_2_correlations.png')
    plt.show()

    fig = plt.figure('Plane 3 Correlations', figsize=(6, 6))
    fig.patch.set_facecolor('white')
    plt.subplot(2,2,1)
    plt.title('3-4 x')
    plt.imshow(corr_hist_34_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,2,3)
    plt.title('3-4 y')
    plt.imshow(corr_hist_34_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,2,2)
    plt.title('4-5 x')
    plt.imshow(corr_hist_35_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,2,4)
    plt.title('4-5 y')
    plt.imshow(corr_hist_35_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.savefig('Plane_3_correlations.png')
    plt.show()

    fig = plt.figure('Plane 4 Correlations', figsize=(3, 6))
    fig.patch.set_facecolor('white')
    plt.subplot(2,1,1)
    plt.title('4-5 x')
    plt.imshow(corr_hist_45_x, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.subplot(2,1,2)
    plt.title('4-5 y')
    plt.imshow(corr_hist_45_y, cmap=plt.cm.jet, interpolation='nearest')
    plt.colorbar()
    plt.clim(0,10)
    plt.savefig('Plane_4_correlations.png')
    plt.show()
