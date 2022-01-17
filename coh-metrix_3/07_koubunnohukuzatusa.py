import re
import spacy
import statistics
import en_core_web_lg
from functools import lru_cache


#nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_lg.load()

#text_listにリストとして読み込む
with open('book/book59.txt', 'r') as f:
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
    sent=sent.lemma_
    bunsyou.append(str(sent))

##for token in doc:
#    print(token.text+', '+token.lemma_) # テキスト, レンマ化

a=0
b=0

@lru_cache(maxsize=4096)
def ld(s, t):
    if not s: return len(t)
    if not t: return len(s)
    if s[0] == t[0]: return ld(s[1:], t[1:])
    l1 = ld(s, t[1:])
    l2 = ld(s[1:], t)
    l3 = ld(s[1:], t[1:])
    return 1 + min(l1, l2, l3)

bun_1=""
bun_2=""

kazu=0
a=0
wariai=[]

 

if len(bunsyou) <= 100:

    while kazu < len(bunsyou):
        print(kazu)
    
        bun_1=bunsyou[kazu]
        bun_2=bunsyou[kazu+1]


        kyori = ld(bun_1,bun_2)

        
        #最小編集距離/（bun_1の文字数＋bun_2の文字数）
        wariai.append(kyori/(len(bunsyou[kazu])+len(bunsyou[kazu+1])))


    
        kazu+=1
else:
    while kazu < 2:
        print(kazu)
        
        bun_1=bunsyou[kazu]
        bun_2=bunsyou[kazu+1]


        kyori = ld(bun_1,bun_2)

        
        #最小編集距離/（bun_1の文字数＋bun_2の文字数）
        wariai.append(kyori/(len(bunsyou[kazu])+len(bunsyou[kazu+1])))


        
        kazu+=1

#リスト内の平均値計算
hasseiritu = statistics.mean(wariai)
print(hasseiritu)








#print(ld('vintner', 'writers'))


#0.820	0.907
#0.894	0.874
