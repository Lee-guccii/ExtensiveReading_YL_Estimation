import re
import spacy
import statistics
import en_core_web_lg
from functools import lru_cache

import numpy as np
from scipy import stats
from scipy.stats import spearmanr

#多読図書のYL
x_tadoku = [1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 
            1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 3.3, 3.9, 5.7, 
            0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 
            0.7, 0.7]

#一般図書のYL
x_ippan = [5.0, 6.0, 6.5, 6.5, 8.0, 8.5, 7.0, 8.0, 5.0, 6.5, 
           8.0, 5.0, 8.0, 7.5, 5.5, 7.5, 8.0, 8.0, 7.0, 8.0, 
           8.0, 5.0, 8.0, 5.0, 5.0, 8.0, 8.5, 5.5, 8.0, 5.5,
           8.0, 5.0]


#多読図書と一般図書のYL
x_zenbu = x_tadoku + x_ippan


text_suu=1 #テキストの番号

keisankekka=[]#１テキストでの計算結果

#nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_lg.load()


@lru_cache(maxsize=4096)
def ld(s, t):
    if not s: return len(t)
    if not t: return len(s)
    if s[0] == t[0]: return ld(s[1:], t[1:])
    l1 = ld(s, t[1:])
    l2 = ld(s[1:], t)
    l3 = ld(s[1:], t[1:])
    return 1 + min(l1, l2, l3)

while text_suu < 65:
    #text_listにリストとして読み込む
    with open('book/book'+ str(text_suu) +'.txt', 'r') as f:
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



    bun_1=""
    bun_2=""

    kazu=0
    a=0
    wariai=[]

    reigai=[36,37,39,40,41,43,44, 57]

    if text_suu > 35:
        while kazu < 2:
        
            bun_1=bunsyou[kazu]
            bun_2=bunsyou[kazu+1]


            kyori = ld(bun_1,bun_2)

            
            #最小編集距離/（bun_1の文字数＋bun_2の文字数）
            wariai.append(kyori/(len(bunsyou[kazu])+len(bunsyou[kazu+1])))

            kazu+=1

    elif len(bunsyou) <= 100:

        while kazu < len(bunsyou)-1:
        
            bun_1=bunsyou[kazu]
            bun_2=bunsyou[kazu+1]


            kyori = ld(bun_1,bun_2)

            
            #最小編集距離/（bun_1の文字数＋bun_2の文字数）
            wariai.append(kyori/(len(bunsyou[kazu])+len(bunsyou[kazu+1])))


        
            kazu+=1
    else:
        while kazu < 100:
            
            bun_1=bunsyou[kazu]
            bun_2=bunsyou[kazu+1]


            kyori = ld(bun_1,bun_2)

            
            #最小編集距離/（bun_1の文字数＋bun_2の文字数）
            wariai.append(kyori/(len(bunsyou[kazu])+len(bunsyou[kazu+1])))


            
            kazu+=1

    #リスト内の平均値計算
    hasseiritu = statistics.mean(wariai)
    #print(hasseiritu)

    #計算結果をリストに入れる
    keisankekka.append(hasseiritu)
    print(text_suu)


    text_suu+=1





###############################
#相関係数の計算

#相関計算
x_np = np.array(x_zenbu)
y_np = np.array(keisankekka)



#x_zenbuが正規性がないので，スピアマンの相関係数
#スピアマンの順位相関係数
correlation, pvalue = spearmanr(x_zenbu, keisankekka)
soukan = correlation


print("状況モデルレベル - 因果関係のある動詞の発生率")
print("相関結果:", soukan)

print("因果関係のある動詞の発生率:", keisankekka)











#0.820	0.907
#0.894	0.874
