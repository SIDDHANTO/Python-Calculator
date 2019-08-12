import tkinter as tk
def handleClick(btnval):
    exp=strVar.get()
    if btnval=="=":
        strVar.set(eval(exp))# inbuild functionality for solving data of string
    elif btnval=="C":
        strVar.set('')
    else:
        if exp=='0':
            strVar.set(btnval)
        else:
            strVar.set(exp+btnval)

window=tk.Tk()
strVar=tk.StringVar()
strVar.set('')
tk.Label(window,textvariable=strVar).grid(row=0,column=0,columnspan=3)
tk.Button(window,text="C",command=lambda :handleClick("C"),width=5,height=2).grid(row=0,column=0)
tk.Button(window,text="7",command=lambda :handleClick("7"),width=5,height=2).grid(row=1,column=0)
tk.Button(window,text="8",command=lambda :handleClick("8"),width=5,height=2).grid(row=1,column=1)
tk.Button(window,text="9",command=lambda :handleClick("9"),width=5,height=2).grid(row=1,column=2)
tk.Button(window,text="/",command=lambda :handleClick("/"),width=5,height=2).grid(row=1,column=3)

tk.Button(window,text="4",command=lambda :handleClick("4"),width=5,height=2).grid(row=2,column=0)
tk.Button(window,text="5",command=lambda :handleClick("5"),width=5,height=2).grid(row=2,column=1)
tk.Button(window,text="6",command=lambda :handleClick("6"),width=5,height=2).grid(row=2,column=2)
tk.Button(window,text="*",command=lambda :handleClick("*"),width=5,height=2).grid(row=2,column=3)

tk.Button(window,text="1",command=lambda :handleClick("1"),width=5,height=2).grid(row=3,column=0)
tk.Button(window,text="2",command=lambda :handleClick("2"),width=5,height=2).grid(row=3,column=1)
tk.Button(window,text="3",command=lambda :handleClick("3"),width=5,height=2).grid(row=3,column=2)
tk.Button(window,text="-",command=lambda :handleClick("-"),width=5,height=2).grid(row=3,column=3)

tk.Button(window,text=".",command=lambda :handleClick("."),width=5,height=2).grid(row=4,column=0)
tk.Button(window,text="0",command=lambda :handleClick("0"),width=5,height=2).grid(row=4,column=1)
tk.Button(window,text="=",command=lambda :handleClick("="),width=5,height=2).grid(row=4,column=2)
tk.Button(window,text="+",command=lambda :handleClick("+"),width=5,height=2).grid(row=4,column=3)

window.mainloop()