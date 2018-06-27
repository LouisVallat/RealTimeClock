#Coded by Louis Vallat
import time, pygame as pg

pg.init()
SCREEN = pg.display.set_mode((640, 480)); pg.mouse.set_visible(False)
SHOW_DATE = True; SHOW_TIME = True; CLOCK = pg.time.Clock(); GREY = (128,128,128,255); WHITE = (255,255,255,255)
pg.display.set_caption('Real Time Clock')
SCREENWASHER = pg.Surface(SCREEN.get_size()).convert_alpha(); SCREENWASHER.fill((0, 0, 0, 255))
CLOCKFONT = pg.font.SysFont(name="segoe", size=175)
DATEFONT = pg.font.SysFont(name="segoe", size=100)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
            pg.quit(); raise SystemExit
        if event.type == pg.KEYUP and event.key == pg.K_F11:
            if SCREEN.get_flags() != pg.FULLSCREEN:
                SCREEN = pg.display.set_mode((640, 480), pg.FULLSCREEN)
            else:
                SCREEN = pg.display.set_mode((640, 480))
    SCREEN.blit(SCREENWASHER,(0,0))
    if SHOW_TIME:
        SCREEN.blit(CLOCKFONT.render(time.strftime("%H:%M:%S"), 4, WHITE), (75,115))
    if SHOW_DATE:
        SCREEN.blit(DATEFONT.render(time.strftime("%A %d"), 4, GREY), (80, 230))
        SCREEN.blit(DATEFONT.render(time.strftime("%B %Y"), 4, GREY), (150, 295))
    pg.display.update(); CLOCK.tick(25)
