import pygame, os, random

class PLAYER():
    def __init__(self, x, y):
        self.delay = 40
        self.ilk = False
        self.pipe_x = x
        self.pipe_y = y - 220
        self.d = 2
        self.start_x = x
        self.start_y = y
        self.jumpD = 18
        self.jumpS = 18
        self.man = [pygame.transform.scale(pygame.image.load(os.path.join('Sheet pics', f'sag{i}.png')), (40, 50)) for i in range(1, 5)]
        self.ground = pygame.transform.scale(pygame.image.load(os.path.join('Sheet pics', 'ground.png')), (40, 40))
        self.pipe = pygame.transform.scale(pygame.image.load(os.path.join('Sheet pics', 'pipe.png')), (45, 60))
        self.image = pygame.Surface((40, 50))
        self.image = self.man[1]
        self.rect = self.image.get_rect()
        self.rect.center = (x//2-150, y-225)
        self.vel = 5
        self.current_frame = 0

    def update(self):
        if self.jumpS >= 0:
            self.rect.y -= int(self.jumpS ** 2 / 4)
            self.image = self.man[2]
            self.jumpS = 18
                  

    def run(self):
        if self.d <= 0:
            self.current_frame = (self.current_frame + 1) % len(self.man)
            self.image = self.man[self.current_frame]
            self.d = 2
        else:
            self.d -= 1
        if self.delay > 1:
            self.delay -= 1
        else:
            if self.rect.y < self.start_y-255:
                self.rect.y += int(self.jumpD ** 2 / 4)
                self.jumpD = 18
                self.delay = 40
                    
                    

    def engel(self):
        if not self.ilk:
            self.pipeImage = pygame.Surface((45, 60))
            self.pipeRect = self.pipeImage.get_rect()
            self.pipeRect.center = (self.pipe_x, self.pipe_y)
            self.ilk = True
        else:
            if self.pipeRect.x-30 < 0:
                self.pipeRect.center = (self.pipe_x, self.pipe_y)
            else:
                self.pipeRect.x -= self.vel
                       
                
    def draw(self, surface):
        for i in range(self.start_x//40+1):
            for j in range((self.start_y-400)//40):
                surface.blit(self.ground, (i*40, 400+40*j))
        self.pipeImage = self.pipe
        surface.blit(self.pipeImage, self.pipeRect)
        surface.blit(self.image, self.rect)

