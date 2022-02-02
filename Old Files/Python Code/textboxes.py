from tkinter import *
from tkinter import ttk
import time

textbox=  Tk()
textbox.geometry('700x130-288-70')

textbox.title('')

text_file = open(r"TextCheck.txt" , 'r')
dialogue=text_file.read()


dialist=dialogue.split('\n\n')

l1=[]
l2=[]

for i in range(len(dialist)):
               tup1=dialist[i].partition(':')
               l1.append(tup1[0])
               l2.append(tup1[-1])

label=ttk.Label(textbox, text='', font='BOLD', wraplength=700)

k=-1
m=-1

def next_line():
    global k
    global m
    k+=1
    m+=1
    if k<(len(l2)) and m<(len(l1)):
        str1=l2[k]
        textbox.title(l1[m])
        label['text']=''
        for j in str1:
            button.state(['disabled'])
            label['text'] = label['text'] + j
            label.update()
            label.pack(side='left')
            time.sleep(.03)
        button.state(['!disabled'])
    else:
        k=0
        m=0
        str1=l2[k]
        textbox.title(l1[m])
        label['text']=''
        for j in str1:
            button.state(['disabled'])
            label['text'] = label['text'] + j
            label.update()
            label.pack(side='left')
            time.sleep(.03)
        button.state(['!disabled'])

button=ttk.Button(textbox, text='>', command= lambda: next_line())
button.pack(side='bottom') 
textbox.mainloop()
