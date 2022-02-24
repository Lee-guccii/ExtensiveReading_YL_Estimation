import numpy as np
from scipy import stats
from scipy.stats import spearmanr
import textstat
import matplotlib.pyplot as plt

#実際のYL
yl= [1.1, 3.5, 4.7, 1.4, 2.1, 5.7, 4.1, 0.7, 5, 6, 
    6.5, 8, 5, 7, 8, 5.5, 1.8, 1.2, 2.6, 3.6, 
    2, 4.4, 4.8, 7, 7, 7.5, 6.6, 5.1, 7.6, 6.5,
    8.5, 7.5]

#予測したYL
y_pred=[3.69360859, 3.86496094, 3.13151928, 1.48092297, 2.32543171, 4.33080428, 3.7525334,  2.52524111, 5.10847349, 5.4741146,
        5.24582291, 7.44985909, 5.74756733, 7.11254456, 8.18835643, 5.37954098, 2.35875224, 1.72260055, 2.95258842, 3.90411524,
        2.84372762, 3.48184256, 4.00933722, 8.04019785, 6.68558658, 8.03455366, 7.22292652, 5.96114542, 7.11254089, 5.78925801,
        6.81335284, 6.43428265]


#ERF
fre=[]

#テストデータのテキスト番号
test_text=[1, 3, 6, 9, 12, 20, 25, 31, 33, 34, 36, 37, 39, 41, 45, 60]

test_text2=[5, 9, 12, 15, 23, 33, 43, 55, 56, 60, 65, 76, 81, 84, 86, 99]


#最初の16冊
keisankekka=[]#１テキストでの計算結果

text_suu=1 #テキストの番号

while text_suu < 64:

    if text_suu in test_text:
        #text_listにリストとして読み込む
        with open('/workspace/python/ExtensiveReading_YL_Estimation/coh-metrix_3/book/book'+ str(text_suu) +'.txt', 'r') as f:
            #改行("\n")を""に変換
            #text_list = f.read().splitlines()
            text = f.read()


        #FREを調べる
        fre.append(textstat.flesch_reading_ease(text))
        

    text_suu+=1


#次の16冊
text_suu=1 #テキストの番号

while text_suu < 100:

    if text_suu in test_text2:
        #text_listにリストとして読み込む
        with open('book'+ str(text_suu) +'_test1.txt', 'r') as f:
            #改行("\n")を""に変換
            #text_list = f.read().splitlines()
            text = f.read()


        #FREを調べる
        fre.append(textstat.flesch_reading_ease(text))
        

    text_suu+=1



###############################
#相関係数の計算

#相関計算
x_np = np.array(yl) #YL
y_np = np.array(fre) #FRE
y_np2 = np.array(y_pred) #予測したYL


#シャピロウィルク検定で正規性の確認
#w値とp_value
shap_w_x, shap_p_value_x = stats.shapiro(yl)
shap_w_y, shap_p_value_y = stats.shapiro(fre)
shap_w_y2, shap_p_value_y2 = stats.shapiro(y_pred)


#YLとERF
#p_valueが0.05以上なら，帰無仮説が採択→正規性がある
if shap_p_value_x >= 0.05 and shap_p_value_y >= 0.05:
    #print("正規性があるといえる")

    #ピアソンの相関係数をとる
    # 相関行列を計算
    coef = np.corrcoef(x_np, y_np)
    soukan = coef[0][1]


#p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
else:
    #print("正規性があるといえない")

    #スピアマンの順位相関係数
    correlation, pvalue = spearmanr(x_np, y_np)
    soukan = correlation


print("YL-ERFの相関")
print(soukan)
print("--------------")

#グラフ

plt.scatter(yl, fre)
plt.xlabel('YL')
plt.ylabel('FRE score')
#plt.legend()
plt.grid()
#plt.show()
plt.savefig("YL-FRE_score.png")
plt.figure().tight_layout() 



######################
#YLと予測したYL
#p_valueが0.05以上なら，帰無仮説が採択→正規性がある
if shap_p_value_x >= 0.05 and shap_p_value_y2 >= 0.05:
    #print("正規性があるといえる")

    #ピアソンの相関係数をとる
    # 相関行列を計算
    coef2 = np.corrcoef(x_np, y_np2)
    soukan2 = coef2[0][1]


#p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
else:
    #print("正規性があるといえない")

    #スピアマンの順位相関係数
    correlation2, pvalue2 = spearmanr(x_np, y_np2)
    soukan2 = correlation2


print("YL-y_predの相関")
print(soukan2)
print("--------------")

#グラフ

plt.scatter(yl, y_pred)
plt.xlabel('YL')
plt.ylabel('y_pred')
#plt.legend()
plt.grid()
#plt.show()
plt.savefig("YL-y_pred.png")
plt.figure().tight_layout() 




import matplotlib.pyplot as plt
x=[2.5936085940242886, 0.3649609355211716, -1.5684807178864082, 0.08092297493428235, 0.22543171481307445, -1.3691957161909167, -0.3474666004673743, 1.8252411101316153, 0.55875223949132, 0.5226005465508596, 0.3525884186972337, 0.3041152432565233, 0.8437276168620489, -0.9181574433326762, -0.7906627803715223, 0.10847348531766343, -0.5258853994325055, -1.2541770882612653, -0.5501409126883967, 0.7475673290440792, 0.11254455566384358, 0.18835643338229602, -0.12045902195570513, 1.0401978506856189, -0.3144134218532173, 0.5345536552762553, 0.6229265175369045, 0.8611454214443981, -0.48745911396300734, -0.7107419915524602, -1.6866471577013176, -1.0657173549843346]
fig, ax = plt.subplots()
ax.boxplot(x)
plt.savefig("誤差_箱ヒゲ図.png")

