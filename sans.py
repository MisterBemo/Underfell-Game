import os
import math
import pygame
import utils
import gaming_objects

# Load images
head_images = utils.load_data(r"Images\sans\faces")
body_images = utils.load_data(r"Images\sans\body")
legs_images = utils.load_data(r"Images\sans\legs")

dialogue_box = pygame.image.load(r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\DialogueBox.png")

class Character:
    def __init__(self, name, x, y,):
        self.name = name
        self.x = x
        self.y = y
        self.dialogue_box = dialogue_box
        
        self.Mercy_text = {         # this will be for the mercy text
                           
            "TEXT": "mercy? heh... you really think i'm that pathetic? ... YOU FOOL !!!!!"
            
            } 
    
        self.hp = 1
        

       
        self.body = Body(name, x + 100, y + 70, body_images)
        self.head = Head(name, 615, 155, head_images)   
        self.legs = Legs(name, 595, 310, legs_images)   
        
        self.Mercy_text = utils.tokenise(self.Mercy_text,520, 90)
        self.Mercy_text = gaming_objects.DialogueManager(self.Mercy_text[0])
        
        

    def draw(self, screen):
        print("HEAD", self.head.x)
        print("BODY", self.body.x)
        print("LEGS", self.legs.x)
        
        self.legs.draw(screen)
        self.body.draw(screen)
        self.head.draw(screen)

    def update(self):
        self.body.update()
        self.head.update()
        
    
    def display_dialogue_box(self,screen):
        screen.blit(self.dialogue_box,(self.head.y + 400,self.head.y))
    
    
    def get_hp(self):
        return self.hp

    def jump_scare(self, parameter_list):
        pass
        
       


# Base class for body 
class BodyPart:
    def __init__(self, name, x, y, images):
        self.name = name
        self.og_x = x
        self.og_y = y
        
        
        self.offset_applied = False
        
        self.x = x
        self.y = y
        
        
        self.base_y = y         
        
        self.images = images
        self.img = images[0]

        self.time = 0             

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def set_image(self, index,offset=0):
        index = max(0, min(index, len(self.images) - 1)) # to clamp
       
        self.img = self.images[index] # get image frm list
        
        if index == 6 or index == 7:
            if not self.offset_applied:
              self.x -= offset
              self.offset_applied = True
        else:
            if self.x != self.og_x:
                self.x =  self.og_x 
                self.offset_applied = False # turn off offset
                

    def update(self):

        self.time += 0.1
        self.y = self.base_y + math.sin(self.time) * 3
        
    



class Body(BodyPart):
    def update(self):
        self.time += 0.1
        self.y = self.base_y + math.sin(self.time) * 3
        


class Head(BodyPart):
    def update(self):                                            
        self.time += 0.1
        self.y = self.base_y + math.sin(self.time + 0.5) * 2


class Legs(BodyPart):
    pass  






