from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
#from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import pygame
import screen_brightness_control as sbc
from tkinter import *
from tkinter import font
from tkinter import ttk
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
        GameWindow=Toplevel()
        GameWindow.resizable(width=False, height=False)
        GameWindow.title('Discrepancy')
        GameWindow.geometry('600x500') 
        GameFont = font.Font(family='Courier', name='GameFont', size=15, weight='bold')
        SceneImage=PhotoImage(file="Scene1.png")
        TextFrame=PhotoImage(file="textframe.png")
        ObjectiveFrame=PhotoImage(file='ObjectiveFrame.png')
        Obj1=PhotoImage(file='DeidMann.png') 
        Obj2=PhotoImage(file='BurningCar.png')
        Obj3=PhotoImage(file='BloodyWrench.png')
        Wit1=PhotoImage(file='Witness.png')
        tutorial_file = open(r"MainTutorial.txt" , 'r')
        tutorial_dialogue=tutorial_file.read() 
        tutorial_list=tutorial_dialogue.split('\n\n') 
        l1=[]
        l2=[]
        for i in range(len(tutorial_list)):
                       tup1=tutorial_list[i].partition(': ')
                       l1.append(tup1[0]) 
                       l2.append(tup1[-1])
        event_file = open(r"EventText.txt" , 'r')
        event_dialogue=event_file.read()
        event_list=event_dialogue.split('\n\n')
        l3=[]
        l4=[]
        for i in range(len(event_list)):
                       tup2=event_list[i].partition(': ')
                       l3.append(tup2[0])
                       l4.append(tup2[-1])
        wit_file = open(r"WitnessText.txt" , 'r')
        wit_dialogue=wit_file.read()
        wit_list=wit_dialogue.split('\n\n')
        l5=[]
        l6=[]
        for i in range(len(wit_list)):
                       tup3=wit_list[i].partition(': ')
                       l5.append(tup3[0])
                       l6.append(tup3[-1])
        SceneScreen= Canvas(GameWindow, width=600, height=500)
        SceneScreen.create_image(300,200,image=SceneImage)
        SceneScreen.create_image(300,400,image=TextFrame) 
        SceneScreen.create_image(300,10,image=ObjectiveFrame)
        SceneScreen.create_image(310,200,image=Obj1, tags="Body")
        SceneScreen.create_image(510,100,image=Obj2, tags="Car")
        #SceneScreen.create_image(210,250,image=Obj3, tags="Wrench")
        SceneScreen.create_image(100, 200, image=Wit1)
        SceneScreen.pack()
        LineButton=ttk.Button(SceneScreen, text='     >     ')
        ObjectiveBar=Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=200)
        def hovertrueobj(): 
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']='[Examine]'
        def hoverfalseobj():
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']=''
        countobj=1
        def clicktrueobj(n, Obj_id):
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                nonlocal countobj
                SceneScreen.delete(Obj_id)
                SceneScreen.pack()
                if countobj<(len(l4)):
                    str1=l4[n]
                    SpeakBox['text']=l3[n]
                    TextBox['text']=''
                    for j in str1:
                        SceneScreen['state']='disabled'
                        ObjectiveBar['text']='[Read]'
                        TextBox['text']+=j
                        TextBox.update()
                        TextBox.pack(side='left')
                        SceneScreen.create_window(300,400, window=TextBox)
                        SceneScreen.update()
                        SceneScreen.pack(side='bottom')
                        time.sleep(0.04)
                    SceneScreen['state']='normal'
                elif countobj==(len(l4)):
                    str1=l4[n]
                    SpeakBox['text']=l3[n]
                    TextBox['text']=''
                    for j in str1:
                        SceneScreen['state']='disabled'
                        ObjectiveBar['text']='[Read]'
                        TextBox['text']+=j
                        TextBox.update()
                        TextBox.pack(side='left')
                        SceneScreen.create_window(300,400, window=TextBox)
                        SceneScreen.update()
                        SceneScreen.pack(side='bottom')
                        time.sleep(0.04)
                    SceneScreen['state']='normal'
                    LineButton['state']='active'
                    TextBox['state']='active'
                countobj+=1
        def hovertruewit():
            if TextBox.instate(['disabled']) and LineButton.instate(['disabled']) and countobj>(len(l4)):
                ObjectiveBar['text']='[Interrogate]'
        def hoverfalsewit():
           if TextBox.instate(['disabled']) and LineButton.instate(['disabled']) and countobj>(len(l4)):
                ObjectiveBar['text']=''
        #def clicktruebut(n, But_id):    
        countwit=1
        def clicktruewit(n, Wit_id):
            if TextBox.instate(['disabled']) and LineButton.instate(['disabled']) and countobj>(len(l4)):
                nonlocal countwit
                SceneScreen.delete(Wit_id)
                SceneScreen.pack()
                l5.reverse()
                l6.reverse()
                for i in l6:
                    if i[0]==str(n):
                        i=i[1:]
                        l2[k:k]=[i]
                for j in l5:
                    if j[0]==str(n):
                        j=j[1:]
                        l1[m:m]=[j]
                l6.reverse()
                l5.reverse()
                str1=l2[k]
                SpeakBox['text']=l1[m]
                TextBox['text']=''
                for j in str1:
                    SceneScreen['state']='disabled'
                    ObjectiveBar['text']='[Read]'
                    TextBox['text']+=j
                    TextBox.update()
                    TextBox.pack(side='left')
                    SceneScreen.create_window(300,400, window=TextBox)
                    SceneScreen.update()
                    SceneScreen.pack(side='bottom')
                    time.sleep(0.04)
                SceneScreen['state']='normal'
                LineButton['state']='active'
                TextBox['state']='active'
                countwit+=1   
        Obj1_id = SceneScreen.create_image(310,200,image=Obj1, tags="Body")
        SceneScreen.tag_bind(Obj1_id, "<Enter>", lambda p: hovertrueobj())
        SceneScreen.tag_bind(Obj1_id, "<Leave>", lambda p: hoverfalseobj())
        SceneScreen.tag_bind(Obj1_id, "<Button-1>", lambda p: clicktrueobj(0,Obj1_id))
        Obj2_id = SceneScreen.create_image(510,100,image=Obj2, tags="Car")
        SceneScreen.tag_bind(Obj2_id, "<Enter>", lambda p: hovertrueobj())
        SceneScreen.tag_bind(Obj2_id, "<Leave>", lambda p: hoverfalseobj())
        SceneScreen.tag_bind(Obj2_id, "<Button-1>", lambda p: clicktrueobj(1,Obj2_id))
        Obj3_id = SceneScreen.create_image(490,175,image=Obj3, tags="Wrench")
        SceneScreen.tag_bind(Obj3_id, "<Enter>", lambda p: hovertrueobj())
        SceneScreen.tag_bind(Obj3_id, "<Leave>", lambda p: hoverfalseobj())
        SceneScreen.tag_bind(Obj3_id, "<Button-1>", lambda p: clicktrueobj(2,Obj3_id))
        Wit1_id = SceneScreen.create_image(100, 200, image=Wit1)
        SceneScreen.tag_bind(Wit1_id, "<Enter>", lambda p: hovertruewit())
        SceneScreen.tag_bind(Wit1_id, "<Leave>", lambda p: hoverfalsewit())
        SceneScreen.tag_bind(Wit1_id, "<Button-1>", lambda p: clicktruewit(0,Wit1_id))
        SceneScreen.pack(side='bottom')
        ObjectiveBar.pack(side='bottom')
        SceneScreen.create_window(300, 20, window=ObjectiveBar)
        SpeakBox = Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=200)
        SpeakBox.pack(side='bottom')
        SceneScreen.create_window(300, 320, window=SpeakBox)
        TextBox = ttk.Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=525)
        TextBox.pack(side='left')
        SceneScreen.create_window(300,400, window=TextBox)
        LineButton.pack(side='bottom')
        SceneScreen.create_window(300,480, window=LineButton)
        k=-1
        m=-1
        def next_line(): 
            nonlocal k
            nonlocal m
            k+=1
            m+=1
            if k<(len(l2)) and m<(len(l1)) :
                str1=l2[k]
                SpeakBox['text']=l1[m]
                TextBox['text']=''
                for j in str1:
                    if str1[-1]=='-':
                        TextBox['state']='disabled'
                        LineButton['state']='disabled'
                        break
                    ObjectiveBar['text']='[Read]'
                    LineButton['state']='disabled'
                    TextBox['text']+=j
                    TextBox.update()
                    TextBox.pack(side='left')
                    SceneScreen.create_window(300,400, window=TextBox)
                    SceneScreen.update()
                    SceneScreen.pack(side='bottom')
                    time.sleep(0.04)
                else:
                    LineButton['state']='active'
        LineButton["command"]=next_line
        GameWindow.mainloop()
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
<<<<<<< Updated upstream
        #devices=AudioUtilities.GetSpeakers()
        #interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
        #volume=cast(interface,POINTER(IAudioEndpointVolume))
        #def redlevelvolume():
            #currentvolume=volume.GetMasterVolumeLevel()
            #volume.SetMasterVolumeLevel(currentvolume-6.0,None)
        Button(frame2,text="Reduce Volume").place(x=250,y=130)
        #devices2=AudioUtilities.GetSpeakers()
        #interface2=devices2.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
        #volume2=cast(interface2,POINTER(IAudioEndpointVolume))
        #def inclevelvolume():
            #currentvolume2=volume2.GetMasterVolumeLevel()
            #volume2.SetMasterVolumeLevel(currentvolume2+6.0,None)
=======
        devices=AudioUtilities.GetSpeakers()
        interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
        volume=cast(interface,POINTER(IAudioEndpointVolume))
        def redlevelvolume():
            currentvolume=volume.GetMasterVolumeLevel()
            volume.SetMasterVolumeLevel(currentvolume-6.0,None)
        Button(frame2,text="Reduce Volume").place(x=250,y=130)
        devices2=AudioUtilities.GetSpeakers()
        interface2=devices2.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
        volume2=cast(interface2,POINTER(IAudioEndpointVolume))
        def inclevelvolume():
            currentvolume2=volume2.GetMasterVolumeLevel()
            volume2.SetMasterVolumeLevel(currentvolume2+6.0,None)
>>>>>>> Stashed changes
        Button(frame2,text="Increase Volume").place(x=100,y=130)
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


