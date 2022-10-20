import sqlite3
from typing import final

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria \n")
            print("1- Cargar Automovil")
            print("2- Modificar Automovil")
            print("3- Eliminar Automovil")
            print("4- Cargar disponibilidad")
            print("5- Listado de automoviles")
            print("6- Cargar Motocicleta")
            print("7- Actualizar precios")
            print("0- Salir de menu \n")
            nro = int(input("Por favor ingrese un número \n"))
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
                print("\n")
            if nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
                print("\n")
            if nro == 3:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                automovil_a_eliminar = Automovil(marca,modelo)
                automovil_a_eliminar.borrar_automovil()
                print("\n")
            if nro == 4:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre de la modelo: ")
                automovil_a_aumentar = Automovil(marca,modelo,cantidadDisponibles)
                automovil_a_aumentar.cargar_disponibilidad()
                print("\n")
            if nro == 5:
                Automovil.listado_automoviles()
                print("\n")
            if nro == 6:
                marca = input("Por favor ingrese la marca de la motocicleta: ")
                modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                precio = input("Por favor ingrese el precio de la motocicleta: ")
                cilindrada = input("Por favor ingrese la cilindrada la motocicleta: ")
                color = input("Por favor ingrese el color de la motocicleta: ")
                
                nueva_motocicleta = Motocicleta(marca,modelo,precio, cilindrada, color)
                nueva_motocicleta.cargar_motocicletas()
                print("\n")
            if nro == 7:
                Motocicleta.pasar_historico()
                Motocicleta.actualizar_precios(self)
                print("\n")
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def crearTablasMoto(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio INTEGER, cilindrada VARCHAR(30), color VARCHAR(30), fechaUltimoPrecio DATETIME DEFAULT CURRENT_TIMESTAMP)")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def crearTablasMoto_H(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETAS (id_moto INTEGER , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio INTEGER, cilindrada VARCHAR(30), color VARCHAR(30), fechaUltimoPrecio DATETIME)")
        conexion.miConexion.commit()
        conexion.cerrarConexion()


class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    
    def borrar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES WHERE marca='{}' and modelo='{}'" .format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Automovil eliminado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()


    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  


    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
    

    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles+1 where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil actualizado exitosamente")
        except:
            print("Error al actualizar la disponibilidad")
        finally:
            conexion.cerrarConexion()
        
    @classmethod
    def listado_automoviles(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()
            for auto in autos:
                id,marca,modelo,precio,cantidadDisponible = auto
                print("El auto con ID: "+str(id)+" marca: "+str(marca)+ " modelo: "+str(modelo)+" precio: "+str(precio)+" cantidad: "+str(cantidadDisponible))
        except:
            print("Error")
        finally:
            conexion.cerrarConexion()
                

    # -------------------------------------------------------------------------
    #                                Motocicletas
    # -------------------------------------------------------------------------


class Motocicleta:
    def __init__(self, marca, modelo, precio, cilindrada, color, fechaUltimoPrecio=None):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cilindrada = cilindrada
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio

    
    def cargar_motocicletas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(marca,modelo,precio,cilindrada,color) VALUES('{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.precio,self.cilindrada,self.color))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
        except:
            print("Error al agregar la motocicleta")
        finally:
            conexion.cerrarConexion()
    

    def actualizar_precios(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio=precio+precio*0.1")
            conexion.miConexion.commit()
            print("Motocicletas actualiza exitosamente")
        except:
            print("Error")
        finally:
            conexion.cerrarConexion()

    @classmethod
    def listado_motocicletas(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motos = conexion.miCursor.fetchall()
            for moto in motos:
                id,marca,modelo,precio,cilindrada,color,fechaUltimoPrecio = moto
                print("La moto con ID: "+str(id)+" marca: "+str(marca)+ " modelo: "+str(modelo)+" precio: "+str(precio)+" cilindrada: "+str(cilindrada)+" color "+str(color)+" fecha: "+str(fechaUltimoPrecio))
        except:
            print("Error")
        finally:
            conexion.cerrarConexion()
    
    @classmethod
    def pasar_historico(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motos = conexion.miCursor.fetchall()
            for moto in motos:
                id,marca,modelo,precio,cilindrada,color,fechaUltimoPrecio = moto
                conexion.miCursor.execute("INSERT INTO HISTORICO_MOTOCICLETAS (id_moto, marca, modelo, precio, cilindrada, color, fechaUltimoPrecio) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(id,marca,modelo,precio,cilindrada,color,fechaUltimoPrecio))
            conexion.miConexion.commit()
        except:
            print("Ha ocurrido un error al pasar los historiales")
        finally:
            conexion.cerrarConexion


class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablasMoto()
programa.crearTablasMoto_H()
programa.menu()