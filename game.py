import random

import utils
import pygame
import gaming_objects
import sans
import attack

def draw_battle_buttons(lst,screen):
    for button in lst:
        button.draw(screen)

        
        
def options_picker(lst,index):
    code = lst[index]
    for button in lst:
        if button == code:
            button.img = button.img2
        else:
            if button.img != button.og_img:
                button.img = button.og_img
            
    return code

attack_combination = {

    "Bone_phase_1": attack.Attacks.create_group(
        5,
        "Bone_1",
        r"Images\Attacks\normal_bone.png",
        200,
        450,
        10
    ),

    "Bone_phase_1_up": attack.Attacks.create_group(
        5,
        "Bone_1",
        r"Images\Attacks\normal_bone.png",
        200,
        300,
        10
    ),

    "Bone_phase_1_long": attack.Attacks.create_group(
        5,
        "long_bone",
        r"Images\Attacks\long_bone.png",
        250,
        450,
        10
    ),

    "Bone_phase_1_long_up": attack.Attacks.create_group(
        5,
        "long_bone",
        r"Images\Attacks\long_bone.png",
        250,
        200,
        10
    ),

    "Bone_phase_1_stack": attack.Attacks.create_group( # change stack to something else
        5,
        "long_bone",
        r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Attacks\stack_bone.png",
        50,
        350,
        10
    ),

    "Bone_phase_1_stack2": attack.Attacks.create_group(
        5,
        "long_bone",
        r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Attacks\stack_bone.png",
        50,
        200,
        10
    ),

    "Normal_Gaster_blaster": attack.Gaster.create_group(
        5, 
        "Normal_Gaster",
        r"Images\Attacks\Gaster_idle_1.png",
        100,
        350,
        250,
        90
    ),
    
    "Normal_Gaster_blaster_opp": attack.Gaster.create_group(
        5,
        "Normal_Gaster_opp",
        r"Images\Attacks\Gaster_idle_1.png",
        500,
        400,
        500,
        90
    ),
    
    
       "Bone_phase_1_blue": attack.Bones.create_group(
        6,
        "blue_bone",
        r"Images\Attacks\normal_blue_bone.png",
        200,
        450,
        1
    ),
       
       "Bone_phase_1_blue_long": attack.Bones.create_group(
        6,
        "blue_bone_long",
        r"Images\Attacks\blue_bone.png",
        250,
        200,
        1
    ),
       
       
      
       "Bone_phase_1_orange": attack.Bones.create_group(
        5,
        "orange_bone",
        r"Images\Attacks\long_bone.png",
        250,
        450,
        1
    ),
       
       
        "Bone_phase_1_orange_long": attack.Bones.create_group(
        5,
        "orange_bone_long",
        r"Images\Attacks\orange_bone.png",
        250,
        200,
        1
    )
}


    
    
    
    
