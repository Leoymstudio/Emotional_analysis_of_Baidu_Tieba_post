import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('all_data123_with_sentiment.xlsx')

# 假设您的DataFrame有一个名为'location'的列，其中包含每个评论的时间戳
# 如果没有，您需要先创建这个列
df['location'] = pd.to_datetime(df['location'])

# 将时间划分为每小时一个时间段
df['hour'] = df['location'].dt.hour

# 将数据按时间排序
df = df.sort_values('hour')

# 计算每个时间点的平均情感
sentiment_over_time = df.groupby('hour')['sentiment'].mean()

# 创建折线图
plt.plot(sentiment_over_time.index, sentiment_over_time.values)
plt.xlabel('Hour of the Day')
plt.ylabel('Average Sentiment')
plt.title('Sentiment Over Time')
plt.show()
