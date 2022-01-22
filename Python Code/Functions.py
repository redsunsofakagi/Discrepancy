#Basic Functions

class setup:
    k=-1
    m=-1
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

        CaseButton=Button(SceneScreen, height=80, width=80)
        x=PhotoImage(file='casenotes.png')
        CaseButton['image']=x
        SceneScreen.create_window(555,255, window=CaseButton)
        SceneScreen.pack(side='bottom')

        global GameWindow, GameFont, MiniFont, SceneScreen, LineButton, SpeakBox, TextBox, CaseButton

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
        global l1, l2

    class obj:
       def __init__(self, img, x,y):
          self.img = PhotoImage(file=img)
          self.x = x
          self.y = y
          
       def create(self):
          base=SceneScreen.create_image(self.x, self.y, image=self.img)
          SceneScreen.pack()
          
       def active(self, speaker, dialogue):
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
  

