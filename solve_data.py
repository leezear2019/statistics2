import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def sub_fig(heu_name, f, ax, time_limit, min_time, h_name):
    print(heu_name)
    # #p1
    root_path = 'D:/exp'
    res_path = 'D:/exp/per'
    root_dir = os.path.join(root_path, heu_name)
    res_dir = os.path.join(res_path, heu_name)

    summary_files = sorted(os.listdir(root_dir))
    # 保留列
    solve_time_list = ['time', 'time.1', 'time.2', 'time.3', 'time.4', 'time.5', 'time.6', 'time.7']
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
        # print(data)
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
    summary_data = summary_data.drop('Choco', 1)
    summary_data = summary_data.drop('OurM', 1)
    new_title.remove('Choco')
    new_title.remove('OurM')
    summary_data = summary_data.apply(lambda x: x.sort_values().values)

    # print(summary_data)

    # 绘图
    print('-------------')

    # ax.figure(figsize=(4, 4))
    # ax.set_style.use("ggplot")
    # ax.rcParams['font.sans-serif'] = ['Times New Roman']
    ax.set_title(h_name)
    # ax.set_xlabel('Constituency Type')
    # ax.set_ylabel('No of Independent Candidates')
    # x = range(0,900)
    size = len(new_title)
    for i in range(size):
        # if i == 0 or i == 3:
        #     continue
        # else:
        ax.plot(summary_data[new_title[i]],  # x轴数据
                summary_data.index,
                label=new_title[i], linewidth=0.7)  # 添加标签
        ax.set_ylabel("#solved instances")
        ax.set_xlabel("CPU time (seconds)")

    # plt.plot(sub_data.date, # x轴数据
    #          sub_data.article_reading_cnts, # y轴数据
    #          linestyle = '-', # 折线类型
    #          linewidth = 2, # 折线宽度
    #          color = 'steelblue', # 折线颜色
    #          marker = 'o', # 点的形状
    #          markersize = 2, # 点的大小
    #          markeredgecolor='black', # 点的边框色
    #          markerfacecolor='steelblue') # 点的填充色
    # ax.semilogx()
    # ax.ylim(0, summary_data.shape[0] + 1)
    # ax.xlim(min_time / 10, time_limit)
    # plt.twiny()
    # plt.loglog()
    # ax.tick_params(top='off', right='off')


if __name__ == '__main__':
    # root_dir = 'D:/data2/out'
    # res_dir = 'D:/data2/sum_rm'
    heu_name = 'def'
    time_limit = 899.9
    min_time = 1
    # new_title = ['Choco', 'Zhang18', 'Zhang20', 'OurMB', 'LO']
    # f.figure(figsize=(4, 4))
    # f.rcParams['font.sans-serif'] = ['Times New Roman']
    heus = ['def', 'abs', 'ibs', 'chs']
    heus_names = ['dom/wdeg', 'ABS', 'IBS', 'CHS']

    f, ax = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(7, 7))
    plt.style.use('ggplot')
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    # f.subplots_adjust(wspace=0)

    for i in range(2):
        for j in range(2):
            idx = i * 2 + j
            sub_fig(heus[idx], f, ax[i][j], time_limit, min_time, heus_names[idx])

    # sub_fig(heus[0], f, ax[0][0], time_limit, min_time, heus_names[0])
    # sub_fig(heus[1], f, ax[0][1], time_limit, min_time, heus_names[1])
    # sub_fig(heus[2], f, ax[1][0], time_limit, min_time, heus_names[2])

    # plt.legend()
    plt.legend(loc=3, bbox_to_anchor=(-1.45,2.3),borderaxespad = 0.,ncol = 6)  ##设置ax4中legend的位置，将其放在图外
    # f.legend(new_title, bbox_to_anchor=(0.95, 0.9), ncol=5, fontsize=10.5)
    # f.legend(new_title)
    # plt.legend(fontsize=10)
    # plt.figlegend(loc = 'upper center', ncol=5 )
    # f.legend(new_title, loc = 'lower center', ncol=5)
    # f.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0.)
    # f.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
    # ncol=2, mode="expand", borderaxespad=0.)
    # f.tight_layout()
    # plt.legend()
    f.subplots_adjust()
    plt.semilogx()
    plt.ylim(0, 200)
    plt.xlim(min_time / 10, time_limit)

    # plt.tight_layout()
    # f.title('Average No Of Independent Candidates by Constituency Type')
    plt.show()
