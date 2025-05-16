from pymongo import MongoClient
import pymysql


def buscar_por_autor(db):
    coleccion = db["posts"]
    autor_a_buscar = input("Ingrese el autor a buscar")
    lista_resultado = coleccion.find({"autor":str(autor_a_buscar)})
    #cliente = coleccion.find_one({"nombre": "Ana"})
    for a in lista_resultado:
        print(a)
    
def insertar_varios_docs(db):
    coleccion = db["posts"]
    lista = []
    cuantos_usuarios = int(input("Ingrese la cantidad de documetnos qe guardará"))
    for a in range(cuantos_usuarios):
        publicacion = { "titulo":input("Ingrese el titulo de la publicacion"),
                "descripcion":input("ingrese la descripcion de la publicacion"),
                "autor":input("ingrese el autor de la publicacion")}
        lista.append(publicacion)
    coleccion.insert_many(lista)
        

def insertar_publicacion(db):
    coleccion = db["posts"]
    publicacion = { "titulo":input("Ingrese el titulo de la publicacion"),
                "descripcion":input("ingrese la descripcion de la publicacion"),
                "autor":input("Ingrese el autor del libro")}
    coleccion.insert_one(publicacion)

def ver_publicaciones(db):
    coleccion = db["posts"]
    lista = coleccion.find()
    for a in lista:
        print(a)

def iniciar_sesion(conexion):
    nombre= input("Ingrese su nombre de usuario")
    contraseña =input("ingrese su contraseña")
    with conexion.cursor() as cursor:   
        sql_select ="SELECT * FROM usuarios WHERE username = %s AND password = %s"    
        usuario = cursor.execute(sql_select,(nombre,contraseña))
        print(usuario)
    conexion.commit()
    if usuario >= 1 :
        return True

def crear_usuario(conexion):
    nombre= input("Ingrese su nombre de usuario")
    contraseña =input("ingrese su contraseña")
    with conexion.cursor() as cursor:   
        sql_insert = "INSERT INTO usuarios (`username`, `password`) VALUES (%s,%s)"
        usuario = cursor.execute(sql_insert,(nombre,contraseña))
        print(usuario)
    conexion.commit()
    
    
def menu():
    while True:
        ## Habilito conexion con Mysql
        host = "localhost"
        user = "root"
        password = "Montero123"
        conexion = pymysql.connect(host=host,
                                   user=user,
                                   password=password,
                                   database="USUARIOS_PUB")
        # Habilito Conexion con Mongo DB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["publicaciones"]
        while True:
            opcion1= input("Bienvenido al publicador, 1: Crear user 2: Inciar sesion")
            if opcion1 =="1":
                crear_usuario(conexion)
            if opcion1 =="2":
                sesion_activa = False
                sesion_activa = iniciar_sesion(conexion)
                if sesion_activa == True: #Inicie sesion
                    while True:
                        print("Bienvenido al publicador de post")
                        print("Ingrese opcion")
                        print("1.- Insertar publicacion")
                        print("2.- Ver publicaciones")
                        print("3.- Agregar Varios")
                        print("4.- Buscar por autor")
                        opcion = input()
                        if opcion == "1":
                            insertar_publicacion(db)
                        elif opcion == "2":
                            ver_publicaciones(db)
                        elif opcion == "3":
                            insertar_varios_docs(db)
                        elif opcion =="4":
                            buscar_por_autor(db)
                        else:
                            print("chao")
                            break
                else:
                    iniciar_sesion(conexion)

menu()