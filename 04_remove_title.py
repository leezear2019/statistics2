import os
import pandas as pd
import numpy as np


# 只保留以下有用的列
def remain(a):
    if a is 'name':
        return 1
    elif a.startswith('algorithm'):
        return 1
    elif a.startswith('node'):
        return 1
    # elif a.startswith('c_prop'):
    #     return 1
    elif a.startswith('time'):
        return 1
    # elif a.startswith('prop'):
    #     return 1
    elif a.startswith('name'):
        return 1

    return 0


# 删除无用列
if __name__ == '__main__':
    path = 'D:/data2/totalavg.csv'

    respath = 'D:/data2/totalavg_rm.csv'

    data = pd.read_csv(path)
    print(data)
    title_list = data.columns.values.tolist()
    title_list.remove('Unnamed: 0')
    print(title_list)
    print(len(title_list))

    for t in title_list:
        if remain(t) != 1:
            del data[t]

    print(data)
    data.to_csv(respath)
