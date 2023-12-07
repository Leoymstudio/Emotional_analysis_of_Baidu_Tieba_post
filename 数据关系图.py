import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('all_data1+2_with_sentiment.xlsx')

# 使用LabelEncoder将非数值列转换为数值列
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['ip'] = le.fit_transform(df['ip'])
df['location'] = le.fit_transform(df['location'])
df['comment'] = le.fit_transform(df['comment'])

# 创建散点图矩阵
sns.pairplot(df[['ip', 'location', 'comment', 'sentiment']], hue='sentiment')
plt.show()
