class obj:
    def __init__(self, img, x,y):
        self.img = PhotoImage(file=img)
        self.x = x
        self.y = y
        countobj=0
        
    def create(self):
        SceneScreen.create_image(self.x, self.y, image=self.img)
        SceneScreen.pack()

    def active(self, speaker, dialogue):
        def hovertrueobj():
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']='[Examine]'
                
        def hoverfalseobj():
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                ObjectiveBar['text']=''
        def clicktrueobj(speaker, dialogue, Obj_id):
            if TextBox.instate(['disabled'])==True and LineButton.instate(['disabled'])==True:
                nonlocal countobj
                SceneScreen.delete(Obj_id)
                SceneScreen.pack()
                if countobj<(len(l4)):
                    SpeakBox['text']=speaker
                    TextBox['text']=''
                    for j in diaogue:
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
                    SpeakBox['text']=speaker
                    TextBox['text']=''
                    for j in dialogue:
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
        Obj_id = SceneScreen.create_image(self.x,self.y, image=self.img)
        SceneScreen.tag_bind(Obj_id, "<Enter>", lambda p: hovertrueobj())
        SceneScreen.tag_bind(Obj_id, "<Leave>", lambda p: hoverfalseobj())
        SceneScreen.tag_bind(Obj_id, "<Button-1>", lambda p: clicktrueobj(speaker, dialogue, Obj_id))
        SceneScreen.pack(side='bottom')

#Objective: Screen transitions- fade in a scene (image) and then fade it out and fade in a new image when the scene ends.
#It should have the width of Scene1.png. We need to generate a black bg to fade out to and fade in from.
#this is probably possible by setting the bg of the main game window to black
#we can make a black bg which is called and displayed over the top of the canvas. it can be then made to slowly become transparent
        #whenever we switch to the next scene it can be made to fade to black, and delete all the items inside
        #then we can call it again, make it set up the objects of the next scene, and keep doing that.

class SceneControl:
    def Call(img):
        global k
        global m
        k+=1
        m+=1
        if k<(len(l2)) and m<(len(l1)) :
          str1=l2[k]
          SpeakBox['text']=l1[m]
          TextBox['text']=''
          for j in str1:
             if str1[0]=='+':
                 
                 
                 
