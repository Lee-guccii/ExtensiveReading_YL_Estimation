import numpy as np
import re
import spacy
from functools import lru_cache
import en_core_web_lg


from scipy import stats
from scipy.stats import spearmanr
from nltk.tokenize import sent_tokenize

nlp = en_core_web_lg.load()




###################
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


#親やすさdicを作成する
###############

#textをnew_listに読み込む
with open("tango_sitasimiyasusa_list.txt", "r", encoding="utf-8") as f:
    list = f.readlines()

new_list = []

for i in list:
    word = i.split()
    new_list.append(word)



#####################################
#使いたいパラメータの数字を取り出す


#単語名，親やすさ（100：親しみがない，700：親しみがある）
sitasimi_tango={}

count_level = 1
while count_level < 6415:

    #値を取り出す
    tango_list = new_list[count_level][0].lower() #単語名
    suuti_list = new_list[count_level][1] #数値

    
    #文字列を数値に変換
    y = round(float(suuti_list)*100)
    sitasimi_tango[tango_list] = y
    

 
    count_level+=1



#本を解析
####################
text_suu=101 #テキストの番号

keisankekka=[]#１テキストでの計算結果


while text_suu < 201:
    #text_listにリストとして読み込む
    with open('book'+ str(text_suu) +'_test1.txt', 'r') as f:
        #改行("\n")を""に変換
        #text_list = f.read().splitlines()
        text = f.read()


    #正規表現で"を削除
    text = re.sub('"', '', text)

    #文章
    pos = nlp(text)



    kazu=0
    hinsi=[]#品詞の名前
    hinsi_kosuu=[]#品詞の個数．配列は品詞の名前と対応している．
    list_bangou=0

    kigou_reigai=["=","+","'"]#総単語数に数えない記号
    kigou=0



    #内容語の品詞
    naiyougo_list=["ADJ","ADV", "NOUN", "VERB"]#名詞，動詞，形容詞，副詞

    sent=""

    wariai=[]

    for token in pos:
        #内容語なら
        if token.pos_ in naiyougo_list:

            #レンマ化
            sent = token.lemma_

            #親やすさdicに入っていれば
            if sent.lower() in sitasimi_tango:
                wariai.append(sitasimi_tango[sent.lower()])
                


    

    #結果
    #print(sum(wariai))
    #print(len(wariai))
    hasseiritu = sum(wariai)/len(wariai)
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


print("単語情報レベル - 親しみのある単語の平均値")
print("相関結果:", soukan)

print("親しみのある単語の平均値:", keisankekka)




#476.452	438.136
#418.619	429.575
