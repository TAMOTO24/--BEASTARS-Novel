import pygame
import main_Functions as mF
import main_Class as mC
# import pyvidplayer

StartDialogue = "" #Saved Dialogue
SavedFileName = "" #Saved File Name
GoToSave = False
def setSaveMenu():
    file = open('.//Assets//ScriptAssets//SaveSpots.txt', 'r')
    Words = [i.split('=') for i in file.read().splitlines()]
    global StartDialogue
    StartDialogue = Words[0][1] + '\n'
    global GoToSave
    GoToSave = True
    global SavedFileName
    SavedFileName = Words[0][0]
def setSave(screen, fileAr, Characters, BackGround, FileName):
    file = open('.//Assets//ScriptAssets//SaveSpots.txt', 'r')
    Words = [i.split('=') for i in file.read().splitlines()]
    global StartDialogue
    StartDialogue = Words[0][1] + '\n'
    global GoToSave
    GoToSave = True
    global SavedFileName
    SavedFileName = Words[0][0]

    for i in range(len(fileAr)):
        fileAr[i].file.close()
        fileAr[i].file = open(fileAr[i].Adress,fileAr[i].Acess)
    for i in Characters: # Reset all characters
        i.OnScreen = False
        i.move = ""
        i.XMove = 0
        i.XY = [0,0]
    BackGround.TwoCharacters = False
    screen.fill((255,255,255))

def Expresion(i,Characters):
    if  i[:-1] == "Jack_Usual<<":#Jack Expresions
        Characters[0].Emotion('./Assets/Characters/Jack/Jack_Usual.png')
    elif i[:-1] == "Jack_Susp<<": 
        Characters[0].Emotion('./Assets/Characters/Jack/Jack_Susp.png')
    elif i[:-1] == "Jack_Puzzled<<":
        Characters[0].Emotion('./Assets/Characters/Jack/Jack_Puzzled.png')
    elif i[:-1] == "Jack_Talk<<":
        Characters[0].Emotion('./Assets/Characters/Jack/Jack_Talk.png')

    if  i[:-1] == "Bill_Usual<<":#Bill Expresions
        Characters[8].Emotion('./Assets/Characters/Bill/Bill.png')
    elif i[:-1] == "Bill_Uniform<<": 
        Characters[8].Emotion('./Assets/Characters/Bill/Bill_Uniform.png')
    elif i[:-1] == "Bill_Uniform_Angry<<": 
        Characters[8].Emotion('./Assets/Characters/Bill/Bill_Uniform_Angry.png')

    if  i[:-1] == "Ellen_Usual<<":#Ellen Expresions
        Characters[4].Emotion('./Assets/Characters/Ellen/Ellen.png')
    elif i[:-1] == "Ellen_Uniform<<": 
        Characters[4].Emotion('./Assets/Characters/Ellen/Ellen_Uniform.png')
    elif i[:-1] == "Ellen_Uniform_Angry<<": 
        Characters[4].Emotion('./Assets/Characters/Ellen/Ellen_Uniform_Angry.png')

    if i[:-1] == "Elz_Usual<<":#Elz Expresions
        Characters[6].Emotion('./Assets/Characters/Elz/Elz.png')
    elif i[:-1] == "Elz_Uniform<<":
        Characters[6].Emotion('./Assets/Characters/Elz/Elz_Uniform.png')
    elif i[:-1] == "Elz_sizers<<":
        Characters[6].Emotion('./Assets/Characters/Elz/Elz_sizers.png')

