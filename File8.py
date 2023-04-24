from tkinter import*

def calcValue(event):
    b=event.widget.cget("text")
    if b=='=':
        try:
            t=txt.get()
            r=eval(t)
            txt.set(r)
            #txt.set(eval(txt.get))
        except Exception as e:
            txt.set("Invalid Inputs")
            #print(e)

    elif b=='c':
        txt.set("")
        
    else:
        t=txt.get()+b
        txt.set(t)

clr="white"
clr1="teal"

win=Tk()
win.title("calc App")
win.wm_iconbitmap("icons/calc.ico")
win.geometry("325x340+200+100")
win.configure(background=clr1)             

x=0
btn=['c','/','*','=','9','8','7','+','6','5','4','-','3','2','1','0']

#widgets
txt=StringVar()
Entry(win,textvariable=txt,font="times 25 bold").pack(fill=X,padx=10,pady=15)

for rows in range(4):
    f=Frame(win,bg="white")
    for cols in range(4):
        b=Button(f,text=btn[x],height=1,width=3,font="times 15 bold",bg="black",fg=clr)
        b.pack(side="left",padx=9,pady=8)
        b.bind("<Button-1>",calcValue)
        x+=1
    f.pack(pady=4)

win.mainloop()    
