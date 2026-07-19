

" INITIALIZE "
# import json
import json

# savefile system
SAVENUM = 0
save_file = open(f"saves/save{SAVENUM}.json","r")
save_json = json.load(save_file)

# language system
lang = save_json["lang"]
lang_file = open("assets/lang.json","r")
lang_json = json.load(lang_file)
def t(path:str) -> str:
    if lang in lang_json:
        if path in lang_json[lang]:
            return lang_json[lang][path]
    return path

# version system
ver_file = open("version.json","r")
ver_json = json.load(ver_file)

menu_name = "main"

# import pygame
try:
    import pygame
except ModuleNotFoundError:
    print(t("error.nopygame"))
    print(t("error.abort"))
    exit()

# pygame stuff
WINDOW_SCALE = 50
pyg_screen = pygame.display.set_mode((16*WINDOW_SCALE,9*WINDOW_SCALE),flags=(pygame.RESIZABLE))
pyg_running = True
pygame.init()
pygame.display.set_caption(f"Marble Playground | {ver_json["group"]}{ver_json["ver"]}")

" MAIN LOOP "
while pyg_running:

    # clear screen
    pyg_screen.fill((0,0,0))

    # event detect
    for pyg_event in pygame.event.get():
        if pyg_event.type == pygame.QUIT: # quit
            pyg_running = False
        elif pyg_event.type == pygame.KEYDOWN: # key
            #if pyg_event.key == pygame.K_F11: # F11 and toggle fullscreen
            #    pygame.display.toggle_fullscreen()
            pass

    # flip
    pygame.display.flip()


" EXIT "
# close all files
lang_file.close()
save_file.close()
ver_file.close()