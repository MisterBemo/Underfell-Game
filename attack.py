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

    def collision(self, char,sfx):
        if self.rect.colliderect(char.rect) and not char.forcefield:
            char.forcefield = True
            sfx.play()
            
            
            if char.gravity_on:
                char.img = char.transparent_img2
            else:
                char.img = char.transparent_img
                
            return True
        else:
            return False


class Bones(Attacks):
    def __init__(self, name, img, x, y, damage):
        super().__init__(name, img, x, y, damage) # do at lunch
        

    def orange_effect(self,char,sfx):
        if not  char.moving and not char.forcefield and  self.collision(char,sfx):
            char.forcefield = True
            self.damage(char)
            
            

    def blue_effect(self,char,sfx):
        if char.moving and not char.forcefield and  self.collision(char,sfx):
            char.forcefield = True
            self.damage(char)
            


class Gaster(Attacks):
    def __init__(self, name, img, x, y, damage, angle):
        super().__init__(name, img, x, y, damage)
        self.state = "spawn"
        self.angle = angle
        self.timer = 0
        self.finished = False
        self.damage_amount = 4
        
        self.vel_x = 0
        self.vel_inc = 2
        
        
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
        
        

        self.start_x = self.x + 120 # start of line
        self.start_y = self.y + 120

        self.end_x = self.start_x + self.length + 40
        self.end_y = self.start_y 
        
        self.blast_beam = pygame.Rect(self.start_x,self.start_y,self.end_x,self.end_y) # beam
        
      
    
    def lock_on_target(self, player):
        pass
    
    
    def gaster_collide(self,char):
        if self.blast_beam.colliderect(char.rect) and not char.forcefield:
            char.forcefield = True
            if char.gravity_on:
                char.img = char.transparent_img2
            else:
                char.img = char.transparent_img
                
            return True
        else:
            return False
    
    def draw_beam(self, screen,char):
        

        self.length += self.vel_x + 20

        start_x = self.x + 160 # start of line
        start_y = self.y + 80

        end_x = start_x + self.length + 150
        
        

        self.blast_beam = pygame.Rect(start_x,start_y,end_x,80)
        
        pygame.draw.rect(screen,"red",self.blast_beam)
        
        if self.gaster_collide(char):
            self.damage(char)
            
            print("TOUCHING")
        
    
            
        
        
        
        
        
        
        
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
        
        
    def move_gaster(self,screen,char,sfx=None): # need to change gaster blaster angle for beam
        if self.state == "fire":
            self.draw_beam(screen,char)
            self.x -= self.vel_x
            self.vel_x +=  self.vel_inc
    
  
            
        
       
  
    






