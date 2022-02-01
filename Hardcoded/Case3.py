from tkinter import *
from tkinter.tix import *
#from tkinter.font import Font
from tkinter import ttk
from PIL import Image, ImageTk
import time
#import threading
import sys
from pyglet import font
import os
#main_dir = os.path.split(os.path.abspath(__file__))[0]
tutorial_file = open("MainTutorial3.txt" , 'r')
tutorial_dialogue=tutorial_file.read() 
tutorial_list=tutorial_dialogue.split('\n\n')
font.add_file('SpecialElite-Regular.ttf')
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
TextFrame=PhotoImage(file="textframe.png")
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
class bObj:
   def __init__(self, img, x,y,):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def bcreate(self):
      bbase=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def bactive(self, speaker, dialogue, c):
      global p
      p=c
      def bhovertrueobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            SpeakBox['text']='[Examine]'
      def bhoverfalseobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
             SpeakBox['text']=''
      def bclicktrueobj(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            global bcountobj
            bcountobj+=1
            SceneScreen.delete(Obj_id)
            SceneScreen.pack()
            if bcountobj<c:
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
            elif bcountobj==c:
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
      bObj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(bObj_id, "<Enter>", lambda p: bhovertrueobj())
      SceneScreen.tag_bind(bObj_id, "<Leave>", lambda p: bhoverfalseobj())
      SceneScreen.tag_bind(bObj_id, "<Button-1>", lambda p: bclicktrueobj(speaker, dialogue, bObj_id))
      SceneScreen.pack(side='bottom')
class cObj:
   def __init__(self, img, x,y,):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def ccreate(self):
      cbase=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def cactive(self, speaker, dialogue, c):
      global p
      p=c
      def chovertrueobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            SpeakBox['text']='[Examine]'
      def choverfalseobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
             SpeakBox['text']=''
      def cclicktrueobj(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            global ccountobj
            ccountobj+=1
            SceneScreen.delete(Obj_id)
            SceneScreen.pack()
            if ccountobj<c:
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
            elif ccountobj==c:
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
      cObj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(cObj_id, "<Enter>", lambda p: chovertrueobj())
      SceneScreen.tag_bind(cObj_id, "<Leave>", lambda p: choverfalseobj())
      SceneScreen.tag_bind(cObj_id, "<Button-1>", lambda p: cclicktrueobj(speaker, dialogue, cObj_id))
      SceneScreen.pack(side='bottom')
class dObj:
   def __init__(self, img, x,y,):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def dcreate(self):
      dbase=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def dactive(self, speaker, dialogue, c):
      global p
      p=c
      def dhovertrueobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            SpeakBox['text']='[Examine]'
      def dhoverfalseobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
             SpeakBox['text']=''
      def dclicktrueobj(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            global dcountobj
            dcountobj+=1
            SceneScreen.delete(Obj_id)
            SceneScreen.pack()
            if dcountobj<c:
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
            elif dcountobj==c:
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
      dObj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(dObj_id, "<Enter>", lambda p: dhovertrueobj())
      SceneScreen.tag_bind(dObj_id, "<Leave>", lambda p: dhoverfalseobj())
      SceneScreen.tag_bind(dObj_id, "<Button-1>", lambda p: dclicktrueobj(speaker, dialogue, dObj_id))
      SceneScreen.pack(side='bottom')
class eObj:
   def __init__(self, img, x,y,):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def ecreate(self):
      ebase=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def eactive(self, speaker, dialogue, c):
      global p
      p=c
      def ehovertrueobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            SpeakBox['text']='[Examine]'
      def ehoverfalseobj():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
             SpeakBox['text']=''
      def eclicktrueobj(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
            global ecountobj
            ecountobj+=1
            SceneScreen.delete(Obj_id)
            SceneScreen.pack()
            if ecountobj<c:
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
            elif ecountobj==c:
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
      eObj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(eObj_id, "<Enter>", lambda p: ehovertrueobj())
      SceneScreen.tag_bind(eObj_id, "<Leave>", lambda p: ehoverfalseobj())
      SceneScreen.tag_bind(eObj_id, "<Button-1>", lambda p: eclicktrueobj(speaker, dialogue, eObj_id))
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
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and acountobj==p:
            SpeakBox['text']='[Interrogate]'
      def hoverfalsewit():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and acountobj==p:
             SpeakBox['text']=''
      def clicktruewit(speaker, dialogue, Obj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and acountobj==p:
            global countwit
            countwit+=1
            SceneScreen.delete(aObj_id)
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
      aObj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(aObj_id, "<Enter>", lambda p: hovertruewit())
      SceneScreen.tag_bind(aObj_id, "<Leave>", lambda p: hoverfalsewit())
      SceneScreen.tag_bind(aObj_id, "<Button-1>", lambda p: clicktruewit(speaker, dialogue, aObj_id))
      SceneScreen.pack(side='bottom')
class aWit:
   def __init__(self, img, x,y):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def acreate(self):
      abase=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def aactive(self, speaker, dialogue, c):
      global q
      q=c
      def ahovertruewit():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and acountobj==p:
            SpeakBox['text']='[Interrogate]'
      def ahoverfalsewit():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and acountobj==p:
             SpeakBox['text']=''
      def aclicktruewit(speaker, dialogue, aObj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and acountobj==p:
            global acountwit
            acountwit+=1
            SceneScreen.delete(aObj_id)
            SceneScreen.pack()
            if acountwit<c:
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
            elif acountwit==c:
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
      SceneScreen.tag_bind(aObj_id, "<Enter>", lambda p: ahovertruewit())
      SceneScreen.tag_bind(aObj_id, "<Leave>", lambda p: ahoverfalsewit())
      SceneScreen.tag_bind(aObj_id, "<Button-1>", lambda p: aclicktruewit(speaker, dialogue, aObj_id))
      SceneScreen.pack(side='bottom')
class dWit:
   def __init__(self, img, x,y):
      self.img = PhotoImage(file=img)
      self.x = x
      self.y = y
   def dcreate(self):
      abase=SceneScreen.create_image(self.x, self.y, image=self.img)
      SceneScreen.pack()
   def dactive(self, speaker, dialogue, c):
      global q
      q=c
      def dhovertruewit():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and dcountobj==p:
            SpeakBox['text']='[Interrogate]'
      def dhoverfalsewit():
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and dcountobj==p:
             SpeakBox['text']=''
      def dclicktruewit(speaker, dialogue, dObj_id):
         if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and dcountobj==p:
            global dcountwit
            dcountwit+=1
            SceneScreen.delete(dObj_id)
            SceneScreen.pack()
            if dcountwit<c:
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
            elif dcountwit==c:
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
      dObj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
      SceneScreen.tag_bind(dObj_id, "<Enter>", lambda p: dhovertruewit())
      SceneScreen.tag_bind(dObj_id, "<Leave>", lambda p: dhoverfalsewit())
      SceneScreen.tag_bind(dObj_id, "<Button-1>", lambda p: dclicktruewit(speaker, dialogue, dObj_id))
      SceneScreen.pack(side='bottom')
Scene9=Obj('Room.png', 300,150)
Scene9.create()
Door02=Obj("door2.png",510,100)
Door02.create()
Pho=Obj("frame.png",200,30)
Pho.create()
countobj=0
countwit=0
acountobj=0
acountwit=0
bcountobj=0
ccountobj=0
dcountobj=0
dcountwit=0
ecountobj=0
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
            Body=Evi('Homen.png','Body:\nThe body of the minister. Electrocuted.','Approaching the body makes perfect sense...', False)
            bill=Evi('Bill.png','Bill:\nAn electric bill with the ministry\'s emblem on it. Laden with Joanne\'s fingerprints.','The bill wouldn\'t seem out of place..', False)
            puddle=Evi('Puddle_1.png','Puddle:\nWater that was spilled...','This doesn\'t seem out of place..', False)
            wires=Evi("Wires.png","Wires:\nDrawn from the outlet within the room. Laden with Joanne\'s fingerprints.","Wouldn't Charles have gotten electrocuted as well?",True)
            Body.active()
            bill.active()
            puddle.active()
            wires.active()
            break
         elif str1=="[opt1]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('The bill.', False)
            B=Opt('The puddle.', False)
            C=Opt("The wires.", False)
            D=Opt("The fingerprints themselves.",True)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[opt2]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt("'Our theory is that she wanted to\nframe it as an electrical accident'", True)
            B=Opt("'Perhaps under that pretence,\nshe called up electrical, and they left behind a bill.'", False)
            C=Opt("'Her intention was to frame it as an accident.\nIt\'s true that the building\nhas been facing power issues of late...'", False)
            D=Opt("'The point is, the only person who had the\nopportunity to set it up was our friendly secretary.'",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[opt3]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('How did Joanne enter?', False)
            B=Opt('How did Charles enter?', True)
            C=Opt("How did Homen enter?", False)
            D=Opt("How did I enter?",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[open2]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            plate=Evi('Plate.png','Plate:\nA single plate.','Someone had to have been waiting here... eating snacks alone. Sounds fun.', True)
            snacks=Evi('Fish.png','Snacks:\nAn assortment of snacks. Barely touched.','Meeting snacks. They seem uneaten, so it\'s not out of place...', True)
            mess=Evi('File Open.png','Messy Files:\nSprawled out on a table. Contains a list of people.','Hm.. if there was no one here, who arranged the files like this?', True)
            plate.active()
            snacks.active()
            mess.active()
            break
         elif str1=="[opt4]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('The number of snack sellers.', False)
            B=Opt('The number of files in the Ministry.', False)
            C=Opt("The number of fingerprint tests taken.", True)
            D=Opt("The number of loners in the Ministry.",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[opt5]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('During Charles\' Accusation.', True)
            B=Opt('During the first investigation.', False)
            C=Opt("During my long sleep......z..z..z..zzz",False)
            D=Opt("During Joanne\'s interrogation.",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[opt6]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('Examine Homen\'s Office.', False)
            B=Opt('Examine Charles\' Ministry Office.', True)
            C=Opt("Examine the Outside.", False)
            D=Opt("Examine my apartment.",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[opt7]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('The files the minister was looking for?', True)
            B=Opt('The snacks?', False)
            C=Opt("The plate?", False)
            D=Opt("The electrical bill?",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[open3]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Body1=Evi('Homen.png','Body:\nThe body of the minister. Electrocuted.','This is brutal...', False)
            vip=Evi('VIP Pass.png','VIP Slip:\nAllows the bearer free access to the building facilities. Only one issued.','Only one found. Not four.', True)
            puddle1=Evi('Puddle_1.png','Puddle:\nWater that was spilled...','What\'s the smell...?', False)
            wires1=Evi("Wires.png","Wires:\nDrawn from the outlet within the room. Laden with Joanne\'s fingerprints.","This is brutal...",False)
            Body1.active()
            vip.active()
            puddle1.active()
            wires1.active()
            break
         elif str1=="[opt8]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('Your office.', True)
            B=Opt('Homen\'s office.', False)
            C=Opt("On the plate.", False)
            D=Opt("Outside the ministry.",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[open4]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            plate1=Evi('Plate.png','Plate:\nA single plate.','This doesn\'t seem right....', False)
            snacks1=Evi('Fish.png','Snacks:\nAn assortment of snacks. Barely touched.','This doesn\'t seem right....', False)
            mess1=Evi('File Open.png','Messy Files:\nSprawled out on a table. Contains a list of people.','A massive list of people.. Which makes no sense without context. One would need an introduction.', True)
            plate1.active()
            snacks1.active()
            mess1.active()
            break
         elif str1=="[open5]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            cover=Evi("File Signed.png","Cover File:\nThe file the minister was looking for. Found on Charles' desk.","Probably the context. A cover explaining the details of the list that was to follow.",True)
            gloves=Evi("Gloves.png","Gloves:\nLatex gloves. Found in Charles\' office.","Caught these on the coat rack.",False)
            cover.active()
            gloves.active()
            break
         elif str1=="[opt9]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('I should give up...', False)
            B=Opt('It\'s a question of when.', False)
            C=Opt("It's a question of how.", False)
            D=Opt("It's not a question of how.",True)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[opt10]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('He\'s a serial killer.', False)
            B=Opt('He hates the Minister.', False)
            C=Opt("He couldn't let the minister see the file.", True)
            D=Opt("He wanted to know more about electricity.",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[open6]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            cover1=Evi("File Signed.png","Cover File:\nThe file the minister was looking for. Found on Charles\' desk.","These don't make sense",False)
            gloves1=Evi("Gloves.png","Gloves:\nLatex gloves. Found in Charles\' office.","Caught these on the coat rack.",True)
            vip2=Evi('VIP Pass.png','VIP Slip:\nAllows the bearer free access to the building facilities. Only one issued.','This is useless  now...', False)
            vip2.active()
            cover1.active()
            gloves1.active()
            break
         elif str1=="[opt11]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('Herself.', False)
            B=Opt('Me.', False)
            C=Opt("Charles.", True)
            D=Opt("Locke.",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[opt12]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('The Government.', False)
            B=Opt('My friends.', False)
            C=Opt("The Jury.", True)
            D=Opt("The Illuminati.",False)
            A.active()
            B.active()
            C.active()
            D.active()
            break
         elif str1=="[open7]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            cover2=Evi("File Signed.png","Cover File:\nThe file the minister was looking for. Found on Charles\' desk.","I would check it out, but.. Charles took it from me. The bureau wouldn't let me keep a copy...",False)
            mess2=Evi('File Open.png','Messy Files:\nSprawled out on a table. Contains a list of people.','This list was the second part of the file, right?', True)
            cover2.active()
            mess2.active()
            break
         elif str1=="[open8]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Body2=Evi('Homen.png','Body:\nThe body of the minister. Electrocuted.','This didn\'t have the smell...', False)
            vip1=Evi('VIP Pass.png','VIP Slip:\nAllows the bearer free access to the building facilities. Only one issued.','This didn\'t have the smell...', False)
            puddle2=Evi('Puddle_1.png','Puddle:\nWater(?) that was spilled. Has a flowery scent.','This.. it was at the crime scene...!', True)
            wires2=Evi("Wires.png","Wires:\nDrawn from the outlet within the room. Laden with Joanne\'s fingerprints.","This didn\'t have the smell...",False)
            Body2.active()
            vip1.active()
            puddle2.active()
            wires2.active()
            break
         elif str1=="[opt13]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt1('Join.', 1)
            B=Opt1('Arrest.', 2)
            A.active1()
            B.active1()
            break
         elif str1=="[close]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            GameWindow.destroy()
            break
         elif str1=='[ENTER_Locke]':
            global Scene9,Door02,Pho
            del Scene9,Door02,Pho
            global Door_2,Pho1,Scene09
            SceneScreen.update()
            Scene09=Obj('Room.png', 300,150)
            Scene09.create()
            Door_2=Obj("door2.png",510,100)
            Door_2.create()
            Door_2.active("Jones","(Door... opening it before whoever on the other side knocks again...)",2)
            Pho1=Obj("frame.png",200,30)
            Pho1.create()
            Pho1.active("Jones","(A photograph of Joanne and I... Despite the war, we found each other... Wait, I should open the door...!)",2)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=='[ENTER_Locke1]':
            del Door_2,Pho1,Scene09
            global Scene009,Door__2,Locke,Pho_
            SceneScreen.update()
            Scene009=Obj('Room.png', 300,150)
            Scene009.create()
            Door__2=Obj("door2.png",510,100)
            Door__2.create()
            Locke=Wit("Locke.png",510,250)
            Locke.create()
            Pho_=Obj("frame.png",200,30)
            Pho_.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=='[10]':
            del Door__2,Pho_,Scene009
            global Scene10,Locke1,Homen,Wires,Puddle,Bill
            SceneScreen.update()
            Scene10=Obj('Homen Office.png', 300,150)
            Scene10.create()
            Locke1=Wit("Locke.png",510,250)
            Locke1.create()
            Puddle=Obj("Puddle.png",420,160)
            Puddle.create()
            Wires=Obj("Wires.png",430,100)
            Wires.create()
            Homen=Obj("Homen.png",330,100)
            Homen.create()
            Bill=Obj("Bill.png",220,270)
            Bill.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_CH]":
            del Scene10,Locke1,Homen,Wires,Puddle,Bill
            global Scene010,Charles,Locke01,Homen1,Wires1,Puddle1,Bill1
            SceneScreen.update()
            Scene010=Obj('Homen Office.png', 300,150)
            Scene010.create()
            Locke01=Wit("Locke.png",510,250)
            Locke01.create()
            Charles=Wit("Charles-removebg-preview.png",300,250)
            Charles.create()
            Puddle1=aObj("Puddle.png",420,160)
            Puddle1.acreate()
            Wires1=aObj("Wires.png",430,100)
            Wires1.acreate() 
            Bill1=aObj("Bill.png",220,270)
            Bill1.acreate()
            Homen1=aObj("Homen.png",330,100)
            Homen1.acreate()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_Jo]":
            del Scene010,Charles,Locke01,Homen1,Wires1,Puddle1,Bill1
            global Scene0010,Charles01,Locke001,Homen01,Wires01,Puddle01,Joanne,Bill01
            SceneScreen.update()
            Scene0010=Obj('Homen Office.png', 300,150)
            Scene0010.create()
            Locke001=Wit("Locke.png",510,250)
            Locke001.create()
            Charles01=Wit("Charles-removebg-preview.png",300,250)
            Charles01.create()
            Charles01.active('Jones', "When did the death of the victim occur?",1)
            Puddle01=aObj("Puddle.png",420,160)
            Puddle01.acreate()
            Puddle01.aactive("Charles","Water, spilt just below the minister\'s side of the table. There are wires next to it. Definitely a safety violation, mm?",4)
            Wires01=aObj("Wires.png",430,100)
            Wires01.acreate()
            Wires01.aactive("Charles","Spotted those, have we? Those wires were drawn from the outlet, which is almost directly connected to the mains.",4)
            Bill01=aObj("Bill.png",220,270)
            Bill01.aactive("Charles","Ah, the electrical bill! Something about erratic voltage. I wonder what it could mean...",4)
            Homen01=aObj("Homen.png",330,100)
            Homen01.acreate()
            Homen01.aactive("Charles","Of course, the elephant in the room. The body of Minister Homen Ofobia. Slumped over his chair, he was electrocuted.",4)
            Joanne=Obj("Joanne.png",90,250)
            Joanne.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[11]":
            del Scene0010,Charles01,Locke001,Homen01,Wires01,Puddle01,Joanne,Bill01
            global Scene11,Locke11,Joanne1
            SceneScreen.update()
            Scene11=Obj("Outside Ministry.png",300,150)
            Scene11.create()
            Locke11=Wit("Locke.png",510,250)
            Locke11.create()
            Joanne1=aWit("Joanne.png",310,250)
            Joanne1.acreate()
            Joanne1.aactive("Joanne", 'The boss is.. Well, was, a bit of a perfectionist. Before leaving for today\'s meeting he asked me to "rearrange" the wiring to his taste.' ,1)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[12]":
            del Scene11,Locke11,Joanne1
            global Locke12,Joanne12,Scene12,Plate,Fish,File
            SceneScreen.update()
            Scene12=Obj("Meeting.png",300,150)
            Scene12.create()
            Plate=bObj("Plate.png",430,100)
            Plate.bcreate()
            Fish=bObj("Fish.png",360,100)
            Fish.bcreate()
            File=bObj("File Open.png",300,100)
            File.bcreate()
            Locke12=Wit("Locke.png",510,250)
            Locke12.create()
            Joanne12=Wit("Joanne.png",90,250)
            Joanne12.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[EXIT_Lo]":
            del Locke12,Joanne12,Scene12,Plate,Fish,File
            global Joanne012,Scene012,Plate12,Fish12,File12
            SceneScreen.update()
            Scene012=Obj("Meeting.png",300,150)
            Scene012.create()
            Joanne012=Wit("Joanne.png",90,250)
            Joanne012.create()
            Plate12=bObj("Plate.png",430,100)
            Plate12.bcreate()
            Plate12.bactive("Jones","(A single plate. Whoever was waiting here must\'ve gotten hungry...)",3)
            Fish12=bObj("Fish.png",360,100)
            Fish12.bcreate()
            Fish12.bactive("Jones","(A bunch of peanuts, fish and chips... Barely any of the snacks have been eaten.)",3)
            File12=bObj("File Open.png",300,100)
            File12.bcreate()
            File12.bactive("Jones","(Contents of a file sprawled out on a table... It lists a bunch of people... But there\'s no context to it.)",3)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[LOCKE ENTERS]":
            del Joanne012,Scene012,Plate12,Fish12,File12
            global Joanne0012,Scene0012,Plate012,Fish012,File012,Locke012
            SceneScreen.update()
            Scene0012=Obj("Meeting.png",300,150)
            Scene0012.create()
            Joanne0012=Wit("Joanne.png",90,250)
            Joanne0012.create()
            Locke012=Wit("Locke.png",510,250)
            Locke012.create()
            Plate012=bObj("Plate.png",430,100)
            Plate012.bcreate()
            Fish012=bObj("Fish.png",360,100)
            Fish012.bcreate()
            File012=bObj("File Open.png",300,100)
            File012.bcreate()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[EXIT_L2]":
            del Joanne0012,Scene0012,Plate012,Fish012,File012,Locke012
            global Joanne00012,Scene00012,Plate0012,Fish0012,File0012
            SceneScreen.update()
            Scene00012=Obj("Meeting.png",300,150)
            Scene00012.create()
            Joanne00012=Wit("Joanne.png",90,250)
            Joanne00012.create()
            Plate0012=bObj("Plate.png",430,100)
            Plate0012.bcreate()
            Fish0012=bObj("Fish.png",360,100)
            Fish0012.bcreate()
            File0012=bObj("File Open.png",300,100)
            File0012.bcreate()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[LOCKE ENTERS2]":
            del Joanne00012,Scene00012,Plate0012,Fish0012,File0012
            global Joanne000012,Scene000012,Plate00012,Fish00012,File00012,Locke0012
            SceneScreen.update()
            Scene000012=Obj("Meeting.png",300,150)
            Scene000012.create()
            Joanne000012=Wit("Joanne.png",90,250)
            Joanne000012.create()
            Plate00012=bObj("Plate.png",430,100)
            Plate00012.bcreate()
            Fish00012=bObj("Fish.png",360,100)
            Fish00012.bcreate()
            File00012=bObj("File Open.png",300,100)
            File00012.bcreate()
            Locke0012=Wit("Locke.png",510,250)
            Locke0012.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[13]":
            del Joanne000012,Scene000012,Plate00012,Fish00012,File00012,Locke0012
            global Joanne13,Scene13,Locke13,Sign,Hanger,Gloves,things
            SceneScreen.update()
            Scene13=Obj("Charles Room.png",300,150)
            Scene13.create()
            Joanne13=Wit("Joanne.png",90,250)
            Joanne13.create()
            Locke13=Wit("Locke.png",510,250)
            Locke13.create()
            things=Obj("things.png",263,140)
            things.create()
            Sign=cObj("File Signed.png",300,115)
            Sign.ccreate()
            Sign.cactive("Jones",'(Standard office supplies... records, and... a file? It looks like a cover page...Contains the victim\'s signature..)',2)
            Hanger=cObj("Hanger.png",510,120)
            Hanger.ccreate()
            Hanger.cactive("Jones","(A coat rack. Nothing on it except.. A pair of gloves... This doesn\'t look good.)",2)
            Gloves=Obj("Gloves.png",505,80)
            Gloves.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[14]":
            del Joanne13,Scene13,Locke13,Sign,Hanger,Gloves,things
            global Scene14,Locke14,Charles14,Puddle14,Wires14,Homen14,Joanne14
            SceneScreen.update()
            Scene14=Obj('Homen Office.png', 300,150)
            Scene14.create()
            Locke14=Wit("Locke.png",510,250)
            Locke14.create()
            Charles14=dWit("Charles-removebg-preview.png",300,250)
            Charles14.dcreate()
            Charles14.dactive('Jones', 'Captain. Have you seen this file before?',1)
            Puddle14=dObj("Puddle.png",420,160)
            Puddle14.dcreate()
            Puddle14.dactive("Jones",'(The puddle... I didn\'t notice it before, but it has a sweet smell. Flowers?)',1)
            Wires14=aObj("Wires.png",430,100)
            Wires14.acreate()
            Homen14=aObj("Homen.png",330,100)
            Homen14.acreate()
            Joanne14=Obj("Joanne.png",90,250)
            Joanne14.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[15]":
            del Scene14,Locke14,Charles14,Puddle14,Wires14,Homen14,Joanne14
            global Scene15
            SceneScreen.update()
            Scene15=Obj("Charles Demon.png",300,150)
            Scene15.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[16]":
            del Scene15
            global Scene16,Joanne16,Door16,Pho16
            SceneScreen.update()
            Scene16=Obj("Room.png",300,150)
            Scene16.create()
            Joanne16=Wit("Joanne.png",150,160)
            Joanne16.create()
            Door16=Obj("door2.png",510,100)
            Door16.create()
            Pho16=Obj("frame.png",200,30)
            Pho16.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[17]":
            del Scene16,Joanne16
            global Scene17
            Scene17=Obj("James House.png",300,150)
            Scene17.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[18]":
            del Scene17
            global Scene18,perfume,Books,Hang
            Scene18=Obj("Living Room.png",300,150)
            Scene18.create()
            perfume=eObj("perfume.png",300,150)
            perfume.ecreate()
            perfume.eactive("Jones","(An empty perfume bottle...? \"L'Essence de Lavande\"... Lavender perfume, I guess.)",3)
            Books=eObj("Books.png",183,125)
            Books.ecreate()
            Books.eactive("Jones","(Books, books and more books... hm? There's a file open on top. Looks.. familiar.)",3)
            Hang=eObj("Hanger James.png",510,150)
            Hang.ecreate()
            Hang.eactive("Jones","(A hanger with... an odd assortment of clothing. There's a mailman's hat, what looks like a bartender's uniform and... a janitor's outfit.)",3)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[19]":
            del Scene18,perfume,Books,Hang
            global Scene19,Pers1i,Wit1i,Pers2i,Obj1i,Obj2i,Obj3i
            SceneScreen.update()
            Scene19=Obj('1 actual.png', 300,150)
            Scene19.create()
            SceneScreen.update()
            Pers1i=Wit("Locke.png",500,250)
            Pers1i.create()
            Wit1i=Wit('Maria.png', 60, 250)
            Wit1i.create()
            Pers2i=Wit('Antonnio.png', 60, 150)
            Pers2i.create()
            Obj1i=Obj("noose(278x137).png", 310, 140)
            Obj1i.create()
            Obj2i=Obj("door(395x42).png", 510, 100)
            Obj2i.create()
            Obj3i=Obj("broken_vase(377x263).png", 210, 250)
            Obj3i.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[20]":
            del Scene19,Pers1i,Wit1i,Pers2i,Obj1i,Obj2i,Obj3i
            global Scene5j,Obj1_5,Obj2_5,Obj3_5,Pers_L1
            SceneScreen.update()
            Scene5j=Obj('Scene5.png', 300,150)
            Scene5j.create()
            SceneScreen.update()
            Obj1_5=Obj("Road.png",300,150)
            Obj1_5.create()
            Obj2_5=Obj("Cars_11.png",300,160)
            Obj2_5.create()
            Obj3_5=Obj("Note1.png",400,140)
            Obj3_5.create()
            Pers_L1=Wit("Locke.png",460,100)
            Pers_L1.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[21]":
            del Scene5j,Obj1_5,Obj2_5,Obj3_5,Pers_L1
            global Scene21,perfume21,Books21,Hang21
            Scene21=Obj("Living Room.png",300,150)
            Scene21.create()
            perfume21=eObj("perfume.png",300,150)
            perfume21.ecreate()
            Books21=eObj("Books.png",183,125)
            Books21.ecreate()
            Hang21=eObj("Hanger James.png",510,150)
            Hang21.ecreate()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[22]":
            del Scene21,perfume21,Books21,Hang21
            global Scene22,Wit22,Pers22,Obj221,Obj222,Obj223
            SceneScreen.update()
            Scene22=Obj('1 actual.png', 300,150)
            Scene22.create()
            SceneScreen.update()
            Wit22=Wit('Maria.png', 60, 250)
            Wit22.create()
            Pers22=Wit('Antonnio.png', 60, 150)
            Pers22.create()
            Obj221=Obj("noose(278x137).png", 310, 140)
            Obj221.create()
            Obj222=Obj("door(395x42).png", 510, 100)
            Obj222.create()
            Obj223=Obj("broken_vase(377x263).png", 210, 250)
            Obj223.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[23]":
            del Scene22,Wit22,Pers22,Obj221,Obj222,Obj223
            global Scene23,Zimmer23
            Scene23=Obj("Scene7.png",300,150)
            Scene23.create()
            Zimmer23=Wit("Zimmerman.png",310,250)
            Zimmer23.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[24]":
            del Scene23,Zimmer23
            global Joanne24,Scene24,Plate24,Fish24,File24
            SceneScreen.update()
            Scene24=Obj("Meeting.png",300,150)
            Scene24.create()
            Joanne24=Wit("Joanne.png",90,250)
            Joanne24.create()
            Plate24=bObj("Plate.png",430,100)
            Plate24.bcreate()
            Fish24=bObj("Fish.png",360,100)
            Fish24.bcreate()
            File24=bObj("File Open.png",300,100)
            File24.bcreate()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[25]":
            del Joanne24,Scene24,Plate24,Fish24,File24
            global Scene25,perfume25,Books25,Hang25
            Scene25=Obj("Living Room.png",300,150)
            Scene25.create()
            perfume25=eObj("perfume.png",300,150)
            perfume25.ecreate()
            Books25=eObj("Books.png",183,125)
            Books25.ecreate()
            Hang25=eObj("Hanger James.png",510,150)
            Hang25.ecreate()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER JAMES]":
            del Scene25,perfume25,Books25,Hang25
            Scene25_=Obj("Living Room.png",300,150)
            Scene25_.create()
            perfume25_=eObj("perfume.png",300,150)
            perfume25_.ecreate()
            Books25_=eObj("Books.png",183,125)
            Books25_.ecreate()
            Hang25_=eObj("Hanger James.png",510,150)
            Hang25_.ecreate()
            James25=Wit("James.png",100,250)
            James25.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
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
class Opt1:
    def __init__(self, desc, func):
        self.func=func
        self.desc=desc
    def active1(self):
        #global main_frame, evicanvas, scroll
        b=Button(menu, height=4, width=100, font=('Special Elite Regular', 9))
        b['text']=self.desc
        #CaseText.pack(side=RIGHT)
        b.pack(side='top')
        def click1():
            if self.func==1:
                     time.sleep(1)
                     menu.grab_release()
                     menu.destroy()
                     LineButton['state']='active'
                     TextBox['state']='active'
                     GameWindow.destroy()
                     main_dir1= os.path.split(os.path.abspath(__file__))[0]
                     tutorial_file1= open("A.txt" , 'r')
                     tutorial_dialogue1=tutorial_file1.read() 
                     tutorial_list1=tutorial_dialogue1.split('\n\n')
                     font.add_file('SpecialElite-Regular.ttf')
                     l11=[]
                     l21=[]
                     for i in range(len(tutorial_list1)):
                        tup11=tutorial_list1[i].partition(': ')
                        l11.append(tup11[0]) 
                        l21.append(tup11[-1])
                     GameWindow1= Tk()
                     global scr_w
                     scr_w=GameWindow1.winfo_screenwidth()
                     global scr_h
                     scr_h=GameWindow1.winfo_screenheight()
                     w=int((scr_w-780)/2)
                     s=int(scr_w/53.33333333333333)+56
                     w+=s
                     GameWindow1.resizable(width=False, height=False)
                     GameWindow1.title('End')
                     GameWindow1.geometry('600x500'+"-"+str(w)+"-"+str(int((scr_h/4.32))))
                     SceneScreen1= Canvas(GameWindow1, width=600, height=500)
                     TextFrame1=PhotoImage(file="textframe.png")
                     SceneScreen1=Canvas(GameWindow1, width=600, height=500)
                     SceneScreen1.create_image(300,400,image=TextFrame1)
                     LineButton1=ttk.Button(SceneScreen1, text='     >     ')
                     LineButton1.pack(side='bottom')
                     SceneScreen1.create_window(300,480, window=LineButton1)
                     SceneScreen1.pack(side='bottom')
                     SpeakBox1= Label(SceneScreen1, text='', font=('Special Elite Regular', 13), foreground='white', background='black', wraplength=200)
                     SpeakBox1.pack(side='bottom')
                     SceneScreen1.create_window(300, 320, window=SpeakBox1)
                     TextBox1= ttk.Label(SceneScreen1, text='', font=('Special Elite Regular', 14), foreground='white', background='black', wraplength=525)
                     TextBox1.pack(side='left')
                     SceneScreen1.create_window(300,400, window=TextBox1)
                     class Obj1:
                        def __init__(self, img, x,y,):
                           self.img = PhotoImage(file=img)
                           self.x = x
                           self.y = y
                        def create1(self):
                           base1=SceneScreen1.create_image(self.x, self.y, image=self.img)
                           SceneScreen1.pack()
                        def active1(self, speaker, dialogue, c):
                           global p
                           p=c
                           def hovertrueobj1():
                              if TextBox1.instate(['disabled'])==True and LineButton1.instate(['disabled'])==True:
                                 SpeakBox1['text']='[Examine]'
                           def hoverfalseobj1():
                              if TextBox1.instate(['disabled'])==True and LineButton1.instate(['disabled'])==True:
                                  SpeakBox1['text']=''
                           def clicktrueobj(speaker, dialogue, Obj_id1):
                              if TextBox.instate(['disabled'])==True and LineButton1.instate(['disabled'])==True:
                                 nonlocal countobj1
                                 countobj1+=1
                                 SceneScreen1.delete(Obj_id1)
                                 SceneScreen1.pack()
                                 if countobj1<c:
                                    SpeakBox1['text']=speaker
                                    TextBox1['text']=''
                                    for j in dialogue:
                                       SceneScreen1['state']='disabled'
                                       TextBox1['text']+=j
                                       TextBox1.update()
                                       TextBox1.pack(side='left')
                                       SceneScreen1.create_window(300,400, window=TextBox1)
                                       SceneScreen1.update()
                                       SceneScreen1.pack(side='bottom')
                                       time.sleep(0.03)
                                    else:
                                       SceneScreen1['state']='normal'
                                 elif countobj1==c:
                                    SpeakBox1['text']=speaker
                                    TextBox1['text']=''
                                    for j in dialogue:
                                       SceneScreen1['state']='disabled'
                                       TextBox1['text']+=j
                                       TextBox1.update()
                                       TextBox1.pack(side='left')
                                       SceneScreen1.create_window(300,400, window=TextBox1)
                                       SceneScreen1.update()
                                       SceneScreen1.pack(side='bottom')
                                       time.sleep(0.03)
                                    else:
                                       SceneScreen1['state']='normal'
                                       LineButton1['state']='active'
                                       TextBox1['state']='active'
                           Obj_id1= SceneScreen1.create_image(self.x,self.y, image=self.img)
                           SceneScreen1.tag_bind(Obj_id1, "<Enter>", lambda p: hovertrueobj1())
                           SceneScreen1.tag_bind(Obj_id1, "<Leave>", lambda p: hoverfalseobj1())
                           SceneScreen1.tag_bind(Obj_id1, "<Button-1>", lambda p: clicktrueobj1(speaker, dialogue, Obj_id1))
                           SceneScreen1.pack(side='bottom')
                     letter1=Obj1("Letter.png",300,150)
                     letter1.create1()
                     countobj1=0
                     k1=-1
                     m1=-1
                     def next_line1():
                         nonlocal k1,m1
                         k1+=1
                         m1+=1
                         if k1<(len(l21)) and m1<(len(l11)) :
                            str11=l21[k1]
                            SpeakBox1['text']=l11[m1]
                            TextBox1['text']=''
                            for j in str11:
                                 if str11=="[openend]":
                                     TextBox1['state']='disabled'
                                     LineButton1['state']='disabled'
                                     End1=Obj1("End 1.png",300,150)
                                     End1.create1()
                                     SceneScreen1.update()
                                     SceneScreen1.pack()
                                     raise NoError
                                 LineButton1['state']='disabled'
                                 TextBox1['text']+=j
                                 TextBox1.update()
                                 TextBox1.pack(side='left')
                                 SceneScreen1.create_window(300,400, window=TextBox1)
                                 SceneScreen1.update()
                                 SceneScreen1.pack(side='bottom')
                                 time.sleep(0.03)
                            else:
                                 LineButton1['state']='active'    
                     LineButton1["command"]=next_line1
                     SceneScreen1.pack(side='bottom')
                     class NoError(Exception):
                        sys.tracebacklimit=0
                     GameWindow1.mainloop()
            elif self.func==2:
                     time.sleep(1)
                     menu.grab_release()
                     menu.destroy()
                     LineButton['state']='active'
                     TextBox['state']='active'
                     GameWindow.destroy()
                     main_dir1= os.path.split(os.path.abspath(__file__))[0]
                     tutorial_file1= open("B.txt" , 'r')
                     tutorial_dialogue1=tutorial_file1.read() 
                     tutorial_list1=tutorial_dialogue1.split('\n\n')
                     font.add_file('SpecialElite-Regular.ttf')
                     l11=[]
                     l21=[]
                     for i in range(len(tutorial_list1)):
                        tup11=tutorial_list1[i].partition(': ')
                        l11.append(tup11[0]) 
                        l21.append(tup11[-1])
                     GameWindow1= Tk()
                     global scr_w1
                     scr_w1=GameWindow1.winfo_screenwidth()
                     global scr_h1
                     scr_h1=GameWindow1.winfo_screenheight()
                     w=int((scr_w-780)/2)
                     s=int(scr_w/53.33333333333333)+56
                     w+=s
                     GameWindow1.resizable(width=False, height=False)
                     GameWindow1.title('End')
                     GameWindow1.geometry('600x500'+"-"+str(w)+"-"+str(int((scr_h/4.32))))
                     SceneScreen1= Canvas(GameWindow1, width=600, height=500)
                     TextFrame1=PhotoImage(file="textframe.png")
                     SceneScreen1=Canvas(GameWindow1, width=600, height=500)
                     SceneScreen1.create_image(300,400,image=TextFrame1)
                     LineButton1=ttk.Button(SceneScreen1, text='     >     ')
                     LineButton1.pack(side='bottom')
                     SceneScreen1.create_window(300,480, window=LineButton1)
                     SceneScreen1.pack(side='bottom')
                     SpeakBox1= Label(SceneScreen1, text='', font=('Special Elite Regular', 13), foreground='white', background='black', wraplength=200)
                     SpeakBox1.pack(side='bottom')
                     SceneScreen1.create_window(300, 320, window=SpeakBox1)
                     TextBox1= ttk.Label(SceneScreen1, text='', font=('Special Elite Regular', 14), foreground='white', background='black', wraplength=525)
                     TextBox1.pack(side='left')
                     SceneScreen1.create_window(300,400, window=TextBox1)
                     class Obj1:
                        def __init__(self, img, x,y,):
                           self.img = PhotoImage(file=img)
                           self.x = x
                           self.y = y
                        def create1(self):
                           base1=SceneScreen1.create_image(self.x, self.y, image=self.img)
                           SceneScreen1.pack()
                        def active1(self, speaker, dialogue, c):
                           global p
                           p=c
                           def hovertrueobj1():
                              if TextBox1.instate(['disabled'])==True and LineButton1.instate(['disabled'])==True:
                                 SpeakBox1['text']='[Examine]'
                           def hoverfalseobj1():
                              if TextBox1.instate(['disabled'])==True and LineButton1.instate(['disabled'])==True:
                                  SpeakBox1['text']=''
                           def clicktrueobj(speaker, dialogue, Obj_id1):
                              if TextBox.instate(['disabled'])==True and LineButton1.instate(['disabled'])==True:
                                 nonlocal countobj1
                                 countobj1+=1
                                 SceneScreen1.delete(Obj_id1)
                                 SceneScreen1.pack()
                                 if countobj1<c:
                                    SpeakBox1['text']=speaker
                                    TextBox1['text']=''
                                    for j in dialogue:
                                       SceneScreen1['state']='disabled'
                                       TextBox1['text']+=j
                                       TextBox1.update()
                                       TextBox1.pack(side='left')
                                       SceneScreen1.create_window(300,400, window=TextBox1)
                                       SceneScreen1.update()
                                       SceneScreen1.pack(side='bottom')
                                       time.sleep(0.03)
                                    else:
                                       SceneScreen1['state']='normal'
                                 elif countobj1==c:
                                    SpeakBox1['text']=speaker
                                    TextBox1['text']=''
                                    for j in dialogue:
                                       SceneScreen1['state']='disabled'
                                       TextBox1['text']+=j
                                       TextBox1.update()
                                       TextBox1.pack(side='left')
                                       SceneScreen1.create_window(300,400, window=TextBox1)
                                       SceneScreen1.update()
                                       SceneScreen1.pack(side='bottom')
                                       time.sleep(0.03)
                                    else:
                                       SceneScreen1['state']='normal'
                                       LineButton1['state']='active'
                                       TextBox1['state']='active'
                           Obj_id1= SceneScreen1.create_image(self.x,self.y, image=self.img)
                           SceneScreen1.tag_bind(Obj_id1, "<Enter>", lambda p: hovertrueobj1())
                           SceneScreen1.tag_bind(Obj_id1, "<Leave>", lambda p: hoverfalseobj1())
                           SceneScreen1.tag_bind(Obj_id1, "<Button-1>", lambda p: clicktrueobj1(speaker, dialogue, Obj_id1))
                           SceneScreen1.pack(side='bottom')
                     letter1=Obj1("Letter.png",300,150)
                     letter1.create1()
                     countobj1=0
                     k1=-1
                     m1=-1
                     def next_line1():
                         nonlocal k1,m1
                         k1+=1
                         m1+=1
                         if k1<(len(l21)) and m1<(len(l11)) :
                            str11=l21[k1]
                            SpeakBox1['text']=l11[m1]
                            TextBox1['text']=''
                            for j in str11:
                                 if str11=="[openend]":
                                     TextBox1['state']='disabled'
                                     LineButton1['state']='disabled'
                                     End1=Obj1("End 2.png",300,150)
                                     End1.create1()
                                     SceneScreen1.update()
                                     SceneScreen1.pack()
                                     raise NoError
                                 LineButton1['state']='disabled'
                                 TextBox1['text']+=j
                                 TextBox1.update()
                                 TextBox1.pack(side='left')
                                 SceneScreen1.create_window(300,400, window=TextBox1)
                                 SceneScreen1.update()
                                 SceneScreen1.pack(side='bottom')
                                 time.sleep(0.03)
                            else:
                                 LineButton1['state']='active'    
                     LineButton1["command"]=next_line1
                     SceneScreen1.pack(side='bottom')
                     class NoError(Exception):
                        sys.tracebacklimit=0
                     GameWindow1.mainloop()
            else:
                pass
        b['command']=click1
class NoError(Exception):
   sys.tracebacklimit=0
GameWindow.mainloop()
