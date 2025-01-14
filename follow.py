from time import sleep
import random
n=0
while True:
    n+=1
    rnd=random.randint(1,3)
    print(f'[{n}] Done Login')
    sleep(rnd)
    print(f'[{n}] Done Report')
    sleep(rnd)