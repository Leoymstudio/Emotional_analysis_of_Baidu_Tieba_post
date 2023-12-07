import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_excel('all_data123_with_sentiment.xlsx')

# 计算正面、负面和中立评论的数量
positive_count = len(data[data['sentiment'] == 1])
negative_count = len(data[data['sentiment'] == 0])

# 将结果绘制成柱状图
labels = ['Positive', 'Negative']
values = [positive_count, negative_count]

plt.bar(labels, values)
plt.title('Sentiment Analysis Result')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
