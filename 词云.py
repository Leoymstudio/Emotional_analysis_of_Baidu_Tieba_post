import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel('all_data123_with_sentiment.xlsx')
comments = df['comment'].tolist()
# 对评论进行分词
comment_words = ''
for comment in comments:
    comment_words += ' '.join(jieba.cut(comment)) + ' '
font_path = 'simsun.ttc'  # 替换为您下载的字体文件名及路径
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10, font_path=font_path).generate(comment_words)

# 生成词云图

# 显示词云图
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
