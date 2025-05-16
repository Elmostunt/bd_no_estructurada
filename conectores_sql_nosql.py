#from pymongo import MongoClient
import pymysql 

#client = MongoClient("mongodb://localhost:27017/")
#db = client["publicaciones"]
#coleccion = db["publicaciones"]

host = "localhost"
user = "root"
password = "Montero123"
bd = "USUARIOS_PUB"
conexion = pymysql.connect(host=host,user=user,password=password,database=bd)

                            
nombre= input("Ingrese su nombre de usuario")
contraseña =input("ingrese su contraseña")
with conexion.cursor() as cursor:   
    #sql_insert = "INSERT INTO usuarios (`username`, `password`) VALUES (%s,%s)"
    #insert2= "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    sql_select ="SELECT * FROM usuarios WHERE username = %s AND password = %s"    
    usuario = cursor.execute(sql_select,(nombre,contraseña))
    print(usuario)
    usuario = cursor.fetchall()
    print(usuario)
    username = usuario[0][1]
    print(username)
conexion.commit()
