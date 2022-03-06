#Debe crear una base de datos que tenga información de clientes: ID, nombre, apellido, edad y contraseña. Cree 4 clientes iniciales para probar el programa
cl1={"ID":1001,"Nombre":"Michael","Apellido":"Scott","Edad":40,"Contraseña":"clave1"}
cl2={"ID":1002,"Nombre":"Jim","Apellido":"Halpert","Edad":28,"Contraseña":"clave2"}
cl3={"ID":1003,"Nombre":"Pam","Apellido":"Beesley","Edad":26,"Contraseña":"clave3"}
cl4={"ID":1004,"Nombre":"Dwight","Apellido":"Schrute","Edad":43,"Contraseña":"clave4"}

clientes = []
clientes.append(cl1)
clientes.append(cl2)
clientes.append(cl3)
clientes.append(cl4)

#Diseñe tres funciones
#Agregar nuevos clientes
def agregarCliente():
    global clientes #Permite que los metodos interactuen con las variables locales
    global nuevaId  #Variable que asigna ID correlativo al nuevo cliente agregado
    nombre = input('Ingrese nombre de nuevo cliente: ').capitalize()
    apellido = input('Ingrese apellido de nuevo cliente: ').capitalize()
    edad = int(input('Ingrese edad de nuevo cliente: '))
    contra = input('Ingrese contraseña de nuevo cliente: ')
    clientes.append({"ID":nuevaId,"Nombre":nombre,"Apellido":apellido,"Edad":edad,"Contraseña":contra})

    print()
# eliminar clientes según ID
def eliminarCliente(ide):
    global clientes
    for x in range(0,len(clientes)): #Elimina cliente segun ID entregada como parametro a la funcion
        if clientes[x]["ID"]==ide:
            clientes.pop(x)
    print()
#mostrar toda la información por cliente
def mostrarInfo(lista):
    for x in lista:
        print(x)
    print()
opcion = 0
nuevaId = clientes[-1]["ID"]+1
while opcion!=4:
    print('1. agregar cliente \n2. eliminar clientes según ID \n3. mostrar toda la información por cliente \n4. salir')
    opcion = int(input('ingrese opcion: \n'))
    if opcion == 1:
        agregarCliente()
        nuevaId+=1
    elif opcion == 2:
        ide = int(input('Ingrese ID que desea eliminar: '))
        eliminarCliente(ide)
    elif opcion == 3:
        mostrarInfo(clientes)
    elif opcion ==4:
        opcion = 4