import comtypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import pygame
import screen_brightness_control as sbc
from tkinter import *
import threading
import time
from PIL import Image


def pyglet2():
    def play_music():
        import pyglet
        global player
        src=pyglet.media.load("title song 4.m4a")
        player=pyglet.media.Player()
        player.queue(src)
        player.loop=True
        player.volume=0.05
        player.play()
        pyglet.app.run()
    t=threading.Timer(0,play_music)
    t.start()
    def stop_music():
            player.pause()
    pyglet2.stop_music=stop_music
    pyglet2.play_music=play_music
pyglet2()
def work():
    top=Tk()
    global scr_w
    scr_w=top.winfo_screenwidth()
    global scr_h
    scr_h=top.winfo_screenheight() 
    top.title("Game")
    top.geometry("10000x10000")
    def button():
        def play():
            pyglet2.stop_music()
            pygame.init()
            white=(255, 255, 255)
            X=442
            Y=500
            display_surface=pygame.display.set_mode((X,Y))
            pygame.display.set_caption('Game')
            image=pygame.image.load(r'azerbaijan.png')
            while True:
                display_surface.blit(image,(0,0))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pyglet2.play_music()
                        pygame.quit()
                        quit()
                    pygame.display.update()
        t2=threading.Timer(0,play)
        t2.start()
        textbox=Toplevel()
        w=int((scr_w-780)/2)
        s=int(scr_w/53.33333333333333)+12
        w+=s
        textbox.geometry('700x130'+"-"+str(w)+"-70")
        textbox.title('')
        text_file=open(r"TextCheck.txt",'r')
        dialogue=text_file.read()
        dialist=dialogue.split('\n\n')
        l1=[]
        l2=[]
        for i in range(len(dialist)):
            tup1=dialist[i].partition(':')
            l1.append(tup1[0])
            l2.append(tup1[-1])
        label=Label(textbox,text='',font='BOLD',wraplength=700)
        k=-1
        m=-1
        button2=Button(textbox, text='     >     ')
        button2.pack(side='bottom')
        def next_line():
            nonlocal k
            nonlocal m
            k+=1
            m+=1
            if k<(len(l2)) and m<(len(l1)):
                str1=l2[k]
                textbox.title(l1[m])
                label['text']=''
                for j in str1:
                    button2["state"]="disabled"
                    label['text']=label['text'] + j
                    label.update()
                    label.pack(side='left')
                    time.sleep(.03)
                button2["state"]="active"
            else:
                k=0
                m=0
                str1=l2[k]
                textbox.title(l1[m])
                label['text']=''
                for j in str1:
                    button2["state"]="disabled"
                    label['text']=label['text'] + j
                    label.update()
                    label.pack(side='left')
                    time.sleep(.03)
                button2["state"]="active"
        button2["command"]=next_line
        textbox.mainloop()
    work.button=button
    def pressed2():
        screen2=Toplevel()
        screen2.title("Credits")
        screen2.geometry("10000x10000")
        canvas2=Canvas(screen2,width=scr_w,height=scr_h)
        canvas2.pack(expand=True,fill="both")
        img_cred = Image.open('credits final.png')
        img_cred = img_cred.resize((scr_w, scr_h), Image.ANTIALIAS)
        img_cred.save('credits final.png')
        background2=PhotoImage(file="credits final.png")
        canvas2.create_image(0,0,image=background2,anchor="nw")
        screen2.mainloop()
    def pressed3():
        screen3=Tk()
        screen3.title("Settings")
        screen3.geometry("10000x10000")
        frame2=Frame(screen3,bg="black")
        frame2.pack(expand=True,fill="both")
        music=Label(frame2,text="Music")
        music.place(x=30,y=90)
        Button(frame2,text="Stop Music",command=pyglet2.stop_music).place(x=100,y=90)
        Button(frame2,text="Play Music",command=pyglet2.play_music).place(x=250,y=90)
        volume=Label(frame2,text="Volume")
        volume.place(x=30,y=130)
        devices=AudioUtilities.GetSpeakers()
        interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
        volume=cast(interface,POINTER(IAudioEndpointVolume))
        def redlevelvolume():
            currentvolume=volume.GetMasterVolumeLevel()
            volume.SetMasterVolumeLevel(currentvolume-6.0,None)
        Button(frame2,text="Reduce Volume",command=redlevelvolume).place(x=250,y=130)
        devices2=AudioUtilities.GetSpeakers()
        interface2=devices2.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
        volume2=cast(interface2,POINTER(IAudioEndpointVolume))
        def inclevelvolume():
            currentvolume2=volume2.GetMasterVolumeLevel()
            volume2.SetMasterVolumeLevel(currentvolume2+6.0,None)
        Button(frame2,text="Increase Volume",command=inclevelvolume).place(x=100,y=130)
        brightness=Label(frame2,text="Brightness")
        brightness.place(x=30,y=50)
        inputbrightness= Entry(frame2)
        inputbrightness.place(x=100,y=50)
        def setlevelbrightness():
            level=inputbrightness.get()
            sbc.set_brightness(level)
        Button(frame2,text="Set Brightness",command=setlevelbrightness).place(x=250,y=50)
        screen3.mainloop()
    frame1=Frame(top,bg="black")
    frame1.pack(side=BOTTOM,expand=True,fill="both")
    start=Button(frame1,text="Start Game",fg="black",command=work.button)
    start.pack(side=BOTTOM)
    menubutton=Menubutton(frame1,text="Menu",fg="black",relief=RAISED)
    menubutton.menu = Menu(menubutton)
    menubutton["menu"]=menubutton.menu
    menubutton.menu.add_cascade(label="Credits",command=pressed2)
    menubutton.menu.add_cascade(label="Settings",command=pressed3)
    menubutton.pack(side=BOTTOM)
    img_tit = Image.open('titles final.png')
    img_tit = img_tit.resize((scr_w, scr_h), Image.ANTIALIAS)
    img_tit.save('titles final.png')    
    background=PhotoImage(file="titles final.png")
    canvas=Canvas(top,width=scr_w,height=scr_h)
    canvas.pack(expand=True,fill="both")
    canvas.create_image(0,0,image=background,anchor="nw")
    top.mainloop()
work()
