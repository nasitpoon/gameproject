import pygame

pygame.init()

#create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("The spacial 2048")  # caption เกม2048
icon = pygame.image.load("logo.png")  # หาภาพชื่อ...
pygame.display.set_icon(icon)  # แสดงภาพicon
bg = pygame.image.load("bg.jpg")  # หาภาพชื่อ...


#loading image
start_img = pygame.image.load("start_btn.png").convert_alpha()
exit_img = pygame.image.load("exit_btn.png").convert_alpha()

#button class
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

#create button instances
start_button = Button(100,200, start_img)
exit_button = Button(450,200, exit_img)

#game loop
run = True
while run:
    
    screen.blit(bg, (0, 0))
    # screen.blit((248,248,248))
    
    start_button.draw()
    exit_button.draw()
    
    #event handler
    for event in pygame.event.get():
        
        #quit game
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit()
pygame.display.update()  # แสดงภาพbackground