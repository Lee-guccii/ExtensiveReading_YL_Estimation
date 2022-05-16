import re
import spacy
import statistics
import en_core_web_lg
from functools import lru_cache
import Levenshtein
from nltk.tokenize import sent_tokenize

import numpy as np
from scipy import stats
from scipy.stats import spearmanr

#nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_lg.load()



#多読図書のYL
#x_tadoku = [1.4,1.8,1.8,1.8,1.8,1.4,1.4,1.4,1.2,1.2,
#                   1.2,2.6,2.6,2.6,3.6,3.6,3.2,3.2,2.4,2.4,
#                   2.4,2.4,2,2,2,2,2.6,3.6,3.2,2.8,
#                   2.8,2.8,4.4,4.4,4.4,4.4,4,4,4,4,
#                   4.8,4.8,4.8,2.5,2.5,2.5,2.5,2.5,2.5,2.5]

#一般図書のYL
#x_ippan = [8,6.6,8.5,6.5,7,7,7,7.6,7.5,7.5,
#                7.3,7,8.2,7,6.6,7.7,7,5,5.5,7,
#                7,7,7,7,7.5,5.1,7,7,7,7,
#                7.6,6.5,7,6.5,7,8.5,7,6.5,9.5,
#                7.7,7.5,7,7,8.5,7,5.5,6.6,8.5,7.5,8]


#多読図書と一般図書のYL
#x_zenbu = x_tadoku + x_ippan

x_zenbu = [1.2, 1.2, 3.6, 6, 6.7, 7, 7, 5, 6.5, 7,
            7, 7, 7, 2.5, 6.5, 8, 5.7, 7, 7, 7,
            7, 7, 5.5, 2.5, 7, 2.5, 6.2, 7, 5, 2.5,
            7.7, 2.5, 8, 5.5, 8, 6, 7.5, 7, 6.5, 2.5,
            8, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 2.5,
            2.5, 7.5, 5.5, 7, 7, 5, 7, 6.3, 7, 7,
            6.5, 8, 5.5, 7, 7, 7.7, 7, 7.5, 7, 7.5,
            7, 8.7, 7, 2.5, 7.5, 8, 2.5, 8, 8, 2.5,
            8, 6.5, 6.5, 8.5, 5, 2.5, 5, 7, 5, 5.5, 
            5.2, 7.5, 7, 5.5, 9.5, 6, 8.5, 4.7, 5, 1.8]


text_suu=101 #テキストの番号

keisankekka=[]#１テキストでの計算結果


while text_suu < 201:
    #text_listにリストとして読み込む
    with open('../book_all/book'+ str(text_suu) +'_test1.txt', 'r') as f:
        #改行("\n")を""に変換
        #text_list = f.read().splitlines()
        text = f.read()

    #正規表現で"を削除
    text = re.sub('"', '', text)



    #隣接する文とのコサインの類似度
    cos_ruizido=[]

    #文区切りの文を入れるリスト
    bunsyou=[]

    sent_tokenize_list = sent_tokenize(text)

    #文章を文ごと区切り，リストに入れる
    for sent in sent_tokenize_list:
        bunsyou.append(str(sent))





    bun_1=""
    bun_2=""

    kazu=0
    a=0
    wariai=[]

    


    while kazu < len(bunsyou)-1:

        bun_1=bunsyou[kazu]
        bun_2=bunsyou[kazu+1]


        kyori = Levenshtein.distance(bun_1,bun_2)

        
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


print("構文の複雑さレベル - 見出し語の最小編集距離")
print("相関結果:", soukan)

print("見出し語の最小編集距離:", keisankekka)











#print(ld('vintner', 'writers'))


#0.820	0.907
#0.894	0.874
