import os
import pandas as pd
import numpy as np

# 合并两个算法到同一个表中
if __name__ == '__main__':
    rootdir = "D:/data2"
    resfile = 'D:/data2/ulti_summary.csv'
    cpu_name = 'avg_time.csv'
    prop_name = 'avg_prop.csv'
    to_name = 'timeout.csv'

    cpu_path = os.path.join(rootdir, cpu_name)
    prop_path = os.path.join(rootdir, prop_name)
    to_path = os.path.join(rootdir, to_name)

    cpu = pd.read_csv(cpu_path)
    prop = pd.read_csv(prop_path)
    to = pd.read_csv(to_path)
    to = to[:len(to) - 1]

    numrow = cpu.shape[0]
    numcol = cpu.shape[1]
    # print(cpu.shape)
    # print(cpu)
    # print(prop.shape)
    # print(prop)
    # print(to.shape)
    # print(to)
    ls = list()

    for i in range(numrow):
        ls.append(cpu.iloc[i].values[1:numcol])
        ls.append(prop.iloc[i].values[1:numcol])
        ls.append(to.iloc[i].values[1:numcol])
        # print(cpu.iloc[i].toList())

    print(ls)

    nd = np.array(ls)
    result = pd.DataFrame(nd)
    # print(result)
    print(result)
    result.to_csv(resfile)
    #
    # for name in common_files:
    #     ct_file = os.path.join(rootdir, pct, name)
    #     strbit_file = os.path.join(rootdir, strbit, name)
    #     summary_file = os.path.join(rootdir, summary, name)
    #     # print(rand10_file)
    #     # with open(rand10_file) as f:
    #     #     reader = csv.reader(f)
    #     #     for row in reader:
    #     #         print(row)
    #
    #     ct_data = pd.read_csv(ct_file)
    #     strbit_data = pd.read_csv(strbit_file)
    #     # print(ct_data)
    #     # print(strbit_data)
    #     # print(ct_data['name'])
    #
    #     sum_data = pd.merge(ct_data, strbit_data, how='inner', on='name')
    #     # print(sum_data)
    #
    #     sum_data.to_csv(summary_file)
