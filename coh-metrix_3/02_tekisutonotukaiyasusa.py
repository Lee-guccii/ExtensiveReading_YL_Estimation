import nltk
import numpy as np
import re
import copy

#text_listにリストとして読み込む
with open('book/book1.txt', 'r') as f:
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

#動詞の原形，過去形，動名詞or現在分詞, 過去分詞，三人称単数以外の現在形，三人称単数の現在形
dousi=["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"] 

kaisuu=0

dousi_kosuu=0



zyuuhuku_list=[]

vb=0
vbd=0
vbg=0
vbn=0
vbp=0
vbz=0


while kazu < len(pos):
    #動詞が出たら，数を数える
    if pos[kazu][1] in dousi:
        if kaisuu == 0:
            dousi_iti=pos[kazu][0]
            kaisuu=1
        
        else:
            dousi_ni=pos[kazu][0]
            print(dousi_ni)
            if dousi_iti == dousi_ni:
                dousi_kosuu+=1 #重複していた動詞の個数
                zyuuhuku_list = dousi_ni #重複している動詞をリストに追加
                


                #重複した動詞の品詞の個数確認
                if pos[kazu][1] == "VB":
                    vb+=1
                elif pos[kazu][1] == "VBG":
                    vbg+=1
                elif pos[kazu][1] == "VBN":
                    vbn+=1
                elif pos[kazu][1] == "VBP":
                    vbp+=1
                elif pos[kazu][1] == "VBZ":
                    vbz+=1

            dousi_iti=dousi_ni
     

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

#重複した動詞をリストに追加
hinsi.append("dousi_zyuuhuku")
hinsi_kosuu.append(dousi_kosuu)

#dousi_zyuuhukuの配列番号を代入
dousi_bangou = hinsi.index("dousi_zyuuhuku")

print(hinsi)
print(hinsi_kosuu)

#重複した分個数を引く
vb_bangou = hinsi.index("VB")
hinsi_kosuu[vb_bangou]=-vb

vbd_bangou = hinsi.index("VBD")
hinsi_kosuu[vbd_bangou]=-vbd

vbg_bangou = hinsi.index("VBG")
hinsi_kosuu[vbg_bangou]=-vbg

vbn_bangou = hinsi.index("VBN")
hinsi_kosuu[vbn_bangou]=-vbn

vbp_bangou = hinsi.index("VBP")
hinsi_kosuu[vbp_bangou]=-vbp

vbz_bangou = hinsi.index("VBZ")
hinsi_kosuu[vbz_bangou]=-vbz



print(hinsi)
print(hinsi_kosuu)

print("動詞",dousi_kosuu)
zentai = sum(hinsi_kosuu)
print("総単語数",zentai)

#zスコアの計算
#平均値
mean = np.mean(hinsi_kosuu)
print(mean)
#標準偏差
std = np.std(hinsi_kosuu)
#標準化
z = (hinsi_kosuu - mean) / std
print('standardized data(z): {}'.format(z))
print('standardized data(z)(接続詞のzスコア): {}'.format(z[dousi_bangou]))
print(z[dousi_bangou])


#0.875	-0.047
#-0.594	-0.491