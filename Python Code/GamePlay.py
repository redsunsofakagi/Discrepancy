#Gameplay. For real this time.

from tkinter import *
from tkinter import font
from tkinter import ttk
import time

GameWindow= Tk()
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

    

SceneScreen= Canvas(GameWindow, width=600, height=2000)
SceneScreen.create_image(300,200,image=SceneImage)
SceneScreen.create_image(300,400,image=TextFrame)
SceneScreen.create_image(300,10,image=ObjectiveFrame)

LineButton=ttk.Button(SceneScreen, text='     >     ')
ObjectiveBar = Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=200)

def hovertrue():
    if TextBox.instate(['disabled'])==True:
        ObjectiveBar['text']='[Examine]'

def hoverfalse():
    if TextBox.instate(['disabled'])==True:
        ObjectiveBar['text']=''

count=0
def clicktrue(n):
    global count
    count+=1
    if TextBox.instate(['disabled'])==True:
        if count<=(len(l4)):
            str1=l4[n]
            SpeakBox['text']=l3[n]
            TextBox['text']=''
            for j in str1:
                ObjectiveBar['text']='[Read]'
                TextBox['text']+=j
                TextBox.update()
                TextBox.pack(side='left')
                SceneScreen.create_window(300,400, window=TextBox)
                SceneScreen.update()
                SceneScreen.pack(side='bottom')
                time.sleep(0.03)
        elif count>(len(l4)):
            LineButton['state']='active'
            TextBox['state']='active'

def clicked(n):
    SceneScreen.tag_bind(id, "<Deactivate>", lambda p: clicktrue(n))
    
id = SceneScreen.create_image(310,200,image=Obj1)
SceneScreen.tag_bind(id, "<Enter>", lambda p: hovertrue())
SceneScreen.tag_bind(id, "<Leave>", lambda p: hoverfalse())
SceneScreen.tag_bind(id, "<Button-1>", lambda p: clicktrue(0), clicked(0))

id = SceneScreen.create_image(510,100,image=Obj2)
SceneScreen.tag_bind(id, "<Enter>", lambda p: hovertrue())
SceneScreen.tag_bind(id, "<Leave>", lambda p: hoverfalse())
SceneScreen.tag_bind(id, "<Button-1>", lambda p: clicktrue(1), clicked(1))

id = SceneScreen.create_image(210,250,image=Obj3)
SceneScreen.tag_bind(id, "<Enter>", lambda p: hovertrue())
SceneScreen.tag_bind(id, "<Leave>", lambda p: hoverfalse())
SceneScreen.tag_bind(id, "<Button-1>", lambda p: clicktrue(2), clicked(2))



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
    global k
    global m
    k+=1
    m+=1
    if k<(len(l2)) and m<(len(l1)) :
        str2=l2[k]
        SpeakBox['text']=l1[m]
        TextBox['text']=''
        for j in str2:
            if str2[-1]=='-':
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
            time.sleep(0.03)
        else:
            LineButton['state']='active'

LineButton["command"]=next_line

GameWindow.mainloop()
