import pygame

class set_Sprite():
    def __init__(self, ImgAdress:str, SpriteW, SpriteH, Name:str):
        self.objSprite = pygame.image.load(ImgAdress)
        self.OnScreen = False
        self.name = Name
        self.Width = SpriteW
        self.Height = SpriteH
        self.rect = ((SpriteW/2),20)
        self.move = ""
        self.XMove = 0
        self.XY = [0,0]
        self.objSprite = pygame.transform.scale(self.objSprite,(self.Width, self.Height))

    def Emotion(self, ImgAdress:str):
        self.objSprite = pygame.image.load(ImgAdress)
        self.objSprite = pygame.transform.scale(self.objSprite,(self.Width, self.Height))
        
class sceneBackground():
    def __init__(self, ImgAdress:str, SpriteW, SpriteH, CharactersOnScreen:str):
        self.objBackground = pygame.image.load(ImgAdress)
        self.objBackground = pygame.transform.scale(self.objBackground,(SpriteW, SpriteH))
        self.TwoCharacters = False
        self.CharactersOnScreen = CharactersOnScreen
class Direct():
    def __init__(self, Adress:str, Acess:str, Name:str):
        self.file = open(Adress,Acess)
        self.fileName = Name
        self.Adress = Adress
        self.Acess = Acess
