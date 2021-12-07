import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

###############


resdic={}
number = 2
#textに読み込む
while number < 61:
    if (number != 22) and (number != 23) and (number != 59) :
        #text_listにリストとして読み込む
        with open("book"+ str(number)+ "_3.txt", "r", encoding="utf-8") as f:
            text = f.read()



        #####################################
        #単語数を計測

        # default separator: space
        result = len(text.split())

        print("book", number)
        print("There are " + str(result) + " words.")

        if result < 20000:
            resdic[number] = result

    number+=1


print()
print("under 20000 words")
print(resdic)