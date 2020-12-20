import tkinter as tk

def key_input(event):
    top=tk.Entry.get(display)
    num="1234567890"
    sym = "+-*/"
    if event.char in num:
        if len(top)>0 and top[-1] in sym:
            hid.delete(0,tk.END)
        display.insert(tk.END, event.char)
        hid.insert(tk.END, event.char)

    elif event.char in sym and len(top)!=0 and top[-1] in num:
        display.insert(tk.END, event.char)



def num_1(event):

    display.insert(tk.END,"1")
def num_2(event):
    display.insert(tk.END,"2")


def cal(event):
    value=tk.Entry.get(display)
    value=eval(value)
    display.delete(0,tk.END)
    hid.delete(0,tk.END)
    hid.insert(0, value)

def clear(event):
    display.delete(0,tk.END)
    hid.delete(0, tk.END)


root=tk.Tk()
root.title("계산기")
root.geometry("400x400")

display=tk.Entry(root,width=20)
display.pack()

hid=tk.Entry(root,width=20)
hid.pack()

button1=tk.Button(root,text="1",width=5)
button1.bind("<Button-1>",num_1)
button1.pack()

button2=tk.Button(root,text="2",width=5)
button2.bind("<Button-1>",num_2)
button2.pack()

root.bind("<Return>",cal)
root.bind("<Escape>",clear)
root.bind("<Key>",key_input)

root.mainloop()