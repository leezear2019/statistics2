import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def printme(root_dir, res_dir):
    summary_files = sorted(os.listdir(root_dir))
    print(summary_files)

    for name in summary_files:
        path = os.path.join(root_dir, name)
        res_path = os.path.join(res_dir, name)
        print(path)
        data = pd.read_csv(path)
        data = data.loc[:, list(data.columns)[53:79]]
        print(data)
        data.to_csv(res_path, index=0)


def removeTimeOut(root_dir, res_dir, time_limit, solve_time_list):
    print(solve_time_list)
    summary_files = sorted(os.listdir(res_dir))

    for name in summary_files:
        path = os.path.join(res_dir, name)
        res_path = os.path.join(res_dir, name)
        print(path)
        data = pd.read_csv(path)

        c1 = data[solve_time_list[0]] >= time_limit
        c2 = data[solve_time_list[1]] >= time_limit

        data.drop(data[c1 | c2].index, inplace=True)

        print(name, data.shape)
        data.to_csv(res_path, index=0)


def reduce_table(root_dir, res_dir):
    summary_files = sorted(os.listdir(root_dir))

    for name in summary_files:
        path = os.path.join(root_dir, name)
        res_path = os.path.join(res_dir, name)
        # print(path)
        data = pd.read_csv(path)

        # 删除无用列
        d = data.drop(data.columns[[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]], axis=1)
        # 重命名列
        d.columns = ['numProp', 'numNone', 'numSkip', 'numP1', 'numP2', 'numP1AndP2']
        # p1 p2各减p1&p2
        d['numP1'] = d['numP1'] - d['numP1AndP2']
        d['numP2'] = d['numP2'] - d['numP1AndP2']
        # 除以numProp求百分比
        # d = d / d['numProp']
        d = d.div(d.numProp, axis='index')
        # 交换'numP2', 'numP1AndP2'两列
        cols = list(d)
        cols.insert(4, cols.pop(cols.index('numP1AndP2')))
        d = d.loc[:, cols]
        d = d.drop(d.columns[[0]], axis=1)
        # 保存
        d.to_csv(res_path, index=0)


def phase_mean(root_dir, res_dir, heu_name):
    root_path = os.path.join(root_dir, heu_name)
    summary_files = sorted(os.listdir(root_path))
    output_name = os.path.join(root_dir, 'summary_' + heu_name + '.csv')
    print(output_name)
    ls = list()
    names = list()

    for name in summary_files:
        l = list()
        path = os.path.join(root_path, name)
        # res_path = os.path.join(res_dir, name)
        # 实例名字
        data = pd.read_csv(path)
        title_list = data.columns.values.tolist()
        series_name = os.path.split(path)[1].split('_')[0]
        # print(series_name)
        names.append(series_name)
        # l.append(series_name)
        for t in title_list:
            s = data[t].mean()
            l.append(s)

        ls.append(l)
        # data = pd.read_csv(path)

    nd = np.array(ls).transpose()
    print(nd)
    print(nd.shape)
    # title_list = ['series'] + title_list
    print(title_list)
    # result = pd.DataFrame(nd, columns=title_list)
    # print(names)
    # print(result)
    # y = len(nd.shape[0])
    x = np.arange(nd.shape[1])
    plt.bar(x, nd[0], width=0.5, label=title_list[0])
    nds = nd[0]

    for i in range(1, nd.shape[0]):
        plt.bar(x, nd[i], bottom=nds, width=0.5, label=title_list[i])
        nds = nds + nd[i]

    #
    # plt.bar(x, nd[0], width=0.5, label='a')
    # plt.bar(x, nd[1], bottom=nd[0], width=0.5, label='b')
    # plt.bar(x, nd[1], bottom=nd[0:1], width=0.5, label='c')
    plt.ylim(0, 1)
    plt.rcParams['font.sans-serif']=['Times New Roman']
    plt.xticks(range(nd.shape[1]), names)
    plt.xlabel('Series')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    heu_name = 'def'
    # #p1
    root_dir = 'D:/exp'
    res_dir = 'D:/exp/per'
    root_dir = os.path.join(root_dir, heu_name)
    res_dir = os.path.join(res_dir, heu_name)
    # time_limit = 900
    #
    # printme(root_dir, res_dir)
    #
    # #p2
    # solve_time_list = list()
    # sample = "D:\exp\per\def\AllInterval_DEFAULT_2020-08-07_21_03_27.csv"
    #
    # data = pd.read_csv(sample)
    # title_list = data.columns.values.tolist()
    # print(title_list)
    # print(len(title_list))
    # #
    # result = pd.DataFrame(columns=title_list)
    # # solve time list
    # for c in title_list:
    #     if c.startswith('time'):
    #         solve_time_list.append(c)
    #
    # print(solve_time_list)
    #
    # removeTimeOut(root_dir, res_dir, time_limit, solve_time_list)

    # # p3
    # # root_dir = R"D:\exp\per\def"
    # # res_dir = R"D:\exp\5p\def"
    # root_dir = 'D:/exp/per'
    # res_dir = 'D:/exp/5p'
    # root_dir = os.path.join(root_dir, heu_name)
    # res_dir = os.path.join(res_dir, heu_name)
    # # 去掉不用的列
    # reduce_table(root_dir, res_dir)
    # # # 算百分比
    # # calculate_percentage(root_dir, res_dir)

    root_dir = 'D:/exp/5p'
    res_dir = 'D:/exp/5p'

    # 统计再算平均值
    phase_mean(root_dir, res_dir, heu_name)
