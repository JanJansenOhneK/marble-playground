

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

# text stuff



# menu stuff
menu_dict = {
    "main": obj.Menu("Main Menu"),
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
    if menustr == "main":
        pass
    else:
        print(t("error.menu_render.menunotregistered"))


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