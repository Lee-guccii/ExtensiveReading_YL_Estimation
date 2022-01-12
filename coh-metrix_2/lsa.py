from math import log
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer


def tf(t, d):
    return d.count(t) / len(d)
    # return d.count(t)


def df(t, docs):
    df = 0
    for doc in docs:
        df += 1 if t in doc else 0
    return df


def idf(t, docs):
    N = len(docs)
    return log(N/df(t, docs)) + 1


def vectorizer_transform(text):

    # 単語を生成
    words = []
    for s in text:
        words += s.split(' ')
    words = list(set(words))
    words.sort()

    tf_idf = []
    for txt in text:
        line_tf_idf = []
        for w in words:
            # tfを計算
            tf_v = tf(w, txt)

            # idfを計算
            idf_v = idf(w, text)

            # tfとidfを乗算
            line_tf_idf.append(tf_v * idf_v)
        tf_idf.append(line_tf_idf)
    return tf_idf


# ベクトル化する文字列
text = [
    'The field was full of lush, green grass.',
    'An elephant is a large animal. No-one appreciates being lied to.',
    'What are we going to have for dinner tonight?'
    
]

tf_idf = vectorizer_transform(text)

for line in tf_idf:
    print(line)