from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sendMsg as SM

def Submit():
        if mobileEntry.get()=='' or messageBoxEntry.get()=='':
                messagebox.showerror('Error', 'All Field Are Required')
        else:
                SM.message(mobileEntry.get(),messageBoxEntry.get())
                root.destroy()
root=Tk()
root.geometry('990x660+50+50')#use with place
root.resizable(False,False)
root.title('SEND WHATSAPP MESSAGE')
bgImage=ImageTk.PhotoImage(file='bg.png')
bgLable=Label(root,image=bgImage)
bgLable.place(x=0,y=0)
# frame.place(x=55,y=125)

heading=Label(root,text='WHATSAPP MESSAGE',font=('Microdoft Yahei UI Light',23,'bold'),bg='lightblue',fg='black')
heading.place(x=55,y=125)

mobileLabel=Label(root,text='MOBILE NUMBER :-',font=('Microsoft Yahei Ui Light',16
        ,'bold'),bg='lightblue',fg='black')
mobileLabel.place(x=45,y=220)

mobileEntry=Entry(root,width=20,font=('Microsoft Yahei Ui Light',16
        ,'bold'),bg='lightblue',fg='white',bd=0)
mobileEntry.place(x=45,y=260)
mobileEntry.insert(0,'+91')
# mobileEntry.bind('<FocusIn>',mobile_enter)

messageBoxLabel=Label(root,text='MESSAGE :-',font=('Microsoft Yahei Ui Light',16
        ,'bold'),bg='lightblue',fg='black')
messageBoxLabel.place(x=45,y=320)

messageBoxEntry=Entry(root,bd=4,font=('Microsoft Yahei Ui Light',16,'bold')
    ,bg='lightblue',fg='black')
messageBoxEntry.place(x=45,y=360,width=300,height=120)

sendButton=Button(root,text='Send',font=('Open Sans',16,'bold'),bd=0,bg='darkblue',fg='White',width=10,command=Submit)
sendButton.place(x=45,y=490)
root.mainloop()