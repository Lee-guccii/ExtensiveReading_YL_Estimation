import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

###############

number = 1

resdic={}
#textに読み込む
while number<19:
    with open("book_text"+str(number)+".txt", "r", encoding="utf-8") as f:
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