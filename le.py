#!/usr/bin/python3.10.2

import random

min = 1
max = 10
count=0

target = random.randint(min, max)
print("猜數字！")

while True:
    keyin=int(input(f"猜數字範圍{min}~{max}:"))
    count+=1
    if(keyin==target):
        print(f"賓果!猜{count}次，答案是{target}")
        break
    elif keyin > target:
        print("再小點")
        max=keyin-1
    elif keyin < target:
        print(f"大點，答錯第{count}次!")
        min=keyin+1
print("遊戲結束")

input("再玩一次？yes/no")

def palyer():
   import random

min = 1
max = 10
count=0

target = random.randint(min, max)
print("猜數字！")

while True:
    keyin=int(input(f"猜數字範圍{min}~{max}:"))
    count+=1
    if(keyin==target):
        print(f"賓果!猜{count}次，答案是{target}")
        break
    elif keyin > target:
        print("再小點")
        max=keyin-1
    elif keyin < target:
        print(f"大點，答錯第{count}次!")
        min=keyin+1

while(Ture):
    player()
    playagain=input("再來?(y,n)")
    if not(playagain=="y"):
        break
print("遊戲結束") 

