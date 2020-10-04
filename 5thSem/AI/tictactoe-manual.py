board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
def printBoard(board):
    print(board[7],'|',board[8],'|',board[9])
    print("+-+-+-+-+")
    print(board[4],'|',board[5],'|',board[6])
    print("+-+-+-+-+")
    print(board[1],'|',board[2],'|',board[3])

def game():
    turn='X'
    count=0

    for i in range(10):
        printBoard(board)
        print("It's your turn",turn)

        move=int(input())

        if(board[move]==' '):
            board[move]=turn
            count+=1
        else:
            print("position filled :/")
            continue

        
        if count>=5:
            if board[1]==board[2]==board[3]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
            elif board[4]==board[5]==board[6]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
            elif board[7]==board[8]==board[9]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
            elif board[1]==board[5]==board[9]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
            elif board[7]==board[5]==board[3]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
            elif board[7]==board[4]==board[1]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
            elif board[8]==board[5]==board[2]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
            elif board[9]==board[6]==board[3]!=' ':
                print(turn,"has won the game")
                printBoard(board)
                break
                
        if(count==9):
            print("The game is a tie! No one wins ")
            print("****************")
            break

        if(turn=='X'):
            turn='O'
        else:
            turn='X'
        

        
if __name__=="__main__":
    game()
    restart= input("Do you want to playn Again?(y/n)")
    if(restart=='Y' or restart=='y'):
        for key in board:
            board[key]=' '

        game()
            