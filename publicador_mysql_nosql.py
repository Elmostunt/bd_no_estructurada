from pymongo import MongoClient
import pymysql

def input_validado(mensaje, tipo="str"):
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("Este campo no puede estar vacío. Inténtelo nuevamente.")
            continue
        if tipo == "int":
            if not entrada.isdigit():
                print("Debe ingresar un número válido.")
                continue
            return int(entrada)
        return entrada

def buscar_por_autor(db):
    coleccion = db["posts"]
    autor_a_buscar = input_validado("Ingrese el autor a buscar: ")
    lista_resultado = coleccion.find({"autor": autor_a_buscar})
    encontrado = False
    for a in lista_resultado:
        print(a)
        encontrado = True
    if not encontrado:
        print("No se encontraron publicaciones para ese autor.")

def insertar_varios_docs(db):
    coleccion = db["posts"]
    lista = []
    cuantos_usuarios = input_validado("Ingrese la cantidad de documentos que guardará: ", tipo="int")
    
    for _ in range(cuantos_usuarios):
        titulo = input_validado("Ingrese el título de la publicación: ")
        descripcion = input_validado("Ingrese la descripción de la publicación: ")
        autor = input_validado("Ingrese el autor de la publicación: ")

        publicacion = {
            "titulo": titulo,
            "descripcion": descripcion,
            "autor": autor
        }
        lista.append(publicacion)

    coleccion.insert_many(lista)
    print(f"{len(lista)} publicaciones insertadas correctamente.")

def insertar_publicacion(db):
    coleccion = db["posts"]
    titulo = input_validado("Ingrese el título de la publicación: ")
    descripcion = input_validado("Ingrese la descripción de la publicación: ")
    autor = input_validado("Ingrese el autor de la publicación: ")

    publicacion = {
        "titulo": titulo,
        "descripcion": descripcion,
        "autor": autor
    }
    coleccion.insert_one(publicacion)
    print("Publicación insertada correctamente.")

def ver_publicaciones(db,username):
    coleccion = db["posts"]
    lista = coleccion.find({"autor":username})
    contador = 0
    for a in lista:
        print(a)
        contador += 1
    if contador == 0:
        print("No hay publicaciones registradas.")

def iniciar_sesion(conexion):
    nombre = input_validado("Ingrese su nombre de usuario: ")
    contraseña = input_validado("Ingrese su contraseña: ")

    with conexion.cursor() as cursor:
        sql_select = "SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s"
        cursor.execute(sql_select, (nombre, contraseña))
        resultado = cursor.fetchone()
        print("resultado es" , resultado)
        for a in resultado:
            print(a)
    return resultado is not None, resultado[1]

def crear_usuario(conexion):
    nombre = input_validado("Ingrese su nombre de usuario: ")
    contraseña = input_validado("Ingrese su contraseña: ")

    with conexion.cursor() as cursor:
        sql_check = "SELECT * FROM usuarios WHERE nombre = %s"
        cursor.execute(sql_check, (nombre,))
        if cursor.fetchone():
            print("El nombre de usuario ya existe. Intente con otro.")
            return
        sql_insert = "INSERT INTO usuarios (nombre, contrasena) VALUES (%s, %s)"
        cursor.execute(sql_insert, (nombre, contraseña))
    conexion.commit()
    print("Usuario creado correctamente.")

def menu():
    try:
        # Conexión MySQL
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="Montero123",
            database="asignador"
        )
    except Exception as e:
        print("Error al conectar con MySQL:", e)
        return

    try:
        # Conexión MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["publicaciones"]
    except Exception as e:
        print("Error al conectar con MongoDB:", e)
        return

    while True:
        print("\nBienvenido al publicador")
        opcion1 = input_validado("1: Crear usuario | 2: Iniciar sesión | 3: Salir\nSeleccione opción: ")

        if opcion1 == "1":
            crear_usuario(conexion)

        elif opcion1 == "2":
            sesion_activa,username = iniciar_sesion(conexion)
            if sesion_activa:
                while True:
                    print("\n--- Menú Publicaciones ---")
                    print("1.- Insertar publicación")
                    print("2.- Ver publicaciones")
                    print("3.- Agregar varias publicaciones")
                    print("4.- Buscar por autor")
                    print("5.- Cerrar sesión")
                    opcion = input_validado("Seleccione opción: ")

                    if opcion == "1":
                        insertar_publicacion(db)
                    elif opcion == "2":
                        ver_publicaciones(db,username)
                    elif opcion == "3":
                        insertar_varios_docs(db)
                    elif opcion == "4":
                        buscar_por_autor(db)
                    elif opcion == "5":
                        print("Sesión cerrada.")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
            else:
                print("Credenciales incorrectas. Intente nuevamente.")

        elif opcion1 == "3":
            print("Adiós.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()