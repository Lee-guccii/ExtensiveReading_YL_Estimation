import nltk
import numpy as np
import re
import copy

#text_listにリストとして読み込む
with open('book2.txt', 'r') as f:
    #改行("\n")を""に変換
    #text_list = f.read().splitlines()
    text = f.read()


#正規表現で"を削除
text = re.sub('"', '', text)
text = text.lower()

morph = nltk.word_tokenize(text)
pos = nltk.pos_tag(morph)
#print(pos)

kazu=0
hinsi=[]#品詞の名前
hinsi_kosuu=[]#品詞の個数．配列は品詞の名前と対応している．
list_bangou=0

be=["is","was","are","ware","am","been","'m","'re","not","n't"]
be_sinkou=["is","are","am","'m","'re"]
be_kanryou=["was","ware","been"]

kigou=0
kigou_reigai=["=","+","'"]



zisei_kazu=0 #変数
zisei=0 #時制，アスペクトの数
zisei_kurikaesi=0 #繰り返されている数


while kazu < len(pos):
    #未来形
    if pos[kazu][1] == "VBG":
        #アスペクト
        #未来形で進行
        if pos[kazu-1][0] in be_sinkou:
            if zisei_kazu==0:
                zisei_1 ="VBG_s"
            else:
                zisei_2 ="VBG_s"
            zisei+=1
        elif pos[kazu-1][0] in be_kanryou:
            if zisei_kazu==0:
                zisei_1 ="VBG_k"
            else:
                zisei_2 ="VBG_k"
            zisei_kazu+=1
            zisei+=1
    #過去形
    elif pos[kazu][1] == "VBD":
        #アスペクト
        if pos[kazu-1][0] in be_sinkou:
            if zisei_kazu==0:
                zisei_1 ="VBD_s"
            else:
                zisei_2 ="VBD_s"
            zisei+=1
        elif pos[kazu-1][0] in be_kanryou:
            if zisei_kazu==0:
                zisei_1 ="VBD_k"
            else:
                zisei_2 ="VBD_k"
            zisei_kazu+=1
            zisei+=1
    #原形
    elif pos[kazu][1] == "VB":
        if zisei_kazu==0:
            zisei_1 ="VB"
            zisei+=1
        else:
            zisei_2 ="VB"
            zisei+=1
        zisei_kazu+=1
        

    #時制＋アスペクトが繰り返されているか確認
    if zisei_kazu == 2:
        if zisei_1 == zisei_2:
            zisei_kurikaesi+=1
        zisei_1 = zisei_2
        zisei_kazu =1

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




#print(hinsi)
#print(hinsi_kosuu)


print("時制の繰り返し",zisei_kurikaesi)
print("時制",zisei)
zisei_sukoa=zisei_kurikaesi/zisei
print(zisei_sukoa)
#zentai = sum(hinsi_kosuu)
#print("総単語数",zentai)
#0.834	0.836 0.851
#0.8645465253239105 0.894649751792609 0.8840952994204765 0.9359415305245056


