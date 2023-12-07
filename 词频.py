import pandas as pd
import jieba
import re
from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
# 读取Excel文件中的数据
df = pd.read_excel('all_data123_with_sentiment.xlsx')
comments = df['comment'].tolist()

# 对评论进行分词和筛选
comment_words = []
for comment in comments:
    # 删除标点、符号、数字和空格，只保留中文字符
    comment = re.sub(r'[^\u4e00-\u9fa5]', '', comment)
    words = jieba.lcut(comment)
    # 筛选长度大于等于2的词语
    words = [word for word in words if len(word) >= 2]
    comment_words += words

# 统计词频
word_count = Counter(comment_words)

# 输出前10个词及其出现频率
top_words = word_count.most_common(40)
for word, count in top_words:
    frequency = count / len(comment_words)
    print(f'{word}: {count} ({frequency:.2%})')
# # 统计词频
# word_count = Counter(comment_words)
#
# # 获取前20个高频词和频率
# top_words = word_count.most_common(20)
# words = [x[0] for x in top_words]
# freqs = [x[1]/len(comment_words) for x in top_words]
#
# # 绘制柱状图
# plt.figure(dpi=120, figsize=(10, 6))
# plt.bar(words, freqs)
#
# # 在柱形上添加数量文本
# for i, v in enumerate(freqs):
#     plt.text(i, v+0.001, str(top_words[i][1]), ha='center')
#
# plt.xlabel('词语', fontsize=14)
# plt.ylabel('频率', fontsize=14)
# plt.title('高频词TOP20', fontsize=16)
#
# ax = plt.gca()
# ax.set_yticklabels(['{:.0%}'.format(x) for x in ax.get_yticks()])
#
# plt.show()