import os
import pandas as pd
import numpy as np

# 传播次数留下来 时间删除 并且吧点数转成M为单位
if __name__ == '__main__':
    root_path = 'D:/data2/avg_rm.csv'
    resfile = 'D:/data2/avg_prop.csv'

    # 获得title
    data = pd.read_csv(root_path)
    name = data.pop('name')
    title_list = data.columns.values.tolist()
    print(name)
    print(title_list)
    print(len(title_list))
    #
    for c in title_list:
        if not (c.startswith('c_sum') or c.startswith('c_prop')):
            del data[c]

    data2 = round(data / 100000, 3)
    data2.insert(0, 'name', name)
    print(data2)

    data2.to_csv(resfile)
