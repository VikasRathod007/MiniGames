from gtn import guess_the_number
from r_p_c import rock_paper_scissors
from wordle import wordle
from connect_four import ConnectFour
from tictactoe import TicTacToe

while True:
    txt='''Mini Games!!!
    -Guess the numbers (1)
    -Rock,Paper,Scissors(2)
    -wordsle (3)
    -ConnectFour (4)
    -Tic Tac toe (5)
    Select a game(Enter a number correspnding to it or 'q' to quit):'''
    value=input(txt)
    if value=="1":
        x=int(input("enter a max number"))
        guess_the_number(x)
    elif value=="2":
        rock_paper_scissors()
    elif value=="3":
         game=wordle()
         game.play()
        
    elif value=="4":
        game=ConnectFour()
        game.play()
    
    elif value=="5":
        game=TicTacToe()
        game.play()
    elif value=="q":
        break