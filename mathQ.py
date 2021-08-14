
import time
from monster import *
from player import *
import re

print("===========================================================")
print("!!!!!!!!!!!!!!MATH CHANLLENGE for JAMES MIAO!!!!!!!!!!!!!!!")
print("===========================================================")

chs = 0
print("THERE ARE FOUR MONSTERS.\n PICK ONE MONSTER YOU WOULD LIKE TO CHALLENGE! BE CAREFUL!!!!!!!!\n")
print("===========================================================")
print("1. Multiplication MONSTER\n2. Division MONSTER\n3. Addition MONSTER\n4. Substraction MONSTER\n")
print("===========================================================")



while (chs not in ['1','2','3','4']):
    chs = input("PLEASE CHOOSE WHICH MONSTER YOU WANT TO FIGHT? (1, 2, 3 or 4?):")

if chs == '1':
    mst = mulMonster()
    mst.loadQ("mulQ.txt")
elif chs == '2':
    mst = divMonster()
    mst.loadQ("divQ.txt")
elif chs == '3':
    mst = addMonster()
    mst.loadQ("addQ.txt")
else:
    mst = subMonster()
    mst.loadQ("subQ.txt")
    
print("===========================================================")
print('YOU NEED TO KILL THE MONSTER BY ANSWERING THE QUESTIONS!\n\nARE YOU READY? :) HIT "Enter" KEY TO PROCEED!\n')


jms = player()

tst = input(":")
if tst == "give me five":
    jms.life = 5

mst.show()

#randomly pick a question
while (mst.stillAlive() and jms.stillAlive()):
    print("===========================================================")
    theQ = mst.pickQ()
    chkOK = jms.answer(theQ)
    time.sleep(1)
    if (chkOK == "Correct"):
        mst.removeQ(theQ)
        mst.lostHeart()
    elif (chkOK == "Help"):
        continue
    else:
        jms.lostHeart()
    time.sleep(1)    
    print("===========================================================")
    
