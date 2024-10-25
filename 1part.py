import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.update()

bg1 = pygame.image.load(r"Game dev 2\flappy bird sprites\background.png")
bg = pygame.transform.scale(bg1,(600,600))
gr = pygame.image.load(r"Game dev 2\flappy bird sprites\Ground.png")

v = 0
fps = 75
clock = pygame.time.Clock()

screen.blit(bg,(0,0))
pygame.display.update()

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"Game dev 2\flappy bird sprites\birdmid.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        pass
flappy = Bird(60,300)
bird_group = pygame.sprite.Group()
bird_group.add(flappy)

pipe_gap = 150
scroll_speed = 4
pipe_frequency = 700
last_pipe = pygame.time.get_ticks() - pipe_frequency
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"Game dev 2\flappy bird sprites\Pipe.png")
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(gr,(v,570))
    v = v - 2
    if v < -200:
        v = 0
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_frequency:
        gp = Pipe(600,300,1)
        gp1 = Pipe(600,300,-1) 
        pipe_group.add(gp)
        pipe_group.add(gp1)  
        last_pipe = time_now
        pygame.display.update()

    bird_group.draw(screen)
    bird_group.update() 
    pipe_group.draw(screen)
    pipe_group.update() 

    pygame.display.update()