import tkinter as tk

root=tk.Tk()
root.title("계산기")
root.geometry("400x400")

display=tk.Entry(root,width=20)
display.pack()

but1=tk.Button(root,padx=15,pady=15,bg='black',text="1")
but1.place(x=10,y=100)
but1=tk.Button(root,padx=15,pady=15,bg='black',text="2")
but1.place(x=80,y=100)


root.mainloop()
