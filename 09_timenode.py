import os
import pandas as pd
import numpy as np

if __name__ == '__main__':
    # path = 'D:/data2/outresult/totalavg_rm.csv'
    # resfile = "D:/data2/outresult/totalavg_rm11.csv"
    path = 'E:/avgalldiff.csv'
    resfile = "E:/avgalldiff1.csv"
    solve_time_list = list()
    delete_list = list()
    # pct_files = os.listdir(pct_path)
    # strbit_files = os.listdir(strbit_path)
    # common_files = list(set(pct_files) & set(strbit_files))
    data = pd.read_csv(path)
    title_list = data.columns.values.tolist()
    ls = list()
    print(data[title_list[0]].size)
    i=0
    while i<data[title_list[0]].size:
        l = list()
        l1 = list()
        l2 = list()
        for t in title_list:
            if 'instance' in t:
                l.append(data[t][i])
                l1.append("")
            elif '#' in t:
                l2 .append("#="+str(data[t][i]))
            elif 'algorithm' in t:
                l.append("t")
                l1.append("n")
                l2 .append("p")
            elif 'ime' in t:
                # s = data[t].mean()
                # s = data[t].sum()
                l.append(data[t][i])
            elif 'percentage' in t:
                # s = data[t].mean()
                # s = data[t].sum()
                l2.append(str(data[t][i]*100)+"%")
            else:
                # s = data[t].mean()
                # s = data[t].sum()
                l1.append(data[t][i])
        print(l)
        print(len(l))
        ls.append(l)
        ls.append(l1)
        ls.append(l2)
        i+=1
    # result.append([l], ignore_index=True)

    # # print(data.columns.values.tolist())
    #
    print('=====')

    nd = np.array(ls)
    print(nd.shape)
    result = pd.DataFrame(nd)
    print(result)
    result.to_csv(resfile,index=0)
