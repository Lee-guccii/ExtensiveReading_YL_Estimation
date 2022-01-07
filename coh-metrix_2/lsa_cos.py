import re
import spacy
import statistics
import en_core_web_lg

#nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_lg.load()

#text_listにリストとして読み込む
with open('book6_3.txt', 'r') as f:
    #改行("\n")を""に変換
    #text_list = f.read().splitlines()
    text = f.read()

#正規表現で"を削除
text = re.sub('"', '', text)



#隣接する文とのコサインの類似度
cos_ruizido=[]

#文区切りの文を入れるリスト
bunsyou=[]

#文章を文ごと区切り，リストに入れる
doc = nlp(text)
for sent in doc.sents:
    bunsyou.append(str(sent))


kazu=0
while kazu < len(bunsyou)-1:
    doc1 = nlp(bunsyou[kazu])
    doc2 = nlp(bunsyou[kazu+1])

    #隣接している文のコサイン類似度の計算結果
    cos_ruizido_keisan = doc1.similarity(doc2)

    #リストに計算結果を入れる
    cos_ruizido.append(cos_ruizido_keisan)

    kazu+=1



#リスト内の平均値計算
mean = statistics.mean(cos_ruizido)
print(mean)


