import json
import modulos.menu as mm
def vali_num_enteros():
    try:
        x=int(input('->'))
        return x
    except ValueError:
        print('numero no valido')
        return vali_num_enteros()

def cargar_zonas():
    try:
        with open('zonas.json', 'r') as archivo:
            zonas = json.load(archivo)
    except FileNotFoundError:
        zonas = []
    return zonas

def guardar_zonas(zonas):
    with open('zonas.json', 'w') as archivo:
        json.dump(zonas, archivo, indent=4)

def addzonas(zonas,identificacion):
    num_zona=input('Ingrese el número de zona: ')
        
    nombre = input('Ingrese el nombre: ')
    print('Ingrese la capacidad: ')
    total_capacidad= vali_num_enteros()
    


    # Crea un diccionario para la nueva zona
    nueva_zona = {
        "num_identificacion": num_zona,
        "nombre": nombre,
        "capacidad":total_capacidad,
        "asignaciones": []
    }
    
    # Carga las zonas existentes del archivo
    zonas = cargar_zonas()
    
    # Agrega la nueva zona a la lista de zonas
    zonas.append(nueva_zona)
    
    # Guarda la lista actualizada de zonas en el archivo
    guardar_zonas(zonas)
    mm.menutres(zonas, identificacion)

def buscar_zona(zonas, identificacion):
    identificacion=input('escriba el numero de identificacion:\n')
    for zona in zonas:
        if zona["num_identificacion"] == identificacion:
            return zona
    return None


def editar_zona(zonas, identificacion):
    zona = buscar_zona(zonas, identificacion)
    if zona:
        print("Información actual de la zona:")
        print(zona)
        
        campo = input("¿Qué campo desea editar? (nro zona/nombre/capacidad): ").lower()
        
        if campo == "nro zona":
            nuevo_valor = input("Ingrese el nuevo nro zona: ")
            zona["num_identificacion"] = nuevo_valor
        elif campo == "nombre":
            nuevo_valor = input("Ingrese el nuevo nombre: ")
            zona["nombre"] = nuevo_valor
        elif campo == "capacidad":
            nuevo_valor = int(input("Ingrese el nuevo número capacidad: "))
            zona["capacidad"] = nuevo_valor
        else:
            print("Campo inválido.")
            return
        
        # Guardar los cambios en el archivo
        guardar_zonas(zonas)
        
        print("Información de la zona actualizada correctamente.")
    else:
        print("No se encontró ninguna zona con ese número de identificación.")
    mm.menutres(zonas, identificacion)

def eliminar_zona(zonas, identificacion):
    zona = buscar_zona(zonas, identificacion)
    if zona:
        print("Información de la zona a eliminar:")
        print(zona)
        zonas.remove(zona)  # Elimina la zona de la lista
        guardar_zonas(zonas)  # Guarda los cambios en el archivo
        print("La información de la zona ha sido eliminada.")
        mm.menutres(zonas, identificacion)

def mostrar_zona(zonas,identificacion):
    zona = buscar_zona(zonas, identificacion)
    print(zona)
    mm.pausar_pantalla()
    mm.menutres(zonas, identificacion)





