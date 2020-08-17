import os
import pandas as pd

# 合并两个算法到同一个表中
if __name__ == '__main__':
    rootdir = "/Users/lizhe/Documents/exp"
    pct = "pct"
    strbit = "strbit"
    summary = "sum"

    pct_path = os.path.join(rootdir, pct)
    strbit_path = os.path.join(rootdir, strbit)
    pct_files = sorted(os.listdir(pct_path))
    strbit_files = sorted(os.listdir(strbit_path))
    common_files = sorted(list(set(pct_files) & set(strbit_files)))
    pct_files.remove('.DS_Store')
    strbit_files.remove('.DS_Store')
    common_files.remove('.DS_Store')
    print(pct_files)
    print(strbit_files)
    print(common_files)

    for name in common_files:
        ct_file = os.path.join(rootdir, pct, name)
        strbit_file = os.path.join(rootdir, strbit, name)
        summary_file = os.path.join(rootdir, summary, name)
        # print(rand10_file)
        # with open(rand10_file) as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         print(row)

        ct_data = pd.read_csv(ct_file)
        strbit_data = pd.read_csv(strbit_file)
        # print(ct_data)
        # print(strbit_data)
        # print(ct_data['name'])

        sum_data = pd.merge(ct_data, strbit_data, how='inner', on='name')
        print(sum_data)

        sum_data.to_csv(summary_file)
