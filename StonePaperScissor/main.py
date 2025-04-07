from Game_modul import Game1
from  score import score_board

def main():
    
    option =["Stone","Paper","Scissor"]
    
    print("\t Welcome to the Game")
    print(
        "1)Play game\n"
        "2)Score Board\n"
        "3)Exit"
    )
    op = int(input("Enter the Option : "))
    match op:
        case 1:
            name = input("Enter the name: ")
            print("\nlet play game(*_*)") 
            chance = 0
            game = Game1(option,0,name)
            
            while chance < 3:
                print("************************************")
                print("1.Stone" "\n2.Paper" "\n3.Scissor")
                cho = int(input("\nEnter ur choice:"))
                
                game.n=cho
                
                bot = game.computer_choice()
                player=game.player_choice()

                chance=game.game(bot,player,chance)
            game.board()
        case 2:
            print("Score") 
            scor = score_board()
            print(scor.read())
        case 3:
            exit()
        

main()