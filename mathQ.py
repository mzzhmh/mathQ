
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
print("1. Multiplication MONSTER\n2. Division MONSTER\n3. Addition MONSTER\n4. Substraction MONSTER\n5. Text Question MONSTER\n")
print("===========================================================")



while (chs not in ['1','2','3','4','5']):
    chs = input("PLEASE CHOOSE WHICH MONSTER YOU WANT TO FIGHT? (1, 2, 3, 4 or 5?):")

if chs == '1':
    mst = mulMonster()
    mst.loadQ("mulQ.txt")
elif chs == '2':
    mst = divMonster()
    mst.loadQ("divQ.txt")
elif chs == '3':
    mst = addMonster()
    mst.loadQ("addQ.txt")
elif chs == '4':
    mst = subMonster()
    mst.loadQ("subQ.txt")
else:
    mst = yytMonster1()
    mst.loadQ("yyt1Q.txt")
    
print("===========================================================")
print('YOU NEED TO KILL THE MONSTER BY ANSWERING THE QUESTIONS!\n\nARE YOU READY? :) HIT "Enter" KEY TO PROCEED!\n')


jms = player()

tst = input(":")
if tst == "give me five":
    jms.life = 10

#give sword to player?
if (mst.__class__.__name__ == 'yytMonster1'):
    pans = ''
    while (pans != 'yes' and pans != 'no'):
        pans = input('\n==============================================\n   DO YOU WANT TO PICKUP A SWORD? ATTACK +5 (Type: yes OR no):\n===========================================\n:')
    if pans == 'yes':
        jms.weapon = 5
        mst.life = mst.life * 5

        
mst.show()
mst.showRank()

print("**********************************")
print("         TIMING STARTED!          ")
print("**********************************")

jms.startT = int(time.time())
#randomly pick a question
while (mst.stillAlive(jms) and jms.stillAlive()):
    print("===========================================================")
    theQ = mst.pickQ()
    chkOK = jms.answer(theQ)
    time.sleep(1)
    if (chkOK == "Correct"):
        mst.removeQ(theQ)
        mst.lostHeart(jms)
    elif (chkOK == "Help"):
        continue
    else:
        jms.lostHeart()
    time.sleep(1)    
    print("===========================================================")
    
