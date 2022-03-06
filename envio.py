b1 = {"Bodega":"Bodega A","Unidades":300}
b2 = {"Bodega":"Bodega B","Unidades":300}
bodegas=[]
bodegas.append(b1)
bodegas.append(b2)

def enviar(kilometros,cantidad):
    global bodegas
    if kilometros <=1000:
        if bodegas[0]["Unidades"]+cantidad > 500:
            print('Supera maxima capacidad de unidades, quedaria con',bodegas[0]["Unidades"]+cantidad, "no puede superar los 500")
        else:
            bodegas[0]["Unidades"]=bodegas[0]["Unidades"]+cantidad
    else:
        if bodegas[1]["Unidades"]+cantidad > 500:
            print('Supera maxima capacidad de unidades, quedaria con',bodegas[1]["Unidades"]+cantidad, "no puede superar los 500")
        else:
            bodegas[1]["Unidades"]=bodegas[1]["Unidades"]+cantidad

opcion = ""
while opcion !="salir":
    k = int(input('ingrese cantidad de kilometros: '))
    c = int(input('Ingrese cantidad de unidades a enviar: '))
    enviar(k,c)
    for x in bodegas:
        print(x)
    opcion = input('Escriba salir para finalizar: ').lower()
