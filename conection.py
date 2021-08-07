
import mysql.connector
from tkinter import Tk, ttk
from tkinter import*
data=0


class MyDatabase:
    def open_connection(self):
        connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="navyportans")
        return connection

    def insert_db(self,nombre,correo,direccion,contraseña):
            my_connection = self.open_connection()
            cursor = my_connection.cursor()
            query = "INSERT INTO tbl_usuarios(NOMBRE, CORREO, CONTRASEÑA,DIRECCION) VALUES (%s,%s,%s,%s)"
            data = (nombre,correo,direccion,contraseña)
            cursor.execute(query, data)
           
            my_connection.commit()
            my_connection.close() 

    def read_db(self,nombre,correo,frame_caja):
        
       
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT * FROM TBL_USUARIOS "
        cursor.execute(query)  
        registro = 0      
        my_table = ttk.Treeview(frame_caja)


                    # Define Our Columns 
        my_table['columns'] = ('NOMBRE', 'CORREO')

                    # Formate Our Columns
        my_table.column('#0', width=120, minwidth=200)
        my_table.column('NOMBRE', anchor=W, width=200)
        my_table.column('CORREO', anchor=W, width=300)
        

                    # Create Headings
        my_table.heading('#0', text='ID_CAMPO', anchor=W)
        my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
        my_table.heading('CORREO', text='CORREo', anchor=W)
       
        my_table.place(x=1, y=1)   
       
        for fila in cursor:
            registro = registro + 1 
            print(str(registro) +" - "+ str(fila))
            ID_campo=fila   [0]
            nombre = fila[1]  
            correo = fila[2]
            
            my_table.insert(parent='', index='end', iid=registro, text=str(registro), 
            values=(nombre,  correo))
    def delete_db(self,nombre,correo,contraseña,direccion):
            my_connection = self.open_connection()
            cursor = my_connection.cursor()
            query = "DELETE FROM tbl_usuarios WHERE NOMBRE=%s and CORREO=%s and CONTRASEÑA=%s AND DIRECCION=%s"
            data = (nombre,correo,contraseña,direccion)
            cursor.execute(query,data)
         
            my_connection.commit()
            my_connection.close()        
       


    
    