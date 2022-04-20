import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x600")

etiqueta = tkinter.Label(ventana,text = "hola mundo",bg="cadetblue")

# etiqueta.pack(side="bottom")

#sirve para los dos ejes (x,y) y que se expanadan
etiqueta.pack(fill="both",expand=True)

def hola():
    print("hola")


boton1 = tkinter.Button(ventana,text="click aqui ! ",padx=40,pady=40,command=hola)
#los paddings funcionan asi en los btotones


boton1.pack()

ventana.mainloop()