import os
import pandas as pd
import numpy as np

# 统计每个算法下超时的个数
if __name__ == '__main__':
    root_path = 'D:/data2/out'
    resfile = 'D:/data2/timeout.csv'
    files = sorted(os.listdir(root_path))
    # files.remove('.DS_Store')
    print(files)

    # 获得title
    sample = "D:/data2/out/aim-50.csv"
    title = list()
    data = pd.read_csv(sample)
    title_list = data.columns.values.tolist()
    print(title_list)
    print(len(title_list))
    #
    result = pd.DataFrame(columns=title_list)
    # solve time list
    for c in title_list:
        if c.startswith('time'):
            title.append(c)

    print(title)

    ls = list()
    # 逐个文件遍历
    for name in files:
        print(name)
        f = os.path.join(root_path, name)
        data = pd.read_csv(f)
        total = data.shape[0]
        # print(total)
        l = list()
        l.append(name)

        for t in title:
            numto = data[data[t] >= 1800].shape[0]
            # print(numto)
            l.append(round(numto / total, 2))

        # # data[data['A'] > 0].count()
        # numto = data[data['time_x'] < 900].shape[0]
        # # numto = data[data['time_x'] >= 900].count()
        # print(numto)

        ls.append(l)
    #
    #
    nd = np.array(ls)
    print(nd)
    result = pd.DataFrame(nd)
    # print(result)
    print(result)
    result.to_csv(resfile)
