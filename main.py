# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    data = pd.read_csv("D:/exp/def/NumberPartitioning_DEFAULT_2020-08-07_21_08_45.csv")
    #显示所有列
    pd.set_option('display.max_columns', None)

    #显示所有行
    pd.set_option('display.max_rows', None)

    #设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth',100)
    print(data)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
