from tkinter import *
from tkinter.tix import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import time
#import threading
import sys
from pyglet import font
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
script_dir = os.path.join(main_dir, "Script")
font_dir = os.path.join(main_dir, "Fonts")
img2_dir= os.path.join(main_dir, "Images", "Cases 2&3")

img_textframe = os.path.join(img2_dir, "textframe.png")
img_Scene4 = os.path.join(img2_dir,'Scene4.png')
img_Locke = os.path.join(img2_dir,"Locke.png")
img_Charles_removebg = os.path.join(img2_dir,"Charles-removebg-preview.png")
img_Scene5 = os.path.join(img2_dir,'Scene5.png')
img_Road = os.path.join(img2_dir,"Road.png")
img_Cars_11 = os.path.join(img2_dir,"Cars_11.png")
img_Note1 = os.path.join(img2_dir,"Note1.png")
img_James = os.path.join(img2_dir,"James.png")
img_Autopsy = os.path.join(img2_dir,"Autopsy.png")
img_Scene6 = os.path.join(img2_dir,"Scene6.png")
img_Todo = os.path.join(img2_dir,"Todo.png")
img_Records = os.path.join(img2_dir,"Records.png")
img_Scene7 = os.path.join(img2_dir,"Scene7.png")
img_Zimmerman = os.path.join(img2_dir,"Zimmerman.png")
img_Scene8 = os.path.join(img2_dir,"Scene8.png")
img_Road_1 = os.path.join(img2_dir,"Road_1.png")
img_Car = os.path.join(img2_dir,'Car.png')
img_Note1 = os.path.join(img2_dir,'Note1.png')


