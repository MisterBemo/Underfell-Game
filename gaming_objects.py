# will just hold all the classess for all the different systems
from os import name

import pygame
import utils




colors = {
    
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "gold": (255,255,0),
    "aqua": (0, 255, 255, 255),
    "white": (255,255,255)
    

        
    
    
}

class Textbutton:
    const_x = x=(240//2) - 50
    const_y = 240
    def __init__(self,text,data="[]",color=colors["red"],data2="",x=const_x,y=const_y):
        self.og_x = x
        self.x = x
        
        self.og_y = y
        self.y = y
    
        
        self.text = text
        
        self.data = data
        self.data1  =  data # origional
        
        self.data2 =   data2 # new data
        
        self.color_og = color
        self.color = color
        self.color2 = colors["gold"]
        
        
    
    def draw(self,screen,font):
        text = font.render(self.text,True,self.color,)
        screen.blit(text,(self.x,self.y))
        
    def draw_data(self,screen,font,color=colors["aqua"]):
        text = font.render(self.data1,True,color)
        screen.blit(text,(self.x+ 200,self.y))



        


class sound: # will be used as a health bar and sound bar
    def __init__(self,x,y,width,height,color):
        self.color = color
        
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height

    def draw(self,screen,ratio=1.0):
        pygame.draw.rect(screen,self.color,pygame.Rect((self.x,self.y),(self.width*ratio,self.height)))




class HPBar:
    def __init__(self,x,y,w,h,max_hp=20):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
        
       
    
    
    def draw(self,screen,player):
        ratio = player.hp/self.max_hp
        
        pygame.draw.rect(screen,colors["red"],(self.x,self.y,self.w,self.h))
        pygame.draw.rect(screen,colors["gold"],(self.x,self.y,self.w*ratio,self.h))
        



class character:
    
    def __init__(self,char,sound,x,y,delay=40,effect=None,color=(255,255,255)):
        self.text = char
        
        self.x = x
        self.y  =  y
        
        self.effect = effect
        self.color = color
        
        self.delay = delay
        self.sound = sound
        
        self.visible = False
        
        
        
    


# dialogue manager
class DialogueManager:
    
    def __init__(self,line):
        self.current_line = line
        
        self.index = 0
        self.timer = 0
        self.finished = False
    
    
    def update(self,dt,sfx):
        if self.finished:
            return self.finished
        else:
            
            self.timer +=dt
            
            if self.index < len(self.current_line): # not finished
                Char = self.current_line[self.index]
                
                
                
              
                if self.timer >= Char.delay:
                    self.timer = 0
                    self.index +=1
                    
                    Char.visible = True
                      
                    sfx.play()
            else:
                self.finished = True
              
                    
                    
                
                    
                
                
                
                
                
                
    def draw(self,screen,font):
        for char in self.current_line:
            if char.visible:
                utils.draw_text(screen,char.text,font,char.color,x=char.x,y=char.y)
                
        







class Box:
    def __init__(self, name):
        self.name = name
        self.color = colors["red"]

        self.og_h = 250
        self.og_w = 250
        self.og_x = 275
        self.og_y = 300

        self.x = self.og_x
        self.y = self.og_y
        self.w = self.og_w
        self.h = self.og_h

        self.box = pygame.Rect((self.x, self.y), (self.w, self.h))

        self.mode = "Off"
        self.size_changed = False
        self.size_changed_back = False

    def change_size(self):
        if self.mode == "on":  # opening the box
            target_x = 120
            target_y = 300
            target_w = 600
            target_h = 200

            if self.x != target_x:
                self.x = target_x
            if self.y != target_y:
                self.y = target_y
            if self.w < target_w:
                self.w += 8
                if self.w > target_w:
                    self.w = target_w
            if self.h > target_h:
                self.h -= 8
                if self.h < target_h:
                    self.h = target_h

            self.box = pygame.Rect((self.x, self.y), (self.w, self.h))
            
            if self.w == target_w and self.h == target_h:
                self.mode = "off"  # finished opening

        elif self.mode == "off":  # closing the box
            self.x = self.og_x
            self.y = self.og_y

            if self.h < self.og_h:
                self.h += 14
                if self.h > self.og_h:
                    self.h = self.og_h

            if self.w > self.og_w:
                self.w -= 14
                if self.w < self.og_w:
                    self.w = self.og_w

            self.box = pygame.Rect((self.x, self.y), (self.w, self.h))
            
            if self.h == self.og_h and self.w == self.og_w:
                return True    
            
            
                
    def set_mode(self,mode_change):
        self.mode = mode_change
    
    
    def get_ratios(self):
        return self.x,self.y
        
            
            
    
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.box,width=10)


