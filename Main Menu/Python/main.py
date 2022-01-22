import pygame
import button
import os
from sys import exit
#from GamePlay import gameplay

pygame.init()
screen = pygame.display.set_mode((1280,720))
screen.fill('Black')
pygame.display.set_caption('Discrepancy')
clock = pygame.time.Clock()
selite_font = pygame.font.Font('Fonts\SpecialElite-Regular.ttf', 50)

#Load Sounds
title_music = pygame.mixer.Sound('Sounds\\title_music.wav')

##Load Images
title_img = pygame.image.load('Photos\Slide1.PNG').convert_alpha()
credits_img = pygame.image.load('Photos\Slide3.PNG').convert_alpha()
start_img = pygame.image.load('Photos\Slide4.PNG').convert_alpha()
options_img = pygame.image.load('Photos\Slide2.PNG').convert_alpha()


##Buttons!
clr_bttn_268x84 = pygame.image.load('Photos\clr_bttn_268x84.png').convert_alpha()
clr_bttn_78x74 = pygame.image.load('Photos\clr_bttn_78x74.png').convert_alpha()
clr_bttn_127x74 = pygame.image.load('Photos\clr_bttn_127x74.png').convert_alpha()
clr_bttn_179x67 = pygame.image.load('Photos\clr_bttn_179x67.png').convert_alpha()

button_start = button.Button(128,549, clr_bttn_268x84)
button_menu = button.Button(509,549, clr_bttn_268x84)
button_credits = button.Button(890,549, clr_bttn_268x84)
button_back = button.Button(502,628, clr_bttn_268x84)

button_vol_plus = button.Button(1019,132, clr_bttn_78x74)
button_vol_min = button.Button(824,134, clr_bttn_78x74)
button_vol_on = button.Button(799,284, clr_bttn_127x74)
button_vol_off = button.Button(999,284, clr_bttn_127x74)

button_case1 = button.Button(126,80, clr_bttn_179x67)
button_case2 = button.Button(980,80, clr_bttn_179x67)
button_case3 = button.Button(544,273, clr_bttn_179x67)

state_start = False
state_options = False
state_credits = False
vol_lvl=1
music_state = True

##Load Fonts and text box
selite_font = pygame.font.Font('Fonts\SpecialElite-Regular.ttf', 36)
control_box = selite_font.render(str(float(vol_lvl)), True, 'White')



game_loop = True
while game_loop:
    control_box = selite_font.render(str(vol_lvl), True, 'White')
   #Exit game; uncomment to crash your PC like I did
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #play background music
    if music_state:
        title_music.play(-1)
        title_music.set_volume(vol_lvl)


    if state_start:
        screen.fill('Black')
        screen.blit(start_img,(0,0))

         
        if button_back.draw(screen):
            state_start = False
        if button_case1.draw(screen):
            #Uncomment below line to open a python file
            #exec(open("*Insert file path*").read())
            print("Hello1")
        if button_case2.draw(screen):
            #Uncomment below line to open a python file
            #exec(open("*Insert file path*").read())
            print("Hello2")
        if button_case3.draw(screen):
            #Uncomment below line to open a python file
            #exec(open("*Insert file path*").read())
            print("Hello3")
    
    elif state_options:
        screen.fill('Black')
        screen.blit(options_img, (0,0))
        screen.blit(control_box, (922,132))

        if button_back.draw(screen):
            state_options = False
        if button_vol_plus.draw(screen):
            vol_lvl += 0.1
        if button_vol_min.draw(screen):
            vol_lvl -= 0.1
        if button_vol_on.draw(screen):
            vol_lvl = 1
        if button_vol_off.draw(screen):
            vol_lvl = 0 
   
    elif state_credits:
        screen.fill('Black')
        screen.blit(credits_img, (0,0))

        if button_back.draw(screen):
            state_credits = False

    else: 
        screen.fill('Black')
        screen.blit(title_img,(0,0))
        
        pygame.time.delay(0)
        if button_start.draw(screen):
            state_start= True

        if button_menu.draw(screen):
            state_options = True

        if button_credits.draw(screen):
            state_credits = True
    


   


    pygame.display.update()

    clock.tick(60)





     
