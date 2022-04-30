import pygame, sys, os
from datetime import datetime

pygame.init()

width, height = 250, 100

screen = pygame.display.Info()
x, y = screen.current_w, screen.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x-width, y-(height+75))

settings = open('./settings.txt', 'r')

#global variables
noFrame = True

#reading settings
for line in settings:
    line = line.split(' ')
    if line[0][0] != '\n' and  line[0][0] != '#':
        if line[0] == 'NoFrameDisplay':
            noFrame = bool(int(line[1][0]))
print(noFrame)

if noFrame:
    flags = pygame.NOFRAME
else:
    flags = pygame.RESIZABLE 

window = pygame.display.set_mode((width, height), flags, 0,0)
    
interval = 1 

def main():
    then = datetime.now()
    totalThenMinutes = int((then.strftime('%H')))*60 + int(then.strftime('%M'))

    while True:
        #time
        now = datetime.now()

        totalNowMinutes = int((now.strftime('%H')))*60 + int(now.strftime('%M'))

        if abs(totalNowMinutes - totalThenMinutes) >=  interval:
            print(str(totalNowMinutes) + 'Get Up Bro!')
            then = datetime.now()
            totalThenMinutes = int((then.strftime('%H')))*60 + int(then.strftime('%M'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        window.fill((0,0,0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
