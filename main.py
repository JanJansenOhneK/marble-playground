

" INITIALIZE "
# import json
import json

# language system
LANG = "en"
lang_file = open("assets/lang.json","r")
lang_json = json.load(lang_file)
def t(path:str) -> str:
    if LANG in lang_json:
        if path in lang_json[LANG]:
            return lang_json[LANG][path]
    return path

# import pygame
try:
    import pygame
except ModuleNotFoundError:
    print(t("error.nopygame"))
    print(t("error.abort"))
    exit()

# pygame stuff
pyg_screen = pygame.display.set_mode(flags=(pygame.FULLSCREEN))
pyg_running = True
pygame.init()

" MAIN LOOP "
while pyg_running:
    for pyg_event in pygame.event.get():
        if pyg_event.type == pygame.QUIT:
            pyg_running = False


" EXIT "
# close all files
lang_file.close()