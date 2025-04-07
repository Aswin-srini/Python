from pathlib import Path
class score_board:
        
    def write(self,name,player,bot,result,):
        def new():
            score = open("score.txt","w")

            score.write( f"Name: {name}   playerscore:   {player}   botscore:   {bot}   result:   {result} \n")
            
            score.close()

        
        def insert():
            score = open ("score.txt","")
                
            score.write( f"Name: {name}   playerscore:   {player}   botscore:   {bot}   result:   {result} \n")
                
            score.close()
            
        file = Path("score.txt")
        if file.exists():
            insert()
        else:
            new()
    
    def read(self):
        score = open ("score.txt","r")
            
        r = score.read()
        print(r.readable)
        score.close()
        return r

    