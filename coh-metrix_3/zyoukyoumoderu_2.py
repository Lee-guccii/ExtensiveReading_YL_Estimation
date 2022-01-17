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

keisankekka=[] #１テキストでの計算結果


while text_suu < 65:
    #text_listにリストとして読み込む
    with open('book'+ str(text_suu) +'.txt', 'r') as f:
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
            if pos[kazu-1][0] in be_sinkou:
                if zisei_kazu==0:
                    zisei_1 ="VBG_s"
                else:
                    zisei_2 ="VBG_s"
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
            else:
                zisei_2 ="VB"
            zisei_kazu+=1
            zisei+=1

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


    #計算結果
    zisei_sukoa=zisei_kurikaesi/zisei
    
    #結果をリストに入れる
    keisankekka.append(zisei_sukoa)

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

print("状況モデルレベル - 時制とアスペクトの繰り返しする割合")
print("相関結果:", soukan)

print("時制とアスペクトの繰り返しする割合:", keisankekka)



