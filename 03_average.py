import os
import pandas as pd
import numpy as np

# 算不超时的实例的平均值
if __name__ == '__main__':
    # rootdir = "D:/data2/outABS"
    # resfile = "D:/data2/outABSR/avg.csv"
    # rootdir = "D:/scaladata"
    # resfile = "D:/scalaResult/avg.csv"
    # rootdir = "E:/scalaWdeg"
    # resfile = "E:/scalaWdegResult/avg.csv"
    # rootdir = "E:/chocodata1"
    # rootdir = "E:/32G/scala"
    # resfile = "E:/avg.csv"
    rootdir = "E:/alldiffp"
    resfile = "E:/avgalldi.csv"

    solve_time_list = list()
    delete_list = list()
    # pct_files = os.listdir(pct_path)
    # strbit_files = os.listdir(strbit_path)
    # common_files = list(set(pct_files) & set(strbit_files))
    summary_files = sorted(os.listdir(rootdir))

    if '.DS_Store' in summary_files:
        summary_files.remove('.DS_Store')
    # print(summary_files)
    # for name in summary_files:
    # sample = "E:/32G/scala/aim-50.csv"
    sample = "E:/alldiff/AllInterval-m1-s1.csv"

    data = pd.read_csv(sample)
    title_list = data.columns.values.tolist()
    # title_list.remove('Unnamed: 0')
    print(title_list)
    print(len(title_list))
    ls = list()
    for c in title_list:
        if c.startswith('time'):
            solve_time_list.append(c)

    for name in summary_files:
        path = os.path.join(rootdir, name)
        # name = "/Users/lizhe/Documents/exp/sum/zzdubois.csv"

        data = pd.read_csv(path)

        if len(data) is not 0:
            l = list()
            l.append(name)
            for t in title_list:
                # if 'name' not in t and 'algorithm' not in t:
                #     s = data[t].mean()
                #     l.append(s)
                if 'instance' in t:
                    pass
                elif 'algorithm' in t:
                    l.append(data[t][0])
                elif 'ime' in t:
                    c1 = data[t] >= 900
                    c=data[t] >= 0
                    s = data[t].mean()
                    # s = data[t].size
                    # l.append(sum(c))
                    # l.append(sum(c1)/sum(c))
                    l.append(round(s, 4))
                    # l.append(round(s, 5))

                else:
                    s = data[t].mean()
                    # s = data[t].size
                    l.append(int(s))
            print(l)
            print(len(l))
            ls.append(l)
        # result.append([l], ignore_index=True)

        # # print(data.columns.values.tolist())
        #
        print('=====')

    # print(ls)

    nd = np.array(ls)
    print(nd.shape)
    result = pd.DataFrame(nd,columns=title_list)
    print(result)
    result.to_csv(resfile,index=0)
    # print(data)
    #
    # for c in solve_time_list:
    #     data.drop(data[data[c] >= 900].index, inplace=True)
    #     # data = [data[c] < 900]
    #     # data = data.reset_index(drop=True)
    # #
    # # train_old = train_old[~(train_old['month'].isin([6]) & (train_old['day'].isin([26])))]
    # #
    # # train_old = train_old.reset_index(drop=True)
    #
    # print(data)
    # data.to_csv(resfile)
