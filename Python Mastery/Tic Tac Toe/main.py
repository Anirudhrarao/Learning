import pygame as pg 
from sys import exit

pg.init()

WIDTH = 600
HEIGHT = 600

# block size or grid size
BLOCK_SIZE = 120

# Chance counter
CHANCE_COUNT = 0

win = pg.display.set_mode((WIDTH, HEIGHT))

# loading images to render them on the screen
board_img = pg.image.load("assets/board.png").convert_alpha()
circle_img = pg.image.load("assets/circle.png").convert_alpha()
cross_img = pg.image.load("assets/cross.png").convert_alpha()

# loading button img to render them on the screen 
restart_img = pg.image.load("assets/restart.png").convert_alpha()
# x, and y position
restart_btn_rect = restart_img.get_rect(center=(300, 530))

# Displaying the text on the screen
font = pg.font.Font("assets/arial.ttf", 20)
label_info=font.render("Player 1 chance",True,(18,18,18))
label_info_rect=label_info.get_rect(center=(300,30))

# Checking whether the player 1 chance is or player 2 chance
is_player1_chance = True 

# Someone won
SOMEONE_WON = False

# Matrix to store empty values
matrix = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]

# Position where we clicked on screen
pos = (0, 0)
result = None

# Storinng position where we clicked on board with img that we gonna display on board
pieces = []

# Locking the fps to save resources of cpu
clock = pg.time.Clock()

def checkedClickedPosition(pos):
    # First row for rendered cross and circle png
    if (pos[0] > 120 and pos[0] < 240) and (pos[1] > 120 and pos[1] < 240):
        return (1,1)
    elif (pos[0] > 240 and pos[0] < 360) and (pos[1] > 120 and pos[1] < 240):
        return (1,2)
    elif (pos[0] > 360 and pos[0] < 480) and (pos[1] > 120 and pos[1] < 240):
        return (1,3)
    
    # Second row for rendered cross and circle png
    elif (pos[0] > 120 and pos[0] < 240) and (pos[1] > 240 and pos[1] < 360):
        return (2,1)
    elif (pos[0] > 240 and pos[0] < 360) and (pos[1] > 240 and pos[1] < 360):
        return (2,2)
    elif (pos[0] > 360 and pos[0] < 480) and (pos[1] > 240 and pos[1] < 360):
        return (2,3)
    
    # Third row for rendered cross and circle png
    elif (pos[0] > 120 and pos[0] < 240) and (pos[1]>360 and pos[1] < 480):
        return (3,1)
    elif (pos[0] > 240 and pos[0] < 360) and (pos[1]>360 and pos[1] < 480):
        return (3,2)
    elif (pos[0] > 360 and pos[0] < 480) and (pos[1]>360 and pos[1] < 480):
        return (3,3)
    return None

def checkCompletion(matrix):
    winner = None  # Initialize winner to None
    # For rows checking whether the patterns is matched or not
    for i in range(3):
        if matrix[i][0]==matrix[i][1]==matrix[i][2]:
            if matrix[i][0]=="x":
                winner="Player 1 is winner"
            elif matrix[i][0]=="o":
                winner="Player 2 is winner"
            if matrix[i][0]!="-":
                return winner,(120,120*(i+1)+60),(480,120*(i+1)+60) 
    
    # For column checking whether the patterns is mathced or not
    for i in range(3):
        if matrix[0][i]==matrix[1][i]==matrix[2][i]:
            if matrix[0][i]=="x":
                winner="Player 1 is winner"
            elif matrix[0][i]=="o":
                winner="Player 2 is winner"
            if matrix[0][i]!="-":
                return winner,(120*(i+1)+60,120),(120*(i+1)+60,480) 
    
    # For diagnol checking whether the patterns is mathced or not
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        if matrix[0][0]=="x":
            winner="Player 1 is winner"
        elif matrix[0][0]=="o":
            winner="Player 2 is winner"
        if matrix[0][0]!="-":
            return winner,(120,120),(480,480)
    
    if matrix[0][2]==matrix[1][1]==matrix[2][0]:
        if matrix[1][2]=="x":
            winner="Player 1 is winner"
        elif matrix[1][2]=="o":
            winner="Player 2 is winner"
        if matrix[0][2]!="-":
            return winner,(480,120),(120,480)
    
    # If not match any pattern
    return "No one is winner!", (0, 0)

            
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONUP:
            # Getting position where we clicked
            pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if restart_btn_rect.collidepoint(pos):
                matrix = [
                    ['-', '-', '-'],
                    ['-', '-', '-'],
                    ['-', '-', '-'],
                ]
                pieces = []
                is_player1_chance = True
                CHANCE_COUNT = 0
                label_info = font.render("Player 1 chance", True, (18, 18, 18))
                SOMEONE_WON = False
                
    # Now we will check the position is valid or not means our target are should be click
    result = checkedClickedPosition(pos)
    
    if result != None:
        if matrix[result[0]-1][result[1]-1] == "-":
            if is_player1_chance:
                # Now we will place cross circle img on board
                pieces.append([cross_img,BLOCK_SIZE*result[1]+20, BLOCK_SIZE*result[0]+20])
                is_player1_chance = False
                matrix[result[0]-1][result[1]-1] = "X"
                label_info = font.render("Player 2 chance",True,(18,18,18))
            else:
                pieces.append([circle_img,BLOCK_SIZE*result[1]+20, BLOCK_SIZE*result[0]+20])
                is_player1_chance = True
                matrix[result[0]-1][result[1]-1] = "O"
                label_info = font.render("Player 1 chance",True,(18,18,18))
            CHANCE_COUNT += 1
            
            temp = checkCompletion(matrix)
            if temp[1] != (0, 0):
                label_info = font.render(temp[0], True, (18, 18, 18))
                SOMEONE_WON = True
                
    pos = (0,0)
            
    win.fill((255, 255, 255))
    win.blit(board_img,(WIDTH//5,HEIGHT//5))
    win.blit(label_info, label_info_rect)
    for piece in pieces:
        win.blit(piece[0],(piece[1], piece[2]))
    
    if SOMEONE_WON == True or CHANCE_COUNT == 9:
        if SOMEONE_WON:
            pg.draw.line(win,(255, 255, 255),temp[1],temp[2])
        else:
            label_info = font.render(temp[0], True, (18, 18, 18))
            
        win.blit(restart_img, restart_btn_rect)
    pg.display.update()
    clock.tick(60)