import csv
import json
import modulos.menu as mm

def csv_to_json(csv_file, json_file):
    data = []
    # Lee el archivo CSV y guarda los datos en la lista
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Escribe los datos en un archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Nombre del archivo CSV de entrada
csv_file = 'data/inventariodatos.csv'

# Nombre del archivo JSON de salida
json_file = 'invent.json'

# Llama a la función para convertir CSV a JSON
csv_to_json(csv_file, json_file)

print("Conversion completa.")


#trabajar con la datos agregar,editar,buscar,borrar,

def cargar_activos():
    try:
        with open('invent.json', 'r') as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = []
    return inventario

def guardar_activos(activos):
    with open('invent.json', 'w') as archivo:
        json.dump(activos, archivo, indent=4)


def addactivo(activos, identificacion):
    #codigo de transaccion
    while True:
        try:
            codtransaccion = input('ingrese el codigo de transacción: ')    
        except ValueError:
            print('Ingrese datos numericos :')
        break
    #numero de formulario
    while True:   
        try:
                numform = input('ingrese el Número de formulario: ')
        except ValueError:
                print('Ingrese datos numericos :')
        break

    #marca
    y = True
    while y:
        listel = [1, 2, 3, 4, 5, 6, 7]
        try:
            opciones = print('1.LG\n2.COMPUMAX\n3.LOGITECH\n4.BENQ\n5.ASUS\n6.LENOVO\n7.HP')
            op = int(input('Ingrese el número de la opcion de la marca la cual desea determinar para el activo: '))
            if not(op in listel):
                return opciones
        except ValueError:
            print('Dato inválido')
            return opciones
        else:
            if op == 1:
                marca="LG"
            elif op == 2:
                marca="COMPUMAX"
            elif op == 3:
                marca="LOGITECH"
            elif op == 4:
                marca="BENQ"
            elif op == 5:
                marca="ASUS"
            elif op == 6:
                marca="LENOVO"
            elif op == 7:
                marca="HP"
            y=False
    #categorias
    W = True
    while W:
        listel = [1, 2, 3]
        try:
            opciones = print('1.EQUIPO DE COMPUTO\n2.ELECTRODOMESTICO\n3.JUEGO')
            op = int(input('Ingrese el número de la opcion de la categoria la cual desea determinar para el activo: '))
            if not(op in listel):
                return opciones
        except ValueError:
            print('Dato inválido')
            return opciones
        else:
            if op == 1:
                ctgoria="EQUIPO DE COMPUTO"
            elif op == 2:
                ctgoria="ELECTRODOMESTICOS"
            elif op == 3:
                ctgoria="JUEGO"
            W=False
    #valor unitario
    while True:   
        try:
                v_unit = float(input('ingrese el valor por la unidad: '))
        except ValueError:
                print('Ingrese datos numericos: ')
        break
    #tipo de activo y al mismo tiempo codigo de barras alfanumerico
    T = True
    while T:
        listel = [1, 2, 3, 4, 5, 6, 7]
        try:
            opciones = print('1.Monitor\n2.CPU\n3.Teclado\n4.Mouse\n5.Aire Acondicionado\n6.Portatil\n7.Impresora')
            op = int(input('Ingrese el número de la opcion del tipo de activo: '))
            if not(op in listel):
                return opciones
        except ValueError:
            print('Dato inválido')
            return opciones
        else:
            if op == 1:
                tp="Monitor"
                tps= "mon"
                num_bar = str(input("ingrese el codigo del activo"))
                codbar = tps + num_bar
            elif op == 2:
                tp="CPU"
                tps= "cp"
                num_bar = str(input("ingrese el codigo del activo"))
                codbar = tps + num_bar
            elif op == 3:
                tp="Teclado"
                tps= "te"
                num_bar = str(input("ingrese el codigo del activo"))
                codbar = tps + num_bar
            elif op == 4:
                tp="Mouse"
                tps= "mou"
                num_bar = str(input("ingrese el codigo del activo"))
                codbar = tps + num_bar
            elif op == 5:
                tp="Aire Acondicionado"
                tps= "aac"
                num_bar = str(input("ingrese el codigo del activo"))
                codbar = tps + num_bar
            elif op == 6:
                tp="Portatil"
                tps= "port"
                num_bar = str(input("ingrese el codigo del activo"))
                codbar = tps + num_bar
            elif op == 7:
                tp="Impresora"
                tps= "imp"
                num_bar = str(input("ingrese el codigo del activo"))
                codbar = tps + num_bar
            T=False
    #proveedor
    proveedor = input("ingrese el nombre del proveedor: ")
    #numero de serial 
    numserial= input("ingrese el numero de serial correctamente:  ")
    #nombre de la empresa responsable
    empresa_responsable =input("ingrese el nombre de la empresa responsable: ")
    #tipo de estado
    E = True
    while E:
        listel = [0, 1, 2, 3]
        try:
            opciones = print('0.noasignado\n1.asignado\n2.dado de baja por daños\n3.en reparacion y/o garantia')
            op = int(input('Ingrese el número de la opcion del estado del activo: '))
            if not(op in listel):
                return opciones
        except ValueError:
            print('Dato inválido')
            return opciones
        else:
            if op == 0:
                est="0"
            elif op == 1:
                est="1"
            elif op == 2:
                est="2"
            elif op == 3:
                est="3"
            E =False
    #codigo de barras representado numericamente
    #nombre
    nombre =input("ingrese el nombre del activo (descripcion): ")
    

    nuevo_activo = {
        "CodTransaccion": codtransaccion,
        "NroFormulario": numform,
        "codcampus": codbar,
        "Marca": marca,
        "categoria":ctgoria ,
        "tipo": tp,
        "valor unitario": v_unit ,
        "Proveedor": proveedor,
        "NroSerial": numserial,
        "EmpresaResponsable": empresa_responsable,
        "Estado": est,
        #"Ubicacion": "",
        "Nombre": nombre,
        "codebar": codbar, 
    }
    print("el activo ha sido guardado exitosamente.")
    activos = cargar_activos()
    activos.append(nuevo_activo)
    guardar_activos(activos)
    mm.pausar_pantalla()
    mm.secondmenu(activos,identificacion) 
    
  
