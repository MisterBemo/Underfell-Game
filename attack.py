# handles attacks
 
import pygame
import random


# normal , blue , orange blaster 



class Attacks:
    def __init__(self,name,img,amount,x,y,damage):
        self.name  = name
        self.x = x
        self.y = y
        
        self.damage_amount  = damage
        self.amount = amount
        
        #self.vel_speed = 2 # speed of bone
        
       
        
        self.img = pygame.image.load(img)
        self.finished = False
        
    @classmethod
    def create_group(cls,amount,*args):
        return [cls(*args) for _ in range(amount)]
    
    
    
    
    def display(self,screen):
        screen.blit(self.img,(self.x,self.y))
    
    def damage(self,player):
        player.hp -= self.damage
    
    def move(self,speed):
        #### movement code
        self.x += speed
      
        
        
        if self.x >= 800:
            self.finished = True
            
            
    def collision(self,char):
        pass
            
       



class Bones(Attacks):
    def __init__(self,name,img,x,y,damage,amount):
        super().__init__(name,img,amount,x,y,damage)
    
    def orange_effect(self): # orange
        pass
    
    def blue_effect(self): # blue bone
        pass


class Gaster(Attacks):
    pass








