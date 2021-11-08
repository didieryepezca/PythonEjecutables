##compnum(16,50)
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hola Dajalma este es un programa python ejecutable!', fg='green', font=('helvetica', 18, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Haz Click',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()