import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
import re
#coding:utf-8    

###############

number=2

while number < 10:
    
    
    text_list = "[illustration abcd] asdfgh 12345 abcde 6789 "

    list_suu =0

    #改行は1行だけのものをなくす→2行以上の改行を全て消すわけではない
    #while list_suu < len(text_list):
        #if text_list[list_suu] == "":
            #text_list[list_suu] = "\n"
        #list_suu+=1

    #正規表現
    #イラスト部分は削除
    #text_list = [s for s in text_list if re.sub('.Illustration:\s\d+.', '', s)]
    #ページ数は削除
    #text_list  = [s for s in  text_list  if re.sub('{\d+}', '', s)]

    #リストを結合して，空白で繋いで，文字列に変換
    #mojiretu = ''.join(text_list)

    #正規表現
    #{数字}（多分ページ数）を削除

    mojiretu = "[illustration2 abcd]    {1} {123} {1243}Asdfg    [janojnsd]chapter 12 Asdfgh[Akcsnd sdnj. MIcnsd ANCd.] adv CHAPTER 1 Chapter ONE 12345 abcde 6789 "

    #正規表現で[illustration ~]を空白に変更
    mojiretu = re.sub('\['+"(illustration|Illustration|ILLUSTRATION).*?"+'\]\s', '', mojiretu)

    
    #正規表現でchapter ~ を空白に変更
    mojiretu = re.sub('(chapter|Chapter|CHAPTER)\s(\d|.*?)\s', '', mojiretu)


    #正規表現で[]は削除
    mojiretu = re.sub('\[.*?\]\s', '', mojiretu)

    mojiretu = re.sub('{\d*?}', '', mojiretu)

    #正規表現で{(2文字以上)}のものを空白に変更
    mojiretu = re.sub('\s{2,}', ' ', mojiretu)

    #正規表現で{(2文字以上)}のものを空白に変更
    mojiretu = re.sub('\n', ' ', mojiretu)

    #ファイルに書き込む
    #f = open('book'+ str(number)+'_3.txt', 'w')
    #f.write(mojiretu)

    #f.close()

    
    number+=1
print(mojiretu)


