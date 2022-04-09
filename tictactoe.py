import pygame
import time
from pygame import mixer

# Initializes the pygame
pygame.init()

# Game Screen
screen = pygame.display.set_mode((800, 600))

# Lines
line_color = (255, 255, 255)

# Tic Tac Toe
gridX = 3
gridY = 3

tttgrid = gridX * gridY

tttboundariesX = 250
tttboundariesY = 150

tttboundsX = []
tttboundsY = []
tttvalue = []
tttmatrix = []

for i in range(gridX):
    tttboundariesX = 250
    for j in range(gridY):
        tttboundsX.append((tttboundariesX, tttboundariesX + 100))
        tttboundsY.append((tttboundariesY, tttboundariesY + 100))
        tttvalue.append(2)
        tttboundariesX += 100
    tttboundariesY += 100

# print(tttboundsX)
# print(tttboundsY)
# print(tttvalue)

# Players

# Score
p1_score = 0
p2_score = 0
tie_score = 0
# Turn
turn = 1
# Round Winner
win1 = 0
win2 = 0

draw = 0
rounds = 1

# Fonts
font = pygame.font.SysFont('arialblack', 32)
font2 = pygame.font.SysFont('arialblack', 50)


# Score
def show_score():
    # First we have to render
    score_p1 = font.render(f"Player 1 : {p1_score}", True, (0, 0, 255))
    score_p2 = font.render(f"Player 2 : {p2_score}", True, (0, 255, 0))
    score_tie = font.render(f"Tie : {tie_score}", True, (255, 0, 0))
    # then blit
    screen.blit(score_p1, (50, 50))
    screen.blit(score_p2, (550, 50))
    screen.blit(score_tie, (350, 50))


# Round Winner
def round_winner(player):
    if player != 0:
        winner = font.render(f"Player {player} wins!!!", True, (0, 0, 255))
    else:
        winner = font.render(f"It's a draw!!!", True, (0, 0, 255))
    screen.blit(winner, (250, 500))


# Drawing X and O
def draw_symbols():
    for i in range(len(tttvalue)):
        if tttvalue[i] == 3 or tttvalue[i] == 5:
            if tttvalue[i] == 3:
                tttsymbol = font.render("X", True, (255, 255, 255))
                screen.blit(tttsymbol,
                            ((tttboundsX[i][0] + tttboundsX[i][1]) / 2, (tttboundsY[i][0] + tttboundsY[i][1]) / 2))
            elif tttvalue[i] == 5:
                tttsymbol = font.render("O", True, (255, 255, 255))
                screen.blit(tttsymbol,
                            ((tttboundsX[i][0] + tttboundsX[i][1]) / 2, (tttboundsY[i][0] + tttboundsY[i][1]) / 2))


# Checks if an player has won
def anyWinning(value):
    if value == 27:
        return 1
    elif value == 125:
        return 2


