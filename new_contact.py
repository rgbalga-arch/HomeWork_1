print("new contact text")
import random


import time
def count():
    for i in range(20):
        yield(i)
        time.sleep(1)

for number in count():
    print(number)