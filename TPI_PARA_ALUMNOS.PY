import sqlite3
from typing import final
from Automoviles import Automovil
from Motocicletas import Motocicleta
from Conexiones import Conexiones

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
            print("8- Buscar registros de motocicletas anteriores a una Fecha")
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
                modelo = input("Por favor ingrese el nombre del modelo: ")
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
            if nro == 8:
                fechaAIngresar = input("Ingrese una fecha para buscar los registros con el formato: 'año-mes-dia': ")
                Motocicleta.listado_fechas(fechaAIngresar)
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
     
programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablasMoto()
programa.crearTablasMoto_H()
programa.menu()