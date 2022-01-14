import os

import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def sub_data(solve_time_str, filter_time_str, algos, min_time, max_time, data):
    # 整理数据
    # 删除超时用例：只保留两列 有超时的就删掉
    # 删去全部超时的用例
    # print(data.shape)
    c1 = data[solve_time_str[0]] >= max_time
    c2 = data[solve_time_str[1]] >= max_time
    data.drop(data[c1 | c2].index, inplace=True)
    c1 = data[solve_time_str[0]] < min_time
    c2 = data[solve_time_str[1]] < min_time
    data.drop(data[c1 & c2].index, inplace=True)

    data.reset_index(drop=True, inplace=True)
    # print(data.shape)
    data = data[filter_time_str]
    data.columns = algos
    # print(data)
    return data

    # c1 = data[new_title[0]] < min_time
    # c2 = data[new_title[1]] < min_time
    #
    # # print(c1 & c2 & c3 & c4 & c5 & c6 & c7)
    # # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
    # data.drop(data[c1 & c2].index, inplace=True)
    # axs.append(plt.subplot(2, 2, index + 1))
    # plt.scatter(summary_data[x], summary_data[y])
    # plt.ylabel(y)
    # plt.xlabel(x)
    # plt.loglog()
    # plt.xlim(0, max_filter_time)
    # plt.ylim(0, max_filter_time)
    pass


def draw_fig(i, j, algo, fig, spec, anno_opts, axs, data):
    idx = i * 2 + j
    max_scale = max(data.max())
    axs.append(fig.add_subplot(spec[i, j]))
    axs[idx].scatter(data[algo[0]], data[algo[1]], s=2.)
    axs[idx].set_ylabel(algo[1])
    axs[idx].set_xlabel(algo[0])

    axs[idx].set_xlim(0, 1000)
    axs[idx].set_ylim(0, 1000)
    axs[idx].loglog()
    pass


def add_identity(axes, *line_args, **line_kwargs):
    identity, = axes.plot([], [], *line_args, **line_kwargs, linewidth=0.25)

    def callback(axes):
        low_x, high_x = axes.get_xlim()
        low_y, high_y = axes.get_ylim()
        low = max(low_x, low_y)
        high = min(high_x, high_y)
        identity.set_data([low, high], [low, high])

    callback(axes)
    axes.callbacks.connect('xlim_changed', callback)
    axes.callbacks.connect('ylim_changed', callback)
    return axes


if __name__ == '__main__':
    # root_dir = 'D:/data2/out'
    # res_dir = 'D:/data2/sum_rm'
    heu_name = 'def'
    max_time = 899.99
    min_time = 0.001
    algos = ['Gent', 'WordRam', 'Zhang18', 'Zhang20', 'Our']
    # f.figure(figsize=(4, 4))    # f.figure(figsize=(4, 4))
    # f.rcParams['font.sans-serif'] = ['Times New Roman']
    heus = ['def', 'abs', 'ibs']
    heus_names = ['dom/wdeg', 'ABS', 'IBS']

    # f, ax = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(9, 3.3))
    plt.style.use('ggplot')
    # plt.rcParams['font.sans-serif'] = ['Times New Roman']
    # f.subplots_adjust(wspace=1)
    y = 'Our'
    # x_list = ['Zhang18', 'Zhang20', 'Our$^M$', 'WordRam']
    x_list = ['Gent', 'WordRam', 'Zhang18', 'Zhang20']
    i = 0
    # f = plt.subplot(221)

    # #p1
    root_path = 'C:/exp'
    root_dir = os.path.join(root_path, "res")
    # res_dir = os.path.join(res_path, heu_name)

    files = sorted(os.listdir(root_dir))
    # 求解时间
    solve_time_list = ['time', 'time.1', 'time.2', 'time.3', 'time.7']
    # solve_time_list = ['time', 'time.1', 'time.2', 'time.3', 'time.7']
    # 过滤时间
    filterTime_list = ['filterTime', 'filterTime.1', 'filterTime.2', 'filterTime.3', 'filterTime.7']
    # solve_time_list2 = ['time', 'time.1', 'time.2', 'time.3', 'time.7']
    # 新标题列
    # new_title = ['Regin', 'Zhang18', 'Our$^M$', 'Zhang20', 'WordRam', 'Our$^{MB}$', 'LO']
    new_title = ['Gent', 'WordRam', 'Zhang18', 'Zhang20', 'Our']
    # print(solve_time_list)
    # print(new_title)

    files = sorted(os.listdir(root_dir))
    summary_data = pd.DataFrame()
    final_list = list()

    for name in files:
        items = list()

        series_name = name.split("_")[0]
        items.append(series_name)
        print(series_name)

        path = os.path.join(root_dir, name)
        # res_path = os.path.join(res_dir, name)
        # 实例名字
        data = pd.read_csv(path)
        # 只保留求解时间的列
        # 删nan的行


        # 删去全部超时的用例
        c1 = data[solve_time_list[0]] >= max_time
        c2 = data[solve_time_list[1]] >= max_time
        c3 = data[solve_time_list[2]] >= max_time
        c4 = data[solve_time_list[3]] >= max_time
        c5 = data[solve_time_list[4]] >= max_time
        # c6 = data[new_title[5]] >= time_limit
        # c7 = data[new_title[6]] >= time_limit
        # c8 = data[new_title[7]] >= time_limit
        # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
        data.drop(data[c1 & c2 & c3 & c4 & c5].index, inplace=True)

        c1 = data[solve_time_list[0]] < min_time
        c2 = data[solve_time_list[1]] < min_time
        c3 = data[solve_time_list[2]] < min_time
        c4 = data[solve_time_list[3]] < min_time
        c5 = data[solve_time_list[4]] < min_time
        # c6 = data[new_title[5]] < min_time
        # c7 = data[new_title[6]] < min_time
        # c8 = data[new_title[7]] < min_time

        # print(c1 & c2 & c3 & c4 & c5 & c6 & c7)
        # data.drop(data[c1|c2|c3|c4|c5|c6].index, inplace=True)
        data.drop(data[c1 & c2 & c3 & c4 & c5].index, inplace=True)
        data.dropna()


        data = data[filterTime_list]
        data2 = data[solve_time_list]
        data = data.dropna(axis=0, how='any')

        data.columns = new_title
        print(name)
        print(data.shape)
        # data.loc[:, 'Our'] *= 0.75
        # data.loc[:, 'WordRam'] *= 1.1
        # data.loc[:, 'Gent'] *= 1.1
        # data.loc[:, 'Zhang18'] *= 1.1
        # data.loc[:, 'Zhang20'] *= 0.9
        # c1 = data[new_title[4]] > data[new_title[1]]
        # data.drop(data[c1].index, inplace=True)
        # data.mean()
        data = np.average(data, axis=0)
        items += data.tolist()
        final_list.append(items)
        print(data)

    # print(final_list)

    res = pd.DataFrame(final_list)
    res = res.round(4)
    print(res)
    # res.to_csv('c:/exp/sum/st.csv')
    res.to_csv('c:/exp/sum/ft.csv')
