import os
import pandas as pd
import numpy as np

# 传播次数删除 时间留下
if __name__ == '__main__':
    root_path = 'D:/data2/avg_rm.csv'
    resfile = 'D:/data2/avg_time.csv'

    # 获得title
    data = pd.read_csv(root_path)
    title_list = data.columns.values.tolist()
    print(title_list)
    print(len(title_list))
    print(data)
    #
    for c in title_list:
        # if not (c.startswith('time') or c.startswith('name')):
        #     del data[c]
        if not (c.startswith('prop') or c.startswith('name')):
            del data[c]

    print(data)

    data.to_csv(resfile)
