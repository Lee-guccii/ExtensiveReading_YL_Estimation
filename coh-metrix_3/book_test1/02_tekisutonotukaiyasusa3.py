import nltk
import numpy as np
import re
import copy

from scipy import stats
from scipy.stats import spearmanr

#多読図書のYL
#x_tadoku = [1.4,1.8,1.8,1.8,1.8,1.4,1.4,1.4,1.2,1.2,
#                   1.2,2.6,2.6,2.6,3.6,3.6,3.2,3.2,2.4,2.4,
#                   2.4,2.4,2,2,2,2,2.6,3.6,3.2,2.8,
#                   2.8,2.8,4.4,4.4,4.4,4.4,4,4,4,4,
#                   4.8,4.8,4.8,2.5,2.5,2.5,2.5,2.5,2.5,2.5]

#一般図書のYL
#x_ippan = [8,6.6,8.5,6.5,7,7,7,7.6,7.5,7.5,
#                7.3,7,8.2,7,6.6,7.7,7,5,5.5,7,
#                7,7,7,7,7.5,5.1,7,7,7,7,
#                7.6,6.5,7,6.5,7,8.5,7,6.5,9.5,
#                7.7,7.5,7,7,8.5,7,5.5,6.6,8.5,7.5,8]


#多読図書と一般図書のYL
#x_zenbu = x_tadoku + x_ippan

x_zenbu = [1.2, 1.2, 3.6, 6, 6.7, 7, 7, 5, 6.5, 7,
            7, 7, 7, 2.5, 6.5, 8, 5.7, 7, 7, 7,
            7, 7, 5.5, 2.5, 7, 2.5, 6.2, 7, 5, 2.5,
            7.7, 2.5, 8, 5.5, 8, 6, 7.5, 7, 6.5, 2.5,
            8, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 2.5,
            2.5, 7.5, 5.5, 7, 7, 5, 7, 6.3, 7, 7,
            6.5, 8, 5.5, 7, 7, 7.7, 7, 7.5, 7, 7.5,
            7, 8.7, 7, 2.5, 7.5, 8, 2.5, 8, 8, 2.5,
            8, 6.5, 6.5, 8.5, 5, 2.5, 5, 7, 5, 5.5, 
            5.2, 7.5, 7, 5.5, 9.5, 6, 8.5, 4.7, 5, 1.8]


text_suu=101 #テキストの番号

keisankekka=[]#１テキストでの計算結果


