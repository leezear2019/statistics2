import os
import pandas as pd
import numpy as np

# 从sum中移除超时的实例
if __name__ == '__main__':
    path = "E:/avg.csv"
    res_path = "E:/avgsum.csv"

    solve_time_list = list()

    sample = "E:/avg.csv"

    data = pd.read_csv(sample)
    title_list = data.columns.values.tolist()
    print(title_list)
    print(len(title_list))
    #
    result = pd.DataFrame(columns=title_list)
    # solve time list
    for c in title_list:
        if c.startswith('Memory'):
            solve_time_list.append(c)

    print(solve_time_list)
    #
    data = pd.read_csv(path)
    #     result.append()
    #     # print(data.columns.values.tolist())
    #
    #     print('=====')
    #     print(data)
    #
    c1 = data[solve_time_list[1]]-data[solve_time_list[0]]
    c2 = data[solve_time_list[2]] - data[solve_time_list[0]]
    c3 = data[solve_time_list[3]] - data[solve_time_list[0]]
    c4 = data[solve_time_list[4]] - data[solve_time_list[0]]
    c5 = data[solve_time_list[5]] - data[solve_time_list[0]]
    c6 = data[solve_time_list[6]] - data[solve_time_list[0]]
    data[solve_time_list[1]]=c1
    data[solve_time_list[2]]=c2
    data[solve_time_list[3]]=c3
    data[solve_time_list[4]]=c4
    data[solve_time_list[5]]=c5
    data[solve_time_list[6]]=c6



    print(c1)
    #
    # print(path, data.shape)
    data.to_csv(res_path, index=0)