battle_speech = {
    # IDLE / CONSTANT PRESSURE
    "Idle_1": "stop moving like you’re thinking it’ll save you.",
    "Idle_2": "you hesitate again and you’re dead.",
    "Idle_3": "i don’t care what you’re planning. it won’t work.",
    "Idle_4": "you’re making this too easy.",
    "Idle_5": "Get read for my special attack !!!!!!!",
    "Idle_6": "i’ve buried worse than you for less.",

    # MID FIGHT
    "Talk_1": "you’re slowing down. bad habit.",
    "Talk_2": "that panic’s starting to show.",
    "Talk_3": "you wanted this fight. now survive it.",
    "Talk_4": "don’t blink. that’s when it gets ugly.",
    "Talk_5": "you’re running out of mistakes.",

    # ATTACK PRESSURE
    "Attack_1": "dodge.",
    "Attack_2": "too slow.",
    "Attack_3": "you’re already done.",
    "Attack_4": "move or die.",
    "Attack_5": "you saw that coming. you just didn’t react.",

    # HIT / REACTION
    "Hit_1": "tch—",
    "Hit_2": "that it?",
    "Hit_3": "you call that damage?",
    "Hit_4": "careful. you’re not untouchable.",

    # LOW HP SANS (more dangerous, less joking)
    "LowHP_1": "alright... now you’re just wasting my time.",
    "LowHP_2": "i’m done holding back.",
    "LowHP_3": "you wanted serious? here it is.",
    "LowHP_4": "don’t expect another opening.",

    # WIN / END
    "Win_1": "pathetic.",
    "Win_2": "that’s what you risked everything for?",
    "Win_3": "stay down."
}








    
#### this dialogue is specficslly for battle. (DO NOT GET THIS MIXED WITH SANS INTRO SPECIFIC DIALOGUE) - EBUKA
    
    
    
    
# TO DO
# Do a bit more on bones , gravity combo, gaster blaster ,get battle music
# later add in mercy button
    
    
    
    




    
def game():
    # indexes for attacks
    global battle_speech

    bone_counter = 0 
    gaster_counter = 0
    speech_lock = False
    
    battle_text_counter = 0
    
    pygame.init()
    pygame.mixer.init()
    
    
    
    theme_song = pygame.mixer.music.load(r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\sounds\theme_tune.mp3")
    
    
    
    
    
    
    gaster_blaster = pygame.mixer.Sound(r"sounds\gaster_blaster_sound_effect_1.mp3")
    
    
    Clock = pygame.time.Clock()
    width = 800
    height = 700
    
    # config
    
    title = pygame.display.set_caption("UNDERFELL CARNAGE")
    screen = pygame.display.set_mode((width,height))
    
    keys = utils.read_data("settings.txt",0,5)
    #print(keys)
    
    game_mode = "intro" # change back to intro later
    
    path = "c:\\USERS\\CHUCH\\APPDATA\\LOCAL\\MICROSOFT\\WINDOWS\\FONTS\\DTM-MONO.OTF" # undertale font - small
    font = pygame.font.Font(path,15)
    large_font = pygame.font.Font(path,30)



    data_to_keys = {
        "[ENTER]":pygame.K_RETURN,
        "[SPACE]":pygame.K_SPACE,
        "[Z]": pygame.K_z, # confirm
        "[X]": pygame.K_x,
        "[C]": pygame.K_c
       
    }
    
    dialogue = {
    "Intro_1": "heh. so you finally showed up.",
    "Intro_2": "got a lot of nerve walking in here.",
    "Intro_3": "this place doesn’t forgive mistakes.",
    "Intro_4": "and you? you look like one.",
    }
    

    
    
    player = gaming_objects.player("Frisk",screen.get_width()//2,screen.get_height()//2)
    
    
    
    
    run =  True
    
    # battle_menus
    
    Act = gaming_objects.Battle_buttons("Act",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Act_1.png",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Act_2.png")
    Fight =  gaming_objects.Battle_buttons("Fight",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Fight_1.png",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Fight_2.png")
    Item =  gaming_objects.Battle_buttons("Item",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Item_1.png",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Item_2.png")
    Mercy =  gaming_objects.Battle_buttons("Mercy",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Mercy_1.png",r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\Images\Buttons\Mercy_2.png")
    
    
    
    
    options = [Act,Fight,Item,Mercy]
    
    utils.general_sort(options,10)
    
    # buttons will be here
    
    index = 0 # for options
    menu_choice = pygame.mixer.Sound("sounds\\Select.mp3")
    
    
    
    
    # underfell sans character fix
    
    
    underfell_sans = sans.Character("sans",200,10)
    underfell_sans.legs.x =  315 # set legs to proper position
    underfell_sans.legs.y = 220
    
    underfell_sans.head.x = 340
    underfell_sans.head.y = 70
    underfell_sans.head.base_y = underfell_sans.head.y # set y to the new y
    underfell_sans.head.og_x = underfell_sans.head.x # set x to new x
    

    
    
    
    box = gaming_objects.Box("Box")
    health_bar = gaming_objects.HPBar(400,570,25,25,20)
    
    phase = 0# counter for phases
    
    state = ""
    choice_made = False
    opcode = 0
    curr_game_mode = "Phase_1"
    sans_eye = pygame.mixer.Sound("sounds\\sans_sfx\\sans-eye-sounds.mp3")
    
    
    take_damage = pygame.mixer.Sound("sounds\\damage_taken.mp3")
    
   
    
    
    sans_voice = pygame.mixer.Sound(r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\sounds\sans_sfx\sans voice.wav")
    normal_text = pygame.mixer.Sound(r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\sounds\text_regular.mp3")
    heal = pygame.mixer.Sound(r"C:\Users\chuch\OneDrive\Desktop\UNDERFELL\sounds\heal.mp3")
    count = 0

    tokens = utils.tokenise(
    dialogue,
    underfell_sans.head.x + 180,  
    underfell_sans.head.y + 20    
    )
    
    
    battle_text = utils.tokenise(battle_speech,
                             underfell_sans.head.x + 180,
                             underfell_sans.head.y + 20
                             
                             
                             )
   
    battle_talk = gaming_objects.DialogueManager(battle_text[battle_text_counter])
    
    
    
    text = gaming_objects.DialogueManager(tokens[count])
    
    button_pressed  = False
    
    #utils.fade_in(screen,width,height,[Act,Item,Fight,Mercy,player,underfell_sans.body,underfell_sans.head,underfell_sans.legs],halt=20)
    #remembe to change count to 0
    # will makee intro
    
    def intro():
        nonlocal count, text, tokens

        underfell_sans.display_dialogue_box(screen)

        finished = text.update(0.005, sans_voice) # for speech text
        text.draw(screen, font)

        if finished:
            if count < len(tokens)-1:
                count += 1
                text = gaming_objects.DialogueManager(tokens[count])
                if count == len(tokens) - 1:
                    finished =  False

        if count == len(tokens)-1 and finished:
            underfell_sans.head.set_image(13)
            return True
        elif count == 1:
            underfell_sans.head.set_image(2)
        elif count == 2:
            underfell_sans.head.set_image(10)
        elif count == 3:
            underfell_sans.head.set_image(14)
        
            
            
        
        

    
    
    
    def draw_data():
        draw_battle_buttons(options,screen)    
        
        player.draw(screen)
        underfell_sans.draw(screen)
        box.draw(screen)
        
        
        health_bar.draw(screen,player)
        
        
        utils.draw_text(screen,f"{player.hp}/20",font,(255,0,0),450,567)
        utils.draw_text(screen,f"CHARA LV 20",font,(255,0,0),100,567)
        utils.draw_text(screen,f"HP",font,(255,0,0),370,567)
    

   
    
    while run:
        fps = Clock.tick(60) 

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if game_mode == "Options":
                
                    if not button_pressed and state == "":
                        #print("I can move")
                        if event.key == pygame.K_RIGHT:
                            index+=1
                            menu_choice.play()
                        if event.key == pygame.K_LEFT:
                            index -= 1
                            menu_choice.play()
                        
                    if state == "Item":
                        
                        if event.key == pygame.K_DOWN:
                            opcode -= 1
                            menu_choice.play()
                        if event.key == pygame.K_UP:
                            opcode += 1
                            menu_choice.play()
                     
                        
                            
                       
                        
                            

                       
                       
                        
                        
                       
                      
                        
                        

                   
                
                
        
        screen.fill((0,0,0))
        
        
        
        # phases
        
        if game_mode == "Phase_1":
            
            bones = []
            
            
            
            if phase == 0:
                bones = attack_combination["Bone_phase_1"]  # normal bones
                bone_up = attack_combination["Bone_phase_1_up"]
            

                if bone_counter < len(bones):
                    bones[bone_counter].move(random.randint(5,10))
                    bones[bone_counter].display(screen)
            
                    bone_up[bone_counter].move(random.randint(5,10))
                    bone_up[bone_counter].display(screen)
                    
                    
                    if bone_up[bone_counter].collision(player,take_damage) or bones[bone_counter].collision(player,take_damage):
                        player.hp -= 1
                        
            
                    if bones[bone_counter].finished:
                        bone_counter += 1
                   # print(bone_counter)
                else:
                    bone_counter = 0 # reset and increments
                    phase += 1
                    underfell_sans.head.set_image(4)
                    sans_eye.play()
                    player.set_gravity()
                    change = True
            
                
            ## part 1 of phase 1###
                 
            # part 2 of phase 1##
            
            # for long bone
            
            elif phase == 1:
                bones = attack_combination["Bone_phase_1_long"]
                bone_up = attack_combination["Bone_phase_1_long_up"]
                
                
                if change: # oof
                    underfell_sans.head.set_image(5)
                  
                
                if bone_counter < len(bones):
            
                    bones[bone_counter].move(random.randint(8,10))
                    bones[bone_counter].display(screen)
            
                    bone_up[bone_counter].move(random.randint(8,10))
                    bone_up[bone_counter].display(screen)
                    
                    if bone_up[bone_counter].collision(player,take_damage) or bones[bone_counter].collision(player,take_damage):
                        player.hp -= 1
                
                    if bones[bone_counter].finished:
                        bone_counter += 1
                else:
                    bone_counter = 0
                    phase += 1
                    player.set_gravity()
                    underfell_sans.head.set_image(14)
                   
                    
               
                """
                if bone_counter >= len(bones):
                    if box.w != 600 or box.h != 200:
                        box.set_mode("on")
                        box.change_size()      
                    else:
                        print("asda")
                        bone_counter = 0
                        phase +=1
                        box.set_mode("off")
                """    
            
            
            elif phase == 2:
                bones = attack_combination["Bone_phase_1_long"]
                bone_up = attack_combination["Bone_phase_1_long_up"] # long
                
                    
                
                if bone_counter < len(bones):
                  
                    bones[bone_counter].move(random.randint(10,20))
                    bones[bone_counter].display(screen)
            
                    bone_up[bone_counter].move(random.randint(10,20))
                    bone_up[bone_counter].display(screen)
                    
                    if bone_up[bone_counter].collision(player,take_damage) or bones[bone_counter].collision(player,take_damage):
                        player.hp -= 1
                
                    if bones[bone_counter].finished:
                        bone_counter += 1
                else:
                    bone_counter = 0
                    phase += 1
                    
                    
                    
            elif phase == 3:
                gaster = attack_combination["Normal_Gaster_blaster"]
                gaster_opp = attack_combination["Normal_Gaster_blaster_opp"]
                
               
                
                print(gaster_counter)
                
                if gaster_counter < len(gaster):
                    
                    gaster[gaster_counter].move_gaster(screen,player)
                    gaster[gaster_counter].gaster_change(screen,gaster_blaster) # gaster_blaster variable is the sfx

                    gaster_opp[gaster_counter].move_gaster(screen,player)
                    gaster_opp[gaster_counter].gaster_change(screen,gaster_blaster) # gaster_blaster variable is the sfx

            
                 
            
                    if gaster[gaster_counter].finished:
                        gaster_counter += 1
                       
                      
                        attack_combination["Normal_Gaster_blaster"]  = attack.Gaster.create_group(
                        3,
                        "Normal_Gaster",
                        r"Images\Attacks\Gaster_idle_1.png",
                         50,
                         random.randint(150,250),
                         200,
                         90
                        )

                        attack_combination["Normal_Gaster_blaster_opp"]  = attack.Gaster.create_group(
                        3,
                        "Normal_Gaster",
                        r"Images\Attacks\Gaster_idle_1.png",
                         50,
                         random.randint(200,400),
                         200,
                         90
                        )
                        
                else: 
                    gaster_counter = 0
                    phase += 1
                    underfell_sans.head.set_image(4)
                    sans_eye.play()
                    player.set_gravity()
                    
                    
                   
                    
            elif phase == 4:
                bones = attack_combination["Bone_phase_1_blue"]
                bone_up = attack_combination["Bone_phase_1_blue_long"]
                
                
        
                if bone_counter < len(bones):
            
                    bones[bone_counter].move(random.randint(8,10))
                    bones[bone_counter].display(screen)
            
                    bone_up[bone_counter].move(random.randint(8,10))
                    bone_up[bone_counter].display(screen)
                    
                    
                   
                    bone_up[bone_counter].blue_effect(player,take_damage)
                    bones[bone_counter].blue_effect(player,take_damage)
                    
                
                    if bones[bone_counter].finished:
                        bone_counter += 1
                else:
                    bone_counter = 0
                    phase += 1
                    underfell_sans.head.set_image(10)
                    
                    
                    
                
                          
            elif phase == 5:
                bones = attack_combination["Bone_phase_1_orange"]
                bone_up = attack_combination["Bone_phase_1_orange_long"]
                
                
        
                if bone_counter < len(bones):
            
                    bones[bone_counter].move(random.randint(8,10))
                    bones[bone_counter].display(screen)
            
                    bone_up[bone_counter].move(random.randint(8,10))
                    bone_up[bone_counter].display(screen)
                    
                    
                   
                    bone_up[bone_counter].orange_effect(player,take_damage)
                    bones[bone_counter].orange_effect(player,take_damage)
                    
                
                    if bones[bone_counter].finished:
                        bone_counter += 1
                        
                        
                else:
                    underfell_sans.head.set_image(3)
                    bone_counter = 0
                    phase += 1
                    
                    attack_combination["Bone_phase_1_orange"]=attack.Bones.create_group(
                    5,
                    "orange_bone",
                     r"Images\Attacks\long_bone.png",
                    250,
                     450,
                     1
                     )
       
       
                    attack_combination["Bone_phase_1_orange_long"] = attack.Bones.create_group(
                    5,
                    "orange_bone_long",
                    r"Images\Attacks\orange_bone.png",
                    250,
                    200,
                    1
                     )
                    
                    
                    
                    
                   
            
            elif phase == 6:
                bones = attack_combination["Bone_phase_1_orange"]
                bone_up = attack_combination["Bone_phase_1_orange_long"]
                
                gaster = attack_combination["Normal_Gaster_blaster"]
                
                
                
                if bone_counter < len(bones):
                    gaster[gaster_counter].move_gaster(screen,player)
                    gaster[gaster_counter].gaster_change(screen,gaster_blaster) 
                 
                        
                  
                    bone_up[bone_counter].orange_effect(player,take_damage)
                    bones[bone_counter].orange_effect(player,take_damage)
                

                    bones[bone_counter].display(screen)
                    bones[bone_counter].move(10) 
                    
                    bone_up[bone_counter].display(screen)
                    bone_up[bone_counter].move(10) 
                    
                    if gaster[gaster_counter].finished:
                        gaster_counter += 1
                        attack_combination["Normal_Gaster_blaster"]  = attack.Gaster.create_group(
                        5,
                        "Normal_Gaster",
                        r"Images\Attacks\Gaster_idle_1.png",
                         50,
                         random.randint(150,450),
                         200,
                         90
                        )
                        
                    if bones[bone_counter].finished:
                        bone_counter += 1
                
                 
                   
                        
                        
                        
                else:
                    print("switch")
                    print(bone_counter)
                    underfell_sans.head.set_image(3)
                    phase += 1
                    gaster_counter = 0      
                   
                    
                    
            
                        
            elif phase == 7:
                underfell_sans.display_dialogue_box(screen)
                battle_talk.draw(screen,font)
                finished =  battle_talk.update(0.01,sans_voice)
                
                if battle_text_counter < 3:
                    if finished:
                        battle_text_counter += 1
                        battle_talk =  gaming_objects.DialogueManager(battle_text[battle_text_counter])
                else:
                    phase+=1
                    player.set_gravity()
                    bone_counter = 0
                    gaster_counter = 0
                    underfell_sans.head.set_image(2)
            
            
            elif phase == 8:
                
                bones = attack_combination["Bone_phase_1_blue_long"]
                bone_up = attack_combination["Bone_phase_1_orange"]
                
                gaster = attack_combination["Normal_Gaster_blaster"]
                
                
                
                if bone_counter < len(bones):
                    gaster[gaster_counter].move_gaster(screen,player)
                    gaster[gaster_counter].gaster_change(screen,gaster_blaster) 
                 
                        
                  
                    bone_up[bone_counter].orange_effect(player,take_damage)
                    bones[bone_counter].blue_effect(player,take_damage)
                

                    bones[bone_counter].display(screen)
                    bones[bone_counter].move(16) 
                    
                    bone_up[bone_counter].display(screen)
                    bone_up[bone_counter].move(20) 
                    
                    if gaster[gaster_counter].finished:
                        
                        gaster_counter += 1
                        attack_combination["Normal_Gaster_blaster"]  = attack.Gaster.create_group(
                        20,
                        "Normal_Gaster",
                        r"Images\Attacks\Gaster_idle_1.png",
                         50,
                         random.randint(150,450),
                         200,
                         90
                        )
                        
                        
                        
                    if bones[bone_counter].finished:
                        bone_counter += 1
                        
                        attack_combination["Bone_phase_1_blue_long"] = attack.Bones.create_group(
                            20,
                            "blue_bone_long",
                            r"Images\Attacks\blue_bone.png",
                            250,
                            200,
                            1
                        )
                        
                        attack_combination["Bone_phase_1_orange"] = attack.Bones.create_group(
                        20,
                        "orange_bone_long",
                        r"Images\Attacks\orange_bone.png",
                        250,
                        450,
                        1
                        )
                       
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        if player.soul_mode == "blue" and not player.on_ground: # applies gravity if user not on ground and soul mode is blue
            player.apply_gravity()
            
        if player.forcefield: # if forcefield user takes no damage for certain amount of time
            if player.forcefield_counter <= 60:
                player.forcefield_counter += 1
                
                #print(player.forcefield_counter)
            else:
                if not player.gravity_on:
                    player.img = player.og_img
                else:
                    player.img = player.img2
                
                player.forcefield = False
                player.forcefield_counter = 0
                
                
                
                
                
            
        
            
            
            
        if game_mode == "intro": # single time use maybe
           intro_speech =  intro()
           pygame.time.delay(10)
           
           
           if intro_speech:
            pos = options_picker(options,index)
            player.x = pos.x + 10
            player.y = pos.y+20
            
            box.set_mode("on")
            box.change_size()
            
            if box.mode == "off":
                game_mode = "Options"
                pygame.mixer.music.play(-1)
                
        
                
                
        
        
        elif game_mode == "Options":
            index = max(0, min(index, len(options)-1))
            
                
                
            pos = options_picker(options,index) # get battle button and position user relative to it
            player.x = pos.x + 10
            player.y = pos.y+20
            
            
            if not button_pressed:
                if box.w != 600 or box.h != 200:
                    box.set_mode("on")
                    box.change_size()
                else:
                    box.set_mode("off")  # finished opening
            elif box.mode == "on":                 
                box.change_size()
                
            if not pos.items and pos.name == "Item":
                utils.draw_text(screen, "NO ITEMS LEFT", large_font, gaming_objects.colors["red"], 300, 350) # fix size
          # will fix 
                
            
            
          
            
            
            key_code = pygame.key.get_pressed()
            
            if key_code[pygame.K_z]:
                if not button_pressed:
                    button_pressed  = True
            
            if key_code[pygame.K_x] and pos.name == "Item":
                if button_pressed:
                    button_pressed  = False
                    state = ""
                
            if pos.name == "Act" and button_pressed:
                state = "Act"
                pos.Act(screen,normal_text,large_font)
            
             
              
            if pos.name == "Item" and button_pressed:
                state = "Item"

                   

                if opcode > len(pos.items)-1:
                    opcode = 0
                elif opcode < 0:
                    opcode = len(pos.items) - 1
                    
                result =  pos.Item(opcode,screen,large_font,player,heal)
                
                if result:
                    choice_made = True
            
            elif pos.name == "Mercy" and button_pressed:
                state = "Mercy"
                pygame.mixer.music.stop()
                result = pos.Mercy(screen,underfell_sans,sans_voice,font)

                if result:
                    choice_made = True
                    
                
                
               
                    

            
           #
           # mercy/ code the death screen and code animatrion of heart and finish sans dialogue
           # fight
           
           
           
            if (button_pressed and pos.text.finished) or choice_made:
                done  = box.change_size()
                box.set_mode("off")  # close the box
                
                player.x = player.og_x
                player.y = player.og_y
                pos.img  = pos.og_img
                
                
                if done:
                 game_mode  = curr_game_mode  # back to options menu
                 button_pressed = False
                 state = ""  # reset state
                 pos.text.finished = False
                 choice_made = False
                
                
        
          
          
          # fix undertale sans text issue
            
        else:
            player.update(box)
            
            
            
        draw_data()
            
            
       
        
        if player.hp <= 0:
            pass
            
        if False:
            # so after game_mode is set to game over we then do a fade after fade we shall show text and then end the game 
            pass
        
        
        
        
        underfell_sans.update()
        pygame.display.update()
        
        
                         
    pygame.quit()
    

if __name__ =="__main__":
    game()