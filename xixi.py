import os

import pandas as pd


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
        print(path)
        data = pd.read_csv(path)

        d = data.drop(data.columns[[0,1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22]],axis=1)
        d.to_csv(res_path, index=0)

if __name__ == '__main__':
    # #p1
    # root_dir = R"D:\exp\default"
    # res_dir = R"D:\exp\per\def"
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

    #p3
    root_dir = R"D:\exp\per\def"
    res_dir = R"D:\exp\5p\def"

    reduce_table(root_dir,res_dir)