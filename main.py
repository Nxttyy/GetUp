import pygame, sys
pygame.init()

size = 250, 100

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
    
screen = pygame.display.set_mode(size, flags)

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
