# taobaoPythonAnalysis
对爬取的淘宝数据进行清洗并进行可视化分析

## 1.pandas包

Pandas 的主要数据结构是 Series （一维数据）与 DataFrame（二维数据），这两种数据结构足以处理金融、统计、社会科学、工程等领域里的大多数典型用例。

Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。

![img](https://www.runoob.com/wp-content/uploads/2021/04/FD659034-1715-4020-A6BF-400FAC9CE849.jpg)

DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

![img](https://www.runoob.com/wp-content/uploads/2021/04/pandas-DataStructure.png)

![img](https://www.runoob.com/wp-content/uploads/2021/04/df-dp.png)

**使用pandas进行数据清洗**

- pandas清洗空值：result.dropna()
- pandas清洗重复值：drop_duplicates
- padas清洗格式错误的数据：

  ```
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
  ```

## 2.matplotlib、Seaborn包

官网解释：

Seaborn is a library for making statistical graphics in Python. It builds on top of [matplotlib](https://matplotlib.org/) and integrates closely with [pandas](https://pandas.pydata.org/) data structures.

```
Seaborn 是一个用 Python 制作统计图形的库。它建立在matplotlib之上，并与pandas数据结构紧密集成。
```

### 2.1 关联图

| 关联性分析  |       介绍       |
| :---------: | :--------------: |
|   relplot   |    绘制关系图    |
| scatterplot | 多维度分析散点图 |
|  lineplot   | 多维度分析线形图 |

```
sns.relplot(x="prize", y="people_buy", hue="shop_name", style="shop_name",data=items)
```

![image-20230511200802346](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230511200802346.png)

### 2.2 类别图

与关联图相似，类别图的 Figure-level 接口是 `catplot`，其为 categorical plots 的缩写。

```
sns.catplot(x="people_buy", y="type", data=items)
```

![image-20230511211353865](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230511211353865.png)

### 2.3 分布图

分布图主要是用于可视化变量的分布情况，一般分为单变量分布和多变量分布。当然这里的多变量多指二元变量，更多的变量无法绘制出直观的可视化图形。

Seaborn 提供的分布图绘制方法一般有这几个：[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html)，[`pairplot`](https://seaborn.pydata.org/generated/seaborn.pairplot.html)，[`distplot`](https://seaborn.pydata.org/generated/seaborn.distplot.html)，[`kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)。接下来，我们依次来看一下这些绘图方法的使用。

Seaborn 快速查看单变量分布的方法是 `distplot`

```
sns.displot(items['prize'])
```

![image-20230511211828273](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230511211828273.png)

`kdeplot` 可以专门用于绘制核密度估计图，其效果和 `distplot(hist=False)` 一致，但 `kdeplot` 拥有更多的自定义设置。

![image-20230511212057228](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230511212057228.png)

`jointplot` 主要是用于绘制二元变量分布图。

![image-20230511212233488](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230511212233488.png)

![image-20230511212301220](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230511212301220.png)

最后要介绍的 `pairplot` 更加强大，其支持一次性将数据集中的特征变量两两对比绘图。默认情况下，对角线上是单变量分布图，而其他则是二元变量分布图。

```
sns.pairplot(items)
```

![image-20230512144832497](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230512144832497.png)

### 2.4 回归图

回归图的绘制函数主要有：[`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html) 和 [`regplot`](https://seaborn.pydata.org/generated/seaborn.regplot.html)。

`regplot` 绘制回归图时，只需要指定自变量和因变量即可，`regplot` 会自动完成线性回归拟合。

`lmplot` 同样是用于绘制回归图，但 `lmplot` 支持引入第三维度进行对比，例如我们设置 `hue="species"`。

### 2.5 矩阵图

矩阵图中最常用的就只有 2 个，分别是：[`heatmap`](https://seaborn.pydata.org/generated/seaborn.heatmap.html) 和 [`clustermap`](https://seaborn.pydata.org/generated/seaborn.clustermap.html)。

意如其名，`heatmap` 主要用于绘制热力图。

除此之外，`clustermap` 支持绘制层次聚类结构图。
