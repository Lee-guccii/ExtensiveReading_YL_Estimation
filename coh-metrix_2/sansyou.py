import nltk
import numpy as np
import re
import copy

#text_listにリストとして読み込む
with open('book33.txt', 'r') as f:
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

naiyougo=0
naiyougo_list=["NN","NNS", "NNP", "NNPS", "VB", "VBN", "VBP", "VBZ","JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
naiyougo_list=["NN", "VB", "JJ", "RB"] #名詞，動詞，形容詞，副詞

naiyougo_iti=[]
naiyougo_ni=[]
kigou=0
kigou_reigai=["=","+","'"]
bunnsuu=0
bun_kazu=0
zyuuhuku_list=[]

zyuuhuku_dic={}

while kazu < len(pos):
    #. が出たら，数を数える
    if pos[kazu][1] == ".":
        if bunnsuu == 0:
            bunnsuu=1
        
        else:
            purasu = set(naiyougo_iti) & set(naiyougo_ni)
            naiyougo+=len(purasu) #重複していた内容語の個数
            purasu2=list(purasu) #リストに変更
            zyuuhuku_list = zyuuhuku_list+purasu2 #重複している内容語をリストに追加
            naiyougo_iti.clear() #リストの中身を消す
            naiyougo_iti = copy.copy(naiyougo_ni) #リスト２の内容をリスト１に入れ替える
            naiyougo_ni.clear() #リスト２の中身を消す

        bun_kazu+=1


    #内容語ができてきたらリストに入れる
    elif pos[kazu][1] in naiyougo_list:
            if bunnsuu == 0:
                naiyougo_iti.append(pos[kazu][0])

            else:
                naiyougo_ni.append(pos[kazu][0])
            
            #品詞をリストに入れる
            #もう出ている品詞なら，hinsi_kosuuの数を１増やす
            if pos[kazu][1] in hinsi:
                list_bangou=hinsi.index(pos[kazu][1])
                hinsi_kosuu[list_bangou]=hinsi_kosuu[list_bangou]+1
            #新しい品詞が出てきたら，hinsiリストに品詞を追加して，hinsi_kosuuリストを１にする．
            else:
                hinsi.append(pos[kazu][1])
                hinsi_kosuu.append(1)
            
            zyuuhuku_dic[pos[kazu][0]] = pos[kazu][1]
     

    #いらない記号は排除
    elif (re.match("\W", pos[kazu][1].lower())) and (pos[kazu][0].lower() not in kigou_reigai) :
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



meisi=0
dousi=0
keiyousi=0
hukusi=0
zyuuhuku_kazu=0
#重複している内容語を品詞分け
while zyuuhuku_kazu < len(zyuuhuku_list):
    if zyuuhuku_list[zyuuhuku_kazu] in zyuuhuku_dic.keys():
        #print(zyuuhuku_dic[zyuuhuku_list[zyuuhuku_kazu]])
        if zyuuhuku_dic[zyuuhuku_list[zyuuhuku_kazu]] == "NN":
            meisi+=1

        elif zyuuhuku_dic[zyuuhuku_list[zyuuhuku_kazu]] == "VB":
            dousi+=1

        elif zyuuhuku_dic[zyuuhuku_list[zyuuhuku_kazu]] == "JJ":
            keiyousi+=1

        else:
            hukusi+=1      
    zyuuhuku_kazu+=1


list_bangou=hinsi.index("NN")
hinsi_kosuu[list_bangou]=hinsi_kosuu[list_bangou]-meisi

list_bangou=hinsi.index("VB")
hinsi_kosuu[list_bangou]=hinsi_kosuu[list_bangou]-dousi

list_bangou=hinsi.index("JJ")
hinsi_kosuu[list_bangou]=hinsi_kosuu[list_bangou]-keiyousi

list_bangou=hinsi.index("RB")
hinsi_kosuu[list_bangou]=hinsi_kosuu[list_bangou]-hukusi

hinsi.append("naiyougo")
hinsi_kosuu.append(naiyougo)


print(hinsi)
print(hinsi_kosuu)

print("内容語",naiyougo)
zentai = sum(hinsi_kosuu)
print("総単語数",zentai)

#リストの中身全部を文数で割る
hinsi_kosuu2 = [n/bun_kazu for n in hinsi_kosuu]

#標準偏差
std = np.std(hinsi_kosuu)
std2 = np.std(hinsi_kosuu2)

print('標準偏差: {}'.format(std))
print('標準偏差: {}'.format(std2))
print(std2)



