import tkinter as tk
from tkinter import *
##libreria para hacer iteraciones...
import itertools

root= tk.Tk()

#canvas1 = tk.Canvas(root, width = 400, height = 780,  relief = 'raised')
#canvas1.pack()

frame=Frame(root,width=400,height=780)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas1=Canvas(frame,width=400,height=400,scrollregion=(0,0,1000,1500))
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas1.yview)
canvas1.config(width=400,height=550)
canvas1.config(yscrollcommand=vbar.set)
canvas1.pack(side=LEFT,expand=False,fill=BOTH)

label1 = tk.Label(root, text='Cantidad de Camiones')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Ingrese datos:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 60, window=label2)

labelnro1 = tk.Label(root, text='% Mínimo de finos:')
labelnro1.config(font=('helvetica', 10))
canvas1.create_window(200, 90, window=labelnro1)

labelnro2 = tk.Label(root, text='% Máximo de finos:')
labelnro2.config(font=('helvetica', 10))
canvas1.create_window(200, 130, window=labelnro2)

labela = tk.Label(root, text='% de Finos A:')
labela.config(font=('helvetica', 10))
canvas1.create_window(200, 175, window=labela)

labelb = tk.Label(root, text='% de Finos B:')
labelb.config(font=('helvetica', 10))
canvas1.create_window(200, 215, window=labelb)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 110, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 150, window=entry2)

entrya = tk.Entry (root) 
canvas1.create_window(200, 195, window=entrya)

entryb = tk.Entry (root) 
canvas1.create_window(200, 235, window=entryb)

labels = []
labelscorrectos = []

def calcularNroCamiones ():
    
    del labels[:] # remove any previous labels from if the callback was called before    
    
    x1 = entry1.get()
    x2 = entry2.get()
    
    A = entrya.get()
    B = entryb.get()
    
    promediofinos = (float(x1)+float(x2))/2
    
  #Creacion de los valores de camiones 1 y 2 para el porcentaje A y B
    n_camiones1=[1,2,3,4,5]
    n_camiones2=[1,2,3,4,5]

#CREAMOS LA LISTA DE LISTAS DE TODAS LAS COMBINACIONES POSIBLES DE n_camiones1 y n_camiones2
    all_combinaciones_listas = [list(zip(x,n_camiones2)) for x in itertools.permutations(n_camiones1,len(n_camiones2))]
#Unificamos la lista de listas en una sola lista de pares de todas las combinaciones posibles DE n_camiones1 y n_camiones2: 
    all_combinaciones_listas_unidas = list(itertools.chain(*all_combinaciones_listas))

#variable para terminar el WHILE
    longitudlista = len(all_combinaciones_listas_unidas)    
    
    label3 = tk.Label(root, text= 'El % Promedio de finos de: ' + x1 + ' y '+x2+' es:',font=('helvetica', 10))
    canvas1.create_window(200, 310, window=label3)    

##LABEL QUE MOSTRATA EL RESULTADO DEL PROMEDIO
    label4 = tk.Label(root, text= promediofinos,font=('helvetica', 14, 'bold'))
    canvas1.create_window(200, 335, window=label4)       
      
    longitudcorrectos = 0
    
#variable i para el contador inicializarlo en 0
    i = 0         
    j = 0
    while i < longitudlista:     
        ## valores independientes N° de camiones 1, i cuenta el elemento de la lista horizontal, 0 de la columna 0, de izq. a der
        #all_combinaciones_listas_unidas[i][0]
        #print(all_combinaciones_listas_unidas[i][0])
        ## valores independientes N° de camiones 2, i cuenta el elemento de la lista horizontal, 1 de la columna 1, de izq. a der
        #print(all_combinaciones_listas_unidas[i][1])       
        
        NC1 = 0
        NC2 = 0
    
        resultado = 0
        aproximacion = 0
        
        numerador = 0
        denominador = 0
        
        NC1 = all_combinaciones_listas_unidas[i][0]
        NC2 = all_combinaciones_listas_unidas[i][1]        
        
        numerador = (float(NC1) * float(A)) + (float(NC2) * float(B))
        denominador =  (float(NC1) + float(NC2))    
        
        resultado = numerador / denominador        
        aproximacion = resultado / promediofinos         
           
         
        if (aproximacion >=0.9 and aproximacion <= 1.01 ):             
                    
            labels.append(Label(text='Para NC1 y NC2 respectivamente: (' + str(NC1) + ','+ str(NC2)+ ') se calculo: ' + str(round(resultado,2)) + '' ,font=('helvetica', 9, 'bold')))            
            #labels[i].place(x=35,y=355+(18*i))            
            #canvas1.create_window(200, 355+(18*i), window=labels[i])           
            
            labelscorrectos.append(Label(text='Para NC1 y NC2 respectivamente: (' + str(NC1) + ','+ str(NC2)+ ') se calculo: ' + str(round(resultado,2)) + '' ,font=('helvetica', 9, 'bold')))                        
            longitudcorrectos = len(labelscorrectos)
            
        else:
            labels.append(Label(text='Para NC1 y NC2 respectivamente: (' + str(NC1) + ','+ str(NC2)+ ') se calculo: ' + str(round(resultado,2)) + '' ,font=('helvetica', 9)))
            #labels[i].place(x=35,y=355+(18*i))    
            #labels[i].after(1000, labels[i].destroy)
            #canvas1.create_window(200, 355+(18*i), window=labels[i])             
        
        i += 1   
    
    while j < 10:
        
        del labelscorrectos[j:10] # remove any previous labels from if the callback was called before        
        
        labelscorrectos[j].place(x=35,y=355+(18*j)) 
        canvas1.create_window(200, 355+(18*j), window=labelscorrectos[j])
        
        j += 1
    
    ##destruir toda la ventana
    ##label4.after(1000, label4.master.destroy)
    
button1 = tk.Button(text='Calcular ! ', command=calcularNroCamiones, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 275, window=button1)

root.mainloop()