running = True
# While loop for pygame
while running:
    for event in pygame.event.get():
        # Screen of the Color
        screen.fill((0, 0, 0))
        # Vertical Lines
        pygame.draw.line(screen, line_color, (250, 250), (550, 250))
        pygame.draw.line(screen, line_color, (250, 350), (550, 350))
        # Hotizontal Lines
        pygame.draw.line(screen, line_color, (350, 150), (350, 450))
        pygame.draw.line(screen, line_color, (450, 150), (450, 450))

        # Check if close button is pressed
        if event.type == pygame.QUIT:
            running = False
        # Checks if a player has played their his/her turn
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in range(tttgrid):
                if pos[0] > tttboundsX[i][0] and pos[0] < tttboundsX[i][1] and pos[1] > tttboundsY[i][0] and pos[1] < \
                        tttboundsY[i][1] and tttvalue[i] == 2:
                    if turn == 1:
                        tttvalue[i] = 3
                        turn = 2
                        x_sound = mixer.Sound('X.wav')
                        x_sound.play()
                    elif turn == 2:
                        tttvalue[i] = 5
                        turn = 1
                        o_sound = mixer.Sound('O.wav')
                        o_sound.play()
                    time.sleep(1)
        # Draws X and O symbols
        draw_symbols()

        # Values in a matrix
        tttmatrix = []
        # Check
        for i in range(gridX):
            j = 3 * i
            tttmatrix.append([tttvalue[j], tttvalue[j + 1], tttvalue[j + 2]])

        # print(tttmatrix)

        # Checks if 3 X or 3 O are in a row, column, or diagonal
        for i in range(gridX):
            for j in range(gridY):
                # Right Row
                if j + 1 < 3 and j + 2 < 3:
                    three_value = tttmatrix[i][j] * tttmatrix[i][j + 1] * tttmatrix[i][j + 2]
                    if anyWinning(three_value) == 1:
                        win1 = 1
                    elif anyWinning(three_value) == 2:
                        win2 = 1

                # Left Row
                # if j - 1 >= 0 and j - 2 >= 0:
                #    three_value = tttmatrix[i][j] * tttmatrix[i][j - 1] * tttmatrix[i][j - 2]
                #    if anyWinning(three_value) == 1:
                #        win1 = 1
                #    elif anyWinning(three_value) == 2:
                #        win2 = 1

                # Down Column
                if i + 1 < 3 and i + 2 < 3:
                    three_value = tttmatrix[i][j] * tttmatrix[i + 1][j] * tttmatrix[i + 2][j]
                    if anyWinning(three_value) == 1:
                        win1 = 1
                    elif anyWinning(three_value) == 2:
                        win2 = 1

                # Up Column
                # if i - 1 >= 0 and i - 1 >= 0:
                #    three_value = tttmatrix[i][j] * tttmatrix[i - 1][j] * tttmatrix[i - 2][j]
                #    if anyWinning(three_value) == 1:
                #        win1 = 1
                #    elif anyWinning(three_value) == 2:
                #        win2 = 1

                # Right Diagonal
                if i + 1 < 3 and i + 2 < 3 and j + 1 < 3 and j + 2 < 3:
                    three_value = tttmatrix[i][j] * tttmatrix[i + 1][j + 1] * tttmatrix[i + 2][j + 2]
                    if anyWinning(three_value) == 1:
                        win1 = 1
                    elif anyWinning(three_value) == 2:
                        win2 = 1

                # Left Diagonal
                if i + 1 < 3 and i + 2 < 3 and j - 1 >= 0 and j - 2 >= 0:
                    three_value = tttmatrix[i][j] * tttmatrix[i + 1][j - 1] * tttmatrix[i + 2][j - 2]
                    if anyWinning(three_value) == 1:
                        win1 = 1
                    elif anyWinning(three_value) == 2:
                        win2 = 1
        # If player 1 has won
        if win1 == 1:
            p1_score += 1
            win1 = 0
            win2 = 0
            tttvalue = [2, 2, 2, 2, 2, 2, 2, 2, 2]
            rounds += 1
            if rounds % 2 == 0:
                turn = 2
            else:
                turn = 1
            round_winner(1)
            next_sound = mixer.Sound('Next.wav')
            next_sound.play()

        # If player 2 has won
        if win2 == 1:
            p2_score += 1
            win1 = 0
            win2 = 0
            tttvalue = [2, 2, 2, 2, 2, 2, 2, 2, 2]
            rounds += 1
            if rounds % 2 == 0:
                turn = 2
            else:
                turn = 1
            round_winner(2)
            next_sound = mixer.Sound('Next.wav')
            next_sound.play()

        # Tie Case
        for i in range(tttgrid):
            if tttvalue[i] == 2:
                draw += 1

        # If it's a tie or a draw
        if draw == 0:
            tie_score += 1
            tttvalue = [2, 2, 2, 2, 2, 2, 2, 2, 2]
            rounds += 1
            if rounds % 2 == 0:
                turn = 2
            else:
                turn = 1
            round_winner(0)
            next_sound = mixer.Sound('Next.wav')
            next_sound.play()

        draw = 0

        # Display score
        show_score()

        # For persistence
        pygame.display.update()
