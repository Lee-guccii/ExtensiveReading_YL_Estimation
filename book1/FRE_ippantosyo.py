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
x = [8, 6.6, 8.5, 6.5, 5, 7, 6, 5, 5, 5, 6.5, 6.5, 7, 8.2, 7.6, 7.5, 7.5, 7.3, 
7, 8.2, 8, 8.5, 7, 6.6, 7.7, 7, 5, 8.5, 8.5, 7, 7, 8]

#FREスケールを入れるリスト
y=[]

number=2

while number < 36:
    if (number != 22) and (number != 23):
        #text_listにリストとして読み込む
        with open('book'+ str(number)+'.txt', 'r') as f:
            #改行("\n")を""に変換
            text_list = f.read().splitlines()

        list_suu =0

        #改行は1行だけのものをなくす→2行以上の改行を全て消すわけではない
        while list_suu < len(text_list):
            if text_list[list_suu] == "":
                text_list[list_suu] = "\n"
            list_suu+=1

        #正規表現
        #イラスト部分は削除
        text_list = [s for s in text_list if re.sub('.Illustration:\s\d+.', '', s)]
        #ページ数は削除
        text_list  = [s for s in  text_list  if re.sub('{\d+}', '', s)]

        #リストを結合して，空白で繋いで，文字列に変換
        mojiretu = ''.join(text_list)

        #正規表現
        #{数字}（多分ページ数）を削除


        mojiretu_p = re.sub('{\d+}', '', mojiretu)
        #[Illustration:00]を消す
        mojiretu_p_ill = re.sub('.Illustration:\s\d+.', '', mojiretu_p)
        
        #FREスケールをリストに入れる
        y.append(textstat.flesch_reading_ease(mojiretu_p_ill))


    number+=1

print(y)
#相関計算
x_np = np.array(x)
y_np = np.array(y)


#シャピロウィルク検定で正規性の確認
#w値とp_value
shap_w, shap_p_value_x = stats.shapiro(x)
shap_w, shap_p_value_y = stats.shapiro(y)
print(shap_p_value_x,"x_shapiro")
print(shap_p_value_y, "y_syapiro")
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


            


            

