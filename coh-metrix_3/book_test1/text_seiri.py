import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
import re
import os
#coding:utf-8    

###############

number=101

while number < 201:
    
    #text_listにリストとして読み込む
    with open('book'+ str(number)+'_test.txt', 'r') as f:
        #改行("\n")を""に変換
        text_list = f.read().splitlines()

    list_suu =0

    #改行は1行だけのものをなくす→2行以上の改行を全て消すわけではない
    while list_suu < len(text_list):
        if text_list[list_suu] == "":
            text_list[list_suu] = "\n"

        list_suu+=1



    #list_suu =0
    #while list_suu < len(text_list)-1:
    #    if text_list[list_suu] == "\n" and text_list[list_suu+1] == "\n":
    #        del text_list[list_suu]
     #   list_suu+=1


      #リストを結合して，空白で繋いで，文字列に変換
    mojiretu = ' '.join(text_list)



    #正規表現で[illustration ~]を空白に変更
    mojiretu = re.sub('\['+"(illustration|Illustration|ILLUSTRATION).*?"+'\]\s', '', mojiretu)
    mojiretu = re.sub('\['+"(illustration:|Illustration:|ILLUSTRATION:)\s\d\d\d\d"+'\]', '', mojiretu)

    
    #正規表現でchapter ~ , stave ~を空白に変更
    #mojiretu = re.sub('(chapter|Chapter|CHAPTER)\s(\d|.*?)', '', mojiretu)
    #mojiretu = re.sub('(stave|Stave|STAVE)\s(\d|.*?)', '', mojiretu)
    #mojiretu = re.sub('(act|Act|ACT)\s(\d|.*?)', '', mojiretu)
    #mojiretu = re.sub('(scene|Scene|SCENE)\s(\d|.*?)', '', mojiretu)


    #正規表現で{数字}のものを空白に変更
    mojiretu = re.sub('{\d*?}', '', mojiretu)
    #mojiretu = re.sub('\d*', '', mojiretu)

    #正規表現で[]は削除
    mojiretu = re.sub('\[.*?\]', '', mojiretu)

    #正規表現で空白２つ以上のものを空白に変更
    mojiretu = re.sub('\s+', ' ', mojiretu)

    #正規表現でchapter ~ , stave ~を空白に変更
    mojiretu = re.sub('(chapter|Chapter|CHAPTER)\s(\d|.*?)\s', '', mojiretu)
    mojiretu = re.sub('(stave|Stave|STAVE)\s(\d|.*?)\s', '', mojiretu)
    mojiretu = re.sub('(act|Act|ACT)\s(\d|.*?)\s', '', mojiretu)
    mojiretu = re.sub('(scene|Scene|SCENE)\s(\d|.*?)\s', '', mojiretu)
    mojiretu = re.sub('(C h a p\.|c h a p\.|C H A P\.)\s.*?\s', '', mojiretu)


    




    #ファイルに書き込む
    f = open('book'+ str(number)+'_test1.txt', 'w')
    f.write(mojiretu)

    f.close()

    #ファイル削除
    os.remove('book'+ str(number)+'_test.txt')

    number+=1



