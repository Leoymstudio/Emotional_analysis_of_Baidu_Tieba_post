import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('all_data1+2_with_sentiment.xlsx')

# 计算每个评论的长度
df['length'] = df['comment'].apply(len)

# 创建分面图
g = sns.FacetGrid(df, col='sentiment', height=4, aspect=1)
g.map(sns.histplot, 'length', bins=20)

plt.show()
