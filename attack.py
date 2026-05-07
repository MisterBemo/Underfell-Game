import pygame
import random
import math

class Attacks:
    def __init__(self, name, img, x, y, damage):
        self.name = name
        self.x = x
        self.y = y
        self.damage_amount = damage
        self.img = pygame.image.load(img)
        self.finished = False
        self.rect = self.img.get_rect(topleft=(x,y))
        
        self.rect.width -= 10
        self.rect.height -= 10
        
     
        
        print(self.rect)

    @classmethod
    def create_group(cls, amount, *args):
        return [cls(*args) for _ in range(amount)]

    def display(self, screen):
        screen.blit(self.img, (self.x, self.y))#
        #pygame.draw.rect(screen,(255,0,0),self.rect)

    def damage(self, player):
        player.hp -= self.damage_amount

    def move(self, speed):
        self.x += speed
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.x >= 800:
            self.finished = True

    def collision(self, char):
        if self.rect.colliderect(char.rect):
            return True
        else:
            return False


class Bones(Attacks):
    def __init__(self, name, img, x, y, damage):
        super().__init__(name, img, x, y, damage) # do at lunch
        

    def orange_effect(self,char):
        if not  char.moving and self.collision(char):
            self.damage(char)
            

    def blue_effect(self,char):
        if char.moving and self.collision(char):
            self.damage(char)


class Gaster(Attacks):
    def __init__(self, name, img, x, y, damage, angle):
        super().__init__(name, img, x, y, damage)
        self.state = "spawn"
        self.angle = angle
        self.timer = 0
        self.finished = False
        
        self.vel_x = 0
        self.vel_inc = 4
        
        
        self.length = 0
        self.thickness = 80
        

        self.img1 = pygame.image.load(r"Images\Attacks\Gaster_idle_1.png")
        self.img2 = pygame.image.load(r"Images\Attacks\Gaster_inter_1.png")
        self.img3 = pygame.image.load(r"Images\Attacks\Gaster_inter_2.png")
        self.img4 = pygame.image.load(r"Images\Attacks\Gaster_inter_3.png")

        self.img1 = pygame.transform.rotate(self.img1, angle )
        self.img2 = pygame.transform.rotate(self.img2, angle )
        self.img3 = pygame.transform.rotate(self.img3, angle )
        self.img4 = pygame.transform.rotate(self.img4, angle )
        
        

        self.images = [self.img1, self.img2, self.img3, self.img4]
        self.img = self.images[0]
        
        self.color = (255,255,255)
        
      
    
    def lock_on_target(self, player):
        pass
    
    
    def draw_beam(self, screen):
        

        self.length += self.vel_x + 10

        start_x = self.x + 120 # start of line
        start_y = self.y + 120

        end_x = start_x + self.length + 40
        end_y = start_y 
        

        pygame.draw.line(screen, (255,0,0),
                     (start_x, start_y),
                     (end_x, end_y),
                     self.thickness)
        
        
        
        
        
    def gaster_change(self, screen,sfx):
        self.timer += 1

        if self.state == "spawn":
            self.img = self.images[0]
            if self.timer >= 5:
                self.state = "charge"
                self.timer = 0
                sfx.play()

        elif self.state == "charge":
            self.img = self.images[1]
            if self.timer >= 10:
                self.state = "fire"
                self.timer = 0
                
                

        elif self.state == "fire":
            self.img = self.images[2]
            if self.timer >= 50:
                self.state = "done"
                self.timer = 0
                
                
        if self.state != "done":
            self.display(screen)
        else:
            self.finished = True
        
        
    def move_gaster(self,screen,sfx=None): # need to change gaster blaster angle for beam
        if self.state == "fire":
            self.draw_beam(screen)
            self.x -= self.vel_x
            self.vel_x +=  self.vel_inc
    
  
            
        
       
  
    






