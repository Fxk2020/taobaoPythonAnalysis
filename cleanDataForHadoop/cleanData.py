# -*- encoding: utf-8 -*-
'''
@File    :   cleanData.py   
@Contact :   13105350231@163.com
@License :   (C)Copyright 2022-2025
@Desciption : 清洗数据

@Modify Time      @Author    @Version   
------------      -------    --------   
2023/5/10 20:46   fxk        1.0         
'''
import multiprocessing
import time

import pandas as pd
import os


def getFiles(DirUrl):
    files = os.listdir(DirUrl)
    return files


def readCsv(url):
    df = pd.read_csv(url, error_bad_lines=False)
    return df


def cleanOutCsv(url):
    result = readCsv(url)  # C:\\Users\\yuanbao\\Desktop\\2.csv
    # result = readCsv("D:\\1.csv")
    # print(result.info)
    result = result.dropna()
    # print(result.info)
    result = result.drop_duplicates()
    # print(result.describe())
    # print(result.sort_values("prize").head())
    itemType = result.loc[0]["type"]
    itemType = itemType.replace("/", "-")

    # 选择指定的列
    # df.filter(items=['column_name1', 'column_name2'])
    result2 = result.filter(items=['title', 'prize', 'people_buy', 'shop_name'])
    # print(result2['people_buy'])

    for people_buy in result2.index:
        # 处理掉“人付款”和“+”
        temp = result2.loc[people_buy, "people_buy"].replace("人付款", "").replace("+", "").replace("\\N", "")
        # 处理掉“万”
        # print(temp)
        if temp == "":
            temp = "0"
        if temp.find("万") == -1:
            temp = int(temp)
        else:
            temp = int(temp.replace("万", "")) * 10000
        result2.loc[people_buy, "people_buy"] = temp

    result2 = result2[result2["people_buy"] > 0]

    result2.to_csv('D:\\taobaoFiles\\' + itemType+'.csv', index=False)


def getArgs(url = 'F:\\fxk\\'):
    args = []
    files = getFiles(url)
    for file in files:
        file = url + file
        args.append(file)
    return args


if __name__ == '__main__':
    args = getArgs()
    start = time.time()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(cleanOutCsv, args)
    pool.close()
    pool.join()
    end = time.time()
    print(end - start)
    # cleanOutCsv("F:\\fxk\\fxk1.csv")