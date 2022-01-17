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

keisankekka=[] #１テキストでの計算結果


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

    itininsyou=0
    itininsyou_list = ["i", "my", "me", "myself"]
    kigou=0
    kigou_reigai=["=","+","'"]



    while kazu < len(pos):
        #一人称単数代名詞の数を数える
        if ((pos[kazu][1] == "PRP" or pos[kazu][1] == "PRP$") and pos[kazu][0].lower() in itininsyou_list):
            #print(pos[kazu][0])
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

    #print(hinsi)
    #print(hinsi_kosuu)


    #総単語数
    zentai = sum(hinsi_kosuu)



    #発生率の計算
    hasseiritu = (itininsyou/zentai)*1000


    #計算結果をリストに入れる
    keisankekka.append(hasseiritu)

    print(text_suu)

    text_suu+=1




###############################
#相関係数の計算

#相関計算
x_np = np.array(x_zenbu)
y_np = np.array(keisankekka)


#シャピロウィルク検定で正規性の確認
#w値とp_value
shap_w, shap_p_value = stats.shapiro(keisankekka)
#p_valueが0.05以上なら，帰無仮説が採択→正規性がある
if shap_p_value >= 0.05 :
    print("正規性があるといえる")
    #print(shap_p_value)


    #ピアソンの相関係数をとる
    # 相関行列を計算
    coef = np.corrcoef(x_np, y_np)
    soukan = coef[0][1]


#p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
else:
    print("正規性があるといえない")
    #print(shap_p_value)
            
    #スピアマンの順位相関係数
    correlation, pvalue = spearmanr(x_zenbu, keisankekka)
    soukan = correlation

print("単語情報レベル - 一人称単一形式の発生割合")
print("相関結果:", soukan)

print("一人称単一形式の発生割合:", keisankekka)


