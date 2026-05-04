import utils
import pygame
import gaming_objects
import sans
from game import game


#BET GAME


colors = {
    
    "red": (155, 45, 40),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "gold": (255,255,0),
    "white": (255,255,255)
        
    
    
}





def menu():
    
    #setup
    pygame.init()
    pygame.display.set_caption("MENU")
    
    width = 950
    height = 527
    clock = pygame.time.Clock()
    
    path = "c:\\USERS\\CHUCH\\APPDATA\\LOCAL\\MICROSOFT\\WINDOWS\\FONTS\\DTM-MONO.OTF" # undertale font - small
    
    font = pygame.font.Font(path,32)
    large_font = pygame.font.Font(path,80)
    
    talking_font = pygame.font.Font(path,25)
    
    
    
    
    
    
    

    run = True
    
    screen = pygame.display.set_mode((width,height))
    
    
    
    
    
    exit = gaming_objects.Textbutton(text="EXIT")
    start = gaming_objects.Textbutton(text="START")
    
    # confirm cancel heal and move all get put in text file
    button_config = gaming_objects.Textbutton(text="BUTTON CONFIG")
    confirm = gaming_objects.Textbutton(text="CONFIRM",data="[Z]",data2="[ENTER]")
    cancel = gaming_objects.Textbutton(text="CANCEL",data="[X]",data2="[SHIFT]")
    heal = gaming_objects.Textbutton(text="HEAL",data="[C]",data2="[SPACE]")
    move = gaming_objects.Textbutton(text="MOVE",data="[ARROWS]",data2="[WASD]")
    Master_volume = gaming_objects.Textbutton(text="MASTER VOLUME")

    buttons  = [start,exit,button_config,confirm,cancel,heal,move,Master_volume]
    utils.assortment(buttons,100)
    
    code = 0 # index in list for buttons
    length =  len(buttons) - 1
    
    play_game  = False
    
    #sfx
    
    menu_choice = pygame.mixer.Sound("sounds\\Select.mp3")
    menu_music = pygame.mixer.music.load("sounds\\Underfell - Egolomania.mp3") # will change and remove this
    
    sans_eye = pygame.mixer.Sound("sounds\\sans_sfx\\sans-eye-sounds.mp3")
    sans_voice = pygame.mixer.Sound("sounds\\sans_sfx\\sans voice.wav")
    
    
    pygame.mixer.music.play(loops=-1) # loop music
   
    
    
    music_vol = 1.0

    
    
    bar_1 = gaming_objects.sound((240//2) + 250, 410, 300, 24, "red")
    bar_2 = gaming_objects.sound((240//2) + 250, 410, 300, 24, "green")
    
    
    shadow = pygame.Surface((950,527))
    shadow = shadow.convert_alpha()
    shadow.set_alpha(120) # shadow effect 
    
    
    
    
    

    underfell_sans = sans.Character("sans",950//2,100)
    
    

    
    
    


    

    while run:
        fps = clock.tick(60) 
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_DOWN:
                    code+=1
                    menu_choice.play()
                
                elif event.key == pygame.K_UP:
                    code-=1
                    menu_choice.play()
                
                
                elif  event.key == pygame.K_z: # if being pressed down and keycode z and text exit then quit
                    if buttons[code].text == "EXIT":
                        run = False
                    elif buttons[code].text == "START":
                        underfell_sans.head.set_image(4)
                        sans_eye.play()
                        play_game = True
                
              
                    
                        
                      
                      
                elif event.key == pygame.K_SPACE:  
                   
                    if buttons[code].text in ["HEAL","MOVE","CANCEL", "CONFIRM"]:
                        if buttons[code].data1 == buttons[code].data:
                            buttons[code].data1 = buttons[code].data2
                            
                        else:
                            buttons[code].data1 = buttons[code].data   
                            
                            
                # for volume
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    if buttons[code].text == "MASTER VOLUME":
                        if event.key == pygame.K_RIGHT:
                            music_vol+=0.1
                        elif event.key == pygame.K_LEFT:
                            music_vol-=0.1
                        
                        music_vol = max(0.0, min(1.0, music_vol))
                        pygame.mixer.music.set_volume(music_vol)
                        menu_choice.play()
                        
                    

        # CLAMP
        
        config = {
            "Master_volume": f"{round(music_vol,1)}",
            "confirm": f"{confirm.data1}",
            "cancel": f"{cancel.data1}",
            "heal": f"{heal.data1}",
            "move": f"{move.data1}"
            
           

            
            
            
        }
        

        
        
        if code > length:
            code = 0
        elif code < 0:
            code = length
            
            
            
        
        screen.fill((0,0,0)) # refresh screen
        
        
        utils.draw_text(screen,"SETTINGS",large_font,colors["white"],(screen.get_width()//2) - 200 ,3,)
        utils.draw_buttons(buttons,screen,font,code)
        
        
        bar_1.draw(screen) # red
        bar_2.draw(screen,music_vol) # green
        
        
        
        underfell_sans.draw(screen) # sans character i made
        underfell_sans.update()
    
        
        
      
        

       
        screen.blit(shadow,(0,0))
        
        
        #text.update(0.0005,sans_voice)
        #text.draw(screen,talking_font)
        
        
        
        if play_game: # play
            config = [f"{key}:{config[key]}" for key in config ]
            print(config)
            
            pygame.mixer.music.stop()
            pygame.time.delay(100)
            utils.fade_out(screen,w=width,h=height,halt=15)
            utils.write_to_file("settings.txt",config)
            game()
        
        
       # print(fps)
        pygame.display.update()
                     
    pygame.quit()




if __name__ == "__main__":
    menu()
    