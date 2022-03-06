b1 = {"Bodega":"Bodega A","Unidades":300}
b2 = {"Bodega":"Bodega B","Unidades":300}
bodegas=[]
bodegas.append(b1)
bodegas.append(b2)

def enviar(kilometros,cantidad):       #El sistema de envío debe ser un programa que pregunta qué tipo de envío es necesario (Rápido o largo)
    global bodegas
    if kilometros <=1000:  #Envio rapido
        if bodegas[0]["Unidades"]+cantidad > 500:   #Consulta si las unidades son menores a 500
            print('Supera maxima capacidad de unidades, quedaria con',bodegas[0]["Unidades"]+cantidad, "no puede superar los 500")
        else:
            bodegas[0]["Unidades"]=bodegas[0]["Unidades"]+cantidad
    else:   #Envio lento
        if bodegas[1]["Unidades"]+cantidad > 500:  #Consulta si las unidades son menores a 500
            print('Supera maxima capacidad de unidades, quedaria con',bodegas[1]["Unidades"]+cantidad, "no puede superar los 500")
        else:
            bodegas[1]["Unidades"]=bodegas[1]["Unidades"]+cantidad

opcion = "" #Variable que permite cerrar el ciclo while
while opcion !="salir":
    k = int(input('ingrese cantidad de kilometros: '))
    c = int(input('Ingrese cantidad de unidades a enviar: '))
    enviar(k,c) #Metodo que permite evaluar tipo de envio (largo o corto)
    for x in bodegas:   #muestra en cada iteracion la cantidad de unidades por bodega
        print(x)
    opcion = input('Escriba salir para finalizar: ').lower()
