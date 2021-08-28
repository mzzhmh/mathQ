import sys
class player:
    def __init__(self,life=2):
        self.life = life
        self.helpCnt = 0
        self.startT = 0
        self.endT = 0
        self.weapon = 1
        self.wrongQF = open('incorrectQ.txt','w')
        
        
    def printLife(self):
        lf = "|"
        for i in range(self.life):
            lf = lf + "♥"
        print("Your Life: "+lf)

    def printDeath(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("!!!!!!!!!!!!!!!!YOUR LIFE BAR IS EMPTY!!!!!!!!!!!!!!!!!!")
        print("""
                        _______________
                       /               \  
                      /                 \
                    //                   \/\
                    \|   XXXX     XXXX   | /
                     |   XXXX     XXXX   |/
                     |   XXX       XXX   |
                     |                   |
                     \__      XXX      __/
                       |\     XXX     /|
                       | |           | |
                       | I I I I I I I |
                       |  I I I I I I  |
                       \_             _/
                         \_         _/
                           \_______/  """)
        print("@@@@@@@@@@  YOU ARE DEAD!!! GAME OVER!!!!!!@@@@@@@@@@@@@")
        sys.exit()

    def stillAlive(self):
        if self.life > 0:
            self.printLife()
            return True
        else:
            self.printDeath()
            return False
    #answer and check the question    
    def answer(self,ques):
        jans = ""
        while(len(jans) == 0):
            jans = input(str(ques[0]))
        if jans == ques[1]:
            return "Correct"
        elif ((jans == 'help me')):
            if (self.helpCnt < 1):
                print("YOU CALLED FOR HELP. ♥ +1 :) \n")
                self.life = self.life + 1
                self.helpCnt = self.helpCnt + 1
            else:
                print("YOU HAVE USED THE 'HELP ME' CMD. SORRY :(\n")
            return "Help"
        else:
            #record the incorrect question.
            self.wrongQF.write((str(ques[0]))+"|||"+(str(jans))+"\n")
            self.wrongQF.flush()
            return "Wrong"
    def lostHeart(self):
        print("<<<<<<AHHHHH! YOUR ANSWER IS WRONG! THE MONSTER HIT YOU REALLY HARD!>>>>>> YOUR Life -1 ♥\n")
        self.life = self.life - 1
