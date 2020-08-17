import os
import pandas as pd
import numpy as np

# 从sum中移除超时的实例
if __name__ == '__main__':
    # root_dir = "D:/data2/out"
    # res_dir = "D:/data2/sum_rm"
    root_dir = "E:/alldiff"
    res_dir = "E:/alldiff-"
    solve_time_list = list()
    delete_list = list()
    # pct_files = os.listdir(pct_path)
    # strbit_files = os.listdir(strbit_path)
    # common_files = list(set(pct_files) & set(strbit_files))
    summary_files = sorted(os.listdir(root_dir))

    # summary_files.remove('.DS_Store')
    # print(summary_files)
    # for name in summary_files:
    # 通过
    sample = "E:/alldiff/AllInterval-m1-s1.csv"

    data = pd.read_csv(sample)
    title_list = data.columns.values.tolist()
    print(title_list)
    print(len(title_list))
    #
    result = pd.DataFrame(columns=title_list)
    # solve time list
    for c in title_list:
        if c.startswith('time'):
            solve_time_list.append(c)

    print(solve_time_list)
    #
    for name in summary_files:
        path = os.path.join(root_dir, name)
        res_path = os.path.join(res_dir, name)
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
        c1 = data[solve_time_list[0]] >= 900
        c2 = data[solve_time_list[1]] >= 900
        c3 = data[solve_time_list[2]] >= 900
        c4 = data[solve_time_list[3]] >= 900
        c5 = data[solve_time_list[4]] >= 900
        c6 = data[solve_time_list[5]] >= 900

        print(c1 & c2 & c3 & c4 & c5 & c6)
        # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
        data.drop(data[c1 & c2 & c3 & c4 & c5 & c6].index, inplace=True)
        # data.drop(data[c5].index, inplace=True)
        #
        print(name, data.shape)
        data.to_csv(res_path, index=0)
