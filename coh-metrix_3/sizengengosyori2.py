import nltk
import numpy as np
import re

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
kigou=0
kigou_reigai=["=","+","'"]

gyaku_setuzokusi=0
#gyaku = ["however", "but", "yet", "though", "in spite of"]
gyaku = ["however", "but"]

huka_setuzokusi=0
#huka = ["and", "also", "another", "moreover", "as well as", "in addition"]
huka = ["and", "moreover"]

hikaku_setuzokusi=0
#hikaku = ["eqally", "similary", "likewise", "whereas", "in contrast", "comparatively"]
hikaku = ["although", "whereas"]

while kazu < len(pos):
    #逆説，付加，比較の接続詞があるか
    if (pos[kazu][0].lower() in gyaku) and (pos[kazu][1] =="CC" or pos[kazu][1] =="IN"):
        gyaku_setuzokusi+=1

    elif (pos[kazu][0].lower() in huka) and (pos[kazu][1] =="CC" or pos[kazu][1] =="IN"):
        huka_setuzokusi+=1

    elif (pos[kazu][0].lower() in hikaku) and (pos[kazu][1] =="CC" or pos[kazu][1] =="IN"):
        hikaku_setuzokusi+=1
    
    #いらない記号は排除
    else:
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




hinsi.append("gyaku")
hinsi_kosuu.append(gyaku_setuzokusi)

hinsi.append("huka")
hinsi_kosuu.append(huka_setuzokusi)

hinsi.append("hikaku")
hinsi_kosuu.append(hikaku_setuzokusi)


gyaku_bangou = hinsi.index("gyaku")
huka_bangou = hinsi.index("huka")
hikaku_bangou = hinsi.index("hikaku")




print(hinsi)
print(hinsi_kosuu)



#zスコアの計算
#平均値
mean = np.mean(hinsi_kosuu)
#print(mean)
#標準偏差
std = np.std(hinsi_kosuu)
#標準化
z = (hinsi_kosuu - mean) / std
#print('standardized data(z): {}'.format(z))
#print('standardized data(z)(逆説接続詞のzスコア): {}'.format(z[gyaku_bangou]))
#print('standardized data(z)(付加接続詞のzスコア): {}'.format(z[huka_bangou]))
#print('standardized data(z)(比較接続詞のzスコア): {}'.format(z[hikaku_bangou]))

print((z[gyaku_bangou]+z[huka_bangou]+z[hikaku_bangou])/3)

-2.403	-3.347

#３つの接続詞と他の品詞とのzスコアの平均値