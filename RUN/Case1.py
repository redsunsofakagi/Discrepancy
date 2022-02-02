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

main_dir = os.path.split(os.path.abspath(__file__))[0]
script_dir = os.path.join(main_dir, "Script")
font_dir = os.path.join(main_dir, "Fonts")
img1_dir= os.path.join(main_dir, "Images", "Case 1")


tutorial_file = open(os.path.join(script_dir, "MainTutorial.txt") , 'r')
tutorial_dialogue=tutorial_file.read() 
tutorial_list=tutorial_dialogue.split('\n\n')
font.add_file(os.path.join(font_dir,'SpecialElite-Regular.ttf'))
l1=[]
l2=[]
for i in range(len(tutorial_list)):
   tup1=tutorial_list[i].partition(': ')
   l1.append(tup1[0]) 
   l2.append(tup1[-1])
GameWindow= Tk()
global scr_w
scr_w=GameWindow.winfo_screenwidth()
global scr_h
scr_h=GameWindow.winfo_screenheight()
w=int((scr_w-780)/2)
s=int(scr_w/53.33333333333333)+56
w+=s
GameWindow.resizable(width=False, height=False)
GameWindow.title('Discrepancy')
GameWindow.geometry('600x500'+"-"+str(w)+"-"+str(int((scr_h/4.32))))
SceneScreen= Canvas(GameWindow, width=600, height=500)
TextFrame=PhotoImage(file=os.path.join(img1_dir,"textframe.png"))
SceneScreen=Canvas(GameWindow, width=600, height=500)
SceneScreen.create_image(300,400,image=TextFrame)
LineButton=ttk.Button(SceneScreen, text='     >     ')
LineButton.pack(side='bottom')
SceneScreen.create_window(300,480, window=LineButton)
SceneScreen.pack(side='bottom')
SpeakBox = Label(SceneScreen, text='', font=('Special Elite Regular', 13), foreground='white', background='black', wraplength=200)
SpeakBox.pack(side='bottom')
SceneScreen.create_window(300, 320, window=SpeakBox)
TextBox = ttk.Label(SceneScreen, text='', font=('Special Elite Regular', 14), foreground='white', background='black', wraplength=525)
TextBox.pack(side='left')
SceneScreen.create_window(300,400, window=TextBox)
class aObj:
   def __init__(self, img, x,y,):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def acreate(self):
      abase=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def aactive(self, speaker, dialogue, c):
      global p
      p=c
      def ahovertrueobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            SpeakBox['text']='[Examine]'
      def ahoverfalseobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
             SpeakBox['text']=''
      def aclicktrueobj(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            global acountobj
            acountobj+=1
            SceneScreen.delete(Obj_id)
            SceneScreen.pack()
            if acountobj<c:
               SpeakBox['text']=speaker
               TextBox['text']=''
               for j in dialogue:
                  SceneScreen['state']='disabled'
                  TextBox['text']+=j
                  TextBox.update()
                  TextBox.pack(side='left')
                  SceneScreen.create_window(300,400, window=TextBox)
                  SceneScreen.update()
                  SceneScreen.pack(side='bottom')
                  time.sleep(0.03)
               else:
                  SceneScreen['state']='normal'
            elif acountobj==c:
               SpeakBox['text']=speaker
               TextBox['text']=''
               for j in dialogue:
                  SceneScreen['state']='disabled'
                  TextBox['text']+=j
                  TextBox.update()
                  TextBox.pack(side='left')
                  SceneScreen.create_window(300,400, window=TextBox)
                  SceneScreen.update()
                  SceneScreen.pack(side='bottom')
                  time.sleep(0.03)
               else:
                  SceneScreen['state']='normal'
                  LineButton['state']='active'
                  TextBox['state']='active'
      aObj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(aObj_id, "<Enter>", lambda p: ahovertrueobj())
      SceneScreen.tag_bind(aObj_id, "<Leave>", lambda p: ahoverfalseobj())
      SceneScreen.tag_bind(aObj_id, "<Button-1>", lambda p: aclicktrueobj(speaker, dialogue, aObj_id))
      SceneScreen.pack(side='bottom')
class Obj:
   def __init__(self, img, x,y,):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def create(self):
      base=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def active(self, speaker, dialogue, c):
      global p
      p=c
      def hovertrueobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            SpeakBox['text']='[Examine]'
      def hoverfalseobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
             SpeakBox['text']=''
      def clicktrueobj(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            global countobj
            countobj+=1
            SceneScreen.delete(Obj_id)
            SceneScreen.pack()
            if countobj<c:
               SpeakBox['text']=speaker
               TextBox['text']=''
               for j in dialogue:
                  SceneScreen['state']='disabled'
                  TextBox['text']+=j
                  TextBox.update()
                  TextBox.pack(side='left')
                  SceneScreen.create_window(300,400, window=TextBox)
                  SceneScreen.update()
                  SceneScreen.pack(side='bottom')
                  time.sleep(0.03)
               else:
                  SceneScreen['state']='normal'
            elif countobj==c:
               SpeakBox['text']=speaker
               TextBox['text']=''
               for j in dialogue:
                  SceneScreen['state']='disabled'
                  TextBox['text']+=j
                  TextBox.update()
                  TextBox.pack(side='left')
                  SceneScreen.create_window(300,400, window=TextBox)
                  SceneScreen.update()
                  SceneScreen.pack(side='bottom')
                  time.sleep(0.03)
               else:
                  SceneScreen['state']='normal'
                  LineButton['state']='active'
                  TextBox['state']='active'
      Obj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(Obj_id, "<Enter>", lambda p: hovertrueobj())
      SceneScreen.tag_bind(Obj_id, "<Leave>", lambda p: hoverfalseobj())
      SceneScreen.tag_bind(Obj_id, "<Button-1>", lambda p: clicktrueobj(speaker, dialogue, Obj_id))
      SceneScreen.pack(side='bottom')
class Wit:
   def __init__(self, img, x,y):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def create(self):
      base=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def active(self, speaker, dialogue, c):
      global q
      q=c
      def hovertruewit():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and countobj==p:
            SpeakBox['text']='[Interrogate]'
      def hoverfalsewit():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and countobj==p:
             SpeakBox['text']=''
      def clicktruewit(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and countobj==p:
            global countwit
            countwit+=1
            SceneScreen.delete(Obj_id)
            SceneScreen.pack()
            if countwit<c:
               SpeakBox['text']=speaker
               TextBox['text']=''
               for j in dialogue:
                  SceneScreen['state']='disabled'
                  TextBox['text']+=j
                  TextBox.update()
                  TextBox.pack(side='left')
                  SceneScreen.create_window(300,400, window=TextBox)
                  SceneScreen.update()
                  SceneScreen.pack(side='bottom')
                  time.sleep(0.03)
               else:
                  SceneScreen['state']='normal'
            elif countwit==c:
               SpeakBox['text']=speaker
               TextBox['text']=''
               for j in dialogue:
                  SceneScreen['state']='disabled'
                  TextBox['text']+=j
                  TextBox.update()
                  TextBox.pack(side='left')
                  SceneScreen.create_window(300,400, window=TextBox)
                  SceneScreen.update()
                  SceneScreen.pack(side='bottom')
                  time.sleep(0.03)
               else:
                  SceneScreen['state']='normal'
                  LineButton['state']='active'
                  TextBox['state']='active'
      Obj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(Obj_id, "<Enter>", lambda p: hovertruewit())
      SceneScreen.tag_bind(Obj_id, "<Leave>", lambda p: hoverfalsewit())
      SceneScreen.tag_bind(Obj_id, "<Button-1>", lambda p: clicktruewit(speaker, dialogue, Obj_id))
      SceneScreen.pack(side='bottom')
Scene01=Obj(os.path.join(img1_dir,'C1S1.png'), 300,150)
Scene01.create()
countobj=0
countwit=0
acountobj=0
k=-1
m=-1
def next_line():
   global k
   global m
   k+=1
   m+=1
   if k<(len(l2)) and m<(len(l1)) :
      str1=l2[k]
      SpeakBox['text']=l1[m]
      TextBox['text']=''
      for j in str1:
         if str1=='[inv]':
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            break
         elif str1=="[open1]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Noose=Evi(os.path.join(img1_dir,'noose.png'),'Noose:\nA scruffily tied rope. Bears signs of a struggle.','The noose is probably the last thing I should show the kid...', False)
            Vase=Evi(os.path.join(img1_dir,'broken_vase(377x263).png'),'Vase:\nA cracked vase. Found it lying on the floor pointing to the backdoor.','Probably the cracking noise Maria heard... not out of the ordinary.', False)
            Door=Evi(os.path.join(img1_dir,'door(395x42).png'),'Backdoor:\nA rusty metal door. It was unlocked when I found it.','Exactly. Maria said she couldn\'t enter the building through the backdoor as it was locked from the inside. The autopsy team didn\'t leave through it either. So how did it get locked from the outside?', True)
            Noose.active()
            Vase.active()
            Door.active()
            break
         elif str1=="[open2]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Noose2=Evi(os.path.join(img1_dir,'noose.png'),'Noose:\nA scruffily tied rope. Bears signs of a struggle.','Where did this rope come from? Maria might know something.', True)
            Vase2=Evi(os.path.join(img1_dir,'broken_vase(377x263).png'),'Vase:\nA cracked vase. Found it lying on the floor pointing to the backdoor.','This is important but... I don\'t know what to ask Maria about it.', False)
            Door2=Evi(os.path.join(img1_dir,'door(395x42).png'),'Backdoor:\nA rusty metal door. It was unlocked when I found it.','This is important but... I don\'t know what to ask Maria about it.', False)
            Noose2.active()
            Vase2.active()
            Door2.active()
            break
         elif str1=="[open3]":
            pass
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('The struggle marks.', True)
            B=Opt('The tipped vase.', False)
            A.active()
            B.active()
            break
         elif str1=="[close]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            GameWindow.destroy()
            break
         elif str1=="[open4]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Rope=Evi(os.path.join(img1_dir,'noose.png'),'Rope:\nUsed to presumably strangle the victim. Was attached to the main doorbell.','A rope that was attached to the main doorbell, and used by many, many people.', True)
            Vase3=Evi(os.path.join(img1_dir,'broken_vase(377x263).png'),'Vase:\nA cracked vase. Found it lying on the floor pointing to the backdoor.','This doesn\'t make sense', False)
            Door3=Evi(os.path.join(img1_dir,'door(395x42).png'),'Backdoor:\nA rusty metal door. It was unlocked when I found it.','This doesn\'t make sense', False)
            Vase3.active()
            Door3.active()
            Rope.active()
            break
         elif str1=="[open5]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Rope2=Evi(os.path.join(img1_dir,'noose.png'),'Rope:\nUsed to presumably strangle the victim. Was attached to the main doorbell.','This doesn\'t make sense', False)
            Backdoor=Evi(os.path.join(img1_dir,'door(395x42).png'),'Backdoor:\nA rusty metal door. May have been used by the killer to escape..','A rarely used backdoor, huh? The handle might contain some useful fingerprints.', True)
            Vase4=Evi(os.path.join(img1_dir,'broken_vase(377x263).png'),'Vase:\nA cracked vase. Found it lying on the floor pointing to the backdoor.','This doesn\'t make sense', False)
            Backdoor.active()
            Rope2.active()
            Vase4.active()
            break
         elif str1=="[open6]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('The method.',False)
            B=Opt('The time frame.',False)
            C=Opt('The location.',False)
            D=Opt('Something else...',True)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=='[01]':
            global Scene01
            del Scene01
            global Scene1,Pers1,Wit1,Pers2,Obj1,Obj2,Obj3
            SceneScreen.update()
            Scene1=Obj(os.path.join(img1_dir,'1 actual.png'), 300,150)
            Scene1.create()
            SceneScreen.update()
            countobj=0
            countwit=0
            Pers1=Wit(os.path.join(img1_dir,"Locke.png"),500,250)
            Pers1.create()
            Wit1=Wit(os.path.join(img1_dir,'Maria.png'), 60, 250)
            Wit1.create()
            Wit1.active('Witness', '...',1)
            Pers2=Wit(os.path.join(img1_dir,'Antonnio.png'), 60, 150)
            Pers2.create()
            Obj1=Obj(os.path.join(img1_dir,"noose(278x137).png"), 310, 140)
            Obj1.create()
            Obj1.active('Jones', '(The noose... it bears the marks of a struggle... Shouldn\'t show this to the kid.)', 3)
            Obj2=Obj(os.path.join(img1_dir,"door(395x42).png"), 510, 100)
            Obj2.create()
            Obj2.active('Jones', '(The backdoor. It\'s... locked from the outside. Maybe the autopsy team left through here.)', 3)
            Obj3=Obj(os.path.join(img1_dir,"broken_vase(377x263).png"), 210, 250)
            Obj3.create()
            Obj3.active('Jones','(A vase that was knocked over presumably by the victim\'s feet. It\'s pointing towards the backdoor.)', 3)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[LEAVE_L]":
            del Scene1,Pers1,Wit1,Pers2,Obj1,Obj2,Obj3
            global Scene001,Wit01,Pers02,Obj01,Obj02,Obj03, acountobj
            acountobj=0
            SceneScreen.update()
            Scene001=Obj(os.path.join(img1_dir,'1 actual.png'), 300,150)
            Scene001.create()
            SceneScreen.update()
            countobj=0
            countwit=0
            Wit01=Wit(os.path.join(img1_dir,'Maria.png'), 60, 250)
            Wit01.create()
            Pers02=Wit(os.path.join(img1_dir,'Antonnio.png'), 60, 150)
            Pers02.create()
            Obj01=aObj(os.path.join(img1_dir,"noose(278x137).png"), 310, 140)
            Obj01.acreate()
            Obj01.aactive("Jones","(The noose.. If it was not a suicide, it shouldn\'t bear the signs of a struggle. Where did this rope come from?)",3)
            Obj02=aObj(os.path.join(img1_dir,"door(395x42).png"), 510, 100)
            Obj02.acreate()
            Obj02.aactive("Jones","(Of course, the backdoor. Who could have locked it?)",3)
            Obj03=aObj(os.path.join(img1_dir,"broken_vase(377x263).png"), 210, 250)
            Obj03.acreate()
            Obj03.aactive("Jones","(The vase... kicked by the suicide victim, or caught in the struggle between two people? It faces the backdoor, perhaps where our killer left from.)",3)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_L]":
            del Scene001,Wit01,Pers02,Obj01,Obj02,Obj03
            global Scene0001,Wit001,Pers002,Obj001,Obj002,Obj003,Pers01
            SceneScreen.update()
            Scene0001=Obj(os.path.join(img1_dir,'1 actual.png'), 300,150)
            Scene0001.create()
            SceneScreen.update()
            countobj=0
            countwit=0
            Pers01=Wit(os.path.join(img1_dir,"Locke.png"),500,250)
            Pers01.create()
            Wit001=Wit(os.path.join(img1_dir,'Maria.png'), 60, 250)
            Wit001.create()
            Pers002=Wit(os.path.join(img1_dir,'Antonnio.png'), 60, 150)
            Pers002.create()
            Obj001=Obj(os.path.join(img1_dir,"noose(278x137).png"), 310, 140)
            Obj001.create()
            Obj002=Obj(os.path.join(img1_dir,"door(395x42).png"), 510, 100)
            Obj002.create()
            Obj003=Obj(os.path.join(img1_dir,"broken_vase(377x263).png"), 210, 250)
            Obj003.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=='[02]':
            Scene2=Obj(os.path.join(img1_dir,"C1S3.png"),300,150)
            Scene2.create()
            SceneScreen.update()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=='[close]':
            GameWindow.destroy()
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
SceneScreen.pack(side='bottom')
def openlog():
    if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
        global menu, hover, second_frame, CaseText
        menu=Toplevel(GameWindow)
        menu.title('Case Log')
        menu.geometry('400x230'+"-"+str(w)+str(int((-(scr_h/4.32))-270)))
        menu.resizable(width=False, height=False)
        menu.grab_set()
        def disable():
            pass
        menu.protocol("WM_DELETE_WINDOW", disable)
        main_frame=Frame(menu)
        main_frame.pack(fill=BOTH, expand=1)
        evicanvas=Canvas(main_frame)
        evicanvas.pack(side=LEFT, fill=BOTH, expand=1)
        scroll=ttk.Scrollbar(main_frame, orient=VERTICAL, command=evicanvas.yview)
        scroll.pack(side=RIGHT, fill=Y, expand=False)
        evicanvas.configure(yscrollcommand=scroll.set)
        evicanvas.bind('<Configure>', lambda e: evicanvas.configure(scrollregion=evicanvas.bbox('all')))
        second_frame=Frame(evicanvas)
        evicanvas.create_window((0,0), window=second_frame, anchor='nw')
        CaseText=ttk.Label(second_frame, text='', font=('Special Elite Regular', 15), wraplength=300)
        hover=Balloon(menu)
class Evi:
    def __init__(self, img, desc, selec, check=None):
        self.img=PhotoImage(file=img)
        self.check=check
        self.desc=desc
        self.selec=selec
    def active(self):
        global main_frame, evicanvas, scroll
        str1= self.selec
        b=Button(second_frame, height=70, width=70)
        b['image']=self.img
        hover.bind_widget(b, balloonmsg=self.desc)
        CaseText.pack(side=RIGHT)
        b.pack(side='top')
        def click():
            if self.check:
                CaseText['text']=''
                for j in str1:
                    for k in second_frame.winfo_children():
                        k.configure(state='disable')
                        if isinstance(k, Button):
                            k.pack(side='top')
                        elif isinstance(k, Label):
                            k.pack(side=RIGHT)
                    CaseText['text']+=j
                    CaseText.update()
                    time.sleep(0.03)
                else:
                    time.sleep(1)
                    menu.grab_release()
                    menu.destroy()
                    LineButton['state']='active'
                    TextBox['state']='active'
            elif self.check==None:
                pass
            else:
                CaseText['text']=''
                for j in str1:
                    for k in second_frame.winfo_children():
                        k.configure(state='disable')
                        if isinstance(k, Button):
                            k.pack(side='top')
                        elif isinstance(k, Label):
                            k.pack(side=RIGHT)
                    CaseText['text']+=j
                    CaseText.update()
                    CaseText.pack(side=RIGHT)
                    time.sleep(0.03)
                else:
                    for k in second_frame.winfo_children():
                        k.configure(state='active')
                        if isinstance(k, Button):
                            k.pack(side='top')
                        elif isinstance(k, Label):
                            k.pack(side=RIGHT)
        b['command']=click
def openopt():
    if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
        global menu, hover, second_frame, CaseText
        menu=Toplevel(GameWindow)
        menu.title('Case Log')
        menu.geometry('400x228'+"-"+str(w)+str(int((-(scr_h/4.32))-272)))
        menu.resizable(width=False, height=False)
        menu.grab_set()
        def disable():
            pass
        menu.protocol("WM_DELETE_WINDOW", disable)
class Opt:
    def __init__(self, desc, check=None):
        self.check=check
        self.desc=desc
    def active(self):
        #global main_frame, evicanvas, scroll
        b=Button(menu, height=4, width=100, font=('Special Elite Regular', 9))
        b['text']=self.desc
        #CaseText.pack(side=RIGHT)
        b.pack(side='top')
        def click():
            if self.check:
                    time.sleep(1)
                    menu.grab_release()
                    menu.destroy()
                    LineButton['state']='active'
                    TextBox['state']='active'
            else:
                pass
        b['command']=click
class NoError(Exception):
   sys.tracebacklimit=0
GameWindow.mainloop()
