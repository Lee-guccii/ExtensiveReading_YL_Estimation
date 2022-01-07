import os

kazu=1
while kazu < 65:
    #path = 'book'+ kazu +'.txt'
    f = open('book'+ str(kazu) +'.txt', 'w')
    f.write('')  # 何も書き込まなくてファイルは作成されました
    f.close()

    
    kazu+=1