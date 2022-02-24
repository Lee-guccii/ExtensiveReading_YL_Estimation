import re
import spacy
import statistics
import en_core_web_lg
import numpy as np
from scipy import stats
from scipy.stats import spearmanr
from nltk.tokenize import sent_tokenize



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
    with open('book'+ str(text_suu) +'_test1.txt', 'r') as f:
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

    #計算結果をリストに入れる
    keisankekka.append(mean)
    
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


print("LSAレベル - 隣接している文のLSAの平均")
print("相関結果:", soukan)

print("隣接している文のLSAの平均:", keisankekka)

