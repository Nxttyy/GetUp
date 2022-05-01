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

#reading settings
for line in settings:
    line = line.split(' ')
    if line[0][0] != '\n' and  line[0][0] != '#':
        if line[0] == 'NoFrameDisplay':
            noFrame = bool(int(line[1][0]))

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

interval = 1 

def main():
    #gobals
    global spriteIndex
    global window

    then = datetime.now()
    totalThenMinutes = int((then.strftime('%H')))*60 + int(then.strftime('%M'))

    clock = pygame.time.Clock()
    while True:

        if spriteIndex < len(sprites)-1:
            spriteIndex += 1
        else:
            spriteIndex = 0

        img = pygame.image.load(sprites[spriteIndex])
        img = pygame.transform.scale(img, (160,160))
        window.blit(img, ((0,0)))
        #time
        now = datetime.now()

        totalNowMinutes = int((now.strftime('%H')))*60 + int(now.strftime('%M'))

        if abs(totalNowMinutes - totalThenMinutes) >=  interval:
            print(str(totalNowMinutes) + 'Get Up Bro!')
            then = datetime.now()
            totalThenMinutes = int((then.strftime('%H')))*60 + int(then.strftime('%M'))
            showWindow(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(5)
        pygame.display.flip()

if __name__ == '__main__':
    main()
