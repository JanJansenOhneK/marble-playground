
import pygame

" MENUS "
# Menu with buttons and stuff
class Menu:
    def __init__(self,caption:str="Default Menu Title"):
        #self.obj = obj
        self.caption = caption
# Menu for playing
class GameMenu(Menu):
    def __init__(self):
        super().__init__("In Game")
