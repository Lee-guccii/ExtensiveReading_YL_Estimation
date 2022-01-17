import nltk
import numpy as np
import re
import copy

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
    with open('book/book'+ str(text_suu) +'.txt', 'r') as f:
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

            #リストの中に動詞が入ってなかったら（重複してなかったら）
            if pos[kazu][0] not in zyuuhuku_list:
                zyuuhuku_list.append(pos[kazu][0])

            #リストの中に動詞が入ってたら（重複してたら)
            else:
                #print(pos[kazu][0],pos[kazu][1])
                #重複した動詞の品詞の個数確認
                if pos[kazu][1] == "VB":
                    vb+=1
                elif pos[kazu][1] == "VBD":
                    vbd+=1
                elif pos[kazu][1] == "VBG":
                    vbg+=1
                elif pos[kazu][1] == "VBN":
                    vbn+=1
                elif pos[kazu][1] == "VBP":
                    vbp+=1
                elif pos[kazu][1] == "VBZ":
                    vbz+=1
                

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

    



    dousi_kosuu=(vb+vbd+vbg+vbn+vbp+vbz)
    

    
    

    #重複した動詞の個数
    #print("動詞",dousi_kosuu)

    zentai = sum(hinsi_kosuu)
    
    hasseiritu=(dousi_kosuu/zentai)*1000
    
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


print("記述的レベル - 総単語数")
print("相関結果:", soukan)

print("総単語数:", keisankekka)
    






    #-0.594	-0.491

