from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as pyp
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoCV
import statistics


from sklearn.preprocessing import PolynomialFeatures

from sklearn import linear_model
from sklearn.model_selection import ShuffleSplit, cross_val_score

###########################
#データセット

#csvを読み込む
#学習用
df_train=pd.read_csv('senkeikaiki2_train.csv')
#テスト用
df_test=pd.read_csv('senkeikaiki2_test.csv')



#説明変数(総単語数，動詞句の発生率抜き)
#学習用
x_train =  df_train.drop(["YL",  "familiarity_for_word"], axis=1)
#テスト用
x_test =  df_test.drop(["YL",  "familiarity_for_word"], axis=1)


#目的変数
#学習用
y_train = df_train[["YL"]]
#テスト用
y_test =  df_test[["YL"]]


##########################################

#次数を決定
kekka=[]
zisuu=1

while zisuu < 6:
  poly = PolynomialFeatures(degree = zisuu)
  x_poly = poly.fit_transform(x_train)
  x_poly_test = poly.fit_transform(x_test)
  #lasso回帰＆交差検定
  clf = LassoCV(alphas=10 ** np.arange(  -6, 1,  0.1), cv=5)
  #学習
  clf.fit(x_poly, y_train) 

  #空モデルを作る
  lasso = Lasso(alpha=clf.alpha_)

  #学習
  lasso.fit(x_poly, y_train) 


  print("次数＝", zisuu)
  print(lasso.score(x_poly, y_train))
  print(lasso.score(x_poly_test, y_test))
  #score = cross_validate(lasso, x_poly, y_train, cv=5,scoring = {"explained_variance","neg_mean_absolute_error","neg_mean_squared_error","neg_mean_squared_log_error","neg_median_absolute_error","r2"})
  #print("決定係数", score["test_r2"].mean())

  #データセットをランダムに５分割するための変数cvを定義
  cv = ShuffleSplit(n_splits=5, test_size = 0.2, random_state=0)
  
  #cvを用いてクロスバリデーションを実行
  scores = cross_val_score(lasso, x_poly, y_train, cv=cv)
  
  #結果を表示
  #print(scores)
  print("R-squared_Average: ", scores.mean())
  kekka.append(scores.mean())


  zisuu+=1

a=0
while a<5:
  print("次数：",a+1)
  print("R-squared_Average: ", kekka[a])

  a+=1


