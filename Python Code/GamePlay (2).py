<<<<<<< Updated upstream
from tkinter import *
from tkinter.tix import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import sys
tutorial_file = open(r"MainTutorial.txt" , 'r')
tutorial_dialogue=tutorial_file.read() 
tutorial_list=tutorial_dialogue.split('\n\n')
eviimgl=[]
evitextl=[]
l1=[]
l2=[]
for i in range(len(tutorial_list)):
   tup1=tutorial_list[i].partition(': ')
   l1.append(tup1[0]) 
   l2.append(tup1[-1])
GameWindow= Tk()
GameWindow.resizable(width=False, height=False)
GameWindow.title('Discrepancy')
GameWindow.geometry('600x500')
GameFont = font.Font(family='Courier', name='GameFont', size=15, weight='bold')
MiniFont = font.Font(family='Courier', name='MiniFont', size=10, weight='bold')
SceneScreen= Canvas(GameWindow, width=600, height=500)
TextFrame=PhotoImage(file="textframe.png")
SceneScreen=Canvas(GameWindow, width=600, height=500)
SceneScreen.create_image(300,400,image=TextFrame)
LineButton=ttk.Button(SceneScreen, text='     >     ')
LineButton.pack(side='bottom')
SceneScreen.create_window(300,480, window=LineButton)
SceneScreen.pack(side='bottom')
SpeakBox = Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=200)
SpeakBox.pack(side='bottom')
SceneScreen.create_window(300, 320, window=SpeakBox)
TextBox = ttk.Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=525)
TextBox.pack(side='left')
SceneScreen.create_window(300,400, window=TextBox)
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
Scene1=Obj('Scene1.png', 300,150)
Scene1.create()
countobj=0
countwit=0
Wit1=Wit('Witness.png', 150, 200)
Wit1.create()
Wit1.active('Witness', 'Huh? Oh, Oh! Are you a detective??!!',1)
Obj1=Obj("DeidMann.png", 310, 200)
Obj1.create()
Obj1.active('Jones', '(The body of the victim... it appears they sustained blunt force trauma to the head.)', 3)
Obj2=Obj("BurningCar.png", 510, 100)
Obj2.create()
Obj2.active('Jones', '(Flames are bellowing out of the car\'s engine...)', 3)
Obj3=Obj("BloodyWrench.png", 210, 250)
#Obj3.create()
Obj3.active('Jones','(Odd, a wrench. It seems to be smeared with blood.)', 3)
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
         if str1[0]=='-':
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            break
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
CaseButton=Button(SceneScreen, height=80, width=80)
x=PhotoImage(file='casenotes.png')
CaseButton['image']=x
SceneScreen.create_window(555,255, window=CaseButton)
SceneScreen.pack(side='bottom')
def openlog():
   if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and countobj==p and countwit==q:
      menu=Toplevel(GameWindow)
      menu.title('Case Log')
      menu.geometry('400x230')
      menu.grab_set()
      main_frame=Frame(menu)
      main_frame.pack(fill=BOTH, expand=1)
      evicanvas=Canvas(main_frame)
      evicanvas.pack(side=LEFT, fill=BOTH, expand=1)
      scroll=ttk.Scrollbar(main_frame, orient=VERTICAL, command=evicanvas.yview)
      scroll.pack(side=RIGHT, fill=Y)
      evicanvas.configure(yscrollcommand=scroll.set)
      evicanvas.bind('<Configure>', lambda e: evicanvas.configure(scrollregion=evicanvas.bbox('all')))
      second_frame=Frame(evicanvas)
      evicanvas.create_window((0,0), window=second_frame, anchor='nw')
      CaseText=ttk.Label(second_frame, text='', font=GameFont, wraplength=300)
      hover=Balloon(menu)
      class evi:
         def __init__(self, img, desc, check=None, dialogue=None):
            self.img=PhotoImage(file=img)
            self.desc=desc
            self.check=check
            self.dialogue=dialogue
            b=Button(second_frame, height=70, width=70)
            b['image']=self.img
            hover.bind_widget(b, balloonmsg=self.desc)
            CaseText.pack(side=RIGHT)
            b.pack(side='top')
            def click():
               if self.check:
                  CaseText['text']=''
                  for j in self.dialogue:
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
                  for j in self.dialogue:
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
      b1=evi('DeidMann.png','The Victim:\nThey seem to have been hit hard by something.',False, '(Well... a car accident can lead to head injury. Nothing odd here...)')
      b2=evi('BloodyWrench.png','Old Wrench:\nIt\'s smeared with blood.',True, '(Hm! Why should this have blood if it was a car accident? I think we have a lead.)')
      b3=evi('BurningCar.png','Burning Car:\nPresumably caught on fire after crashing\ninto the tree.',False, 'This is probably the last thing I should show this man...')
   return
