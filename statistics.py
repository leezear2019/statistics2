import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

first_ax = plt.axes()
n = np.linspace(0, 220)


def sub_fig(index, heu_name, time_limit, min_time, h_name, f):
    print(heu_name)
    # #p1
    root_path = 'D:/exp'
    res_path = 'D:/exp/per'
    root_dir = os.path.join(root_path, heu_name)
    res_dir = os.path.join(res_path, heu_name)

    summary_files = sorted(os.listdir(root_dir))
    # 保留列
    solve_time_list = ['filterTime', 'filterTime.1', 'filterTime.2', 'filterTime.3', 'filterTime.4', 'time.5', 'time.6', 'time.7']
    # 新标题列
    new_title = ['Choco', 'Regin', 'Zhang18', 'OurM', 'Zhang20', 'OurMB', 'LO', 'WordRam']
    print(solve_time_list)
    print(new_title)
    summary_files = sorted(os.listdir(root_dir))

    summary_data = pd.DataFrame(columns=new_title)

    for name in summary_files:
        path = os.path.join(root_dir, name)
        # res_path = os.path.join(res_dir, name)
        # 实例名字
        data = pd.read_csv(path)
        # 只保留求解时间的列
        # 删nan的行
        data = data[solve_time_list]
        data = data.dropna(axis=0, how='any')
        data.columns = new_title
        # print(name)
        # print(data.shape)

        # 删去全部超时的用例
        c1 = data[new_title[0]] >= time_limit
        c2 = data[new_title[1]] >= time_limit
        c3 = data[new_title[2]] >= time_limit
        c4 = data[new_title[3]] >= time_limit
        c5 = data[new_title[4]] >= time_limit
        c6 = data[new_title[5]] >= time_limit
        c7 = data[new_title[6]] >= time_limit
        c8 = data[new_title[7]] >= time_limit
        # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
        data.drop(data[c1 & c2 & c3 & c4 & c5 & c6 & c7 & c8].index, inplace=True)

        c1 = data[new_title[0]] < min_time
        c2 = data[new_title[1]] < min_time
        c3 = data[new_title[2]] < min_time
        c4 = data[new_title[3]] < min_time
        c5 = data[new_title[4]] < min_time
        c6 = data[new_title[5]] < min_time
        c7 = data[new_title[6]] < min_time
        c8 = data[new_title[7]] < min_time

        # print(c1 & c2 & c3 & c4 & c5 & c6 & c7)
        # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
        data.drop(data[c1 & c2 & c3 & c4 & c5 & c6 & c7 & c8].index, inplace=True)

        # print(data)
        # print(data.shape)
        summary_data = summary_data.append(data, ignore_index=True)
        # d = data.apply(lambda x: x.sort_values().values)
        # pandas.concat([df[col].order().reset_index(drop=True) for col in df], axis=1, ignore_index=True)
        # print(d)
    print('-------------')
    #
    # #显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    print(summary_data.shape)
    summary_data = summary_data.drop('Fair', 1)
    summary_data = summary_data.drop('OurM', 1)
    new_title.remove('Fair')
    new_title.remove('OurM')
    # summary_data = summary_data.apply(lambda x: x.sort_values().values)

    # print(summary_data)

    # 保存
    print('-------------')
    # data.to_csv(res_path, index=0)
    # 绘图
    print('-------------')


if __name__ == '__main__':
    # root_path = 'D:/exp'
    # res_path = 'D:/exp/per'
    time_limit = 899.999
    min_time = 0.001
    # summary_files = sorted(os.listdir(root_dir))
    # 保留列
    solve_time_list = ['instance', 'time', 'time.1', 'time.2', 'time.3', 'time.4']
    # 新标题列
    new_title = ['instance','Regin', 'Zhang18', 'Zhang20', 'WordRam', 'OurMB']
    print(solve_time_list)
    print(new_title)
    # summary_files = sorted(os.listdir(root_dir))
    #
    # summary_data = pd.DataFrame(columns=new_title)
    #
    # for name in summary_files:
    #     path = os.path.join(root_dir, name)
    # res_path = os.path.join(res_dir, name)
    # 实例名字
    series_name = ""
    # data = pd.read_csv("D:\exp\large\LantinSquare.csv")
    # data = pd.read_csv("D:\exp\large\CostasArrays.csv")
    data = pd.read_csv("D:\exp\large\MagicSquare.csv")
    # 只保留求解时间的列
    # 删nan的行
    data = data[solve_time_list]
    data = data.dropna(axis=0, how='any')
    data.columns = new_title
    summary_data = pd.DataFrame(columns=new_title)
    # print(name)
    # print(data.shape)

    # 删去全部超时的用例
    c1 = data[new_title[1]] >= time_limit
    c2 = data[new_title[2]] >= time_limit
    c3 = data[new_title[3]] >= time_limit
    c4 = data[new_title[4]] >= time_limit
    c5 = data[new_title[5]] >= time_limit
    # c6 = data[new_title[5]] >= time_limit
    # c7 = data[new_title[6]] >= time_limit
    # c8 = data[new_title[7]] >= time_limit
    # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
    # data.drop(data[c1 & c2 & c3 & c4 & c5 & c6 & c7 & c8].index, inplace=True)
    data.drop(data[c1 & c2 & c3 & c4 & c5].index, inplace=True)

    c1 = data[new_title[1]] < min_time
    c2 = data[new_title[2]] < min_time
    c3 = data[new_title[3]] < min_time
    c4 = data[new_title[4]] < min_time
    c5 = data[new_title[5]] < min_time
    # c6 = data[new_title[5]] < min_time
    # c7 = data[new_title[6]] < min_time
    # c8 = data[new_title[7]] < min_time

    # print(c1 & c2 & c3 & c4 & c5 & c6 & c7)
    # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
    # data.drop(data[c1 & c2 & c3 & c4 & c5 & c6 & c7 & c8].index, inplace=True)
    data.drop(data[c1 & c2 & c3 & c4 & c5].index, inplace=True)

    # c1 = data["Zhang18"] <= data["Zhang20"]
    # data.drop(data[c1].index, inplace=True)
    # print(data)
    # print(data.shape)
    # data.to_csv("D:\exp\large\Solve_LantinSquare2.csv", index=0)
    # data.to_csv("D:\exp\large\Solve_CostasArrays2.csv", index=0)
    data.to_csv("D:\exp\large\Solve_MagicSquare2.csv", index=0)
    # data.to_csv("D:\exp\large\Filter_MagicSquare2.csv", index=0)
    # data = pd.read_csv("D:\exp\large\MagicSquare.csv")
    # d = data.apply(lambda x: x.sort_values().values)
    # pandas.concat([df[col].order().reset_index(drop=True) for col in df], axis=1, ignore_index=True)
    # print(d)
