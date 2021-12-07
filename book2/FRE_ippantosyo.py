import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
import re
import textstat
from scipy import stats
from scipy.stats import spearmanr

#coding:utf-8    

###############
#一般図書のYL
#x = [8, 6.6, 8.5, 6.5, 5, 7, 6, 5, 5, 5, 6.5, 6.5, 7, 8.2, 7.6, 7.5, 7.5, 7.3, 7, 8.2, 8, 8.5, 7, 6.6, 7.7, 7, 5, 8.5, 8.5, 7, 7, 8
#,7, 5, 7, 7, 7.3, 8, 7, 7, 6.5, 7, 8.5, 7.6, 6.5, 7.5, 6.5]
x = [1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 3.3, 3.9, 5.7, 0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 0.7, 0.7, 8, 6.6, 8.5, 6.5, 5, 7, 6, 5, 5, 5, 6.5, 6.5, 7, 8.2, 7.6, 7.5, 7.5, 7.3, 7, 8.2, 8, 8.5, 7, 6.6, 7.7, 7, 5, 8.5, 8.5, 7, 7, 8
,7, 5, 7, 7, 7.3, 8, 7, 7, 6.5, 7, 8.5, 7.6, 6.5, 7.5, 6.5
,7, 8.5, 8, 7, 5, 6.5, 9.5, 7.7, 7]

#FREスケールを入れるリスト
#y=[]
y=[95.770, 93.664, 94.626, 82.730, 75.817, 86.917, 83.664, 91.104, 93.382, 92.240, 100, 100, 90.173, 86.723, 80.507, 84.371,85.839,	100, 84.001, 73.389, 87.398,100, 99.936, 93.694, 94.041, 87.121, 92.373,88.865,	96.275,	92.907,	86.598,	93.263]

number=2

while number < 61:
    if (number != 22) and (number != 23) and (number != 59):
        #text_listにリストとして読み込む
        with open('book'+ str(number)+'_3.txt', 'r') as f:
            #改行("\n")を""に変換
            text_list = f.read()

        #FREスケールをリストに入れる
        y.append(textstat.flesch_reading_ease(text_list))


    number+=1


#相関計算
x_np = np.array(x)
y_np = np.array(y)


#シャピロウィルク検定で正規性の確認
#w値とp_value
shap_w, shap_p_value_x = stats.shapiro(x)
shap_w, shap_p_value_y = stats.shapiro(y)

#p_valueが0.05以上なら，帰無仮説が採択→正規性がある
if shap_p_value_x >= 0.05 and shap_p_value_y >= 0.05 :
    print("正規性があるといえる")

    #ピアソンの相関係数をとる
    # 相関行列を計算
    coef = np.corrcoef(x_np, y_np)
    soukan = coef[0][1]


#p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
else:
    print("正規性があるといえない")

            
    #スピアマンの順位相関係数
    correlation, pvalue = spearmanr(x, y)
    soukan = correlation

            
##############################

print("一般図書のFRE")
print(soukan)

##グラフの描写
# グラフの大きさ指定
plt.figure(figsize=(5, 5))

# グラフの描写
plt.plot(x, y, 'o', label='Score')
plt.title('Correlation coefficient') # タイトル
plt.xlabel('YL') # x軸のラベル
plt.ylabel('FRE_No.104') # y軸のラベル

plt.grid(True) # gridの表示
plt.legend() # 凡例の表示
plt.savefig("FRE_tamesi.png")


            


            

