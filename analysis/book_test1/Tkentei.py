import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import spearmanr
import scipy
import statistics




#####################################
#多読図書の誤差
gosa_t = [2.5936085940242886, 0.3649609355211716, -1.5684807178864082, 0.08092297493428235, 0.22543171481307445, -1.3691957161909167, -0.3474666004673743, 1.8252411101316153, 0.55875223949132, 0.5226005465508596, 0.3525884186972337, 0.3041152432565233, 0.8437276168620489, -0.9181574433326762, -0.7906627803715223]

#一般図書の誤差
gosa_i = [0.10847348531766343, -0.5258853994325055, -1.2541770882612653, -0.5501409126883967, 0.7475673290440792, 0.11254455566384358, 0.18835643338229602, -0.12045902195570513, 1.0401978506856189, -0.3144134218532173, 0.5345536552762553, 0.6229265175369045, 0.8611454214443981, -0.48745911396300734, -0.7107419915524602, -1.6866471577013176, -1.0657173549843346]





tadoku_np = np.array(gosa_t)
ippan_np = np.array(gosa_i)





#シャピロウィルク検定で正規性の確認
#w値とp_value
shap_w_tadoku, shap_p_value_tadoku = stats.shapiro(tadoku_np)
shap_w_ippan, shap_p_value_ippan = stats.shapiro(ippan_np)


#F検定で等分散性の確認
fkentei_w, fkentei_p_value = scipy.stats.bartlett(tadoku_np,ippan_np)



print("正規性p値", shap_p_value_tadoku, shap_p_value_ippan)
print("等分散性p値", fkentei_p_value)
#p_valueが0.05以上なら，帰無仮説が採択→正規性がある
if (shap_p_value_tadoku >= 0.05) and (shap_p_value_ippan >= 0.05) :
    print("正規性があるといえる")

    #p_valueが0.05以上なら，帰無仮説が採択→等分散である
    if fkentei_p_value>= 0.05:

        #正規性を示し，等分散性である
        #スチューデントのt検定
        stu_w, stu_p = stats.ttest_ind(tadoku_np, ippan_np)
        
        
        #スチューデント検定のpが0.05以上なら，帰無仮説は採択→２郡間には差がない→多読図書と一般図書を一緒に考えられる
        if stu_p >= 0.05:

            print("２郡間に差があるとはいえない", stu_p)

        else:
            print("２郡間に差がある", stu_p)
        
        
    #p_valueが0.05以下なら，帰無仮説が棄却→等分散でない
    else:
        #ウェルチのt検定
        wel_w, wel_p = stats.ttest_ind(tadoku_np, ippan_np, equal_var=False)
        
        #ウェルチのt検定のpが0.05以上なら，帰無仮説は採択→２郡間には差がない→多読図書と一般図書を一緒に考えられる
        if wel_p >= 0.05:
            print("２郡間に差があるとはいえない", wel_p)


        #ウェルチのt検定のpが0.05以下なら，帰無仮説は棄却→２郡間には差がある→多読図書と一般図書を一緒に考えられない
        else:
            print("２郡間に差がある", wel_p)



#p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
else:
    print("正規性がない")

    #マン・ホイットニー検定
    man_w, man_p = stats.mannwhitneyu(tadoku_np, ippan_np, alternative='two-sided')
        
    #マン・ホイットニー検定のpが0.05以上なら，帰無仮説は採択→２郡間には差がない→多読図書と一般図書を一緒に考えられる
    if man_p >= 0.05:
        print("２郡間に差があるとはいえない", man_p)

    #マン・ホイットニー検定のpが0.05以下なら，帰無仮説は棄却→２郡間には差がある→多読図書と一般図書を一緒に考えられない
    else:
        print("２郡間に差がある", wel_p)



print(statistics.mean(gosa_t))
print(statistics.mean(gosa_i))
import scipy.stats as st


MU = abs(statistics.mean(gosa_t)-statistics.mean(gosa_i))
SE =  MU/stu_w
DF = len(gosa_t)+len(gosa_i)-2
CI = st.t.interval( alpha=0.95, loc=MU, scale=SE, df=DF )

print('対応なしt検定')
print(f'p値 = {stu_p:.3f}')
print(f't値 = {stu_w:.2f}')
print(f'平均値の差   = {MU:.2f}')
print(f'差の標準誤差 = {SE:.2f}')
print(f'平均値の差の95%信頼区間CI = [{CI[0]:.2f} , {CI[1]:.2f}]')