def setBackGround(BackGround, i):
    if i[:-1] == "Frame1<<": #Frame addition
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame1.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Street1<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Street1.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Room701<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Room701.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "School<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/School.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Frame2.3<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame2.3.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Frame2.2<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame2.2.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Frame2.1<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame2.1.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "SchoolFrame<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/SchoolFrame.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Black<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Black.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Room701Grouph<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Room701Grouph.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "DramaClubStreet<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/DramaClubStreet.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "DramaClubPeople<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/DramaClubPeople.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Frame4.1<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame4.1.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Frame4.2<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame4.2.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "MaleDressingRoom<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/MaleDressingRoom.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Preview1<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Preview1.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Preview<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Preview.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Frame4.3<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame4.3.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Frame4.4<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame4.4.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Frame4.5<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame4.5.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Frame4.6<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame4.6.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "HerbivoresHostel<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/HerbivoresHostel.png')
        BackGround.CharactersOnScreen = True
    elif i[:-1] == "Frame5.1<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Frame5.1.png')
        BackGround.CharactersOnScreen = False
    elif i[:-1] == "Pr2<<":
        BackGround.objBackground = pygame.image.load(r'./Assets/Other/Background/Preview2.png')
        BackGround.CharactersOnScreen = False

def MoveFunc(line, Characters): 
    CharName = ""
    RemCharNamePos = 0
    for i in range(len(line)):
        if line[i] != "_": #Read name To first _ symbol
            CharName += line[i]
        else:
            RemCharNamePos = i + 1 # +1 because to step out _ symbol
            break #Exit cycle
    for i in range(len(Characters)):
        if Characters[i].name == CharName:
            Characters[i].move = line[RemCharNamePos:-1]

def MainCycle(screen, Characters, BackGround, file, FileName:str):
    global StartDialogue
    global GoToSave
    global SavedFileName
    for i in file:
        if i == '\n': #Skip empty line
            continue
        if i[-3:] != "<<\n" and i[-2:] != "<<" and GoToSave:
            if i != StartDialogue and i != StartDialogue[:-1] and GoToSave == True: #If we not in our dialogue
                continue 
            else:
                if SavedFileName == FileName: #If we on need dialogue, and if we on needed file name
                    StartDialogue = ""
                    GoToSave = False
                else:# if not then skip
                    print("|", SavedFileName, FileName, "|")
                    continue
        Comand = ""
        if i[:8] == 'OnScreen':
            text = i.split('=')
            mF.ItenOnSc(screen, text[1][:-1])
        if i[:-1] == 'StopTime=' or i == 'StopTime=\n': #Slow time comand
            time = 0
            while time <= 1200000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                time += 1
        Expresion(i,Characters)
        if i[0] == '#': #Question command
            Value = ""
            RemDot = 1
            EndofLine = -1
            if i[-1] == '\n': EndofLine = -2#If last element in \n then we skip 2 last symbols (# and \n)
            for j in range(1,len(i)): #Take question
                if i[j] == '.': #Take question and remember dot index
                    RemDot = j + 1
                    break
                else: Value += i[j]#get symbols
            if RemDot == 1: 
                Comand = mF.ChoiceMenu(screen, BackGround, i[RemDot:EndofLine], Value, FileName, i) #If dot >1 then we have question
            else: 
                Comand = mF.ChoiceMenu(screen, BackGround, i[RemDot:EndofLine], Value, FileName, i, True) #Last True calling dialogue icon

        setBackGround(BackGround, i) 
        if i[0:6] == "Theme_":
            Name = ""
            if i[-1] == '\n':
                Name = i[6:-3]
            else:
                Name = i[6:-2]
            pygame.mixer.music.load(f"Assets/Theme/{Name}")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)

        # if i[0:4] == 'Vid_':
        #     Name = ""
        #     if i[-1] == '\n':
        #         Name = i[4:-1]
        #     else:
        #         Name = i[4:]
        #     vid = pyvidplayer.Video(f"Media/{Name}")
        #     vid.set_size((screen.get_width(), screen.get_height()))
        #     vid.set_volume(0.7)
        #     while vid._frame_num < vid.frame_count - 4:
        #         for event in pygame.event.get():
        #             if event.type == pygame.QUIT:
        #                 pygame.quit()
        #                 exit()
        #             if event.type == pygame.KEYDOWN:
        #                 if pygame.key.get_pressed()[pygame.K_e]: #and time >= 20:
        #                     vid._frame_num = vid.frame_count
        #         vid.draw(screen, (0,0))
        #         pygame.display.update()
        #     vid.close()
        #     del vid
        if i[0] == "=":# Move character position
            MoveFunc(i[1:],Characters)
        for j in range(len(Characters)): #Clear move properties
            if Characters[j].move != "" and Characters[j].XMove > screen.get_width() or Characters[j].XMove < 0:
               Characters[j].move = ""
               Characters[j].XMove = 0

        if i == "DimmingSc" or i == "DimmingSc\n":
            mF.ScreenDimmingFunc(screen,screen.get_width(),screen.get_height())
        elif i == "UnDimmingSc" or i == "UnDimmingSc\n":
            mF.ScreenUnDimmingFunc(screen,BackGround) 

        if i[:-1] == 'Two<<':
            BackGround.TwoCharacters = True
        elif i[:-2] == 'OffTwo' or i[:-3] == 'OffTwo': # Return Back all properties
            BackGround.TwoCharacters = False
            for j in range(len(Characters)):
                Characters[j].OnScreen = False

        if i == 'End<<' or i == 'End<<\n':
            for j in range(len(Characters)):
                Characters[j].OnScreen = False

        for j in range(len(Characters)): #Cycle set Onscreen Character
            if i[:-3] == Characters[j].name:
                Characters[j].OnScreen = True
                Characters[j].XMove = 0
        if i[-2] == '+' or i[-1] == '+':
            Comand = mF.DialogueFunction(screen,Characters, screen.get_width(), screen.get_height(), BackGround, i, FileName, Icon=True)
        elif i[-1] == '-' or i[-2] == '-':
            Comand = mF.DialogueFunction(screen,Characters, screen.get_width(), screen.get_height(), BackGround, i, FileName, Icon=False)

        if Comand == "LoadSave" or Comand == "Quit":
            return Comand

