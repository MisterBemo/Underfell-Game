import os
import pygame

from gaming_objects import character


colors = {
    
    "red": (155, 45, 40),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "gold": (255, 255, 0),
    "white": (255,255,255),
    "black": (0,0,0)
        
    
    
}

def assortment(button_list, start_y):
    LINE_STEP = 40
    SECTION_STEP = 24  # extra space between sections

    y = start_y

    for button in button_list:
        if button.text == "MASTER VOLUME":
            button.y  = 400
        else:
            if button.text in ["HEAL","MOVE","CANCEL"]:
                button.x += 50
            elif button.text == "EXIT":
                button.x +=20
            elif button.text == "CONFIRM":
                button.x+=50
        
           
            button.y = y
            y += LINE_STEP
            

def general_sort(buttons,x_start):
    start_x = x_start
    
    for button in buttons:
        button.x = start_x
        start_x += 200
    
    


def debug():
    option  = input("Check debug option")
    
    
def redraw(screen,items):
    for item in items:
        screen.blit(item.img,(item.x,item.y))
        
    
    
    
    
def fade_out(screen, w,h,speed=1, halt=10,color=colors["black"]):
    width, height = screen.get_size()

    fade = pygame.Surface((w, h))
    fade.fill(color)

    for alpha in range(0, 256, speed):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(halt)
        



def fade_in(screen,w,h ,items,speed=1, halt=10,color=colors["black"]):

    fade = pygame.Surface((w, h))
    fade.fill(color)

    for alpha in range(255,-1,-speed):
        redraw(screen,items)
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(halt)


        

    





def draw_buttons(button_list,window,font_Style,button_code):
    
    for button in button_list:
        if button.text == button_list[button_code].text: # if text is the same then we know
            button.color = button.color2
        else:
            if button.color != button.color_og:
                button.color = button.color_og
        
        
        
        if button.data != "[]":
          button.draw_data(window,font_Style)
        
        button.draw(window,font_Style)
        



    

    
        
def load_data(path): # load multiple images in a llist 
    data = []
    folder  = os.listdir(path)
    
    
    
    for image in os.listdir(path):

        
        image_path = os.path.join(path,image)
        new_image = pygame.image.load(image_path)
        
       
        data.append(new_image)
        

    return data

# might edit utils so that the parts are in order



def read_data(path,start,stop):
    with open(path,"r") as file:
        data = file.read().splitlines()
        filtered_data = data[start:stop]   # the data that we actually want
        print(filtered_data)
        to_return = []
        
        for items in filtered_data:
            temp = items.split(":",1)[1]
            to_return.append(temp)
            
        
            
        return to_return
    


def write_to_file(path,data):# e.g. ()
    with open(path,"w") as file:
        for line in data:
            file.write(f"{line}\n")
            

            
        

def draw_text(screen,text,font,color,x,y):
        text = font.render(text,True,color,)
        screen.blit(text,(x,y))
        
    

def tokenise(speech,x=40,y=200,spacing=10,wrap=750,new_line=20):
    tokenised_lst = []
    talk_sfx = "sounds\\sans_sfx\\sans voice.wav"
    
    og_x = x
    og_y = y
    
   
    
    for letter in speech:
        token_form = []
        for item in speech[letter]:
            
            delay = 0.05
            
            if item in ".!?":
                delay = 0.2
            
            text_char = character(item,x=x,y=y,delay=delay,sound=talk_sfx,color=colors["red"]) 
            token_form.append(text_char)
    
            x+=spacing
        
            if x >= wrap:
                y+= new_line
                x = og_x
        x = og_x
        y = og_y
        
        
        tokenised_lst.append(token_form)
        
    
        
   

        
    return tokenised_lst








if __name__ == "__main__":
    #write_to_file("settings.txt",1,2,3,4)
    head_images = load_data("Images\\sans\\faces")
    
