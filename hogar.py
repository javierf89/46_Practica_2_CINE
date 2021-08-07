import conection

from tkinter import*

from tkinter import ttk
root= Tk()
root.title("Naviportans")
root.geometry("900x800")
root.resizable(False,False)

frame_caja = Frame(root, width=1000, height=400, bg="#2ac17e")
frame_caja.place(x=300,y=60)
my_table = ttk.Treeview(frame_caja)


                    # Define Our Columns 
my_table['columns'] = ('NOMBRE', 'CORREO', 'DIRECCION',)

                    # Formate Our Columns
my_table.column('#0', width=120, minwidth=200)
my_table.column('NOMBRE', anchor=W, width=200)
my_table.column('CORREO', anchor=W, width=300)


                    # Create Headings
my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
my_table.heading('CORREO', text='CORREO', anchor=W)

my_table.place(x=1, y=1)   



def ingresar():
    nombre = Entry_2.get()
    correo = Entry_3.get()
    contraseña = Entry_4.get()
    direccion= Entry_5.get()
    navyportans = conection.MyDatabase()
   
    navyportans.insert_db(nombre,correo,contraseña,direccion)

def mostrar_usuario():
    

    nombre = Entry_2.get()
    correo = Entry_3.get()
    
    direccion= Entry_5.get()
    navyportans = conection.MyDatabase()
    registro  =0
    navyportans.read_db(nombre,correo,frame_caja)
    
def eliminar_1():
        nombre = Entry_2.get()
        correo = Entry_3.get()
        contraseña = Entry_4.get()
        direccion= Entry_5.get()
        navyportans = conection.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
        navyportans.delete_db(nombre,correo,contraseña,direccion)
Etiqueta =  Label(root,text="Bienvenido Naviportans", font=("Arial",28), bg="white", fg="black", width="50", height="1").pack()
Etiqueta_1 = Label(root,text="Registrarte",font=("Arial",8),bg="white",fg="#2d572c").place(x=650,y=5)
Entry_2 = Entry(root,width=30)

Entry_2.place(x=100,y=110)


Etiqueta_3 = Label(root,text="Nombre de usuario",font=("Arial",15),bg="white").place(x=100,y=68)

Etiqueta_4 = Label(root,text="Correo Electronico",font=("Arial",15),bg="white",).place(x=100,y=150)
Entry_3 = Entry(root,width=30)

Entry_3.place(x=100,y=200)
Etiqueta_5 = Label(root,text="contraseña",font=("Arial",15),bg="white").place(x=100,y=260)
root.config(bg="white")
Entry_4 = Entry(root,width=30)

Entry_4.place(x=100,y=300)
Etiqueta_6 = Label(root,text="Direccion",font=("Arial",15),bg="white").place(x=100,y=360)
root.config(bg="white")
Entry_5 = Entry(root,width=30)

Entry_5.place(x=100,y=400)

frame_app = Frame(root, width=1000, height=250, bg="#2ac17e")
frame_app.place(x=0,y=450)

Imagen=PhotoImage(file="imagen.png")

Imagen_2 =Label(frame_app, image=Imagen,width=188,height=124)

Imagen_2.place(x=330, y=100)

boton1= Button(frame_app,text="Registrate",width="20", height="1",font=("arial",15),bg="black", fg="white",command=ingresar)
boton1.place(x=100,y=50)
boton2= Button(frame_app,text="Leer",width="20", height="1",font=("arial",15),bg="black", fg="white",command=mostrar_usuario)
boton2.place(x=550,y=50)

root.mainloop()
