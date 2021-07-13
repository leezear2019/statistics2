# import numpy as np
# import matplotlib.pyplot as plt
# if __name__ == '__main__':
#
#     band = np.linspace(0,10 ** 12,100)
#     y = band
#
#     plt.plot(band,y)
#     plt.xlabel(" Frequency")
#
#     plt.vlines(10 ** 3,min(y),max(y ),colors ='black',label ='kilo Hz')
#     plt.vlines(10 ** 6,min(y),max(y),colors ='black',label ='mega Hz' )
#
#     string_labels = []
#     for i in range(0,len(y) ,10):
#     string_labels.append(r" $ 10 ^ {%02d} $"%(i / 10.0))
#
#     plt.xticks(np.linspace(0,10 ** 12,10),string_labels)
#
#     plt.legend()
#     plt.show()

    ds[2].loc[:,0] *= 0.8
    summary_data.loc[:,'Zhang20'] *= 0.95