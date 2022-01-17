import nltk
import numpy as np
import re
import copy

#text_listにリストとして読み込む
with open('book/book33.txt', 'r') as f:
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
naiyougo_list=["NN","NNS", "NNP", "NNPS", "VB","VBD","VBG", "VBN", "VBP", "VBZ","JJ", "JJR", "JJS", "RB", "RBR", "RBS","CD","UH"]#名詞，動詞，形容詞，副詞，基数，感嘆詞
#naiyougo_list=["NN", "VB", "JJ", "RB"] #名詞，動詞，形容詞，副詞

naiyougo_iti=[]
naiyougo_ni=[]
kigou=0
kigou_reigai=["=","+","'"]
bunnsuu=0

zyuuhuku_list=[]

zyuuhuku_dic={}

tangosuu_1=0
tangosuu_2=0
a=0 #文の数確認
wariai=[]#重複してる内容語の割合を隣接している文ごと配列に入れる


while kazu < len(pos):
    #文ごとの文字数を数える
    tangosuu_2+=1

    #. が出たら，数を数える
    if pos[kazu][1] == ".":
        if bunnsuu == 0:
            bunnsuu=1

            tangosuu_1=tangosuu_2
            a+=tangosuu_1
            tangosuu_2=0
            
        
        else:
            purasu = set(naiyougo_iti) & set(naiyougo_ni)
            naiyougo+=len(purasu) #重複していた内容語の個数
            purasu2=list(purasu) #リストに変更
            zyuuhuku_list = zyuuhuku_list+purasu2 #重複している内容語をリストに追加
            naiyougo_iti.clear() #リストの中身を消す
            naiyougo_iti = copy.copy(naiyougo_ni) #リスト２の内容をリスト１に入れ替える
            naiyougo_ni.clear() #リスト２の中身を消す

            #内容語の数/隣接する文の単語数
            if tangosuu_1!=0 and tangosuu_2!=0:
                wariai.append(len(purasu)/(tangosuu_1+tangosuu_2))
                
            else:
                wariai.append(0)
                    
            a+=tangosuu_2
            tangosuu_1=tangosuu_2
            tangosuu_2=0
            




    #内容語ができてきたらリストに入れる
    elif pos[kazu][1] in naiyougo_list:
        if bunnsuu == 0:
            naiyougo_iti.append(pos[kazu][0])

        else:
            naiyougo_ni.append(pos[kazu][0])
            
    
     

    #いらない記号は排除
    if (re.match("\W", pos[kazu][1].lower())) and (pos[kazu][0].lower() not in kigou_reigai) :
        kigou+=1
        tangosuu_2-=1
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

print("内容語",naiyougo)
zentai = sum(hinsi_kosuu)
print("総単語数",zentai)



#重複する内容語の割合
hasseiritu = sum(wariai)/len(wariai)

print('平均値: ', hasseiritu)


print(a)
print(len(wariai))
print(sum(wariai))



#0.154	0.102
#0.118	0.106