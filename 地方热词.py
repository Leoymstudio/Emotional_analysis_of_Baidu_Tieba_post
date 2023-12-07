import re
import pandas as pd
import jieba
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 读取Excel文件
df = pd.read_excel('all_data123_with_sentiment.xlsx')

# 将IP地址和评论列分别提取出来
ips = df['ip'].tolist()
comments = df['comment'].tolist()

# 定义一个字典来存储各个地址中出现的词语及其频率
word_freq_by_location = {}

# 定义正则表达式模式
pattern = re.compile(r'[\W0-9\s_]+')

# 遍历所有评论，对于每个评论，使用jieba分词并统计各个地址中出现的词语及其频率
for i in range(len(comments)):
    # 删除标点、符号、数字和空格，只保留中文字符
    cleaned_comment = pattern.sub('', comments[i])
    words = jieba.lcut(cleaned_comment)
    location = ips[i].split(':')[1]
    if location not in word_freq_by_location:
        word_freq_by_location[location] = {}
    for word in words:
        if len(word) >= 2:
            if word not in word_freq_by_location[location]:
                word_freq_by_location[location][word] = 1
            else:
                word_freq_by_location[location][word] += 1

# 定义一个字典来存储各个城市的最高频词及其出现次数
top_words_by_location = {}

# 遍历所有城市，找出每个城市的最高频词及其出现次数
for location in word_freq_by_location:
    sorted_words = sorted(word_freq_by_location[location].items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        if "没有" not in word and "流行语" not in word:
            if location not in top_words_by_location:
                top_words_by_location[location] = (word, count)
                break

# 对各个城市的最高频词根据在该城市的词语出现次数进行排序，并仅展示前10个城市的结果在图中
sorted_top_words = sorted(top_words_by_location.items(), key=lambda x: x[1][1], reverse=True)[:10]
cities = [x[0] for x in sorted_top_words]
words = [x[1][0] for x in sorted_top_words]
counts = [x[1][1] for x in sorted_top_words]

fig, ax = plt.subplots()
ax.bar(cities, counts)
ax.set_xlabel('城市')
ax.set_ylabel('词语出现次数')
ax.set_title('各个城市中出现频率最高的词语')
for i, count in enumerate(counts):
    ax.text(i, count, words[i], ha='center', va='bottom')
plt.show()


# # 输出各个地址中出现频率最高的词语
# for location in word_freq_by_location:
#     sorted_words = sorted(word_freq_by_location[location].items(), key=lambda x: x[1], reverse=True)
#     print(f"地址 {location} 中出现频率最高的词语是 {sorted_words[0][0]}，出现次数为 {sorted_words[0][1]}")
