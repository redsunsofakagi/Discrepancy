import pygame
from tkinter import *
from tkinter.tix import *
from tkinter.font import Font
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import sys
from pyglet import font
import os
import button
from PIL import Image

pygame.init()
infoObject = pygame.display.Info()
main_dir = os.path.split(os.path.abspath(__file__))[0]


main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join("Images", "Menu")
font_dir = os.path.join("Fonts")
music_dir = os.path.join("Music")

h=int((infoObject.current_h-50)/1.3566666666666667) +30
hf=int((infoObject.current_h-50)/1.3566666666666667)+80
hn=int((infoObject.current_h-50)/1.3566666666666667)+100
hc=int((infoObject.current_h-50)/1.3566666666666667)+25
w1=(infoObject.current_w/4)-50-150
wt2=(2*infoObject.current_w/4)
w2=(2*infoObject.current_w/4)-150
w3=(3*infoObject.current_w/4)-60
wt3=(3*infoObject.current_w/4)-30
w_2=(2*infoObject.current_w/4)-30
w_3=(3*infoObject.current_w/4)-50
w01=(infoObject.current_w/4)+120
w02=(2*infoObject.current_w/4)-100
w03=(3*infoObject.current_w/4)+30

img_cred = Image.open(os.path.join(img_dir, 'Slide1.png'))
img_cred = img_cred.resize((infoObject.current_w, infoObject.current_h-50), Image.ANTIALIAS)
img_cred.save(os.path.join(img_dir, 'Slide1.png'))
img_cred = Image.open(os.path.join(img_dir, 'Slide3.png'))
img_cred = img_cred.resize((infoObject.current_w, infoObject.current_h-50), Image.ANTIALIAS)
img_cred.save(os.path.join(img_dir, 'Slide3.png'))
img_cred = Image.open(os.path.join(img_dir, 'Slide4.png'))
img_cred = img_cred.resize((infoObject.current_w, infoObject.current_h-50), Image.ANTIALIAS)
img_cred.save(os.path.join(img_dir, 'Slide4.png'))
img_cred = Image.open(os.path.join(img_dir, 'Slide2.png'))
img_cred = img_cred.resize((infoObject.current_w, infoObject.current_h-50), Image.ANTIALIAS)
img_cred.save(os.path.join(img_dir, 'Slide2.png'))

screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h-50))
screen.fill('Black')
pygame.display.set_caption('Discrepancy')
clock = pygame.time.Clock()
selite_font = pygame.font.Font(os.path.join(font_dir, 'SpecialElite-Regular.ttf'), 50)
title_music = pygame.mixer.Sound(os.path.join(music_dir, 'title_music.wav'))
title_img = pygame.image.load(os.path.join(img_dir, 'Slide1.png')).convert_alpha()
credits_img = pygame.image.load(os.path.join(img_dir, 'Slide3.png')).convert_alpha()
start_img = pygame.image.load(os.path.join(img_dir, 'Slide4.png')).convert_alpha()
options_img = pygame.image.load(os.path.join(img_dir, 'Slide2.png')).convert_alpha()

clr_bttn_268x84 = pygame.image.load(os.path.join(img_dir, 'clr_bttn_268x84.png')).convert_alpha()
clr_bttn_78x74 = pygame.image.load(os.path.join(img_dir, 'clr_bttn_78x74.png')).convert_alpha()
clr_bttn_127x74 = pygame.image.load(os.path.join(img_dir, 'clr_bttn_127x74.png')).convert_alpha()
clr_bttn_179x67 = pygame.image.load(os.path.join(img_dir, 'clr_bttn_179x67.png')).convert_alpha()

button_start = button.Button(w1,h, clr_bttn_268x84)
button_menu = button.Button(w2,h, clr_bttn_268x84)
button_credits = button.Button(w3,h, clr_bttn_268x84)
button_back = button.Button(w2,int(h*1.166666666666), clr_bttn_268x84)
button_vol_plus = button.Button(int(wt3*1.09),int(hf/4.545454545), clr_bttn_78x74)
button_vol_min = button.Button(int(wt2*1.3),int(hf/4.477611940298507), clr_bttn_78x74)
button_vol_on = button.Button(int(w_2*1.3),int(hf/2.112676056338), clr_bttn_127x74)
button_vol_off = button.Button(int(w_3*1.09),int(hf/2.112676056338), clr_bttn_127x74)
button_case1 = button.Button(int(w01/2.75),int(hn/7.5), clr_bttn_179x67)
button_case2 = button.Button(w03,int(hn/7.5), clr_bttn_179x67)
button_case3 = button.Button(w02,hc/2, clr_bttn_179x67)

state_start = False
state_options = False
state_credits = False
vol_lvl=0.10
music_state = True
selite_font = pygame.font.Font(os.path.join(font_dir, 'SpecialElite-Regular.ttf'), 36)
control_box = selite_font.render(str(float(vol_lvl)), True, 'White')
game_loop = True

while game_loop:
    control_box = selite_font.render(str(vol_lvl), True, 'White')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if music_state:
        title_music.play(-1)
        title_music.set_volume(vol_lvl)

    if state_start:
        screen.fill('Black')
        screen.blit(start_img,(0,0)) 
        if button_back.draw(screen):
            state_start = False
        if button_case1.draw(screen):
            exec(open("Case1.py").read())
        if button_case2.draw(screen):
            exec(open("Case2.py").read())
        if button_case3.draw(screen):
            exec(open("Case3.py").read())

    elif state_options:
        screen.fill('Black')
        screen.blit(options_img, (0,0))
        if button_back.draw(screen):
            state_options = False
        if button_vol_plus.draw(screen):
            vol_lvl += 0.05
        if button_vol_min.draw(screen):
            vol_lvl -= 0.05
        if button_vol_on.draw(screen):
            vol_lvl = 0.1
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
