from tkinter import *
from tkinter import font
from tkinter import ttk #ttk is necessary to check whether a widget is disabled or not
import time

GameWindow= Tk()
GameWindow.resizable(width=False, height=False)
GameWindow.title('Discrepancy')
GameWindow.geometry('600x500') #size specified, but positioning on monitor to be dealt with later

GameFont = font.Font(family='Courier', name='GameFont', size=15, weight='bold')
SceneImage=PhotoImage(file="Scene1.png")
TextFrame=PhotoImage(file="textframe.png")
ObjectiveFrame=PhotoImage(file='ObjectiveFrame.png')

tutorial_file = open(r"MainTutorial.txt" , 'r')
tutorial_dialogue=tutorial_file.read() #Text file stores content in a dialogue format. This is read as string.
tutorial_list=tutorial_dialogue.split('\n\n') #Splits on spacing between lines
l1=[]
l2=[]
for i in range(len(tutorial_list)):
               tup1=tutorial_list[i].partition(': ')
               l1.append(tup1[0]) #Stores name of speaking character
               l2.append(tup1[-1]) #Stores dialogue spoken

event_file = open(r"EventText.txt" , 'r')
event_dialogue=event_file.read()
event_list=event_dialogue.split('\n\n')
l3=[]
l4=[]
for i in range(len(event_list)):
               tup2=event_list[i].partition(': ')
               l3.append(tup2[0])
               l4.append(tup2[-1])

    

SceneScreen= Canvas(GameWindow, width=600, height=500, bg='black')
SceneScreen.create_image(300,200,image=SceneImage)
SceneScreen.create_image(300,400,image=TextFrame) 
SceneScreen.create_image(300,10,image=ObjectiveFrame)

countobj=1
class Obj:
    def __init__(self, img, x,y):
        self.img = PhotoImage(file=img)
        self.x = x
        self.y = y
        
    def create(self):
        SceneScreen.create_image(self.x, self.y, image=self.img)
        SceneScreen.pack()

    def active(self, n):
        def hovertrueobj():
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']='[Examine]'
                
        def hoverfalseobj():
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']=''
        
        def clicktrueobj(n, Obj_id):
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                global countobj
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
                        time.sleep(0.03)
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
                        time.sleep(0.03)
                    SceneScreen['state']='normal'
                    LineButton['state']='active'
                    TextBox['state']='active'
                countobj+=1
        Obj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
        SceneScreen.tag_bind(Obj_id, "<Enter>", lambda p: hovertrueobj())
        SceneScreen.tag_bind(Obj_id, "<Leave>", lambda p: hoverfalseobj())
        SceneScreen.tag_bind(Obj_id, "<Button-1>", lambda p: clicktrueobj(n,Obj_id))
        SceneScreen.pack(side='bottom')

Obj1=Obj("DeidMann.png", 310, 200)
Obj1.create()
Obj1.active(0)
Obj2=Obj("BurningCar.png", 510, 100)
Obj2.create()
Obj2.active(1)
Obj3=Obj("BloodyWrench.png", 210, 250)
#Obj3.create()
Obj3.active(2)

LineButton=ttk.Button(SceneScreen, text='     >     ')
ObjectiveBar = Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=200)

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
def next_line(): #For normal dialogue. To proceed, the button 'LineButton' is clicked. It gets 'disabled' or becomes unclickable while special events occur. Activates once over.
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
            SceneScreen['state']='disabled'
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
            SceneScreen['state']='normal'

LineButton["command"]=next_line

GameWindow.mainloop()
