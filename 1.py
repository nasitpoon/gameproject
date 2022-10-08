import pygame
pygame.init()
screen = pygame.display.set_mode((692,443)) #แสดงจอ 800 * 600 pixel
pygame.display.set_caption("The spacial 2048")  #caption เกม2048
icon = pygame.image.load("logo.png") #หาภาพชื่อ...
pygame.display.set_icon(icon) #แสดงภาพicon
bg = pygame.image.load("bg.jpg") #หาภาพชื่อ...
# game_exit =True
# while game_exit:
#     for event in pygame.event.get():
#        print(event)
# pygame.quit()
# quit()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    screen.blit(bg,(0,0)) #ให้ภาพอยู่ที่ ตำแหน่งx=0,y=0
    pygame.display.update() #แสดงภาพbackground