import re
import spacy
import statistics
import en_core_web_lg

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

nlp = en_core_web_lg.load()

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
        bunsyou.append(str(sent))


    kazu=0
    kazu_2=0

    while kazu < len(bunsyou)-1:
        doc1 = nlp(bunsyou[kazu])
        kazu_2 = kazu+1
        while kazu_2 <  len(bunsyou):
            doc2 = nlp(bunsyou[kazu_2])

            #隣接している文のコサイン類似度の計算結果
            cos_ruizido_keisan = doc1.similarity(doc2)

            #リストに計算結果を入れる
            cos_ruizido.append(cos_ruizido_keisan)

            kazu_2+=1

        kazu+=1



    #リスト内の平均値計算
    hasseiritu = statistics.mean(cos_ruizido)
    #print(mean)

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


print("参照の結束性レベル - 隣接している文における重複する内容語の割合")
print("相関結果:", soukan)

print("隣接している文における重複する内容語の割合:", keisankekka)

    
