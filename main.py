import pygame, sys, os
from datetime import datetime

pygame.init()

width, height = 160, 160

screen = pygame.display.Info()
x, y = screen.current_w, screen.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x-width, y-(height+75))

settings = open('./settings.txt', 'r')

#global variables
noFrame = True
window = None
interval = None

#reading settings
for line in settings:
    line = line.split(' ')
    if line != '\n' and line[0][0] != '#':
        if line[0] == 'NoFrameDisplay':
            noFrame = bool(int(line[1][0]))
        elif line[0] == 'interval':
            interval = int(line[1])

#font
pygame.font.init()
my_font = pygame.freetype.SysFont('Comic Sans MS', 15)

#sprite list
sprites = ['./sprites/1.png', './sprites/2.png', './sprites/3.png', './sprites/4.png']
spriteIndex = 0

    
def showWindow(prop):
    global window

    if noFrame and prop:
        flags = pygame.NOFRAME|pygame.SHOWN
    elif noFrame and not prop:
        flags = pygame.NOFRAME|pygame.HIDDEN
    elif not noFrame and prop:
        flags = pygame.RESIZEABLE|pygame.SHOWN
    else:
        flags = pygame.RESIZEABLE|pygame.HIDDEN

    window = pygame.display.set_mode((width, height), flags, 0,0)

showWindow(False)
pygame.display.set_caption('Get Up!')

def main():
    #gobals
    global spriteIndex
    global window

    noInputTime = 0
    click = False

    then = datetime.now()
    totalThenMinutes = int((then.strftime('%H')))*60 + int(then.strftime('%M'))

    clock = pygame.time.Clock()
    while True:

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                click = True


        if spriteIndex < len(sprites)-1:
            spriteIndex += 1
        else:
            spriteIndex = 0

        #time
        now = datetime.now()

        totalNowMinutes = int((now.strftime('%H')))*60 + int(now.strftime('%M'))

        if abs(totalNowMinutes - totalThenMinutes) >=  interval:
            showWindow(True)
            img = pygame.image.load(sprites[spriteIndex])
            img = pygame.transform.scale(img, (160,160))
            window.blit(img, ((0,0)))

            print(abs(totalNowMinutes - totalThenMinutes))
            if noInputTime < 30:
                noInputTime += 1
                print(f'{noInputTime}waiting')
            else:
                text_surface, rect = my_font.render("DONE", (0, 0, 0))
                window.blit(text_surface, (width/2 - rect.width/2, height-rect.height-5))

                my_rect = pygame.draw.rect(window, (200,234,46), (width/2 - rect.width/2 - 2  , height-rect.height-9, rect.width + 4, rect.height + 6), 1)


                if my_rect.collidepoint(pygame.mouse.get_pos()):
                     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                     if click:
                        noInputTime = 0
                        then = datetime.now()
                        totalThenMinutes = int((then.strftime('%H')))*60 + int(then.strftime('%M'))
                        showWindow(False)
                
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        clock.tick(5)
        pygame.display.flip()

if __name__ == '__main__':
    main()
