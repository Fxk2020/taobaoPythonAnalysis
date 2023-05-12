# -*- encoding: utf-8 -*-
'''
@File    :   seabornTaobao.py   
@Contact :   13105350231@163.com
@License :   (C)Copyright 2022-2025
@Desciption : 对清洗后的数据进行可视化展示

@Modify Time      @Author    @Version   
------------      -------    --------   
2023/5/11 16:49   fxk        1.0         
'''
import multiprocessing
import time

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from cleanData import readCsv, getFiles

dirUrl = "D:\\taobaoFiles\\"
outputUrl = "D:\\taobaoFilesOut\\"


def getAllType(url, threshold):
    items = readCsv(url)
    items = items[items['people_buy'] > threshold]
    return items


def savaPng(filename):
    items = getAllType(dirUrl + filename, 500)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    sns.relplot(x="prize", y="people_buy", hue="shop_name", style="shop_name", data=items)
    plt.savefig(outputUrl + "figs\\" + filename + ".png")
    plt.close()


def getArgs():
    args = []
    files = getFiles(dirUrl)
    for file in files:
        args.append(file)
    return args


def mul_defs(defName = "savaPng"):
    args = getArgs()
    start = time.time()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(defName, args)
    pool.close()
    pool.join()
    end = time.time()
    print(end - start)


def outFile2(url="D:\\taobaofilesOut\\all\\all.csv"):
    fileNames = getArgs()
    items = getAllType(dirUrl + fileNames[0], 500)
    items['type'] = fileNames[0].replace(".csv", "")
    print(items.info)
    for i in range(len(fileNames)):
        if i != 0:
            temp = getAllType(dirUrl + fileNames[i], 500)
            temp['type'] = fileNames[i].replace(".csv", "")
            items = pd.concat([items, temp])
    items.to_csv(url, index=False)


def getFig2(url='D:\\taobaofilesOut\\all\\all.csv'):
    sns.set()
    items = getAllType(url, 50000)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    sns.catplot(x="type", y="people_buy", data=items)
    plt.show()


if __name__ == '__main__':
    getFig2()
