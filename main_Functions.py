import pygame
import os

AlphaValue = [0, False]
def ItenOnSc(screen, imgname):
    img = pygame.image.load(f".\Assets\Other\FrameImg\{imgname}")
    surf = pygame.Surface((screen.get_width(), screen.get_height()))
    surf.fill((0, 0, 0))
    for i in range(20):
        surf.set_alpha(i)
        screen.blit(surf,(0,0))
        pygame.display.update(surf.get_rect())
    screen.blit(img, (0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                 if pygame.key.get_pressed()[pygame.K_e]:
                    return
        pygame.display.update(surf.get_rect())
        pygame.display.update(img.get_rect())

def MenuOnScreen(screen, font, text, FileName):
    Load_File = font.render("Load", 1, (0, 0, 0))
    Save_File = font.render("Save", 1, (0, 0, 0))
    Quit_File = font.render("Quit", 1, (0, 0, 0))
    Mouse_x, Mouse_y = pygame.mouse.get_pos() #Get Mouse position
    MouseClick = pygame.mouse.get_pressed()
    Click = True

    surf = pygame.Surface((300, 60))#Black Cube behind text
    surf.set_alpha(150)
    surf.fill((200, 200, 200))

    if Mouse_x > 20 and Mouse_y > 5 and Mouse_x < 20 + Save_File.get_width() and Mouse_y < 5 + Save_File.get_height():
        Save_File = font.render("Save", 1, (255, 0, 0))
    if Mouse_x > 120 and Mouse_y > 5 and Mouse_x < 120 + Load_File.get_width() and Mouse_y < 5 + Load_File.get_height():
        Load_File = font.render("Load", 1, (255, 0, 0))
    if Mouse_x > 220 and Mouse_y > 5 and Mouse_x < 220 + Quit_File.get_width() and Mouse_y < 5 + Quit_File.get_height():
        Quit_File = font.render("Quit", 1, (255, 0, 0))
    screen.blit(surf,(0, 0))
    if Mouse_x > 20 and Mouse_y > 5 and Mouse_x < 20 + Save_File.get_width() and Mouse_y < 5 + Save_File.get_height() and MouseClick[0] and Click:
        Click = False
        if not os.path.exists('./Assets/ScriptAssets/SaveSpots.txt'):
            open('./Assets/ScriptAssets/SaveSpots.txt', 'x')
        file = open('./Assets/ScriptAssets/SaveSpots.txt','w')
        file.write(FileName + "=" + text)
        file.close()
        Save_File = font.render("Save", 1, (9, 0, 255),)
        screen.blit(pygame.font.SysFont('Comic Sans MS', 40, False).render(" - Saved!", 1, (0, 0, 0)),(300, 5))
        pygame.display.flip()
        pygame.time.delay(1300)

    if Mouse_x > 120 and Mouse_y > 5 and Mouse_x < 120 + Load_File.get_width() and Mouse_y < 5 + Load_File.get_height() and MouseClick[0] and Click:
        Load_File = font.render("Load", 1, (9, 0, 255))
        screen.blit(Load_File,(120, 5))
        # print(os.path.getsize('.//Assets//ScriptAssets//SaveSpots.txt'))
        if os.path.getsize('.//Assets//ScriptAssets//SaveSpots.txt') == 0:
            screen.blit(font.render(" - No saves!", 1, (0, 0, 0)),(350, 5))
            screen.blit(Save_File,(20, 5))
            screen.blit(Load_File,(120, 5))
            screen.blit(Quit_File,(220, 5))
            pygame.display.update()
            pygame.time.delay(1300)
        else:
            return "LoadSave"
    if Mouse_x > 220 and Mouse_y > 5 and Mouse_x < 220 + Quit_File.get_width() and Mouse_y < 5 + Quit_File.get_height() and MouseClick[0] and Click:
        return "Quit"
    
    screen.blit(Save_File,(20, 5))
    screen.blit(Load_File,(120, 5))
    screen.blit(Quit_File,(220, 5))
    
def blit_text(screen, Text, Pos, font, FieldW, FieldH):
    Words = [i.split(' ') for i in Text.splitlines()]
    SpaceValue = font.size(' ')[0] #Get word space width

    x,y = Pos
    for i in Words: # Array cycle
        for j in i: #Words cycle
            word_surface = font.render(j, 1, (255, 255, 255, 255))
            wordW, wordH = word_surface.get_size() #Get word size
            if x + wordW >= FieldW - 50: # if : X position + word width is >= than Screen Width, then we start on new row.
                x = Pos[0] # Reset x position
                y += wordH # Paragraph of text
            screen.blit(word_surface, (x, y))
            x += wordW + SpaceValue # Space between words
        x = Pos[0] # Reset x position
        y += wordH # Paragraph of text 

def CharacterOutp(screen, Characters, BackGround, FieldW, FieldH, IconText): #Output and set Characters to them positions
    if BackGround.CharactersOnScreen:# if backsceen allow output
        if not BackGround.TwoCharacters: #If only one character
            for i in range(len(Characters)):
                if Characters[i].name == IconText or Characters[i].OnScreen: # Find character that need to output
                    Characters[i].XY = list(Characters[i].rect) #Set original obj coordinates
                    screen.blit(Characters[i].objSprite, (Characters[i].XY[0] + Characters[i].XMove, Characters[i].XY[1])) # + Characters[i].XMove need object to move
                    break
        elif BackGround.TwoCharacters == True:
            RemValue = -1 #To not flip two same objects
            for i in range(2):
                for j in range(len(Characters)):
                    if Characters[j].OnScreen and j != RemValue: 
                        RemValue = j
                        if i == 0: #First object
                            Characters[j].XY = [50 + Characters[j].XMove,20]
                            screen.blit(Characters[j].objSprite, Characters[j].XY)
                        else:#Second object
                            Characters[j].XY = [(FieldW- 500) + Characters[j].XMove ,20]
                            screen.blit(Characters[j].objSprite, Characters[j].XY)
                        break
    for i in range(len(Characters)): # Move obj by it's code
        if Characters[i].move == "Left": 
            Characters[i].XMove -= 10
        elif Characters[i].move == "Right": 
            Characters[i].XMove += 10

def ChoiceMenu(screen, BackGround, line, Question, FileName, FullLine, DialogueQuestion=False):
    Words = [i.split(';') for i in line.splitlines()] #Take words
    if Question[-1] == "\n" and DialogueQuestion == False:
        print("'",Question,"'")
        print(DialogueQuestion)
        Question = Question[:-1]

    dialogueSprite = pygame.image.load(".\Assets\Dialogue\Dialogue.png")

    font = pygame.font.SysFont('Comic Sans MS', 30, False) #Set system Font
    text = font.render("", 1, (255, 255, 255, 255)) #Set font

    Coord = []#Varible saves all coordinates
    y = 0

    surf = pygame.Surface((480, 60))#Black Cube behind text
    surf.set_alpha(100)
    surf.fill((150, 150, 150))

    Copy = [] #List that will save all information about file
    file = open('.//Assets//ScriptAssets//1.1//ActionScript.txt','r') #Open Action Script to read
    for i in file: # Take file to Array
        Copy.append(i)
    file.close()
    os.remove('.//Assets//ScriptAssets//1.1//ActionScript.txt') #Remove FIle
    file = open('.//Assets//ScriptAssets//1.1//ActionScript.txt','w') #Create File
    if len(Copy) <= 0:
        Copy.append("Start\n")

    if len(Words[0]) == 2: y = (screen.get_height()/2) - 200 #if 2 words then height == (screen.get_height()/2) - 200
    elif len(Words[0]) == 3: y = (screen.get_height()/2) - 300 
    elif len(Words[0]) >= 4: y = (screen.get_height()/2) - 400

    for i in Words[0]: # Set Coordinates
        y += 100
        Coord.append([(screen.get_width()/2) - 100, y])
    while True:
        Mouse_x, Mouse_y = pygame.mouse.get_pos() #Get Mouse position
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #IF WE OUT THEN SAVE EVERYTHING
                file.writelines(Copy)
                pygame.quit()
                exit()

        Index = 0 #Counter for array
        screen.blit(BackGround.objBackground,(0,0)) #blit background
        MouseClick = pygame.mouse.get_pressed()
        
        for i in Words[0]:
            text = font.render(i, 1, (0, 0, 0, 255))
            if Mouse_x > (Coord[Index][0] - (surf.get_width()/2) + 100) and Mouse_y >= Coord[Index][1] and Mouse_x < (Coord[Index][0] - (surf.get_width()/2) + 100) + surf.get_width() and Mouse_y <= Coord[Index][1] + surf.get_height(): #If we on button then start new game
                text = font.render(i, 1, (240, 0, 0, 255))
                for event in pygame.event.get():
                    if MouseClick[0]: # Rewrite ActionScriptFile
                        for j in range(len(Copy)): #//////////////////////CAN BE SOME ERRORS AND BUGS, CHECK THIS UP////////////////////////
                            if Copy[j][:len(Question)] == Question:
                                print("Replace")
                                Copy[j] = Question + ";" + i +"\n"
                                break
                            elif j == len(Copy) - 1:
                                print("append")
                                Copy.append(Question + ";" + i + "\n")
                        file.writelines(Copy)
                        file.close()
                        return
            screen.blit(surf, (Coord[Index][0] - (surf.get_width()/2) + 100, Coord[Index][1])) 
            screen.blit(text, (Coord[Index][0] - (text.get_width()/2) + 100, Coord[Index][1]))
            Index += 1
        
        if DialogueQuestion:
            screen.blit(dialogueSprite,((screen.get_width() - 1000)/2, 500))
            blit_text(screen, Question, ((screen.get_width() - 1000)/2 + 70, 540), font, screen.get_width(), screen.get_width())#text
        Command = MenuOnScreen(screen,font,FullLine, FileName)
        if Command == "LoadSave" or Command == "Quit":
            if not file.closed:
                file.writelines(Copy)
                file.close()
            return Command
        pygame.display.flip() 
    
def DialogueFunction(screen, Characters, FieldW, FieldH, BackGround, text, FileName, Icon=False):
    dialogueIconSprite = pygame.image.load(".\Assets\Dialogue\Dialogue_Icon.png")
    dialogueSprite = pygame.image.load(".\Assets\Dialogue\Dialogue.png")

    font = pygame.font.SysFont('Comic Sans MS', 30, False) #Set system Font
    Dialogue = []
    Letter = ""
    IconText = ""

    Legosi_Icon = False
    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi2.png")
    for i in range(len(text)): #take replics
        if text[i] == ';': # IF ; then this is icon name - character name
            IconText = Letter #Take Characters name
            Letter = "" #Clear word
            if Icon == False:
                if IconText == "Legosi_Angry":
                    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi_Angry.png")
                elif IconText == "Legosi_Confused":
                    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi_Confused.png")
                elif IconText == "Legosi_Susp":
                    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi_Susp.png")
                elif IconText == "Legosi_Calm":
                    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi_Calm.png")
                elif IconText == "Legosi_AngryFace":
                    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi_AngryFace.png")
                elif IconText == "Legosi_Sad":
                    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi_Sad.png")
                elif IconText == "Legosi_Suprised":
                    IconSprite = pygame.image.load(".\Assets\Legosi_Icon\Legosi_Suprised.png")
                IconSprite = pygame.transform.scale(IconSprite, (IconSprite.get_width() - 200,IconSprite.get_height() - 200)) #Change Legosi icon sprite
                Legosi_Icon = True
        else:
            if text[i] == '|':
                Dialogue.append(Letter)
                Letter = ""
            else:
                Letter += text[i]
    DialogueCounter = 0
    clock = pygame.time.Clock()
    
    while DialogueCounter < len(Dialogue):
        screen.blit(BackGround.objBackground, (0,0))#background
        CharacterOutp(screen, Characters, BackGround, FieldW, FieldH, IconText)

        if not Icon: #Icon dialogue check
            screen.blit(dialogueSprite,((FieldW - 1000)/2, 500))
        else:
            screen.blit(dialogueIconSprite,((FieldW - 1000)/2, 500))
            if IconText == "Jack":
                screen.blit(font.render(IconText, 1, (255, 234, 37, 255)), ((FieldW - 1000)/2 + 78, 490))#text
            elif IconText == "Miguno":
                screen.blit(font.render(IconText, 1, (183, 115, 47, 255)), ((FieldW - 1000)/2 + 78, 490))#text
            elif IconText == "Durham":
                screen.blit(font.render(IconText, 1, (169, 163, 105, 255)), ((FieldW - 1000)/2 + 78, 490))#text
            else:
                screen.blit(font.render(IconText, 1, (255, 255, 255, 255)), ((FieldW - 1000)/2 + 78, 490))#text
        if Legosi_Icon and BackGround.CharactersOnScreen:
            if DialogueCounter >= len(Dialogue):
                blit_text(screen, Dialogue[len(Dialogue) - 1], ((FieldW - 1000)/2 + 70, 540), pygame.font.SysFont('Comic Sans MS', 25, False), FieldW - IconSprite.get_width() + 120, FieldH)#text
            else:
                blit_text(screen, Dialogue[DialogueCounter], ((FieldW - 1000)/2 + 70, 540), pygame.font.SysFont('Comic Sans MS', 25, False), FieldW - IconSprite.get_width() + 150, FieldH)#text
        else:
            if DialogueCounter >= len(Dialogue):
                blit_text(screen, Dialogue[len(Dialogue) - 1], ((FieldW - 1000)/2 + 70, 540), font, FieldW, FieldH)#text
            else:
                blit_text(screen, Dialogue[DialogueCounter], ((FieldW - 1000)/2 + 70, 540), font, FieldW, FieldH)#text

        for j in range(len(Characters)): #Stop move properties
            if Characters[j].XMove >= FieldW or Characters[j].XMove < -FieldW:
               Characters[j].move = ""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_e]: #and time >= 20:
                    DialogueCounter += 1

        Command = MenuOnScreen(screen,font,text, FileName)
        if Command == "LoadSave" or Command == "Quit": return Command

        if Legosi_Icon == True: # Main Character icon
            screen.blit(IconSprite, (FieldW - IconSprite.get_width() + 30, FieldH-IconSprite.get_height())) 
        pygame.display.flip()
        clock.tick(60)

def ScreenDimmingFunc(screen, FieldW, FieldH):
        surf = pygame.Surface((FieldW, FieldH))
        surf.fill((0, 0, 0))
        for i in range(0, 100):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            surf.set_alpha(i)
            screen.blit(surf, (0, 0))
            pygame.display.flip()
            pygame.time.delay(10)
        AlphaValue[0] = surf.get_alpha() + 100
        AlphaValue[1] = True

def ScreenUnDimmingFunc(screen,BackGround): #UnDimming function for screen
    surf = pygame.Surface((screen.get_width(), screen.get_height()))
    surf.fill((0, 0, 0))

    while AlphaValue[1] != False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()   
        surf.set_alpha(AlphaValue[0])
        screen.blit(BackGround.objBackground, (0, 0))
        screen.blit(surf, (0, 0))
        pygame.display.flip()

        AlphaValue[0] -= 10
        if AlphaValue[0] <= 0:
            AlphaValue[1] = False