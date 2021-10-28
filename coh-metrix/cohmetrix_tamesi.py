import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

###############
#textをnew_listに読み込む
with open("CohMetrixOutput.txt", "r", encoding="utf-8") as f:
    list = f.readlines()

new_list = []

for i in list:
    word = i.split()
    new_list.append(word)



#####################################
#使いたいパラメータの数字を取り出す→相関の確認

#x軸の数値(本のERFPTレベル)
x = [5, 6, 7, 8, 8, 10, 10, 11, 3, 4, 5, 4, 5, 7, 11, 13, 13, 8, 
8, 10, 14, 2, 2, 2, 9, 12, 12, 9, 3, 3, 3, 2, 2, 17, 18, 16]

#x = [?, 1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 
#3.3, 3.9, 5.7, 0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 0.7, 0.7, ?, ?, ?]
#1,34,35,36排除
x = [1.1, 1.1, 3.5, 3.3, 3.9, 4.7, 4.7, 1.2, 1.4, 1.8, 1.3, 2.1, 2.7, 3.8, 3.5, 4.7, 3.3, 
3.3, 3.9, 5.7, 0.6, 0.6, 0.7, 3.3, 4.1, 4.1, 3.3, 0.9, 0.8, 0.8, 0.7, 0.7]#試し追加分

#numpy配列
x_np = np.array(x)

count_list = [3, 31, 47, 92, 104, 106, 96, 99, 67, 102, 44, 77, 73,
              60, 100,91, 11] #パラメータの番号
count_zyunban = 0 #count_listの順番を決める変数
soukankekka = {} #パラメータ：相関係数の結果　のディクショナリ




while count_zyunban < len(count_list):
    count = count_list[count_zyunban] #count_listの中身を順番に出す
    
    #[3:39]まで数字
    #y軸の数値を取り出す
    suuti_list = new_list[count][3:39]
    suuti_list = new_list[count][4:36] #試し追加分
    
    #文字列を数値に変換
    y = [float(s) for s in suuti_list]
    #print(new_suuti_list)


    ##############################
    #相関をとる

    #相関計算
    y_np = np.array(y)

    # 相関行列を計算
    coef = np.corrcoef(x_np, y_np)


    ##グラフの描写
    # グラフの大きさ指定
    plt.figure(figsize=(5, 5))

    # グラフの描写
    plt.plot(x, y, 'o', label='Score')
    
   
    #総単語数
    if count == 3:
        plt.title('YL_Number of words') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Number of words_No.3') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("soutango_tamesi.png")



        para = "3, 総単語数"
        

    
    elif count == 31:
        plt.title('YL_Noun overlap') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Noun Overlap_No.31') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("NounOverlap_all_tamesi.png")



        para = "31, 名詞の重なり"

    #語彙の多様性
    elif count == 47:
        plt.title('YL_Lexical diversity') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Lexical diversity_No.47') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("tayousei_all_tamesi.png")


        
        para = "47, 語彙の多様性"


    #語彙の頻度
    elif count == 92:
        plt.title('YL_CELEX word frequency for content words') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('RDL2_No.92') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("word frequency_tamesi.png")
        
        
        para = "92, 語彙の頻度"

    #FRE
    elif count == 104:
        plt.title('YL_FRE') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('FRE_No.104') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("FRE_tamesi.png")


        para = "104, FRE"
    


    #RDL2
    elif count == 106:
        plt.title('YL_RDL2') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('RDL2_No.106') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("RDL2_tamesi.png")


        para = "106, RDL２"
        


    #単語の親しみやすさ
    elif count == 96:
        plt.title('YL_Familiarity for content word') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Familiarity_No.96') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("Familiarity_tamesi.png")

    
        para = "96, 単語の親しみやすさ"
    
    #単語の意味性
    elif count == 99:
        plt.title('YL_Word meaningfulness every word') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('meaningfulness_No.99') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("meaningfulness_tamesi.png")

    
        para = "99, 単語の意味性"

    #主動詞の前の単語数
    elif count == 67:
        plt.title('YL_Number of words before the main verb') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Number of words before the main ver_No.67') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("NumberOfWordsBeforeTheMainVerb_tamesi.png")

    
        para = "67, 主動詞の前の単語数"

    
    #動詞の上位概念語
    elif count == 102:
        plt.title('YL_hypernymy for Verb') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('hypernymy for Verb_No.102') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("hypernymyForVerb_tamesi.png")

    
        para = "102, 動詞の上位概念語"

    
    #LSA given/new
    elif count == 44:
        plt.title('YL_LSA given/new') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('LSA_No.44') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("LSAgiven_new_tamesi.png")

    
        para = "44, LSA given/new"


    #前置詞の密度
    elif count == 77:
        plt.title('YL_preposition') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('preposition_No.77') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("preposition_tamesi.png")

    
        para = "77, 前置詞の密度"


    #文章構造の類似性
    elif count == 73:
        plt.title('YL_Sentence syntax similarity') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Sentence syntax similarity_No.73') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("Sentence syntax similarity_tamesi.png")

    
        para = "73, 文章構造の類似性"


    #因果関係のある動詞と助詞の割合
    elif count == 60:
        plt.title('YL_Causal verbs and causal particles incidence') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Causal verbs and causal particles incidence_No.60') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("CausalVerbsAndCausalParticlesIncidence_tamesi.png")

    
        para = "60, 因果関係のある動詞と助詞の割合"


    #単語の多義性
    elif count == 100:
        plt.title('YL_Polysemy for content words') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Polysemy for content words_No.100') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("PolysemyForContentWords_tamesi.png")

    
        para = "100, 単語の多義性"


    #代名詞，三人称，複数型の発生スコア
    elif count == 91:
        plt.title('YL_Third person plural pronoun incidence') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Third person plural pronoun incidence_No.91') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("ThirdPersonPluralPronounIncidence.png")

    
        para = "91, 代名詞，三人称，複数型の発生スコア"

    #単語の文字数の標準偏差
    elif count == 11:
        plt.title('Correlation coefficient') # タイトル
        plt.xlabel('YL') # x軸のラベル
        plt.ylabel('Standard deviation of the mean number of letter_No.11') # y軸のラベル

        plt.grid(True) # gridの表示
        plt.legend() # 凡例の表示
        plt.savefig("StandardDeviationOfTheMeanNumberOfLetterInWords.png")

    
        para = "11, 単語の文字数の標準偏差"
    



    #パラメータと相関係数でディクショナリを作成
    soukankekka[para] = coef[0][1] # パラメータ，相関の結果

    count_zyunban += 1



#ディクショナリをソート
#相関係数を絶対値(abs())で大きい順に並び替え
soukankekka = sorted(soukankekka.items(), key = lambda x : abs(x[1]), reverse=True)

print("相関係数")
#パラメータと相関係数の結果を，相関係数の大きい順で表示
for s in soukankekka:
    print(s)
    print("-------------")

