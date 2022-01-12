import nltk
import numpy as np
import re

#text_listにリストとして読み込む
with open('book33.txt', 'r') as f:
    #改行("\n")を""に変換
    #text_list = f.read().splitlines()
    text = f.read()

morph = nltk.word_tokenize(text)
pos = nltk.pos_tag(morph)
#print(pos)

kazu=0
hinsi=[]#品詞の名前
hinsi_kosuu=[]#品詞の個数．配列は品詞の名前と対応している．
list_bangou=0

itininsyou=0
itininsyou_list = ["i", "my", "me", "myself"]
kigou=0
kigou_reigai=["=","+","'","''"]


while kazu < len(pos):
    #一人称単数代名詞の数を数える
    if pos[kazu][0].lower() in itininsyou_list:
        itininsyou+=1

    #新しい品詞が出てきたら，hinsiリストに品詞を追加して，hinsi_kosuuリストを１にする．
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




print("一人称単数代名詞",itininsyou)
zentai = sum(hinsi_kosuu)
print("総単語数",zentai)


#発生率の計算
hasseiritu = (itininsyou/zentai)*1000
print('一人称単数代名詞の発生率:', hasseiritu)


print(((119+27+17+1)/15527)*1000)