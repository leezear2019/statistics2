import os
import pandas as pd
import numpy as np

if __name__ == '__main__':

    root_dir = "E:/LY"
    res_dir = "E:/LY.csv"
    solve_time_list = list()
    delete_list = list()
    ls = list()
    # pct_files = os.listdir(pct_path)
    # strbit_files = os.listdir(strbit_path)
    # common_files = list(set(pct_files) & set(strbit_files))
    summary_files = sorted(os.listdir(root_dir))

    # summary_files.remove('.DS_Store')
    # print(summary_files)
    # for name in summary_files:
    # 通过
    sample = "E:/LY/step1_0601.csv"
    list = [0] * 900

    data = pd.read_csv(sample)
    title_list = data.columns.values.tolist()
    print(title_list)
    print(len(title_list))
    #
    result = pd.DataFrame(columns=title_list)
    # solve time list
    for c in title_list:
        if c.startswith('SOG'):
            solve_time_list.append(c)

    print(solve_time_list)
    #
    for name in summary_files:
        path = os.path.join(root_dir, name)
        print(path)
        # name = "/Users/lizhe/Documents/exp/sum/zzdubois.csv"
        #
        data = pd.read_csv(path)
        #     result.append()
        #     # print(data.columns.values.tolist())
        #
        #     print('=====')
        #     print(data)
        #
        for i in range(0,899):
            c1=data[solve_time_list[0]]>=0.1*i
            c2=data[solve_time_list[0]]<0.1*i+0.1
            list[i]=list[i]+sum(c1&c2)


        # data.drop(data[c5].index, inplace=True)
        #
        print(name, data.shape)

    ls.append(list)
    print(list)
    nd = np.array(ls)
    print(nd.shape)
    result = pd.DataFrame(nd)
    print(result)
    result.to_csv(res_dir, index=0)