while text_suu < 201:
    #text_listにリストとして読み込む
    with open('book'+ str(text_suu) +'_test1.txt', 'r') as f:
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




    #重複した分個数を引く
    if vb>0:
        vb_bangou = hinsi.index("VB")
        #hinsi_kosuu[vb_bangou]-=vb

    if vbd>0:
        vbd_bangou = hinsi.index("VBD")
        #hinsi_kosuu[vbd_bangou]-=vbd

    if vbg>0:
        vbg_bangou = hinsi.index("VBG")
        #hinsi_kosuu[vbg_bangou]-=vbg

    if vbn>0:
        vbn_bangou = hinsi.index("VBN")
        #hinsi_kosuu[vbn_bangou]-=vbn

    if vbp>0:
        vbp_bangou = hinsi.index("VBP")
        #hinsi_kosuu[vbp_bangou]-=vbp

    if vbz>0:
        vbz_bangou = hinsi.index("VBZ")
        #hinsi_kosuu[vbz_bangou]-=vbz


    jj_kosuu=0
    jjr_kosuu=0
    jjs_kosuu=0
    if  "JJ" in hinsi:
        jj_bangou=hinsi.index("JJ")
        jj_kosuu=hinsi_kosuu[jj_bangou]
        hinsi_kosuu.pop(jj_bangou)
        hinsi.pop(jj_bangou)

    if "JJR" in hinsi:
        jjr_bangou=hinsi.index("JJR")
        jjr_kosuu=hinsi_kosuu[jjr_bangou]
        hinsi_kosuu.pop(jjr_bangou)
        hinsi.pop(jjr_bangou)

    if  "JJS" in hinsi:
        jjs_bangou=hinsi.index("JJS")
        jjs_kosuu=hinsi_kosuu[jjs_bangou]
        hinsi_kosuu.pop(jjs_bangou)
        hinsi.pop(jjs_bangou)



    jj_zenbu = jj_kosuu + jjr_kosuu + jjs_kosuu

    hinsi.append("JJ_zenbu")
    hinsi_kosuu.append(jj_zenbu)



    nn_kosuu =0
    nns_kosuu =0
    nnp_kosuu =0
    nnps_kosuu =0

    if "NN" in hinsi:
        nn_bangou=hinsi.index("NN")
        nn_kosuu=hinsi_kosuu[nn_bangou]
        hinsi_kosuu.pop(nn_bangou)
        hinsi.pop(nn_bangou)

    if "NNS" in hinsi:
        nns_bangou=hinsi.index("NNS")
        nns_kosuu=hinsi_kosuu[nns_bangou]
        hinsi_kosuu.pop(nns_bangou)
        hinsi.pop(nns_bangou)

    if "NNP" in hinsi:
        nnp_bangou=hinsi.index("NNP")
        nnp_kosuu=hinsi_kosuu[nnp_bangou]
        hinsi_kosuu.pop(nnp_bangou)
        hinsi.pop(nnp_bangou)

    if "NNPS" in hinsi:
        nnps_bangou=hinsi.index("NNPS")
        nnps_kosuu=hinsi_kosuu[nnps_bangou]
        hinsi_kosuu.pop(nnps_bangou)
        hinsi.pop(nnps_bangou)



    nn_zenbu = nn_kosuu + nns_kosuu + nnp_kosuu + nnps_kosuu

    hinsi.append("NN_zenbu")
    hinsi_kosuu.append(nn_zenbu)





    rb_kosuu =0
    rbr_kosuu =0
    rbs_kosuu =0
    if "RB" in hinsi:
        rb_bangou=hinsi.index("RB")
        rb_kosuu=hinsi_kosuu[rb_bangou]
        hinsi_kosuu.pop(rb_bangou)
        hinsi.pop(rb_bangou)

    if "RBR" in hinsi:
        rbr_bangou=hinsi.index("RBR")
        rbr_kosuu=hinsi_kosuu[rbr_bangou]
        hinsi_kosuu.pop(rb_bangou)
        hinsi.pop(rb_bangou)
    if "RBS" in hinsi:
        rbs_bangou=hinsi.index("RBS")
        rbs_kosuu=hinsi_kosuu[rbs_bangou]
        hinsi_kosuu.pop(rb_bangou)
        hinsi.pop(rb_bangou)


    rb_zenbu = rb_kosuu + rbr_kosuu + rbs_kosuu

    hinsi.append("RB_zenbu")
    hinsi_kosuu.append(rb_zenbu)





    vb_kosuu =0
    vbd_kosuu =0
    vbg_kosuu =0
    vbn_kosuu =0
    vbp_kosuu =0
    vbz_kosuu =0
    if "VB" in hinsi:
        vb_bangou=hinsi.index("VB")
        vb_kosuu=hinsi_kosuu[vb_bangou]
        hinsi_kosuu.pop(vb_bangou)
        hinsi.pop(vb_bangou)

    if "VBD" in hinsi:
        vbd_bangou=hinsi.index("VBD")
        vbd_kosuu=hinsi_kosuu[vbd_bangou]
        hinsi_kosuu.pop(vbd_bangou)
        hinsi.pop(vbd_bangou)

    if "VBG" in hinsi:
        vbg_bangou=hinsi.index("VBG")
        vbg_kosuu=hinsi_kosuu[vbg_bangou]
        hinsi_kosuu.pop(vbg_bangou)
        hinsi.pop(vbg_bangou)

    if "VBN" in hinsi:
        vbn_bangou=hinsi.index("VBN")
        vbn_kosuu=hinsi_kosuu[vbn_bangou]
        hinsi_kosuu.pop(vbn_bangou)
        hinsi.pop(vbn_bangou)

    if "VBP" in hinsi:
        vbp_bangou=hinsi.index("VBP")
        vbp_kosuu=hinsi_kosuu[vbp_bangou]
        hinsi_kosuu.pop(vbp_bangou)
        hinsi.pop(vbp_bangou)

    if "VBZ" in hinsi:
        vbz_bangou=hinsi.index("VBZ")
        vbz_kosuu=hinsi_kosuu[vbz_bangou]
        hinsi_kosuu.pop(vbz_bangou)
        hinsi.pop(vbz_bangou)



    vb_zenbu = vb_kosuu + vbd_kosuu + vbg_kosuu + vbn_kosuu + vbp_kosuu + vbz_kosuu

    hinsi.append("VB_zenbu")
    hinsi_kosuu.append(vb_zenbu)



    dousi_kosuu=(vb+vbd+vbg+vbn+vbp+vbz)
    

    
    #重複した動詞をリストに追加
    hinsi.append("vb_zyuuhuku")
    hinsi_kosuu.append(vb)

    hinsi.append("vbd_zyuuhuku")
    hinsi_kosuu.append(vbd)

    hinsi.append("vbg_zyuuhuku")
    hinsi_kosuu.append(vbg)

    hinsi.append("vbn_zyuuhuku")
    hinsi_kosuu.append(vbn)

    hinsi.append("vbp_zyuuhuku")
    hinsi_kosuu.append(vbp)

    hinsi.append("vbz_zyuuhuku")
    hinsi_kosuu.append(vbz)



    #dousi_zyuuhukuの配列番号を代入
    vb_bangou = hinsi.index("vb_zyuuhuku")

    vbd_bangou = hinsi.index("vbd_zyuuhuku")

    vbg_bangou = hinsi.index("vbg_zyuuhuku")

    vbn_bangou = hinsi.index("vbn_zyuuhuku")

    vbp_bangou = hinsi.index("vbp_zyuuhuku")

    vbz_bangou = hinsi.index("vbz_zyuuhuku")

    

    #重複した動詞の個数
    #print("動詞",dousi_kosuu)

    zentai = sum(hinsi_kosuu)
    #print("総単語数",zentai)

    #zスコアの計算
    #平均値
    mean = np.mean(hinsi_kosuu)
    #print(mean)
    #標準偏差
    std = np.std(hinsi_kosuu)
    #標準化
    z = (hinsi_kosuu - mean) / std
    #print('standardized data(z): {}'.format(z))
    #print('standardized data(z)(接続詞のzスコア): {}'.format(z[dousi_bangou]))
    #print(z[dousi_bangou])

    hasseiritu=(z[vb_bangou]+z[vbd_bangou]+z[vbg_bangou]+z[vbn_bangou]+z[vbp_bangou]+z[vbz_bangou])/6
    
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

