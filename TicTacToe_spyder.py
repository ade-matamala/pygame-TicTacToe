import pygame #imports pygame, user interface
import numpy as np #imports numpy, background code
pygame.init() #initializes the game
pygame.font.init() #initializes fonts

win = pygame.display.set_mode((550,550)) #creates the window

pygame.display.set_caption('TicTacToe') #sets the title for the window

board = np.zeros((3,3),dtype=int) #creates a white board

def clear(board): #clears board to zeros
    board = np.zeros((3,3), dtype=int)
    return(board)

def play(char,place,board): #char = 1 or 2 ; place  ; board 
    if board[place] == 0:
        board[place] = char
        return(board) 
    
def check_winner(board):
    l=[]
    winner = 0
    c=0
    for i in board: #linearize the 3x3 array
        for j in i:
            l.append(j)
            
    for n in (0,3,6): #check for rows
        if l[n]==l[n+1] and l[n+1]==l[n+2] and l[n] == 1 and l[n]!=0 and l[n+1]!=0 and l[n+2]!=0:
            print("player 1 wins, rows")
            winner = 1
        elif l[n]==l[n+1] and l[n+1]==l[n+2] and l[n] == 2 and l[n]!=0 and l[n+1]!=0 and l[n+2]!=0:
            print("player 2 wins, rows")
            winner = 2
        
    for n in (0,1,2): #check for columns
        if l[n]==l[n+3] and l[n+3]==l[n+6] and l[n] == 1 and l[n]!=0 and l[n+3]!=0 and l[n+6]!=0:
            print("player 1 wins, columns")
            winner = 1
        elif l[n]==l[n+3] and l[n+3]==l[n+6] and l[n] == 2 and l[n]!=0 and l[n+3]!=0 and l[n+6]!=0:
            print("player 2 wins, columns")
            winner = 2
        
    #check for diagonal1
    if l[0]==l[4] and l[4]==l[8] and l[0] == 1 and l[0]!=0 and l[4]!=0 and l[8]!=0:
        print("player 1 wins, diagonal")
        winner = 1
    elif l[0]==l[4] and l[4]==l[8] and l[0] == 2 and l[0]!=0 and l[4]!=0 and l[8]!=0:
        print("player 2 wins, diagonal")
        winner = 2
        
    #check for diagonal2
    if l[2]==l[4] and l[4]==l[6] and l[2] == 1 and l[2]!=0 and l[4]!=0 and l[6]!=0:
        print("player 1 wins, diagonal")
        winner = 1
    elif l[2]==l[4] and l[4]==l[6] and l[2] == 2 and l[2]!=0 and l[4]!=0 and l[6]!=0:
        print("player 2 wins, diagonal")
        winner = 2
    
    for n in l: #check for draw
        if n!=0:
            c = c+1
        if c == 9:
            winner = 3
            print('draw')
    
    return winner #if winner=1, player 1 won; if winner=2, player 2 won; if winner = 3, draw

def winner_screen(winner):
    s10 = pygame.draw.rect(win,(255,255,0),(75,75,400,400))
    myfont = pygame.font.SysFont("Comic Sans", 100)
    if winner == 1:
        label1 = myfont.render("Player 1", 1, (255,0,0)) 
        label2 = myfont.render("wins!", 1, (255,0,0))
        swin = pygame.draw.rect(win, (255,0,0), (225,125,100,100))
        win.blit(label1, (150, 250))
        win.blit(label2, (150, 325))
    if winner == 2:
        label1 = myfont.render("Player 2", 1, (255,0,0)) 
        label2 = myfont.render("wins!", 1, (255,0,0))
        swin = pygame.draw.circle(win, (0,255,0), (275,175),50)
        win.blit(label1, (150, 250))
        win.blit(label2, (150, 325))
    if winner == 3:
        label1 = myfont.render("It's a", 1, (255,0,0)) 
        label2 = myfont.render("draw!", 1, (255,0,0))
        win.blit(label1, (125, 150))
        win.blit(label2, (120, 250))
        
s0 = pygame.draw.rect(win,(255,255,255),(25,25,150,150))  #creates a white(255,255,255) square(150,150) at position (25,25)
s1 = pygame.draw.rect(win,(255,255,255),(200,25,150,150)) #creates a white(255,255,255) square(150,150) at position (200,25)
s2 = pygame.draw.rect(win,(255,255,255),(375,25,150,150)) #creates a white(255,255,255) square(150,150) at position (375,25)                               

s3 = pygame.draw.rect(win,(255,255,255),(25,200,150,150)) #                                 "
s4 = pygame.draw.rect(win,(255,255,255),(200,200,150,150))#                                 "
s5 = pygame.draw.rect(win,(255,255,255),(375,200,150,150))#                                 "

s6 = pygame.draw.rect(win,(255,255,255),(25,375,150,150)) #                                 "
s7 = pygame.draw.rect(win,(255,255,255),(200,375,150,150))#                                 "
s8 = pygame.draw.rect(win,(255,255,255),(375,375,150,150))#                                 "

