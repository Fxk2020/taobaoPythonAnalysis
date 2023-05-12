# -*- encoding: utf-8 -*-
'''
@File    :   test.py   
@Contact :   13105350231@163.com
@License :   (C)Copyright 2022-2025
@Desciption : 

@Modify Time      @Author    @Version   
------------      -------    --------   
2023/5/10 20:39   fxk        1.0         
'''
import matplotlib
import pandas
# Import seaborn
import pandas as pd
import seaborn as sns

# # Apply the default theme
# sns.set_theme()
#
# # Load an example dataset
# tips = sns.load_dataset("tips")
#
# # Create a visualization
# sns.relplot(
#     data=tips,
#     x="total_bill", y="tip", col="time",
#     hue="smoker", style="smoker", size="size",
# )
#
# matplotlib.pyplot.show()
from matplotlib import pyplot as plt

from seabornTaobao import getArgs, getAllType, dirUrl
sns.set()  # 声明使用 Seaborn 样式
items = getAllType(dirUrl + "Lenovo-联想.csv", 100)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
# sns.displot(items['people_buy'])
# sns.kdeplot(items['prize'])
# sns.jointplot(x='prize', y='people_buy', data=items, kind='reg')
# sns.pairplot(items, hue='title')
sns.relplot(x='people_buy', y='prize', data='items')
plt.show()
# plt.savefig(outputUrl + "figs\\" + filename + ".png")
# plt.close()