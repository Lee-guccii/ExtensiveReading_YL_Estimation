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
#new_listから文字検索
kekka = 0

time = 0
while time < 2:
    retu = 0
    kekka = 0
    string = input("Number or Word?:")
    if string == "N".lower() or string == "Number".lower():
        print("Search for Number")

        kensaku = input("検索したいナンバーを入力：") #←検索したい文字
        while retu <107:
            #検索したい番号があるか
            if kensaku == new_list[retu][0]: 
                print("番号：", new_list[retu][0])
                print(new_list[retu])
                print("--------------")
                kekka+=1
            retu+=1

        if kekka >0:
            print("検索個数：", kekka)
        else:
            print("結果：なし")
        time+=1

    elif string == "W".lower() or string == "Word".lower():
        print("Search for Word")

        kensaku = input("検索したい単語を入力：") #←検索したい文字
        while retu <107:
            gyou = 0
            while gyou < len(new_list[retu]):
                #検索したい文字列があるか
                if kensaku.lower() in new_list[retu][gyou].lower(): 
                    print("番号：", new_list[retu][0])
                    print(new_list[retu])
                    print("--------------")
                    kekka+=1
                gyou+=1
            retu+=1

        if kekka >0:
            print("検索個数：", kekka)
        else:
            print("結果：なし")
            
        time+=1

    else:
        print("One more time")

    print("もう一回検索する？")
    while time == 1:
        mokkai = input("Yes or No?:")
        
        if mokkai == "Y".lower() or mokkai == "Yes".lower():
            time = 0

        elif mokkai == "N".lower() or mokkai == "No".lower():
            time +=1
        
        else:
            print("One more time")


#kensaku = "WRDPOLc" #←検索したい文字



#while retu <107:
 #   
  #  
   # gyou = 0
    #while gyou < len(new_list[retu]):
        #検索したい文字列があるか
#        if kensaku.lower() in new_list[retu][gyou].lower(): 
 #           print("番号：", new_list[retu][0])
  #          print(new_list[retu])
   #         print("--------------")

#            kekka+=1
 #       gyou+=1
#
 #   retu+=1


#if kekka >0:
 #   print("検索個数：", kekka)

#else:
 #   print("結果：なし")
        
#####################################

