import pygame, sys
import numpy as np
from button import Button
import random

from game import BG_COLORS

pygame.init()
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("The special 2048")



def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


def play1():
    while True:

        BG_COLORS = {
    0: (250, 250, 250),
    2: (238, 228, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 201, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

class Game2048:
    def __init__(self) -> None:
        self.N = 4
        self.cellSize = 150
        self.gap = 4
        self.windowBgColor = (187, 173, 160)
        self.blockSize = self.cellSize + self.gap * 2
        
        self.windowWidth = 1280
        self.windowHeight = 720

        pygame.init()

        # create window
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.myFont = pygame.font.SysFont("Comic Sans MS", 30)
        pygame.display.set_caption("The Special 2048")
        icon = pygame.image.load("logo.png")
        pygame.display.set_icon(icon)


        # init board status
        self.boardStatus = np.zeros((self.N, self.N))
        self.addNewNumber() # add new number to board

    
    def addNewNumber(self):
        freePos = zip(*np.where(self.boardStatus == 0))
        freePos = list(freePos)

        for pos in random.sample(freePos, k=1):
            self.boardStatus[pos] = 2

    def drawBoard(self):
        self.window.fill(self.windowBgColor)

        for r in range(self.N):
            rectY = self.blockSize * r + self.gap
            for c in range(self.N):
                rectX = self.blockSize * c + self.gap
                cellValue = int(self.boardStatus[r][c])

                pygame.draw.rect(
                    self.window,
                    BG_COLORS[cellValue],
                    pygame.Rect(rectX+300, rectY+50, self.cellSize, self.cellSize)
                )

                if cellValue != 0:
                    textSurface = self.myFont.render(f"{cellValue}", True, (0, 0, 0))
                    textRect = textSurface.get_rect(center=(rectX+300 + self.blockSize/2, rectY+50 + self.blockSize/2))
                    self.window.blit(textSurface, textRect)

    def compressNumber(self, data):
        result = [0]
        data = [x for x in data if x != 0]
        for element in data:
            if element == result[len(result) - 1]:
                result[len(result) - 1] *= 2
                result.append(0)
            else:
                result.append(element)
        
        result = [x for x in result if x != 0]
        return result

    def move(self, dir):
        for idx in range(self.N):

            if dir in "UD":
                data = self.boardStatus[:, idx]
            else:
                data = self.boardStatus[idx, :]

            flip = False
            if dir in "RD":
                flip = True
                data = data[::-1]

            data = self.compressNumber(data)
            data = data + (self.N - len(data)) * [0]

            if flip:
                data = data[::-1]

            if dir in "UD":
                self.boardStatus[:, idx] = data
            else:
                self.boardStatus[idx, :] = data

    def isGameOver(self):
        boardStatusBackup = self.boardStatus.copy()
        for dir in "UDLR":
            self.move(dir)

            if (self.boardStatus == boardStatusBackup).all() == False:
                self.boardStatus = boardStatusBackup
                return False
        return True

    def play(self):
        running = True
        while running:
            self.drawBoard()
            pygame.display.update()

            for event in pygame.event.get():
                oldBoardStatus = self.boardStatus.copy()

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move("U")
                    elif event.key == pygame.K_DOWN:
                        self.move("D")
                    elif event.key == pygame.K_LEFT:
                        self.move("L")
                    elif event.key == pygame.K_RIGHT:
                        self.move("R")
                    elif event.key == pygame.K_ESCAPE:
                        running = False

                    if self.isGameOver():
                        print("Game Over !!")
                        return

                    if (self.boardStatus == oldBoardStatus).all() == False:
                        self.addNewNumber()

if __name__ == "__main__":
    game = Game2048()
    # game.play()


def leaderboard():
    while True:
        LEADERBOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("grey")

        LEADERBOARD_TEXT = get_font(35).render("This is the leaderboard screen.", True, "Black")
        LEADERBOARD_RECT = LEADERBOARD_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEADERBOARD_TEXT, LEADERBOARD_RECT)

        LEADERBOARD_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        LEADERBOARD_BACK.changeColor(LEADERBOARD_MOUSE_POS)
        LEADERBOARD_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEADERBOARD_BACK.checkForInput(LEADERBOARD_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def main_menu():
    while True:

        
        SCREEN.fill((227,207,87))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        load_button = pygame.image.load("Options Rect.png")
        scaled_button = pygame.transform.scale(load_button, (700, 120))

        MENU_TEXT = get_font(65).render("The Special 2048", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


        # Button
        PLAY_BUTTON = Button(image=scaled_button, pos=(640, 250), 
                            text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        LEADERBOARD_BUTTON = Button(image=scaled_button, pos=(640, 400), 
                            text_input="LEADERBOARD", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=scaled_button, pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,LEADERBOARD_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play1()
                    game.play()
                if LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    leaderboard()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()