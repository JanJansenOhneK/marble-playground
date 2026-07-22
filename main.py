

" INITIALIZE "
# import json
import json

# savefile system
SAVENUM = 0
save_file = open(f"saves/save{SAVENUM}.json","r")
save_json = json.load(save_file)

# language system
lang_file = open("assets/lang.json","r")
lang_json = json.load(lang_file)
def t(path:str,lang:str=save_json["lang"]) -> str:
    if lang in lang_json:
        if path in lang_json[lang]:
            return lang_json[lang][path]
    return path

# version system
ver_file = open("version.json","r")
ver_json = json.load(ver_file)

# vars to be implemented later
BG_COLOR = (0,0,30)

# import pygame
try:
    import pygame
except ModuleNotFoundError:
    print(t("error.nopygame"))
    print(t("error.abort"))
    exit()

# import obj
import assets.obj as obj

# pygame stuff
pyg_screen = pygame.display.set_mode((800,450),flags=pygame.RESIZABLE|pygame.SCALED)
pyg_running = True
pygame.init()
pygame.display.set_caption(f"Marble Playground | {ver_json["group"]}{ver_json["ver"]}")

# generators
def text_gen(text:str="lorum ipcem whatever",size:int=20,color=(255,255,255)):
    return pygame.font.Font("assets/fonts/main.ttf",size).render(text,True,color)
def button_gen(text:str="button text"):
    BTG_COLOR = (100,100,100)
    btg_text = text_gen(text)
    btg_surf = pygame.Surface((btg_text.width+20,25))
    btg_surf.fill(BTG_COLOR)
    btg_surf.blit(btg_text,(10,0))
    return btg_surf

# button class
class Button:
    def __init__(self,surface,pos:pygame.rect.RectLike=(30,30)):
        self.surface = surface
        self.pos = pos
    
    def render(self):
        pyg_screen.blit(self.surface,self.pos)

# menu stuff
menu_dict = {
    "main": obj.Menu("Main Menu",{"quit":Button(button_gen("Quit Game"),(50,50))}),
    "game": obj.GameMenu()
}
menu_current = "main"
def menu_switch(menustr:str):
    global menu_current
    if menustr in list(menu_dict.keys()):
        menu_current = menustr
    else:
        print(t("error.menu_switch.menunotfound"))
def menu_render(menustr:str):
    # menu specific things
    if menustr == "main":
        pyg_screen.blit(text_gen("main menu lol"),(0,0))
    else:
        print(t("error.menu_render.menunotregistered"))
    # render buttons
    for button in list(menu_dict[menu_current].buttons.values()):
        button.render()




" MAIN LOOP "
while pyg_running:

    " EVENTS "
    # event detect
    for pyg_event in pygame.event.get():
        if pyg_event.type == pygame.QUIT: # quit
            pyg_running = False
        elif pyg_event.type == pygame.KEYDOWN: # key
            if pyg_event.key == pygame.BUTTON_LEFT:
                pass
            #elif pyg_event.key == pygame.K_F11: # F11 and toggle fullscreen
            #    pygame.display.toggle_fullscreen()

    " RENDER "
    # clear screen
    pyg_screen.fill(BG_COLOR)

    # render menu
    menu_render(menu_current)

    # flip
    pygame.display.flip()


" EXIT "
# close all files
lang_file.close()
save_file.close()
ver_file.close()