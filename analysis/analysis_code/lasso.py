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
from sklearn.model_selection import ShuffleSplit

import math
from sklearn.metrics import mean_squared_error

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
poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x_train)
x_poly_test = poly.fit_transform(x_test)
#x0, x1, x2, ... , x0*x1, x0*x2...が作成





###########################################
#lasso回帰＆交差検定
clf = LassoCV(alphas=10 ** np.arange(  -6, 1,  0.1), cv=5)

#学習
clf.fit(x_poly, y_train)

#最適なα
print("α=", clf.alpha_)

#偏回帰変数
print("偏回帰係数", clf.coef_)

#切片
print("切片", clf.intercept_)





#####
#空モデルを作る
lasso = Lasso(alpha=clf.alpha_)

#学習
lasso.fit(x_poly, y_train)

#偏回帰係数
#print(lasso.coef_)

#切片
#print(lasso.intercept_)

#テストデータでやってみる
y_pred = lasso.predict(x_poly_test)
print("予測したYL", y_pred)

#グラフ
plt.scatter(y_test, y_pred)
plt.ylim(0, 10)
plt.xlim(0, 10)
plt.plot([0 , 10],[0, 10], 'k-')
plt.xlabel('y_test')
plt.ylabel('y_predict')
plt.legend()
plt.grid()
plt.show()

#########################################
#[縦指定][横指定]
kazu=0
sihyou=0

wariai=[]
wariai_t=[]
wariai_i=[]

mrse=[]
while kazu < len(y_pred):
  print(kazu)
  print("YL", y_pred[kazu], y_test.loc[kazu][0])
  print("差", y_pred[kazu] - y_test.loc[kazu][0])


  mrse.append((y_pred[kazu] - y_test.loc[kazu][0])**2)

  wariai.append(abs(y_pred[kazu] - y_test.loc[kazu][0]))
  if kazu < 8 or 15 < kazu < 23:
    wariai_t.append(y_pred[kazu] - y_test.loc[kazu][0])
  
  else:
    wariai_i.append(y_pred[kazu] - y_test.loc[kazu][0])
  kazu+=1




mean = statistics.mean(wariai)
print("差の平均",mean)
mean_t = statistics.mean(wariai_t)
print("多読図書の差の平均",mean_t)
mean_i = statistics.mean(wariai_i)
print("一般図書の差の平均", mean_i)

print("多読図書の誤差")
print(wariai_t)
print("一般図書の誤差")
print(wariai_i)

means= statistics.mean(mrse)
means2=math.sqrt(means)
print("MRSE", means2)
#データセットをランダムに５分割するための変数cvを定義
cv = ShuffleSplit(n_splits=5, test_size = 0.2, random_state=0)
score = cross_validate(lasso, x_poly, y_train, cv=cv,scoring = {"explained_variance","neg_mean_absolute_error","neg_mean_squared_error","neg_mean_squared_log_error","neg_median_absolute_error","r2" ,"neg_root_mean_squared_error"}, return_train_score=True, return_estimator=True)
print("決定係数", score["test_r2"].mean())
print("MAE(誤差の絶対値の平均)", score["test_neg_mean_absolute_error"].mean())
print("RMSE", score["test_neg_root_mean_squared_error"].mean())

print(lasso.score(x_poly_test, y_test))


print("RMSE/MAE:", score["test_neg_root_mean_squared_error"].mean()/score["test_neg_mean_absolute_error"].mean())


from sklearn.metrics import mean_absolute_percentage_error
print(mean_absolute_percentage_error(y_test, y_pred))
