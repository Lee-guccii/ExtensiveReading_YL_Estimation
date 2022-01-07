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
    'I JIMMY SKUNK IS PUZZLED Old Mother West Wind had just come down from the Purple Hills and turned loose her children, the Merry Little Breezes, from the big bag in which she had been carrying them',
    'They were very lively and very merry as they danced and raced across the Green Meadows in all directions, for it was good to be back there once more',
    
]

tf_idf = vectorizer_transform(text)

for line in tf_idf:
    print(line)