import os

kazu=101
while kazu < 201:
    #path = 'book'+ kazu +'.txt'
    f = open('../book_all/book'+ str(kazu) +'_testq.txt', 'w')
    f.write('')  # 何も書き込まなくてファイルは作成されました
    f.close()

    
    kazu+=1