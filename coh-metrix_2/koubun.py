import nltk
import numpy as np
import re
from scipy.stats import spearmanr

#text_listにリストとして読み込む
with open('book6_3.txt', 'r') as f:
    #改行("\n")を""に変換
    #text_list = f.read().splitlines()
    text = f.read()


#正規表現で"を削除
text = re.sub('"', '', text)

morph = nltk.word_tokenize(text)
pos = nltk.pos_tag(morph)
#print(pos)

kazu=0
hinsi=[]#品詞の名前
hinsi_kosuu=[]#品詞の個数．配列は品詞の名前と対応している．
list_bangou=0

zentisi=0
zentisi_list = ["about", "aboard", "above", "across", "after", "against", "along", "alongside", "amid", "among",  "anti", "around", "as", "at",
"bar", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by",
"considering", 
"despite", "down", "during", 
"except",
"for", "from",
"in", "inside", "into"
"less", "like"
"minus",
"near", "notwithstanding",
"of", "off", "on", "onto", "opposite", "out", "outside", "over",
"pace", "past", "pending", "per", "plus", 
"re", "regarding", "round", 
"save", "saving", "since", 
"than", "through", "throughout", "till", "to", "touching", "toward", 
"under", "underneath", "unless", "unlike", "until", "up", 
"versus", "via", "vice", 
"with", "within", "without"]
dousi=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "IN", "TO", ",", "."]
kigou=0
kigou_reigai=["=","+","'"]



while kazu < len(pos):
    #一人称単数代名詞の数を数える
    if (pos[kazu][1] == "IN" or pos[kazu][1] == "TO") and (pos[kazu+1][1] not in dousi ) and (pos[kazu][0].lower() in zentisi_list):
        print(pos[kazu][0], pos[kazu+1][1])
        zentisi+=1

    #いらない記号は排除
    if (re.match("\W", pos[kazu][1].lower())) and (pos[kazu][0].lower() not in kigou_reigai) :
        kigou+=1
    #品詞をリストに入れる
    #もう出ている品詞なら，hinsi_kosuuの数を１増やす
    elif pos[kazu][1] in hinsi:
        list_bangou=hinsi.index(pos[kazu][1])
        hinsi_kosuu[list_bangou]=hinsi_kosuu[list_bangou]+1
        
    #新しい品詞が出てきたら，hinsiリストに品詞を追加して，hinsi_kosuuリストを１にする．
    else:
        hinsi.append(pos[kazu][1])
        hinsi_kosuu.append(1)



    kazu+=1




print("前置詞",zentisi)
zentai = sum(hinsi_kosuu)
print("総単語数",zentai)


#発生率の計算
hasseiritu = (zentisi/zentai)*1000
print('前置詞の発生率:', hasseiritu)
print(72.519/1000*15541)
print(72.519/1000*15527)
