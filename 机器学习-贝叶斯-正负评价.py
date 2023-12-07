import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
path = './weibo_senti_100k/'
# 读取数据集
data = pd.read_csv(path + 'weibo_senti_100k.csv')

# 分词
comments = []
for comment in data['review']:
    words = jieba.lcut(comment)
    comments.append(words)

# 将分词后的评论转换为数字特征向量
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([' '.join(words) for words in comments])

# 训练朴素贝叶斯分类器
y = data['label']
clf = MultinomialNB()
clf.fit(X, y)

# 读取待分类的评论数据
all_data = pd.read_excel('all_data123_with_sentiment.xlsx')
comments_to_classify = all_data['comment']

# 对待分类的评论进行情感分类
classified_sentiments = []
for comment in comments_to_classify:
    words = jieba.lcut(comment)
    X_to_classify = vectorizer.transform([' '.join(words)])
    probabilities = clf.predict_proba(X_to_classify)[0]
    if max(probabilities) >= 0.5:
        sentiment = clf.predict(X_to_classify)[0]
    else:
        sentiment = 2
    classified_sentiments.append(sentiment)

# 将分类结果保存到all_data_with_sentiment.xlsx的sentiment列中
all_data['sentiment'] = classified_sentiments
all_data.to_excel('all_data123_with_sentiment.xlsx', index=False)