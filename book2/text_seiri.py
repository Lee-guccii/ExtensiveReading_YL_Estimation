import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
import re
#coding:utf-8    

###############

number=51

while number < 61:
    if (number != 22) and (number != 23) and (number != 59):
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


        #ファイルに書き込む
        f = open('book'+ str(number)+'_3.txt', 'w')
        f.write(mojiretu_p_ill)

        f.close()
    number+=1



