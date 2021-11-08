import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Suma de dos numeros')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Escribe 2 numeros:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)


labelnro1 = tk.Label(root, text='Numero 1:')
labelnro1.config(font=('helvetica', 10))
canvas1.create_window(200, 123, window=labelnro1)


labelnro2 = tk.Label(root, text='Numero 2:')
labelnro2.config(font=('helvetica', 10))
canvas1.create_window(200, 173, window=labelnro2)


entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 190, window=entry2)

def getSquareRoot ():
    
    x1 = entry1.get()
    x2 = entry2.get()
    
    label3 = tk.Label(root, text= 'La suma de los numeros: ' + x1 + ' y '+x2+' es:',font=('helvetica', 10))
    canvas1.create_window(200, 270, window=label3)
    
    ##LABEL QUE MUESTRA EL RESULTADO DE LA RAIZ CUADRADA
    ##label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 14, 'bold'))
    ##canvas1.create_window(200, 240, window=label4)
    
    ##LABEL QUE MOSTRATA EL RESULTADO DE LA SUMA
    label4 = tk.Label(root, text= float(x1)+float(x2),font=('helvetica', 14, 'bold'))
    canvas1.create_window(200, 300, window=label4)
    
    ##destruir toda la ventana
    ##label4.after(1000, label4.master.destroy)
    
button1 = tk.Button(text='Calcular ! ', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 240, window=button1)

root.mainloop()