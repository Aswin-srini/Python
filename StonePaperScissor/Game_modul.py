import random
from  score import score_board

class Game1:
    
    def __init__(self,op,n,name):
        self.op = op
        self.n = n
        self.point = 0
        self.bot_poit = 0
        self.name=name
        
    def game(self,computer_choice,player_choice,chance):
        
        if (computer_choice == "Stone" and player_choice == "Paper") or (computer_choice == "Paper" and player_choice == "Scissor") or (computer_choice == "Scissor" and player_choice == "Stone"):
            
            chance+= 1
            self.point += 1
            print("\nu win")
        
        elif computer_choice == player_choice:
            print("\nmatch draw")
            
        else:
            chance+= 1
            self.bot_poit+=1
            print("bot win")
            
        print("\nReminig chance:",3-chance)
        print("\nYour point:",self.point)
        print("Bot point:",self.bot_poit)
            
        return chance

    def computer_choice(self):
        bot = random.choice(self.op)
        print("\nBot choice : " + bot)    
        return bot
        
    def player_choice(self):
        try:
            player = self.op[self.n-1]
            print("Player choice : " + player)
        except :
            print("give valide input")
        return player
    
    def result(self):
        if self.point > self.bot_poit:
            result = "Win"
            print("Congratulation " + self.name + " You win the Game ^_^") 
        else:
            result = "loss"
            print(self.name + " You loss the Game!!!")
        return result
            
    def board(self):
       scor = score_board()
       scor.write(self.name,self.point,self.bot_poit,self.result())