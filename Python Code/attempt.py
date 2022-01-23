from tkinter import *
from tkinter.tix import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import sys
menu=Tk()
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
CaseText=ttk.Label(second_frame, text='', wraplength=300)
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
