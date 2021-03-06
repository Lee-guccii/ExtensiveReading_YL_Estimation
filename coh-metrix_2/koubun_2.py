import nltk
import numpy as np
import re

from scipy import stats
from scipy.stats import spearmanr

#多読図書のYL
x_tadoku = [1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 
            1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 3.3, 3.9, 5.7, 
            0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 
            0.7, 0.7]

#一般図書のYL
x_ippan = [5.0, 6.0, 6.5, 6.5, 8.0, 8.5, 7.0, 8.0, 5.0, 6.5, 
           8.0, 5.0, 8.0, 7.5, 5.5, 7.5, 8.0, 8.0, 7.0, 8.0, 
           8.0, 5.0, 8.0, 5.0, 5.0, 8.0, 8.5, 5.5, 8.0, 5.5,
           8.0, 5.0]


#多読図書と一般図書のYL
x_zenbu = x_tadoku + x_ippan


text_suu=1 #テキストの番号

keisankekka=[]#１テキストでの計算結果


while text_suu < 65:
    #text_listにリストとして読み込む
    with open('book'+ str(text_suu) +'.txt', 'r') as f:
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
        #if (pos[kazu][1] == "IN" or pos[kazu][1] == "TO") and (pos[kazu+1][1] == "DT" or pos[kazu+1][1] == "NN" or pos[kazu+1][1] == 'NNP' or pos[kazu+1][1] == 'NNS' or pos[kazu+1][1] == 'NNPS') and (pos[kazu][0].lower() in zentisi_list):
        if (pos[kazu][1] == "IN" or pos[kazu][1] == "TO") and (pos[kazu+1][1] not in dousi ) and (pos[kazu][0].lower() in zentisi_list):
        #if (pos[kazu][1] == "IN" or pos[kazu][1] == "TO") and (pos[kazu][0].lower() in zentisi_list):
            #print(pos[kazu][0], pos[kazu+1][1])
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


    #print("前置詞",zentisi)
    zentai = sum(hinsi_kosuu)
    #print("総単語数",zentai)


    #発生率の計算
    hasseiritu = (zentisi/zentai)*1000
    #print('前置詞の発生率:', hasseiritu)

    #計算結果をリストに入れる
    keisankekka.append(hasseiritu)
    print(text_suu)


    text_suu+=1





###############################
#相関係数の計算

#相関計算
x_np = np.array(x_zenbu)
y_np = np.array(keisankekka)



#x_zenbuが正規性がないので，スピアマンの相関係数
#スピアマンの順位相関係数
correlation, pvalue = spearmanr(x_zenbu, keisankekka)
soukan = correlation


print("構文パターン密度 - 前置詞句の発生率")
print("相関結果:", soukan)

print("前置詞の発生率:", keisankekka)