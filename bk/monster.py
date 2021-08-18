import ast
import random
import json
import time
class monster:
    def __init__(self):
        self.life = 0
        self.mathDict = {}
        self.rankfile = ""
    def loadQ(self,qFile):        
        file = open(qFile, "r")
        contents = file.read()
        self.mathDict = ast.literal_eval(contents)
        file.close()
        self.life = len(self.mathDict)
    def printLife(self):
        lf = "|"
        for i in range(self.life):
            lf = lf + "♥"
        print("Monster Life: "+lf)
    def printRoar(self):
        print(""" """)
    def stillAlive(self,player):
        if self.life > 0:
            self.printLife()
            return True
        else:
            self.printVictory(player)
            return False
    def pickQ(self):
        rkey = random.choice(list(self.mathDict.keys()))
        ans = self.mathDict.get(rkey)
        return (rkey,ans)
    def printVictory(self,player):
        print("==========   YOU HVAE SUCCESSFULLY KILLED THE MONSTER !!!  ===============")
        print("""                __      __
                                ( _\    /_ )
                                 \ _\  /_ / 
                                  \ _\/_ /_ _
                                  |_____/_/ /|
                                  (  (_)__)J-)
                                  (  /`.,   /
                                   \/  ;   /
                                    | === |
            """)


        print("=====================        CONGRATULATIONS!!!!    ======================")
        #get finish time and update the ranking table
        self.updateRank(player)
    def updateRank(self,player):
        player.endT = int(time.time())
        playT = player.endT - player.startT
        #load current ranking
        with open(self.rankfile) as rfile:
            lines = rfile.readlines()
            tuples = []
            for eachEntry in lines:
                pname = eachEntry.strip().split(':')[0].ljust(20)
                score = eachEntry.split(':')[1].strip()
                tuples.append((pname,int(score)))
        rfile.close()
        
        sort_rank = sorted(tuples, key=lambda x: x[1], reverse=False)
        #print(sort_rank)
        lastV = int(sort_rank[-1][1])
        if playT < lastV:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("$$ YOUR COMPLETION time is in TOP 10 Ranking!                  $$")
            print("$$ Your Completion Time is: "+str(playT)+" seconds")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            self.showRank()
            playerName = ""
            while(len(playerName)==0):
                playerName = input("PLEASE ENTER YOUR NAME SO YOUR NAME CAN BE SHOWN IN THE RANKING LIST:")
            sort_rank.append((playerName,playT))
            #print(sort_rank)
            resort_rank = (sorted(sort_rank, key=lambda x: x[1], reverse=False))[0:10]
            #print(resort_rank)
            #dump to new top 10 to the file
            with open(self.rankfile,'w') as wfile:
                for each in resort_rank:
                    wfile.write(each[0].strip()+":"+str(each[1]).strip()+"\n")
                wfile.close()
            self.showRank()
        else:
            print("=================================================================")
            print("== SORRY, Your COMPLETION time is NOT in TOP 10 Ranking.       ==")
            print("== Your Completion Time is: "+str(playT)+" seconds. Try faster next time.")
            print("=================================================================")
            dummy = input("HIT 'Enter' to continue....")
            
    def removeQ(self,question):
        del self.mathDict[question[0]]
    def lostHeart(self):
        print("VERY GOOD! YOU HIT THE MONSTER REALLY HARD!!!!!! MONSTER's Life -1 ♥\n")
        self.life = self.life - 1
    def showRank(self):
        with open(self.rankfile) as rfile:
            lines = rfile.readlines()
            print("~~~~~~~~~~~~~~~~~~~~~~PLAYER RANKING TABLE~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("   |PLAYER NAME         | COMPLETE TIME (Seconds)")
            print("---------------------------------------------------------------------")
            cnt = 1
            for eachEntry in lines:
                pname = eachEntry.strip().split(':')[0].ljust(20)
                score = eachEntry.split(':')[1].strip()
                print(str(cnt).ljust(3)+"|"+pname+"| "+ score)
                cnt = cnt + 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")	
            rfile.close()
class mulMonster(monster):
    def __init__(self):
        self.life = 0
        self.mathDict = {}
        self.rankfile = "mulRank.txt"
    def show(self):
        print("===========================================================")
        print ('''                                             / \           ^
                       _,-~~~--~~~--._      (   \         / \
                   _,-'               `.__  (    \_.---._/   )
                 ,' give me  "a hand"?    `-(_` -'       `-. )   
                /       "--..                \.'           `/  
               ,             `-.              :  _  .-.  _  : 
              /                 ;             : (0).oYo.(0) ;
            /                    `             \.-'V'"'V'-./
           /when you are in dange'              \\^     ^//
  /\      /                      '     :    : .-'\\^   ^//
 ;  \    ;   /  help me         ,'  _.-`.    `. : \\^_^//
 ;   \   ;  ;`.               ,'~~-'     `.    `.`.`-.-'
  \   |_/   ;  `.        /-'/___.---.      `-.   `.`---.
   \       /     |      /____.---.)))         `-. `---.\
    \_____/      (____________))))\\\            `-.\\\\
                               \\\\''')
        print("===========================================================")

    def printRoar(self):
        print("========== MONSTER: 'AHAHAHHAHAHAHHA' !!!  ===============")
        print("""             .'''''-,              ,-`````.
               \   `.                ,'   /
                \    \              /    /
                 \   .`.  __.---. ,`.   /
                  \.' .'``        `. `./
                   \.'  -'''-..     `./
                   /  /        '.      \
                  /  / .--  .-'''`      '.
                 '   |    ,---.    _      \
     /``-----._.-.   \   / ,-. '-'   '.   .-._.-----``\
     \__ .     | :    `.' ((O))   ,-.  \  : |     . __/
      `.  '-...\_`     |   '-'   ((O)) |  '_/...-`  .'
 .----..)    `    \     \      /  '-'  / /    '    (..----.
(o      `.  /      \     \    /\     .' /      \  .'      o)
 ```---..   `.     /`.    '--'  '---' .'\     .'   ..---```
         `-.  `.  /`.  `.           .' .'\  .'  .-'
            `..` /   `.'  ` - - - ' `.'   \ '..'
                /    /                \    \
               /   ,'                  `.   \
               \  ,'`.                .'`.  /
                `/    \              /    \'
                /    .'            `.    \
              .-'''  |                |  ```-.
              `......'                `......'""")
        print("=====================        I STILL HAVE SO MANY ♥ LEFT !!!!    ======================")
    	

class addMonster(monster):
    def __init__(self):
        self.life = 0
        self.mathDict = {}
        self.rankfile = "addRank.txt"
    def show(self):
        print("===========================================================")
        print ('''          ,     .
            /(     )\               A
       .--.( `.___.' ).--.         /_\  
       `._ `%_&%#%$_ ' _.'     /| <___> |\
          `|(@\*%%/@)|'       / (  |L|  ) \
           |  |%%#|  |       J d8bo|=|od8b L
            \ \$#%/ /        | 8888|=|8888 |
            |\|%%#|/|        J Y8P"|=|"Y8P F
            | (.".)%|         \ (  |L|  ) /
        ___.'  `-'  `.___      \|  |L|  |/
      .'#*#`-       -'$#*`.       / )|
     /#%^#%*_ *%^%_  #  %$%\    .J (__)
     #&  . %%%#% ###%*.   *%\.-'&# (__)
     %*  J %.%#_|_#$.\J* \ %'#%*^  (__)
     *#% J %$%%#|#$#$ J\%   *   .--|(_)
     |%  J\ `%%#|#%%' / `.   _.'   |L|
     |#$%||` %%%$### '|   `-'      |L|
     `|||||  #$$|%#%  | L|         |L|
          |  #$%|$%%  | ||l        |L|
           *#$%| | #$*g i v e     m e   a  'hand'?
          /$#' ) ( `%%\    in danger?
         /#$# /   \ %$%\    help me
        ooooO'     `Ooooo''')
        print("===========================================================")

    def printRoar(self):
        print("========== MONSTER: 'AHAHAHHAHAHAHHA' !!!  ===============")
        print("""       __   __
             .-'  "."  '-.
           .'   ___,___   '.
          ;__.-; | | | ;-.__;
          | \  | | | | |  / |
           \ \/`"`"`"`"`\/ /
            \_.-,-,-,-,-._/
             \`-:_|_|_:-'/
              '.       .'
                `'---'`""")
        print("=====================        I STILL HAVE SO MANY ♥ LEFT !!!!    ======================")

class subMonster(monster):
    def __init__(self):
        self.life = 0
        self.mathDict = {}
        self.rankfile = "subRank.txt"
    def show(self):
        print("===========================================================")
        print ('''      -. -. `.  / .-' _.'  _
                     .--`. `. `| / __.-- _' `
                    '.-.  \  \ |  /   _.' `_
                    .-. g i ve || me .' _five`.
                 .' _ \ '  -    -'  - ` _.-.
                   .' `. %%%%%   | %%%%% _.-.`-
                 .' .-. ><(@)> ) ( <(@)>< .-.`.
                   (("`(   -   | |   -   )'"))
                  / \\#)\    (.(_).)    /(#//\
                 ' / ) ((  /   | |   \  )) (`.`.
                 .'  (.) \ .md88o88bm. / (.) \)
                   / /| / \ `Y88888Y' / \ | \ \
                 .' / O  / `.   -   .' \  O \ \\
                  / /(O)/ /| `.___.' | \\(O) \
                   / / / / |  |   |  |\  \  \ \
                   / / // /| help me |  \  \ \  VK
                 _.--/--/'( ) ) ( ) ) )`\-\-\-._
                ( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) ) ''')
        print("===========================================================")

class divMonster(monster):
    def __init__(self):
        self.life = 0
        self.mathDict = {}
        self.rankfile = "divRank.txt"
    def show(self):
        print("===========================================================")
        print ("""                  __.......__
                                .-:::::::::::::-.
                              .:::''':::::::''':::.
                            .:::'     `:::'     `:::. 
                          .'\  ::'   ^^^  `:'  ^^^   '::  /`.
                      :   \ :give_.__me  five__._   :: /   ;
                     :     \`: .' ___\     /___ `. :'/     ; 
                    :       /\   (_|_)\   /(_|_)   /\       ;
                    :      / .\   __.' ) ( `.__   /. \      ;
                    :      \ (        {   }        ) /      ; 
                     :      `-(     .  ^"^  .     )-'      ;
                      `.       \  .'<`-._.-'>'.  /       .'
                        `.      \    \;`.';/    /      .'
                     help  `._    `-._       _.-'me _.'
                           .'`-.__ .'`-._.-'`. __.-'`.
                         .'       `.         .'       `.
                       .'           `-.   .-'           `. """)
        print("===========================================================")

        

        
