import nltk
import numpy as np
import re
from scipy.stats import spearmanr


#text_listにリストとして読み込む
with open('book/book2.txt', 'r') as f:
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

#因果関係のある接続詞
inga_setuzokusi=["come", "comes", "came","coming", "result", "results", "resulted","resulting","lead","leads","leading","led","contribute","contributes","contributed","contributing","derive","derivss","deriving","derived"]

#接続詞の品詞
setuzokusi=["VB","VBD","VBG","VBN","VBP","VBZ"]

inga=0
a=0

while kazu < len(pos):
    #もし接続詞なら
    if pos[kazu][1] in setuzokusi:
        a+=1
        if pos[kazu][0].lower() in inga_setuzokusi:
            inga+=1

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




zentai = sum(hinsi_kosuu)
#総単語数
print("総単語数",zentai)
print(inga)
print(a)

print(inga/zentai*1000)
print(inga/a*1000)

hasseiritu = inga/zentai*1000

#計算結果をリストに入れる







print(25.568*352/1000)
print(27.307/15527*1000)
    #36.932	42.520
    #31.687	20.389
