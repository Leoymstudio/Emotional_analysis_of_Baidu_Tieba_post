import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 读取Excel文件
df = pd.read_excel('all_data123_with_sentiment.xlsx')

# 将非数值列转换为数值列
le = LabelEncoder()
df['ip'] = le.fit_transform(df['ip'])
df['location'] = le.fit_transform(df['location'])
df['id_name'] = le.fit_transform(df['id_name'])

# 使用KMeans进行聚类
kmeans = KMeans(n_clusters=3)  # 假设我们想要3个聚类
kmeans.fit(df.drop(columns=['comment']))

# 输出聚类结果
df['cluster'] = kmeans.labels_

# 使用jieba进行分词
df['cut_comment'] = df['comment'].apply(lambda x: ' '.join(jieba.cut(x)))

# 使用 CountVectorizer 将文本数据转换为文档-词矩阵
vectorizer = CountVectorizer(max_df=0.95, min_df=2)
dtm = vectorizer.fit_transform(df['cut_comment'])

# 使用 LDA 模型进行主题建模
num_topics = 5  # 指定主题数量
lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
lda.fit(dtm)

# 打印每个主题的前几个关键词
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(lda.components_):
    print(f"主题 #{topic_idx + 1}:", [feature_names[i] for i in topic.argsort()[:-10 - 1:-1]])

# 将每个评论分配到主题
df['topic'] = lda.transform(dtm).argmax(axis=1)

# 可视化主题分布
topic_distribution = df['topic'].value_counts().sort_index()
topic_distribution.plot(kind='bar', xlabel='主题', ylabel='评论数量', title='主题分布')
plt.show()