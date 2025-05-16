def menu():
    quiere_seguir = True
    lista_clientes = []
    lista_vehiculos = []
    while quiere_seguir == True:
        print("bienveido al programa de manteniminteo de vehiculos")
        print("opcion 1 registrar_clientes")
        print("opcion 2 : buscar_cliente")
        print("opcion 3 registrar_vehiculos")
        print("opcion 4 calcular_total")
        print("opcion 5 eliminar_vehiculo")
        print("opcion 6 vehiculo mas caro")
        print("opcion 7 salir")
        opcion_a_ejecutar = input("Ingrese opcion : ")
        if opcion_a_ejecutar == "1":
            lista_clientes = registrar_cliente(lista_clientes)
            print(lista_clientes)
        elif opcion_a_ejecutar == "2":
            telefono = input("Ingrese el telefono a buscar")
            buscar_cliente(lista_clientes, telefono)
        # Una vez que hace alguna funcion pregunta si quiere seguir
        seguir = input("quiere seguir 1.-si 2.-no")
        if seguir == "1":
            quiere_seguir = True
        else:
            quiere_seguir= False
        print("hola")

def registrar_cliente(lista_clientes):
    for a in range(5):
        dic={}
        dic["nombre"] = input("Ingrese nombre")
        dic["telefono"] = input("ingrese telefono")
        lista_clientes.append(dic)
    return lista_clientes

def buscar_cliente(lista_clientes, telefono):
    for a in lista_clientes:
        if a["telefono"] == telefono:
            print("Telefono encontrado , usuarios es ",a["nombre"])
            
def funcion4():
    print("hola")
def funcion5():
    print("hola")
def funcion6():
    print("hola")
def funcion7():
    print("hola")
    
menu()