def main(screen, FieldW, FieldH):
    BackGround = mC.sceneBackground('./Assets/Other/Background/Room701.png', FieldW, FieldH, True) #mC.sceneBackground('./Assets/Other/Frame1.png', FieldW, FieldH, False)]
    pygame.mouse.set_visible(True)

    #//////////////////////
    file = [mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon.txt",'r',"AcquaintanceOnAFullMoon.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon_FChoice.txt",'r',"AcquaintanceOnAFullMoon_FChoice.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon_SChoice.txt",'r',"AcquaintanceOnAFullMoon_SChoice.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon2.txt",'r',"AcquaintanceOnAFullMoon2.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon3.txt",'r',"AcquaintanceOnAFullMoon3.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon3_SChoice.txt",'r',"AcquaintanceOnAFullMoon3_SChoice.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon4.txt",'r',"AcquaintanceOnAFullMoon4.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon4_FChoice.txt",'r',"AcquaintanceOnAFullMoon4_FChoice.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon4_SChoice.txt",'r',"AcquaintanceOnAFullMoon4_SChoice.txt"),
            mC.Direct(r"./Assets/ScriptAssets/1.1/AcquaintanceOnAFullMoon5.txt",'r',"AcquaintanceOnAFullMoon5.txt")]
    Characters = [mC.set_Sprite(r'./Assets/Characters/Jack/Jack_Usual.png', 460, 700, "Jack"), 
                  mC.set_Sprite(r'./Assets/Characters/Miguno.png', 460, 700, "Miguno"),
                  mC.set_Sprite(r'./Assets/Characters/Durham.png', 460, 700, "Durham"),
                  mC.set_Sprite(r'./Assets/Characters/Liza.png', 460, 700, "Liza"),
                  mC.set_Sprite(r'./Assets/Characters/Ellen/Ellen.png', 460, 700, "Ellen"),
                  mC.set_Sprite(r'./Assets/Characters/Pipi.png', 460, 700, "Pipi"),
                  mC.set_Sprite(r'./Assets/Characters/Elz/Elz.png', 460, 700, "Elz"),
                  mC.set_Sprite(r'./Assets/Characters/Collot.png', 460, 700, "Collot"),
                  mC.set_Sprite(r'./Assets/Characters/Bill/Bill.png', 460, 700, "Bill"),
                  mC.set_Sprite(r'./Assets/Characters/San.png', 460, 700, "San"),
                  mC.set_Sprite(r'./Assets/Characters/Tao.png', 460, 700, "Tao"),
                  mC.set_Sprite(r'./Assets/Characters/Kai.png', 460, 700, "Kai"),
                  mC.set_Sprite(r'./Assets/Characters/Squirrel.png', 460, 700, "Squirrel"),
                  mC.set_Sprite(r'./Assets/Characters/Lemur.png', 460, 700, "Lemur"),
                  mC.set_Sprite(r'./Assets/Characters/Sheila.png', 460, 700, "Sheila")]
    #//////////////////////
    Size = 0
    SizeIterator = 0
    if Size == 0:
        Size = 1
    global GoToSave
    ListOfSkipedScripts = [i for i in range(len(file))]
    while SizeIterator < len(file): #MAIN DIALOGUE CICLE
        #////////////////
        ActionSc = open(r'.//Assets//ScriptAssets//1.1//ActionScript.txt', 'r')
        getChocie = [i for i in ActionSc]
        ActionSc.close()
        #////////////////
        #////////////////
        if SizeIterator == 1: #First Choice
            if 'Возможно это не так важно;Пойти с Джеком\n' in getChocie or 'Возможно это не так важно;Пойти с Джеком' in getChocie:
                ListOfSkipedScripts[SizeIterator + 1] = -1
            if 'Возможно это не так важно;Пойти за контактами\n' in getChocie or 'Возможно это не так важно;Пойти за контактами' in getChocie:
                ListOfSkipedScripts[SizeIterator] = -1
        if SizeIterator == 5:
            if 'Когда же мне пойти в раздевалку;После Драматического кружка\n' in getChocie or 'Когда же мне пойти в раздевалку;После Драматического кружка' in getChocie:
                ListOfSkipedScripts[SizeIterator] = -1
                ListOfSkipedScripts[SizeIterator + 3] = -1
                # print("Change", ListOfSkipedScripts)

        if SizeIterator == 6: #Second Choice
            if 'Когда же мне пойти в раздевалку;После Драматического кружка\n' in getChocie or 'Когда же мне пойти в раздевалку;После Драматического кружка' in getChocie:
                ListOfSkipedScripts[SizeIterator + 2] = -1
            if 'Когда же мне пойти в раздевалку;Зайти сейчас\n' in getChocie or 'Когда же мне пойти в раздевалку;Зайти сейчас' in getChocie:
                ListOfSkipedScripts[SizeIterator + 1] = -1
        #////////////////
        if SizeIterator == len(file):
            # print("End")
            return
        if ListOfSkipedScripts[SizeIterator] == -1 and not GoToSave:# Ignore list of skipped scripts, to manipulate with saving
            if SizeIterator + 1 == len(file):
                return
            SizeIterator += 1
        Command = MainCycle(screen, Characters, BackGround, file[SizeIterator].file, file[SizeIterator].fileName)
        #////////////////
        if SizeIterator == 1: #First choice change to fix saving Error
            ListOfSkipedScripts[2] = -1
        elif SizeIterator == 2:
            ListOfSkipedScripts[1] = -1

        if SizeIterator == 5 and ListOfSkipedScripts[SizeIterator] != -1: #First choice change to fix saving Error
            ListOfSkipedScripts[7] = -1
            ListOfSkipedScripts[8] = 8
        elif SizeIterator == 7:
            ListOfSkipedScripts[8] = -1
        elif SizeIterator == 8:
            ListOfSkipedScripts[7] = -1
        #////////////////
        #print(ListOfSkipedScripts, SizeIterator, ListOfSkipedScripts[SizeIterator])
        SizeIterator += 1
        if Command == "Quit":
            pygame.mixer.music.pause()
            return
        elif Command == "LoadSave":
            SizeIterator = 0
            Size = 1
            mF.ScreenDimmingFunc(screen, FieldW, FieldH)
            setSave(screen,file, Characters, BackGround, file[SizeIterator].fileName)