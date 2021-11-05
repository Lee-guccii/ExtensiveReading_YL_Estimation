import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

###############
#textに読み込む
with open("book_text5.txt", "r", encoding="utf-8") as f:
    text = f.read()




#####################################
#単語数を計測

# default separator: space
result = len(text.split())

print()
print("There are " + str(result) + " words.")