import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 读取CSV文件
df = pd.read_csv('.\weibo_senti_100k\weibo_senti_100k.csv')

# 使用jieba进行分词
df['cut_review'] = df['review'].apply(lambda x: ' '.join(jieba.cut(x)))

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df['cut_review'], df['label'], test_size=0.2)

# 将文本数据转换为向量
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 训练迭代次数
n_iter = 10

# 保存每次训练的模型
clfs = []

for i in range(n_iter):
    clf = MultinomialNB()
    clf.fit(X_train_vec, y_train)
    clfs.append(clf)

# 多轮预测
y_preds = []
for clf in clfs:
    y_pred = clf.predict(X_test_vec)
    y_preds.append(y_pred)

# 投票统计
y_pred_final = [max(set(y), key=y.count) for y in zip(*y_preds)]

# 对给定的主题进行情感分析
tp1= ['不等式', '野榜', '唐妞', '怎么', '上榜', '回旋', '10', '就是', '低能', '波波']
tp2= ['没有', '遥遥领先', '原神', '哈基米', '启动', '同意', '流行', '尊嘟', '假嘟', '怎么']
tp3= ['流行语', 'ogc', '十大', '我们', '一个', '可以', '几个', '12', '打个', '投票']
tp4= ['成为', '不是', '理解', '质疑', 'xx', '多巴胺', '生产力', '情绪', '价值', '人工智能']
tp5= ['一个', '什么', '不如', '流行语', '没听说过', '感觉', '知道', '第一个', '最后', '今年']

import numpy as np
import matplotlib.pyplot as plt

topics = [tp1, tp2, tp3, tp4, tp5]
avg_sentiments = []

for i, topic in enumerate(topics):
    sentiments = []
    for word in topic:
        word_vec = vectorizer.transform([' '.join(jieba.cut(word))])
        sentiment = clf.predict(word_vec)
        sentiments.append(sentiment[0])
    avg_sentiment = np.mean(sentiments)
    avg_sentiments.append(avg_sentiment)

# 创建柱状图
plt.bar(range(1, len(topics) + 1), avg_sentiments, tick_label=[f"主题 {i+1}" for i in range(len(topics))])
plt.xlabel('主题')
plt.ylabel('平均情感')
plt.title('主题的平均情感')
plt.show()

