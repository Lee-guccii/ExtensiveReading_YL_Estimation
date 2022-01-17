import nltk
import numpy as np
import re


with open('book/book33.txt', 'r') as f:
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

inga_dousi=0
#１語の因果関係の動詞
ingadousi_list1 = ["result", "lead","bring","brought","contribute","derive","trigger","explain"]
#２語の因果関係の動詞
ingadousi_list2 = ["lead to", "result in", "bring about", "contribute to","come from", "result from","stem from", "account for"]
#３語の因果関係の動詞
ingadousi_list3 = ["is responsible for", "is derived from", "are responsible for", "give rise to"]
kigou=0
kigou_reigai=["=","+","'"]



#文字列であるテキストを空白ごとで配列にするリストにする
text_list=text.split(' ')

while kazu < len(text_list):
    #リストを空白で繋げて文字列に変更
    dousi3 = ' '.join(text_list[kazu:kazu+3])#3文字
    dousi2 = ' '.join(text_list[kazu:kazu+2])#2文字
    dousi1 = text_list[kazu]#1文字

    #3語の因果関係の動詞
    if dousi3.lower() in ingadousi_list3:
        inga_dousi+=1

    #2語の因果関係の動詞
    elif dousi2.lower() in ingadousi_list2:
        inga_dousi+=1

    #1語の因果関係の動詞
    elif dousi1.lower() in ingadousi_list1:
        inga_dousi+=1
    kazu+=1




kazu_2=0
while kazu_2 < len(pos):
    #いらない記号は排除
    if (re.match(r"\W", pos[kazu_2][1].lower())) and (pos[kazu_2][0].lower() not in kigou_reigai) :
        kigou+=1
    #品詞をリストに入れる
    #もう出ている品詞なら，hinsi_kosuuの数を１増やす
    elif pos[kazu_2][1] in hinsi:
        list_bangou=hinsi.index(pos[kazu_2][1])
        hinsi_kosuu[list_bangou]=hinsi_kosuu[list_bangou]+1
        
    #新しい品詞が出てきたら，hinsiリストに品詞を追加して，hinsi_kosuuリストを１にする．
    else:
        hinsi.append(pos[kazu_2][1])
        hinsi_kosuu.append(1)

    kazu_2+=1



zentai = sum(hinsi_kosuu)
#print("総単語数",zentai)


#発生率の計算
hasseiritu = (inga_dousi/zentai)*100
print('因果関係の動詞の発生率:', hasseiritu)







#36.932	42.520
#31.687	20.389
