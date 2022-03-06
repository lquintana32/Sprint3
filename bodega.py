import random
import time
#Los productos son vasos, cucharas, cuchillos y tenedores. Cada producto debe tener un stock aleatorio entre 300 y 500 unidades y una descripción del producto.
vasos = {"Nombre":"Vasos","Stock":random.randint(300,500),"Descripcion":"recipiente de tamaño variado​ que sirve para beber, contener o trasladar algo, por lo general líquido"}
cuchara = {"Nombre":"Cucharas","Stock":random.randint(300,500),"Descripcion":"utensilio que consiste en una pequeña cabeza cóncava en el extremo de un mango, usada principalmente para servir o comer un alimento"}
cuchillo = {"Nombre":"Cuchillos","Stock":random.randint(300,500),"Descripcion":"instrumento que se emplea para cortar; consta de una fina hoja metálica con uno o dos bordes afilados y de un mango por el cual se sostiene"}
tenedores = {"Nombre":"Tenedores","Stock":random.randint(300,500),"Descripcion":"utensilio de mesa que consta de un mango y una cabeza con dientes largos a modo de clavos"}

#Crear bodega virtual
productos =[]
productos.append(vasos)
productos.append(cuchara)
productos.append(cuchillo)
productos.append(tenedores)

#Debe definir funciones que puedan:
#Sumar y disminuir el número de unidades por producto
def aumentarStock():    #Pide datos por consola y de acuerdo al nombre del prodcuto agrega stock
    n = input('ingrese nombre: ').capitalize()
    s = int(input('ingrese stock a sumar: '))    
    global productos
    for x in productos:
        if x["Nombre"]==n:
            x["Stock"]=x["Stock"]+s
    print()
def disminuirStock():   ##Pide datos por consola y de acuerdo al nombre del prodcuto disminuye stock
    n = input('ingrese nombre: ').capitalize()  #Usa capitalize() para unificar el formato del texto
    s = int(input('ingrese stock a disminuir: '))    
    global productos
    for x in productos:
        if x["Nombre"]==n:
            x["Stock"]=x["Stock"]-s
    print()
#Agregar nuevos productos
def agregarProducto():  #Solicita datos para crear producto en formato diccionario y agregar a lista productos
    n = input('Ingrese nombre de producto: ').capitalize()
    s = int(input('Ingrese cantidad de stock: '))
    d = input('Ingrese uns descripcion del producto: ')
    global productos
    productos.append({"Nombre":n,"Stock":s,"Descripcion":d})
    print()
#Quitar productos de la bodega virtual
def eliminarProducto(): #Solicita nombre de producto para eliminarlo de la lista
    global productos
    n = input('Ingrese nombre de producto que quiere eliminar: ').capitalize()
    for x in range(0,len(productos)-1):
        if productos[x]["Nombre"]==n:
            productos.pop(x)
    print()
#Mostrar todos los productos disponibles y su stock. Debe tener un desfase de un segundo entre cada producto
def mostrarStock(): #Muestra nombre y stock cada 1 segundo
    global productos
    for x in productos:
        print(x["Nombre"], x["Stock"])
        time.sleep(1)
    print() 
#Verificar si un producto tiene menos de 400 unidades y enviar una alerta
def alerta():   #En caso de tener menos de 400 en stock, muestra alerta
    global productos
    for x in productos:
        if x["Stock"]<400:
            print('**** El producto',x["Nombre"],'tiene stock menor a 400 ****') 
            time.sleep(1)
    print()
opcion = 0 #Variable numerica que permite navegar en el menu
while opcion!= 7:
    print('1. mostrar stock \n2. aumentar stock \n3. disminuir stock \n4. agregar producto \n5. eliminar producto \n6. revisar stock \n7. salir')
    opcion = int(input('ingrese opcion: \n'))
    if opcion == 1:
        mostrarStock()
    elif opcion == 2:
        aumentarStock()
    elif opcion == 3:
        disminuirStock()
    elif opcion == 4:
        agregarProducto()
    elif opcion == 5:
        eliminarProducto()
    elif opcion == 6:
        alerta()
    elif opcion == 7:
        opcion = 7