CaseButton['command']=openlog
GameWindow.mainloop()
=======
from tkinter import *
from tkinter.tix import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import sys
tutorial_file = open(r"MainTutorial.txt" , 'r')
tutorial_dialogue=tutorial_file.read() 
tutorial_list=tutorial_dialogue.split('\n\n')
eviimgl=[]
evitextl=[]
l1=[]
l2=[]
for i in range(len(tutorial_list)):
   tup1=tutorial_list[i].partition(': ')
   l1.append(tup1[0]) 
   l2.append(tup1[-1])
GameWindow= Tk()
GameWindow.resizable(width=False, height=False)
GameWindow.title('Discrepancy')
GameWindow.geometry('600x500')
GameFont = font.Font(family='Courier', name='GameFont', size=15, weight='bold')
MiniFont = font.Font(family='Courier', name='MiniFont', size=10, weight='bold')
SceneScreen= Canvas(GameWindow, width=600, height=500)
TextFrame=PhotoImage(file="textframe.png")
SceneScreen=Canvas(GameWindow, width=600, height=500)
SceneScreen.create_image(300,400,image=TextFrame)
LineButton=ttk.Button(SceneScreen, text='     >     ')
LineButton.pack(side='bottom')
SceneScreen.create_window(300,480, window=LineButton)
SceneScreen.pack(side='bottom')
SpeakBox = Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=200)
SpeakBox.pack(side='bottom')
SceneScreen.create_window(300, 320, window=SpeakBox)
TextBox = ttk.Label(SceneScreen, text='', font=GameFont, foreground='white', background='black', wraplength=525)
TextBox.pack(side='left')
SceneScreen.create_window(300,400, window=TextBox)
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
Scene1=Obj('Scene1.png', 300,150)
Scene1.create()
countobj=0
countwit=0
Wit1=Wit('Witness.png', 150, 200)
Wit1.create()
Wit1.active('Witness', 'Huh? Oh, Oh! Are you a detective??!!',1)
Obj1=Obj("DeidMann.png", 310, 200)
Obj1.create()
Obj1.active('Jones', '(The body of the victim... it appears they sustained blunt force trauma to the head.)', 3)
Obj2=Obj("BurningCar.png", 510, 100)
Obj2.create()
Obj2.active('Jones', '(Flames are bellowing out of the car\'s engine...)', 3)
Obj3=Obj("BloodyWrench.png", 210, 250)
#Obj3.create()
Obj3.active('Jones','(Odd, a wrench. It seems to be smeared with blood.)', 3)
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
         if str1[0]=='-':
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            break
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
CaseButton=Button(SceneScreen, height=80, width=80)
x=PhotoImage(file='casenotes.png')
CaseButton['image']=x
SceneScreen.create_window(555,255, window=CaseButton)
SceneScreen.pack(side='bottom')
def openlog():
   if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True and countobj==p and countwit==q:
      menu=Toplevel(GameWindow)
      menu.title('Case Log')
      menu.geometry('400x230')
      menu.grab_set()
      main_frame=Frame(menu)
      main_frame.pack(fill=BOTH, expand=1)
      evicanvas=Canvas(main_frame)
      evicanvas.pack(side=LEFT, fill=BOTH, expand=1)
      scroll=ttk.Scrollbar(main_frame, orient=VERTICAL, command=evicanvas.yview)
      scroll.pack(side=RIGHT, fill=Y)
      evicanvas.configure(yscrollcommand=scroll.set)
      evicanvas.bind('<Configure>', lambda e: evicanvas.configure(scrollregion=evicanvas.bbox('all')))
      second_frame=Frame(evicanvas)
      evicanvas.create_window((0,0), window=second_frame, anchor='nw')
      CaseText=ttk.Label(second_frame, text='', font=GameFont, wraplength=300)
      hover=Balloon(menu)
      class evi:
         def __init__(self, img, desc, check=None, dialogue=None):
            self.img=PhotoImage(file=img)
            self.desc=desc
            self.check=check
            self.dialogue=dialogue
            b=Button(second_frame, height=70, width=70)
            b['image']=self.img
            hover.bind_widget(b, balloonmsg=self.desc)
            CaseText.pack(side=RIGHT)
            b.pack(side='top')
            def click():
               if self.check:
                  CaseText['text']=''
                  for j in self.dialogue:
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
                  for j in self.dialogue:
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
      b1=evi('DeidMann.png','The Victim:\nThey seem to have been hit hard by something.',False, '(Well... a car accident can lead to head injury. Nothing odd here...)')
      b2=evi('BloodyWrench.png','Old Wrench:\nIt\'s smeared with blood.',True, '(Hm! Why should this have blood if it was a car accident? I think we have a lead.)')
      b3=evi('BurningCar.png','Burning Car:\nPresumably caught on fire after crashing\ninto the tree.',False, 'This is probably the last thing I should show this man...')
   return
CaseButton['command']=openlog
GameWindow.mainloop()
>>>>>>> Stashed changes