def buscar_activo(activos, identificacion):
    identificacion = input('escriba el codigo del campus del activo:\n')
    for activo in activos:
        if activo["codcampus"] == identificacion:
            return activo
    return None

def editar_activo(activos, identificacion):
    activo = buscar_activo(activos, identificacion)
    if activo:
        print("Información actual del activo:")
        print(activo)
        list_categoria = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        try:
            campo_act = int(input("¿Qué campo desea editar? \n1. Codigo de transacción\n2. Numero de formulario\n3. Marca\n4. Categoria\n5. Tipo\n6. Valor unitario\n7. Proveedor\n8. Numero serial\n9. Empresa responsable\n10. Estado\n --> "))
        except ValueError:
            print("ingrese un valor numerico. ")
            if  not(campo_act in list_categoria):
                return editar_activo(activos, identificacion)
            
        if campo_act == 1:
            nuevo_valor = input("Ingrese el Codigo de transacción: ")
            activo["codtransaccion"] = nuevo_valor
        elif campo_act == 2:
            nuevo_valor = input("Ingrese el nuevo numero de formulario: ")
            activo["numform"] = nuevo_valor
        elif campo_act == 3:
            y = True
            while y:
                listel = [1, 2, 3, 4, 5, 6, 7]
                try:
                    opciones = print('1.LG\n2.COMPUMAX\n3.LOGITECH\n4.BENQ\n5.ASUS\n6.LENOVO\n7.HP\n')
                    op = int(input('Ingrese el número de la opcion de la marca la cual desea determinar para el activo. '))
                    if not(op in listel):
                        return opciones
                except ValueError:
                    print('Dato inválido')
                    return opciones
                else:
                    if op == 1:
                        activo["Marca"]="LG"
                    elif op == 2:
                        activo["Marca"]="COMPUMAX"
                    elif op == 3:
                        activo["Marca"]="LOGITECH"
                    elif op == 4:
                        activo["Marca"]="BENQ"
                    elif op == 5:
                        activo["Marca"]="ASUS"
                    elif op == 6:
                        activo["Marca"]="LENOVO"
                    elif op == 7:
                        activo["Marca"]="HP"
                    y=False
        elif campo_act == 4:
            W = True
            while W:
                listel = [1, 2, 3]
                try:
                    opciones = print('1.EQUIPO DE COMPUTO\n2.ELECTRODOMESTICO\n3.JUEGO\n')
                    op = int(input('Ingrese el número de la opcion de la categoria la cual desea determinar para el activo. '))
                    if not(op in listel):
                        return opciones
                except ValueError:
                    print('Dato inválido')
                    return opciones
                else:
                    if op == 1:
                        activo["categoria"]="EQUIPO DE COMPUTO"
                    elif op == 2:
                        activo["categoria"]="ELECTRODOMESTICOS"
                    elif op == 3:
                        activo["categoria"]="JUEGO"
                    W=False                  
        #tipo
        elif campo_act==5:
            T = True
            while T:
                listel = [1, 2, 3, 4, 5, 6, 7]
                try:
                    opciones = print('1.Monitor\n2.CPU\n3.Teclado\n4.Mouse\n5.Aire Acondicionado\n6.Portatil\n7.Impresora\n')
                    op = int(input('Ingrese el número de la opcion del tipo de activo. '))
                    if not(op in listel):
                        return opciones
                except ValueError:
                    print('Dato inválido')
                    return opciones
                else:
                    if op == 1:
                        activo["tipo"]="Monitor"
                    elif op == 2:
                        activo["tipo"]="CPU"
                    elif op == 3:
                        activo["tipo"]="Teclado"
                    elif op == 4:
                        activo["tipo"]="Mouse"
                    elif op == 5:
                        activo["tipo"]="Aire Acondicionado"
                    elif op == 6:
                        activo["tipo"]="Portatil"
                    elif op == 7:
                        activo["tipo"]="Impresora"
                    T=False            
        #valor unitario
        elif campo_act==6:
            nuevo_valor = input("Ingrese el valor unitario: ")
            activo["valor unitario"] = nuevo_valor
        #nombre del proveedor
        elif campo_act == 7:
            nuevo_valor = input("Ingrese el nombre del proveedor: ")
            activo["Proveedor"] = nuevo_valor
        #numero serial  
        elif  campo_act == 8:
              nuevo_valor = input("ingrese el numero de serial correctamente: -> ")
              activo["NroSerial"] = nuevo_valor
        #Empresa Responsabele       
        elif campo_act == 9:
            nuevo_valor = input("Ingrese el nombre de la empresa responsable: ")
            activo["EmpresaResponsable"] = nuevo_valor
        #estado
        elif campo_act == 10:
            E = True
            while E:
                listel = [0, 1, 2, 3]
                try:
                    opciones = print('0.noasignado\n1.asignado\n2.dado de baja por daños\n3.en reparacion y/o garantia\n')
                    op = int(input('Ingrese el número de la opcion del estado del activo. '))
                    if not(op in listel):
                        return opciones
                except ValueError:
                    print('Dato inválido')
                    return opciones
                else:
                    if op == 0:
                        activo["Estado"] ="0"
                    elif op == 1:
                        activo["Estado"]="1"
                    elif op == 2:
                        activo["Estado"]="2"
                    elif op == 3:
                        activo["Estado"]="3"
                    E =False
        else:
            print("Campo inválido.")
            return
#-----------------------------------------------------------------------------------------#
        # Guardar los cambios en el archivo
        guardar_activos(activos)
        
        print("Información de la activo actualizada correctamente.")
    else:
        print("No se encontró ninguna activo con ese número de identificación.")
    mm.secondmenu(activos, identificacion)
    
def eliminar_activo(activos, identificacion):
    activo = buscar_activo(activos, identificacion)
    if activo:
        print("codigo de campus del activo a eliminar:")
        print(activo)
        activos.remove(activo)  
        guardar_activos(activos)  
        print("El activo ha sido eliminado")
    
def mostrar_activo(activos, identificacion):
    activo = buscar_activo(activos, identificacion)
    print(activo)
    


    






