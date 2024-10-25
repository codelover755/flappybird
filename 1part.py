import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.update()

bg1 = pygame.image.load("background.png")
bg = pygame.transform.scale(bg1,(600,600))
gr = pygame.image.load("Ground.png")

v = 0
fps = 75
clock = pygame.time.Clock()


class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f'bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False
    def update(self):
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index = self.index + 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        self.vel += 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.bottom < 560:
            self.rect.y += int(self.vel)
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.image = pygame.transform.rotate(self.images[self.index],self.vel * -2)
        
flappy = Bird(60,300)
bird_group = pygame.sprite.Group()
bird_group.add(flappy)

pipe_gap = 200
scroll_speed = 4
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"Pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y - int(pipe_gap/2)]
        if pos == -1:
            self.rect.topleft = [x,y + int(pipe_gap/2)]
    def update(self):
        self.rect.x = self.rect.x - scroll_speed
        if self.rect.right <0:
            self.kill()


pipe_group = pygame.sprite.Group()

while True:
    clock.tick(fps)

    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_frequency:
        pipe_height = random.randint(-150,150)
        gp = Pipe(600,300 + pipe_height,1)
        gp1 = Pipe(600,300 + pipe_height,-1) 
        pipe_group.add(gp)
        pipe_group.add(gp1)  
        last_pipe = time_now
        pygame.display.update()

    screen.blit(gr,(v,570))
    v = v - 2
    if v < -200:
        v = 0

    bird_group.draw(screen)
    bird_group.update() 
    pipe_group.draw(screen)
    pipe_group.update() 

    pygame.display.update()
