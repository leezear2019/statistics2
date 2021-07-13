import os

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
    max_time = 899.9
    min_time = 0.01
    algos = ['Fair', 'Zhang18', 'Zhang20', 'WordRam', 'OurMB']
    # f.figure(figsize=(4, 4))    # f.figure(figsize=(4, 4))
    # f.rcParams['font.sans-serif'] = ['Times New Roman']
    heus = ['def', 'abs', 'ibs']
    heus_names = ['dom/wdeg', 'ABS', 'IBS']

    # f, ax = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(9, 3.3))
    plt.style.use('ggplot')
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    # f.subplots_adjust(wspace=1)
    y = 'OurMB'
    x_list = ['Fair', 'Zhang18', 'Zhang20', 'WordRam']
    i = 0
    # f = plt.subplot(221)

    # #p1
    root_path = 'D:/exp'
    res_path = 'D:/exp/per'
    root_dir = os.path.join(root_path, heu_name)
    res_dir = os.path.join(res_path, heu_name)

    files = sorted(os.listdir(root_dir))
    # 求解时间
    solve_time_list = ['time', 'time.1', 'time.2', 'time.3', 'time.4', 'time.5', 'time.6', 'time.7']
    # 过滤时间
    filterTime_list = ['filterTime', 'filterTime.1', 'filterTime.2', 'filterTime.3', 'filterTime.4', 'filterTime.5',
                       'filterTime.6', 'filterTime.7']
    # 新标题列
    new_title = ['Choco', 'Fair', 'Zhang18', 'OurM', 'Zhang20', 'OurMB', 'LO', 'WordRam']
    # print(solve_time_list)
    # print(new_title)

    files = sorted(os.listdir(root_dir))
    summary_data = pd.DataFrame()

    for name in files:
        path = os.path.join(root_dir, name)
        # 实例名字
        data = pd.read_csv(path)
        # 删nan的行
        data = data.dropna(axis=0, how='any')
        # 加入summary_data
        summary_data = summary_data.append(data, ignore_index=True)

    # print('------------------')
    # print(summary_data.shape)
    # print(summary_data)

    compare_idx = [2, 7, 5]
    axs = list()
    ds = list()
    ts = list()
    max_filtering_time = 0
    dest_idx = 2

    for i in range(2):
        algo = [new_title[compare_idx[i]], new_title[compare_idx[dest_idx]]]
        ts.append(algo)
        solve_time_str = [solve_time_list[compare_idx[i]], solve_time_list[compare_idx[dest_idx]]]
        filter_time_str = [filterTime_list[compare_idx[i]], filterTime_list[compare_idx[dest_idx]]]
        ds.append(sub_data(solve_time_str, filter_time_str, algo, min_time, max_time, summary_data))

    # 绘图
    # fig = plt.figure( figsize=(6.2, 6)   )
    # spec = fig.add_gridspec(ncols=2, nrows=2)
    # anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
    #                  va='center', ha='center')
    # for i in range(2):
    #     for j in range(2):
    #         draw_fig(i, j, ts[i], fig, spec,anno_opts, axs, ds[i])

    f, ax = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(8, 4))
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    f.subplots_adjust()
    plt.ylim(0.0001, 600)
    plt.xlim(0.0001, 600)
    plt.xscale('log', base=10)
    plt.yscale('log', base=10)

    # plt.xticks(rotation = 90)

    for i in range(2):
        idx = i
        algo = ts[idx]
        ax[i].scatter(ds[idx][algo[0]], ds[idx][algo[1]], s=0.25)
        ax[i].set_xlabel(algo[0])
        ax[i].set_ylabel(algo[1])
        # ax[i][j].set_xlim(0,60000)
        # ax[i][j].set_ylim(0,60000)
        # add_identity(ax[i][j], color='g', ls='--')
        # add_identity(ax[i][j], color='g', ls='--')
        ax[i].plot(ax[i].get_xlim(), ax[i].get_ylim(), color='g', ls='--')
        # ax[i].tick_params(axis='x', rotation=45)
        # diag_line, = ax[i][j].plot(ax[i][j].get_xlim(), ax[i][j].get_ylim(), ls="--", c=".3")

    # plt.loglog()
    # plt.xlim(min_time / 10, time_limit)
    plt.tight_layout()
    # plt.subplots_adjust(wspace=0)
    # f.title('Average No Of Independent Candidates by Constituency Type')

    plt.show()

    # f = plt.figure()

    # print(summary_data)
    # for i in range(len(x_list)):
    #     sub_fig(i, axs, time_limit, min_time, heus[0], heus_names[0], algos[i], y)

    # sub_fig(heus[0], f, ax[0][0], time_limit, min_time, heus_names[0])
    # sub_fig(heus[1], f, ax[0][1], time_limit, min_time, heus_names[1])
    # sub_fig(heus[2], f, ax[1][0], time_limit, min_time, heus_names[2])

    # plt.legend()
    # f.legend(new_title, bbox_to_anchor=(0.95, 0.9), ncol=5, fontsize=10.5)
    # plt.legend(fontsize=10)
    # plt.figlegend(loc = 'upper center', ncol=5 )
    # f.legend(new_title, loc = 'lower center', ncol=5)
    # f.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0.)
    # f.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
    # ncol=2, mode="expand", borderaxespad=0.)
    # f.tight_layout()
    # plt.legend()
    # plt.semilogx()
    # plt.ylim(0, 230)
    # plt.xlim(min_time / 10, time_limit)
    # plt.tight_layout()
    # # f.title('Average No Of Independent Candidates by Constituency Type')
    # plt.show()
