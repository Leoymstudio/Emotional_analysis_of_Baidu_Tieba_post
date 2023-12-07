import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel('all_data123_with_sentiment.xlsx')
locations = df['location'].tolist()

# 统计频率
location_count = pd.Series(locations).value_counts().sort_index()

# 生成频率时序图
plt.figure(figsize=(10, 6))
location_count.plot(kind='line')
plt.xlabel('Location')
plt.ylabel('Frequency')
plt.title('Frequency Time Series of Locations')
plt.show()
