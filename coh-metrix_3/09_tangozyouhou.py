import nltk
import numpy as np
import re
from scipy import stats
from scipy.stats import spearmanr
import spacy
from functools import lru_cache
import en_core_web_lg

nlp = en_core_web_lg.load()


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
#使いたいパラメータの数字を取り出す→相関の確認


#単語名，親やすさ（100：親しみがない，700：親しみがある）
sitasimi_tango={}

count_level = 1
while count_level < 1945:

    #値を取り出す
    tango_list = new_list[count_level][0] #単語名
    suuti_list = new_list[count_level][5] #数値

    
    #文字列を数値に変換
    y = round(float(suuti_list)*100)
    sitasimi_tango[tango_list] = y
    

 
    count_level+=1







with open('book/book33.txt', 'r') as f:
    #改行("\n")を""に変換
    #text_list = f.read().splitlines()
    text = f.read()


#正規表現で"を削除
text = re.sub('"', '', text)

morph = nltk.word_tokenize(text)
pos = nltk.pos_tag(morph)
#[0]=元の文字，[1]=品詞タグ


kazu=0
hinsi=[]#品詞の名前
hinsi_kosuu=[]#品詞の個数．配列は品詞の名前と対応している．
list_bangou=0

kigou_reigai=["=","+","'"]#総単語数に数えない記号
kigou=0



#内容語の品詞
naiyougo_list=["NN","NNS", "NNP", "NNPS", "VB", "VBN", "VBP", "VBZ","JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
#naiyougo_list=["NN", "VB", "JJ", "RB"] #名詞，動詞，形容詞，副詞

sent=""

wariai=[]
while kazu < len(pos):
    #もし内容語なら
    if pos[kazu][1] in naiyougo_list:
        a = nlp(pos[kazu][0])
        sent=(a.lemma_)
        print(sent,pos[kazu][0].lower)
        #親やすさdicに入っている単語なら
        if pos[kazu][0].lower() in sitasimi_tango:

            wariai.append(sitasimi_tango[pos[kazu][0].lower()])
            print(pos[kazu][0].lower(),sitasimi_tango[pos[kazu][0].lower()])
            


    kazu+=1






#結果
print(sum(wariai))
print(len(wariai))
hasseiritu = sum(wariai)/len(wariai)
print(hasseiritu)




#476.452	438.136
#418.619	429.575