tutorial_file = open(os.path.join(script_dir, "MainTutorial2.txt"), 'r')
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
TextFrame=PhotoImage(file=img_textframe)
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
Scene004=Obj(img_Scene4, 300,150)
Scene004.create()
countobj=0
countwit=0
acountobj=0
acountwit=0
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
         elif str1=="[ENTER_L1]":
            global Scene004
            global Scene04, Pers001
            del Scene004
            Scene04=Obj(img_Scene4, 300,150)
            Scene04.create()
            Pers001=Wit(img_Locke,150,220)
            Pers001.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_C]":
            del Scene04
            del Pers001
            global Scene4, Pers1, Pers2
            Scene4=Obj(img_Scene4, 300,150)
            Scene4.create()
            Pers1=Wit(img_Locke,150,220)
            Pers1.create()
            countobj=0
            countwit=0
            Pers2=Wit(img_Charles_removebg,150,100)
            Pers2.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=='[05]':
            del Scene4
            del Pers1
            del Pers2
            global Scene5,Obj1_5,Obj2_5,Obj3_5,Pers_L1
            SceneScreen.update()
            Scene5=Obj(img_Scene5, 300,150)
            Scene5.create()
            SceneScreen.update()
            countobj=0
            countwit=0
            Obj1_5=Obj(img_Road,300,150)
            Obj1_5.create()
            Obj1_5.active("Jones","(The road... supposedly deserted when found. Bustling with traffic at the moment.)",2)
            Obj2_5=Obj(img_Cars_11,300,160)
            Obj2_5.create()
            Obj2_5.active("Jones","(The car... the tire marks point towards the intersection, but then veer towards the tree.)",2)
            Obj3_5=Obj(img_Note1,400,140)
            Obj3_5.create()
            Pers_L1=Wit(img_Locke,460,100)
            Pers_L1.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[LEAVE_L]":
            del Scene5,Obj1_5,Obj2_5,Obj3_5,Pers_L1
            global Scene05,Obj1_05,Obj2_05,Obj3_05
            SceneScreen.update()
            Scene05=Obj(img_Scene5, 300,150)
            Scene05.create()
            SceneScreen.update()
            countobj=0
            countwit=0
            Obj1_05=Obj(img_Road,300,150)
            Obj1_05.create()
            Obj2_05=Obj(img_Cars_11,300,160)
            Obj2_05.create()
            Obj3_05=Obj(img_Note1,400,140)
            Obj3_05.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_J]":
            del Scene05,Obj1_05,Obj2_05,Obj3_05
            global Scene005,Obj1_005,Obj2_005,Obj3_005,Pers_J
            SceneScreen.update()
            Scene005=Obj(img_Scene5, 300,150)
            Scene005.create()
            SceneScreen.update()
            countobj=0
            countwit=0
            Obj1_005=Obj(img_Road,300,150)
            Obj1_005.create()
            Obj2_005=Obj(img_Cars_11,300,160)
            Obj2_005.create()
            Obj3_005=Obj(img_Note1,400,140)
            Obj3_005.create()
            Pers_J=Wit(img_James,500,250)
            Pers_J.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_L]":
            del Scene005,Obj1_005,Obj2_005,Obj3_005,Pers_J
            global Scene0005,Obj1_0005,Obj2_0005,Obj3_0005,Aut,Pers_J0,PersLo1
            SceneScreen.update()
            Scene0005=Obj(img_Scene5, 300,150)
            Scene0005.create()
            SceneScreen.update()
            countobj=0
            countwit=0
            Obj1_0005=Obj(img_Road,300,150)
            Obj1_0005.create()
            Obj2_0005=Obj(img_Cars_11,300,160)
            Obj2_0005.create()
            Obj3_0005=Obj(img_Note1,400,140)
            Obj3_0005.create()
            Pers_J0=Wit(img_James,500,250)
            Pers_J0.create()
            PersLo1=Wit(img_Locke,460,100)
            PersLo1.create()
            Aut=Obj(img_Autopsy,550,100)
            Aut.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[06]":
            del Scene0005,Obj1_0005,Obj2_0005,Obj3_0005,Aut,Pers_J0,PersLo1
            global acountobj,acountwit
            global Scene6,Locke,James,Todo,Rec
            Scene6=Obj(img_Scene6,300,150)
            Scene6.create()
            acountobj=0
            acountwit=0
            Locke=Wit(img_Locke,510,100)
            Locke.create()
            James=Wit(img_James,90,100)
            James.create()
            Todo=aObj(img_Todo,290,100)
            Todo.acreate()
            Todo.aactive("Jones","(The warden, Columbus\'s itinerary of the day... It ends with an early morning meeting with someone named... Zimmerman?)",2)
            Rec=aObj(img_Records,200,90)
            Rec.acreate()
            Rec.aactive("Jones","(Prison records... a series of people and the \'crimes\' they committed.)",2)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[07]":
            del Scene6,Locke,James,Todo,Rec
            global Scene7
            Scene7=Obj(img_Scene7,300,150)
            Scene7.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_Z]":
            del Scene7
            global Scene_7,Zimmer
            countwit=0
            Scene_7=Obj(img_Scene7,300,150)
            Scene_7.create()
            Zimmer=Wit(img_Zimmerman,310,250)
            Zimmer.create()
            Zimmer.active('Jones:' ,'Can you tell me about your meeting with Columbus Olfonso yesterday?' ,1)
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[ENTER_LA]":
            del Scene_7,Zimmer
            global Scene07,Zimmer1,Locke1
            Scene07=Obj(img_Scene7,300,150)
            Scene07.create()
            Zimmer1=Wit(img_Zimmerman,310,250)
            Zimmer1.create()
            Locke1=Wit(img_Locke,510,250)
            Locke1.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1=="[08]":
            del Scene07, Zimmer1, Locke1
            Scene8=Obj(img_Scene8,300,150)
            Scene8.create()
            SceneScreen.update()
            SceneScreen.pack()
            raise NoError
         elif str1==' [inv1]':
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            break
         elif str1=='[inv1]':
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            break
         elif str1=="[open1]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Road=Evi(img_Road_1,"Road:\nCar was found on it. Supposedly deserted.", "Was it really deserted during the evening rush hour?", True)
            Car=Evi(img_Car,'Car:\nThe charred remains of a car. Tire marks point towards the intersection, the sharply skidding left.','I don\'t think this has anything to do with the timing.', False)
            Note=Evi(img_Note1,'Suicide Note:\nI tire of this futile existence. Perhaps it is better this way.','I don\'t think this has anything to do with the timing.', False)
            Road.active()
            Car.active()
            Note.active()
            break
         elif str1=="[open2]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Road2=Evi(img_Road_1,"Road:\nCar was found on it. Supposedly deserted.", "This child cannot lift the road, Jones.",- False)
            Car2=Evi(img_Car,'Car:\nThe charred remains of a car. Tire marks point towards the intersection, the sharply skidding left.','This child cannot lift the car, Jones.', False)
            Note2=Evi(img_Note1,'Suicide Note:\nI tire of this futile existence. Perhaps it is better this way.','Have \'em analyse the handwriting... just in case.', True)
            Road2.active()
            Car2.active()
            Note2.active()
            break
         elif str1=="[open3]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Road3=Evi(img_Road_1,"Road:\nCar was found on it. Supposedly deserted.", 'This is brutal...', True)
            Car3=Evi(img_Car,'Car:\nThe charred remains of a car. Tire marks point towards the intersection, the sharply skidding left.','This is brutal...', True)
            Note3=Evi(img_Note1,'Suicide Note:\nI tire of this futile existence. Perhaps it is better this way.','This is brutal...', True)
            Road3.active()
            Car3.active()
            Note3.active()
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
            Road4=Evi(img_Road_1,"Road:\nCar was found on it. Supposedly deserted.", 'It keeps bugging me... why was the road empty?', False)
            Car4=Evi(img_Car,'Car:\nThe charred remains of a car. Tire marks point towards the intersection, the sharply skidding left.','Tire marks of an accident, not a suicide. Not to mention the alcohol...', False)
            Note4=Evi(img_Note1,'Suicide Note:\nI tire of this futile existence. Perhaps it is better this way.','Of course... Even if we don\'t have handwriting, we can always rely on fingerprints!', True)
            Aut1=Evi(img_Autopsy,"Autopsy Report:\n'Victim died of blunt force trauma to the head, indication of intoxication by alcohol.'",'Marks of an drunken crash, not a suicide. Not to mention the tire marks...', False)
            Road4.active()
            Car4.active()
            Note4.active()
            Aut1.active()
            break
         elif str1=="[open5]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('It was a suicide.', False)
            B=Opt('It was an accident.', True)
            C=Opt('It was a murder.', False)
            A.active()
            B.active()
            C.active()
            break
         elif str1=="[open6]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('The suicide note was left by the victim.', False)
            B=Opt('The tire marks don\'t make sense.', False)
            C=Opt('The suicide note was planted.', True)
            A.active()
            B.active()
            C.active()
            break
         elif str1=="[open7]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openopt()
            A=Opt('It was a suicide.', False)
            B=Opt('It was a murder.', False)
            C=Opt('We lack evidence.', True)
            A.active()
            B.active()
            C.active()
            break
         elif str1=="[open8]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            Road5=Evi(img_Road_1,"Road:\nCar was found on it. Supposedly deserted.", 'Even a bustling road would definitely be deserted at 5:20 in the morning!', True)
            It=Evi(img_Todo,"Itinerary:\nLists the busy life of the warden.","Yesterday was a busy day for the warden... His day ended with a meeting at 5:00.",False)
            Car5=Evi(img_Car,'Car:\nThe charred remains of a car. Tire marks point towards the intersection, the sharply skidding left.','The crash...? But the road was full... or was it?', False)
            Car5.active()
            Road5.active()
            It.active()
            break
         elif str1=="[open9]":
            TextBox['state']='disabled'
            LineButton['state']='disabled'
            openlog()
            It1=Evi(img_Todo,"Itinerary:\nLists the busy life of the warden.","The warden\'s day ended with a meeting at 5:00am.. With Zimmerman.",True)
            Note5=Evi(img_Note1,'Suicide Note:\nI tire of this futile existence. Perhaps it is better this way.','No... this is clear evidence of manslaughter, not murder.', False)
            Aut2=Evi(img_Autopsy,"Autopsy Report:\n'Victim died of blunt force trauma to the head, indication of intoxication by alcohol.'",'No... this is clear evidence of manslaughter, not murder.', False)
            It1.active()
            Note5.active()
            Aut2.active()
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
