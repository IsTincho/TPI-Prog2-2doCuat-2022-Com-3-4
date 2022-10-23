import sqlite3
from typing import final
from Conexiones import Conexiones

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
            print("Motocicletas actualizadas exitosamente")
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

    @classmethod
    def listado_fechas(cls,fechaAIngresar):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS WHERE fechaUltimoPrecio <= '{}'".format(fechaAIngresar))
            motos = conexion.miCursor.fetchall()
            for moto in motos:
                id,marca,modelo,precio,cilindrada,color,fechaUltimoPrecio = moto
                print("La moto con ID: "+str(id)+" marca: "+str(marca)+ " modelo: "+str(modelo)+" precio: "+str(precio)+" cilindrada: "+str(cilindrada)+" color "+str(color)+" fecha: "+str(fechaUltimoPrecio))
        except:
            print("Error no se han encontrado registros anteriores a esa fecha")
        finally:
            conexion.cerrarConexion()