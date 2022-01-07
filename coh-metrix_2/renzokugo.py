import nltk
import numpy as np
import re

#text_listにリストとして読み込む
with open('book8_3.txt', 'r') as f:
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

setuzoku=0
#時間的接続詞
setuzokusi_list = ["hour later", "a consequence of", "after some time", "after a time", "after", "after this", "after that", "after all", "again", "all this time", "as", "as soon as", "as long as", "as a consequence", "at first in the end", "at first finally", "at last", "at once", "at the same time", "at this moment", "at this point", "before", "by this time", "earlier", "even then", "finally", "first", "next", "second", "then", "follow that", "from now on", "further", "immediately", "in the meantime", "instantly", "It follows that", "It follows", "just before", "later", "meanwhile", "now that", "on another occasion", "once again", "once more", "only when", "presently", "previously", "secondly", "simultaneously", "since", "so far", "soon", "suddenly", "the consequence of", "the last time", "the previous moment", "then again", "then at last", "this time", "throughout", "to that end", "up till that time", "up to now", "when", "whenever", "while", "until", "until then"]
#１語の時間的接続詞
setuzokusi_list1 = ["after","again", "as","before","earlier","finally", "first", "next", "second", "then", "immediately","instantly","later", "meanwhile","presently", "previously", "secondly", "simultaneously", "since", "soon", "suddenly", "throughout","when", "whenever", "while", "until"]
#２語の時間的接続詞
setuzokusi_list2 = ["hour later", "after this", "after that", "after all","at last", "at once","even then", "follow that","It follows", "just before", "now that", "once again", "once more", "only when", "simultaneously", "so far", "then again", "this time", "until then"]
#３語の時間的接続詞
setuzokusi_list3 = ["a consequence of", "after some time", "after a time","all this time", "as soon as", "as long as", "as a consequence", "at first finally", "at this moment", "at this point", "by this time", "from now on", "in the meantime", "It follows that", "on another occasion", "the consequence of", "the last time", "the previous moment", "then at last", "to that end", "up to now"]
#４語の時間的接続詞
setuzokusi_list4 = ["at first in the end", "at the same time", "up till that time"]
kigou=0
kigou_reigai=["=","+","'"]



#文字列であるテキストを空白ごとで配列にするリストにする
text_list=text.split(' ')

while kazu < len(text_list):
    #リストを空白で繋げて文字列に変更
    setuzokusi4 = ' '.join(text_list[kazu:kazu+4])#4文字
    setuzokusi3 = ' '.join(text_list[kazu:kazu+3])#3文字
    setuzokusi2 = ' '.join(text_list[kazu:kazu+2])#2文字
    setuzokusi1 = text_list[kazu]#1文字
    #4語の時間的接続詞
    if setuzokusi4.lower() in setuzokusi_list4:
        setuzoku+=1

    #3語の時間的接続詞
    elif setuzokusi3.lower() in setuzokusi_list3:
        setuzoku+=1

    #2語の時間的接続詞
    elif setuzokusi2.lower() in setuzokusi_list2:
        setuzoku+=1

    #1語の時間的接続詞
    elif setuzokusi1.lower() in setuzokusi_list1:
        setuzoku+=1
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


print("前置詞",setuzoku)
zentai = sum(hinsi_kosuu)
print("総単語数",zentai)


#発生率の計算
hasseiritu = (setuzoku/zentai)*1000
print('前置詞の発生率:', hasseiritu)



