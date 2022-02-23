import time
from tkinter import *
from tkinter import font
import mysql.connector
from tkinter import ttk

from mysql.connector.constants import SQLMode
mydb=mysql.connector.connect(user='root',host='localhost',passwd='1234',database='mini_projects')
myCursor=mydb.cursor()

"""
------SQL-------

show databases;
create database todoListProject;
use todoListProject;
or #use mini_projects
show tables;
create table todo(
id int,
task varchar(255)not null
);
select * from todo;

"""

root=Tk()
root.geometry('1280x720+35+10')
root.resizable(False,False)
root.title("To Do list")
root.config(bg='white')
Heading=Label(root,text="My To-Do List",font=('times new roman',50,'bold'),bg='indianred',width=53)
Heading.pack()
myCanvas=Canvas(root,width=1280)
myCanvas2=Canvas(root,width=1280)
myCanvas.create_rectangle(0,2,1280,0,fill='black')
myCanvas2.create_rectangle(0,2,1280,0,fill='black')
myCanvas.place(x=0,y=85)
myCanvas2.place(x=0,y=89)

Heading=Label(root,text="Enter Today's Goals",font=('times new roman',30,'bold'),width=55,bg='indianred')
Heading.place(x=0,y=110)

def submit():
    val=textEntry.get()
    if(val=="" or val==" "*len(val)):
        DoneLabe2.config(text='Some information is Incorrect, Please Recheck')
    else:
        query=f'insert into todo (task) values ("{val}")'
        global myCursor
        myCursor.execute(query)
        global mydb
        mydb.commit()
        textEntry.delete('0',END)
        DoneLabe2.config(text="Made by : Anmol main")
        refresh()

textEntry=Entry(root,width=50,font=('times new roman',30,'bold'),border=8,highlightcolor='black',bg='wheat')
textEntry.place(x=35,y=180)

submitBtn=Button(root,text="Enter",font=('times new roman',20,'bold'),border=8,height=1,bg='indianred',command=submit)
submitBtn.place(x=1125,y=178)

myCanvas3=Canvas(root,width=1280)
myCanvas3.create_rectangle(0,2,1280,0,fill='black')
myCanvas3.place(x=0,y=260)
myCanvas4=Canvas(root,width=1280)
myCanvas4.create_rectangle(0,2,1280,0,fill='black')
myCanvas4.place(x=0,y=264)

myCanvas4=Canvas(root,width=1280)
myCanvas4.create_rectangle(0,2,1280,0,fill='black')
myCanvas4.place(x=0,y=264)

timer=Label(root,text="TIME",font=('times new roman',30,'bold'),width=55,bg='indianred')
def digitalclock():
    timer.place(x=0,y=278)
    txt=time.strftime("%H:%M:%S")
    timer.config(text=txt)
    timer.after(100, digitalclock)

digitalclock()

columns=('task')
tree=ttk.Treeview(root,columns=columns,show='',height=6)
def show():
    query='select task from todo'
    myCursor.execute(query)
    li=[]
    for i in myCursor:
        i=list(i)
        li.append(i)

    style=ttk.Style()
    style.configure('Treeview',
    background='indianred',
    foreground='wheat',
    rowheight=35,
    font=('times new roman',20,'bold'),
    fieldbackground='silver'
    )
    style.map('Treeview',background=[('selected','teal')])
    tree.column("#1",anchor=CENTER, stretch=NO, width=1200)
    scrollbar = Scrollbar(root)
    scrollbar.place(x=1230,y=350,relheight=0.3,anchor='ne')
    tree.configure(yscroll=scrollbar.set)
    scrollbar.config( command = tree.yview )

    for item in li:
        # for i in range(0,3):
        tree.insert("",END,values=item)
    tree.place(x=30,y=350)
show()
def refresh():
    for item in tree.get_children():
        tree.delete(item)
    # DoneLabel.config(text='')
    DoneLabe2.config(text="Made by : Anmol main")

    show()


dataToBeDeleted=''
def getValue(event):
    id=tree.selection()[0]
    select=tree.set(id)
    DoneLabel.config(text=select['task'])
    # print(select['task'])
    global dataToBeDeleted
    dataToBeDeleted=select['task']

def dlt():
    value=dataToBeDeleted
    # print(dataToBeDeleted)
    query=f'delete from todo where task = "{dataToBeDeleted}"'
    # print(query)
    myCursor.execute(query)
    mydb.commit()
    # print("done")
    textEntry.delete('0',END)
    DoneLabel.config(text='')
    refresh()

def doit(event):
    global dataToBeDeleted
    dataToBeDeleted=''
    DoneLabel.config(text='')
    DoneLabe2.config(text="Made by : Anmol main")

tree.bind('<Double-Button-1>',getValue)
root.bind('<Triple-Button-1>',doit)

DoneLabel=Label(root,width=62,font=('times new roman',20,'bold'),border=8,highlightcolor='black',bg='wheat')
DoneLabel.place(x=35,y=595)
DoneBtn=Button(root,text="Done",font=('times new roman',20,'bold'),border=8,height=1,bg='indianred',command=dlt)
DoneBtn.place(x=1125,y=590)
DoneLabe2=Label(root,width=110,font=('times new roman',15,'bold'),border=8,highlightcolor='black',bg='indianred',text="Made by : Anmol main")
DoneLabe2.place(x=0,y=670)
root.mainloop()