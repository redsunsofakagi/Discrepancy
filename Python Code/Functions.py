#Basic Functions

class setup:
    def window(title):
        GameWindow= Tk()
        GameWindow.resizable(width=False, height=False)
        GameWindow.title(title)
        GameWindow.geometry('600x500')
        
        GameFont = font.Font(family='Courier', name='GameFont', size=15, weight='bold')
        MiniFont = font.Font(family='Courier', name='MiniFont', size=10, weight='bold')
        SceneScreen= Canvas(GameWindow, width=600, height=500)
        
        TextFrame=PhotoImage(file="textframe.png")
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

        '''CaseButton=Button(SceneScreen, height=80, width=80)
        x=PhotoImage(file='casenotes.png')
        CaseButton['image']=x
        SceneScreen.create_window(555,255, window=CaseButton)
        SceneScreen.pack(side='bottom')'''

        k=-1
        m=-1
        def next_line():
           global l1, l2
           global k
           global m
           k+=1
           m+=1
           if k<(len(l2)) and m<(len(l1)) :
              str1=l2[k]
              SpeakBox['text']=l1[m]
              TextBox['text']=''
              for j in str1:
                 if str1[0]=='#':
                    c=int(str1[-1])
                    TextBox['state']='disabled'
                    LineButton['state']='disabled'
                    break            
                 elif str1[0]=='@':
                    w=int(str1[-1])
                    TextBox['state']='disabled'
                    LineButton['state']='disabled'
                    break
                 elif str1[0]=='$':
                    e=int(str1[-1])
                    TextBox['state']='disabled'
                    LineButton['state']='disabled'
                    break
                 elif str1[0]=='%':
                    o=int(str1[-1])
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

    def textfile(textfile):
        tutorial_file= open(textfile, 'r')
        tutorial_dialogue=tutorial_file.read()
        tutorial_list=tutorial_dialogue.split('\n\n')
        l1=[]
        l2=[]
        for i in range(len(tutorial_list)):
            tup1=tutorial_list[i].partition(': ')
            l1.append(tup1[0])
            l2.append(tup1[-1])
        #global l1, l2

    def objfile(textfile):
        tutorial_file= open(textfile, 'r')
        tutorial_dialogue=tutorial_file.read()
        tutorial_list=tutorial_dialogue.split('\n\n')
        l3=[]
        l4=[]
        for i in range(len(tutorial_list)):
            tup1=tutorial_list[i].partition(': ')
            l3.append(tup1[0])
            l4.append(tup1[-1])
        #global l3, l4

    def witfile(textfile):
        tutorial_file= open(textfile, 'r')
        tutorial_dialogue=tutorial_file.read()
        tutorial_list=tutorial_dialogue.split('\n\n')
        l5=[]
        l6=[]
        for i in range(len(tutorial_list)):
            tup1=tutorial_list[i].partition(': ')
            l5.append(tup1[0])
            l6.append(tup1[-1])
        #global l5, l6

    def evifile(textfile):
        tutorial_file= open(textfile, 'r')
        tutorial_dialogue=tutorial_file.read()
        tutorial_list=tutorial_dialogue.split('\n\n')
        l7=[]
        l8=[]
        for i in range(len(tutorial_list)):
            tup1=tutorial_list[i].partition(': ')
            l7.append(tup1[0])
            l8.append(tup1[-1])

    def optfile(textfile):
        tutorial_file= open(textfile, 'r')
        tutorial_dialogue=tutorial_file.read()
        tutorial_list=tutorial_dialogue.split('\n\n')
        l9=[]
        l10=[]
        for i in range(len(tutorial_list)):
            tup1=tutorial_list[i].partition(': ')
            l9.append(tup1[0])
            l10.append(tup1[-1])

countobj=0
class Obj:
    global GameWindow, GameFont, MiniFont, SceneScreen, LineButton, SpeakBox, TextBox, CaseButton
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
                global l3, l4
                global countobj, c
                SceneScreen.delete(Obj_id)
                SceneScreen.pack()
                if countobj<c:
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
                elif countobj==c:
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
                    countobj=-1
                countobj+=1
        Obj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
        SceneScreen.tag_bind(Obj_id, "<Enter>", lambda p: hovertrueobj())
        SceneScreen.tag_bind(Obj_id, "<Leave>", lambda p: hoverfalseobj())
        SceneScreen.tag_bind(Obj_id, "<Button-1>", lambda p: clicktrueobj(n,Obj_id))
        SceneScreen.pack(side='bottom')

countwit=0
class Wit:
    def __init__(self, img, x,y):
        self.img = PhotoImage(file=img)
        self.x = x
        self.y = y
        
    def create(self):
        SceneScreen.create_image(self.x, self.y, image=self.img)
        SceneScreen.pack()

    def active(self, n): 
        def hovertruewit():
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']='[Examine]'
                
        def hoverfalsewit():
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']=''
        
        def clicktruewit(n, Obj_id):
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                global l5, l6
                global countwit, w
                SceneScreen.delete(Obj_id)
                SceneScreen.pack()
                if countwit<w:
                    str1=l6[n]
                    SpeakBox['text']=l5[n]
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
                elif countwit==w:
                    str1=l6[n]
                    SpeakBox['text']=l4[n]
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
                    countwit=-1
                countwit+=1
        Obj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
        SceneScreen.tag_bind(Obj_id, "<Enter>", lambda p: hovertrueobj())
        SceneScreen.tag_bind(Obj_id, "<Leave>", lambda p: hoverfalseobj())
        SceneScreen.tag_bind(Obj_id, "<Button-1>", lambda p: clicktrueobj(n,Obj_id))
        SceneScreen.pack(side='bottom')

'''def openlog():
   if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True
      menu=Toplevel(GameWindow)
      menu.title('Case Log')
      menu.geometry('400x230')
      menu.grab_set()
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
      b3=evi('BurningCar.png','Burning Car:\nPresumably caught on fire after crashing\ninto the tree.',False, 'This is probably the last thing I should show this man...')
      b3=evi('BurningCar.png','Burning Car:\nPresumably caught on fire after crashing\ninto the tree.',False, 'This is probably the last thing I should show this man...')
      b3=evi('BurningCar.png','Burning Car:\nPresumably caught on fire after crashing\ninto the tree.',False, 'This is probably the last thing I should show this man...')
      b3=evi('BurningCar.png','Burning Car:\nPresumably caught on fire after crashing\ninto the tree.',False, 'This is probably the last thing I should show this man...')

   return
CaseButton['command']=openlog'''

countevi=0
class Evi:
    def __init__(self, img, check=None):
        self.img=PhotoImage(file=img)
        self.check=check
        if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
          menu=Toplevel(GameWindow)
          menu.title('Case Log')
          menu.geometry('400x230')
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
          CaseText=ttk.Label(second_frame, text='', font=GameFont, wraplength=300)
          hover=Balloon(menu)
    def active(self, n):
          global l7, l8, countevi,e
          if countevi<e:
              str1= l8[n]
              b=Button(second_frame, height=70, width=70)
              b['image']=self.img
              hover.bind_widget(b, balloonmsg=l7[n])
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
          elif countevi==e:
              str1= l8[n]
              b=Button(second_frame, height=70, width=70)
              b['image']=self.img
              hover.bind_widget(b, balloonmsg=l7[n])
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
              countevi=-1
          countevi+=1
