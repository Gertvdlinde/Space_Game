import pygame, random

pygame.init()

class SpadeShip(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        self.shield_surface = pygame.image.load("images\shield.png")
        self.health = 5

    def update(self): #Update spaceship to follow mouse
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()

    def screen_constrain(self): # Constrain the image inside of the screen
        if self.rect.right >= 1280:
            self.rect.right = 1280
        elif self.rect.left <= 0:
            self.rect.left =0

        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 720:
            self.rect.bottom = 720





class Meteor(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self): #Update spaceship to follow mouse
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
        #self.screen_constrain()
        if self.rect.centery >=800:
            self.kill()

    def screen_constrain(self): # Constrain the image inside of the screen
        if self.rect.right >= 1280:
            self.rect.right = 1280
        elif self.rect.left <= 0:
            self.rect.left =0

        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 720:
            self.rect.bottom = 720


class Laser(pygame.sprite.Sprite):
    def __init__(self,path,pos,speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed

    def update(self): #Update spaceship to follow mouse
        self.rect.centery -= self.speed
        if self.rect.centery <= -10:
            self.kill()




def generate_rand_meteor():
    meteor_path = random.choice(("images\Meteor1.png", "images\Meteor2.png", "images\Meteor3.png"))
    random_xpos = random.randrange(0, 1280)
    random_ypos = random.randrange(-500, -50)
    random_xspeed = random.randrange(-1, 1)
    random_yspeed = random.randrange(3, 9)
    meteor = Meteor(meteor_path, random_xpos, random_ypos, random_xspeed, random_yspeed)
    meteor_group.add(meteor)

spaceship = SpadeShip("images\spaceship.png",640,500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()