class Battle_buttons(Box):
    
    information = {
        "data1":"*You feel like you are going to have a bad time . . . ."
        
        }  
    
    
    x,y = 400,1000
   

    def __init__(self,name,img,img2):
        #import utils
        
        self.items = [Food("Monster Candy"),Food("Spider Donut"),Food("Butterscotch Pie"),Food("Nice Cream")]
      
        
        self.tokenised = utils.tokenise(self.information,200, 350,20,550,25) 
        self.text = DialogueManager(self.tokenised[0])
        self.c_pressed  = False
        
        
        self.name = name
        
        self.x = 400
        self.y = 600
        
        self.img = pygame.image.load(img)
        self.img2 = pygame.image.load(img2)
        
        self.og_img = self.img
        
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
        
    
    def reset_text(self):
        for x in self.text.current_line:
               x.visible = False
        
        
    def Act(self,screen,sfx,font):
       self.text.draw(screen,font) #
       self.text.update(0.008,sfx)
       
       if self.text.finished:
           self.text.index = 0
           self.reset_text()
           
           
           
    def Item(self,opcode,screen,font,p1,sfx): # p1 is player
      
      def display(screen,font,code):
          
          if not self.items:
              return False
          

         
        

          key_code = pygame.key.get_pressed()

          for item in self.items:
             # print(code)
              if item.current_text == self.items[code].current_text: # issue is here
                    item.current_text = item.new_text
                    item.curr_color = item.new_color
              else:
                  if item.current_text != item.og_text:
                      item.current_text = item.og_text
                      item.curr_color = item.og_color
                
              
    
              utils.draw_text(screen, item.current_text, font, item.curr_color, 140, item.y)
          
          
          if self.items[code].curr_color != colors["red"]:
              self.items[code].curr_color = colors["red"]
              if key_code[pygame.K_c]:
                if not self.c_pressed:
                 sfx.play()
                 if p1.hp < 20:
                    p1.hp += self.items[code].index[self.items[code].og_text]
                 self.items.pop(code)
                 self.c_pressed =  True
                 return True
              else:
                 self.c_pressed = False
          
        
                  
      result = display(screen,font,opcode)
      return result
  
    def Mercy(self,screen,char,sfx,text_style): # char is underfell sans character
        char.display_dialogue_box(screen)
        char.Mercy_text.update(0.005,sfx)
        char.Mercy_text.draw(screen,text_style)
        
        if char.Mercy_text.index < 15:
            char.head.set_image(9)
        elif char.Mercy_text.index < 20:
            char.head.set_image(10)
        elif char.Mercy_text.index < 30:
            char.head.set_image(1)
        elif char.Mercy_text.index < 60:
            char.head.set_image(12)
        elif char.Mercy_text.index < 65:
            char.head.set_image(4)
            
        
      
      
          
      
      
                
                
        
    
      
          
    
   
      
      
  
# FOOD / ITEM CLASS
class Food:
    offset_x = 100
    y = 800
    def __init__(self, name):
        self.index = {
            "Monster Candy": 2,
            "Spider Donut": 3,
            "Butterscotch Pie": 8,
            "Nice Cream": 4
        }
       
        
        self.curr_color = colors["white"]
        self.og_color = colors["white"]
        self.new_color = colors["green"]
        
        self.current_text = name  # how it appears when selected
        self.og_text = name
        self.new_text = f"* {name}"
        
        self.x = Food.offset_x
        self.y = Food.y
        
        
        
        
        
        Food.y -= 45# in pygame negative goes up            
        
        
        
       
            
        
        #print(Food.offset_x,Food.y)
        
        
        
        
        
       
        
           
           
           
        
        
        
        
        
    
def change_Key(self):
    pass

### player




class player:
    def __init__(self,name,x,y):
        self.name = name
        
        self.og_x = x
        self.og_y = y
        
        self. x = x
        self.y = y
        
        self.speed = 4# default speed 
        self.moving = False
        
        
        self.img = pygame.image.load(r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\red_soul.png")
        self.img2 = pygame.image.load(r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\blue soul.png")
        
        self.og_img = self.img
        
        self.gravity_on = False
        
        self.hp = 20
        
        self.on_ground = False
        self.soul_mode = "red"
        
        self.ground_y = self.y # ground level
        self.gravity = 0.5
        self.jump_strenghth = -12
        self.ground_y = 510
        self.vel_y = 0
        
        self.rect = self.img.get_rect(topleft=(self.x,self.y))
        
        
      
        
        
        self.width  = self.img.get_width()
        self.height = self.img.get_height()

    def update(self,box): # just check keys
        keys =  pygame.key.get_pressed()
       # print(self.moving)
        if keys[pygame.K_UP]: # if gravity on this gonna need to be locked
            self.moving = True
            
            if self.gravity_on:
                if self.on_ground:
                    self.vel_y = self.jump_strenghth
                    self.on_ground = False
                    
            else:
                self.y -= self.speed
        else:
            self.moving = False
                
                
            
        if keys[pygame.K_DOWN]:
            self.moving = True
            self.y+=self.speed
        if keys[pygame.K_RIGHT]:
            self.moving = True
            self.x += self.speed
        
        if keys[pygame.K_LEFT]:
            self.moving = True
            self.x -= self.speed
            
            
        # i will check collisions
        
                  
        if self.x-10 < box.box.left : # if left and slightly less to execute
            self.x = box.box.left + 10
            
        if (self.x + self.width) + 10  > box.box.right:
            self.x = (box.box.right - self.width) - 10
        
    
        if self.y-10 < box.box.top: # check top
            self.y = box.box.top+10
        
        if (self.y + self.height)+10 > box.box.bottom: # 
            self.y = (box.box.bottom - self.height) - 10
        
        self.rect.x = self.x
        self.rect.y = self.y
            
        
        
        
    def set_gravity(self):
        if not self.gravity_on:
            self.gravity_on = True
            self.img = self.img2
            self.soul_mode = "blue"
        else:
            self.gravity_on = False
            self.img = self.og_img
            self.soul_mode  = "red"
            
            
    def apply_gravity(self):
        self.vel_y += self.gravity
       
        self.y += self.vel_y
         
        
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.vel_y = 0
            self.on_ground = True
       
    
    
    def draw(self,screen): # draw
        screen.blit(self.img,(self.x,self.y))
        
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)
    
    
   
            
        
        
        

if __name__ == "__main__":
    print("debug")
    print(player(2,3,4).rect)