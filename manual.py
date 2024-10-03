import os
import pygame
import FirstScript
import main_Class as mC
import main_Functions as mF
def StartGameFunc(screen, FieldW, FieldH): #main function for novelle chapters
    if not os.path.exists(r'script.txt'):
        fileCopy = open(r'script.txt', 'w')
        fileCopy.write("1.1")
        fileCopy.close()
    file = open(r'script.txt', 'r')
    for i in file:
        if i[:-1] == "1.1" or i == "1.1":
            FirstScript.main(screen, FieldW, FieldH)
    file.close()

pygame.init()
FieldW = 1060
FieldH = 720

screen = pygame.display.set_mode([FieldW, FieldH], vsync=1) # Screen properties
pygame.display.set_caption('BEASTARS')

MenuSprite = mC.sceneBackground(r".//Menu.jpg", FieldW, FieldH, True)

font = pygame.font.Font(r".//Fonstars-4Bo0p.otf", 35) #Set system Font
text1 = font.render("", 1, (0, 0, 0, 255))
text2 = font.render("", 1, (0, 0, 0, 255))
text3 = font.render("", 1, (0, 0, 0, 255))

Main_TextCoord = [[800, 20],[695,80],[920,140]] #For Menu

pygame.mouse.set_visible(False)
cursor_img = pygame.image.load(r".//Assets//Other//Cursor.png")
img = pygame.image.load(r".//icon.ico")
pygame.display.set_icon(img)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        Mouse_x = pygame.mouse.get_pos()[0]
        Mouse_y = pygame.mouse.get_pos()[1]

        if Mouse_x > Main_TextCoord[0][0] and Mouse_y >= Main_TextCoord[0][1] and Mouse_x < Main_TextCoord[0][0] + text1.get_width() and Mouse_y <= Main_TextCoord[0][1] + text1.get_height(): #If new game, then start new game
            text1 = font.render("NewGAme", 1, (255, 10, 0, 105))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mF.ScreenDimmingFunc(screen, FieldW, FieldH)
                StartGameFunc(screen, FieldW, FieldH)
        else:
            text1 = font.render("NewGAme", 1, (0, 0, 0, 255))
        if Mouse_x > Main_TextCoord[1][0] and Mouse_y >= Main_TextCoord[1][1] and Mouse_x < Main_TextCoord[1][0] + text2.get_width() and Mouse_y <= Main_TextCoord[1][1] + text2.get_height(): #Load from last save
            text2 = font.render("LoAdLastSAve", 1, (255, 10, 0, 105))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if os.path.getsize('.//Assets//ScriptAssets//SaveSpots.txt') == 0:
                    screen.blit(pygame.font.SysFont('Comic Sans MS', 30, False).render("No saves! - ", 1, (0, 0, 0)),(Main_TextCoord[1][0] - 160, Main_TextCoord[1][1]))
                    pygame.display.flip()
                    pygame.time.delay(1300)
                else:
                    FirstScript.setSaveMenu()
                    mF.ScreenDimmingFunc(screen, FieldW, FieldH)
                    StartGameFunc(screen, FieldW, FieldH)
        else:
            text2 = font.render("LoAdLastSAve", 1, (0, 0, 0, 255))
        if Mouse_x > Main_TextCoord[2][0] and Mouse_y >= Main_TextCoord[2][1] and Mouse_x < Main_TextCoord[2][0] + text3.get_width() and Mouse_y <= Main_TextCoord[2][1] + text3.get_height(): #Load from last save 
            text3 = font.render("Quit", 1, (255, 10, 0, 105))
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((255,255,255))
                screen.blit(pygame.font.Font("Fonstars-4Bo0p.otf", 60).render("Seeyounexttime", 1, (0, 0, 0)),(screen.get_width()/2 - 320, screen.get_height()/2 - 50))
                pygame.display.flip()
                pygame.time.delay(1300)
                pygame.quit()
                exit()
        else:
            text3 = font.render("Quit", 1, (0, 0, 0, 255))
    
    screen.blit(MenuSprite.objBackground, (0,0)) #Output MenuBackGround
    screen.blit(text1, (Main_TextCoord[0][0], Main_TextCoord[0][1]))
    screen.blit(text2, (Main_TextCoord[1][0], Main_TextCoord[1][1]))
    screen.blit(text3, (Main_TextCoord[2][0], Main_TextCoord[2][1]))
    screen.blit(pygame.image.load(".//Assets//Other//Cursor.png"), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) # draw the cursor
    pygame.display.flip()