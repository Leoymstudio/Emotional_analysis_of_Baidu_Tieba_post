# Emotional_analysis_of_Baidu_Tieba_post

#### 介绍
百度贴吧帖子的情感检测与数据分析。
用网络爬虫爬取百度贴吧的帖子并进行词云图，频率次数等分析。并利用贝叶斯分类和聚类进行情感检测。
其中情感分析部分采用了[weibo_senti_100k](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/weibo_senti_100k/intro.ipynb)数据集。
本项目为南京农业大学Python大作业的内容，在项目里附上了答辩的PPT。

#### 软件架构
软件架构说明

"爬虫.py"，"爬虫2.py"，"爬虫3.py"为爬取百度贴吧的爬虫代码，结果保存为xlsx文件。注：此处并没有采用任何绕过验证码的措施。
其余python文件根据标题生成相关的图。
机器学习-贝叶斯-聚类分析.py需要将聚类分析生成的类别进行导入后再进行分析。


#### 安装教程

1.  此处所用库较为分散，可以根据py文件自行下载
1.  根据编译器提示，出现很多新版库不适配情况，需要更正

#### 使用说明

​		1.修改爬虫文件进行爬取（爬虫通过多次正则表达式适配和调整，对于数据爬取较为精确）

```python
for page in range(0, XXXXXX要爬的页数XXXXXX):
    url = f"https://tieba.baidu.com/p/XXXXXXXX要爬的网址XXXXXXXX?pn={page}"
    ............
# 将所有数据写入 Excel 文件
all_data_df.to_excel('XXXXX保存文件XXXXXX.xlsx', index=False)
print('所有数据保存为 XXXXX保存文件XXXXXX.xlsx')
```

​		2.进行图片生成

```python
# 读取Excel文件中的数据
df = pd.read_excel('XXXXX保存文件XXXXXX.xlsx')
comments = df['comment'].tolist()
..........
```

​		3.贝叶斯聚类分析

```python
# 对给定的主题进行情感分析  将聚类.py的命令行输出结果填入到下列表格
tp1= []
tp2= []
tp3= []
tp4= []
tp5= []
```

#### 问题

1.优秀的情绪识别需要爬取非常多的数据量

2.优秀的情绪识别需要更新的模型（网络用词迭代非常快，需要更新的评价标准，有些词的褒贬在几年间发生了非常大的变化）诸如本文所用的贴吧数据如果进行人工分类将是一个很好很新的数据集。

3.更细的情感分析标准（用词的情绪应该有更多的标准去衡量，但不宜过多，容易打乱判断）
	诸如近几年非常火的mbti就用四个标准清晰的进行概括

4.分词上的调控（jieba库在中文分词上具有卓越的效果，但在网络用词上存在过细的效果，也容易出现无效数据）
	可以尝试使用聚类+jieba进行一个新的网络用词分割定义，此外，神经网络的训练并重写jieba库也将会是一个良好的办法。	