run = True #flag for running the game

draw_object = 'rect' #the initial player (1) plays as rect

s0_open = True #is square 1 open to a player?
s1_open = True #is square 2 open to a player?
s2_open = True #is square 3 open to a player?
s3_open = True #            "
s4_open = True #            "
s5_open = True #            "
s6_open = True #            "
s7_open = True #            "
s8_open = True #            "

while run: #while the game runs
    pygame.time.delay(100) #delay between program refreshes?
    for event in pygame.event.get(): #checks for events happening
        if event.type == pygame.QUIT: #checks if the program has quitted and terminates it
            run = False
        if event.type == pygame.KEYDOWN: #checks if a key is pressed
            if event.key == pygame.K_SPACE: #checks if the spacebar key is pressed, the reset button
                
                board = clear(board) #clears the background board
                
                print(board)
                
                s0_open = True #opens every square
                s1_open = True
                s2_open = True
                s3_open = True
                s4_open = True
                s5_open = True
                s6_open = True
                s7_open = True
                s8_open = True
                
                sback = pygame.draw.rect(win,(0,0,0),(0,0,550,550))
                
                s0 = pygame.draw.rect(win,(255,255,255),(25,25,150,150)) #redraws the initial state of every square
                s1 = pygame.draw.rect(win,(255,255,255),(200,25,150,150))
                s2 = pygame.draw.rect(win,(255,255,255),(375,25,150,150))

                s3 = pygame.draw.rect(win,(255,255,255),(25,200,150,150))
                s4 = pygame.draw.rect(win,(255,255,255),(200,200,150,150))
                s5 = pygame.draw.rect(win,(255,255,255),(375,200,150,150))

                s6 = pygame.draw.rect(win,(255,255,255),(25,375,150,150))
                s7 = pygame.draw.rect(win,(255,255,255),(200,375,150,150))
                s8 = pygame.draw.rect(win,(255,255,255),(375,375,150,150))               
                
        if event.type == pygame.MOUSEBUTTONUP: #checks if the mouse button is pressed
            pos = pygame.mouse.get_pos() #stores the position of the mouse when it's pressed as pos
            
            if s0.collidepoint(pos) and s0_open: #checks if square 1 and pos collide AND if square 1 is open
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (50,50,100,100)) #draws a red(255,0,0) square(100,100) at position(50,50) if it's the rect player turn
                    play(1,(0,0),board)
                    print(board)
                    draw_object = 'circle' #changes shape to the circle player
                else:
                    pygame.draw.circle(win, (0,255,0), (100,100),50) #draws a green(0,255,0) circle centered at position(50,50) with radius (50) if it's the rect player turn
                    play(2,(0,0),board)
                    print(board)                   
                    draw_object = 'rect' #changes shape to the rect player
                s0_open = False #closes square 1 to anymore players
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
            if s1.collidepoint(pos) and s1_open: #checks if square 2 and pos collide AND if square 2 is open
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (225,50,100,100))
                    play(1,(0,1),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (275,100),50)
                    play(2,(0,1),board)
                    print(board)
                    draw_object = 'rect'
                s1_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
            if s2.collidepoint(pos) and s2_open: #checks if square 3 and pos collide AND if square 3 is open
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (400,50,100,100))
                    play(1,(0,2),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (450,100),50)
                    play(2,(0,2),board)
                    print(board)
                    draw_object = 'rect'
                s2_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
                
            if s3.collidepoint(pos) and s3_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (50,225,100,100))
                    play(1,(1,0),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (100,275),50)
                    play(2,(1,0),board)
                    print(board)
                    draw_object = 'rect'
                s3_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
            if s4.collidepoint(pos) and s4_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (225,225,100,100))
                    play(1,(1,1),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (275,275),50)
                    play(2,(1,1),board)
                    print(board)
                    draw_object = 'rect'
                s4_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
            if s5.collidepoint(pos) and s5_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (400,225,100,100))
                    play(1,(1,2),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (450,275),50)
                    play(2,(1,2),board)
                    print(board)
                    draw_object = 'rect'
                s5_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
                
            if s6.collidepoint(pos) and s6_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (50,400,100,100))
                    play(1,(2,0),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (100,450),50)
                    play(2,(2,0),board)
                    print(board)
                    draw_object = 'rect'
                s6_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
            if s7.collidepoint(pos) and s7_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (225,400,100,100))
                    play(1,(2,1),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (275,450),50)
                    play(2,(2,1),board)
                    print(board)
                    draw_object = 'rect'
                s7_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
            if s8.collidepoint(pos) and s8_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (255,0,0), (400,400,100,100))
                    play(1,(2,2),board)
                    print(board)
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (0,255,0), (450,450),50)
                    play(2,(2,2),board)
                    print(board)
                    draw_object = 'rect'
                s8_open = False
                if check_winner(board) != 0: #checks if anyone won
                    winner_screen(check_winner(board))
                
    pygame.display.update() #updates 

pygame.quit()
