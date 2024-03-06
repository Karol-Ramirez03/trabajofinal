import json
import os
import sys

#definiciones de funciones utilizables...
def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")
    
def cargar_zonas():
    try:
        with open('zonas.json', 'r') as archivo:
            json1 = json.load(archivo)
    except FileNotFoundError:
        json1 = []
    return json1

def cargar_personas():
    try:
        with open('personas.json', 'r') as archivo:
            json2 = json.load(archivo)
    except FileNotFoundError:
        json2 = []
    return json2

def cargar_activos():
    try:
        with open('invent.json', 'r') as archivo:
            json3 = json.load(archivo)
    except FileNotFoundError:
        json3 = []
    return json3
    
def crear_asignacion(json1,json2,json3,personas,activos,zonas,asignaciones):
    #nueva asignación...
    
    numero_asignacion = int(input('Ingrese el número de asignacion '))
    fecha_asignacion = input('Ingrese la fecha en que se asigno el activo (Dia/Mes/Año)')
    #tipo de asignacion...
    opc_asignar=[1,2]
    try:
        print('1. personal\n2. zona')
        op= int(input('ingrese el tipo de asignacion: (1/2) '))
        if not(op in opc_asignar):
            print('tu opcion no esta disponible por favor vuelve a digitar la asignacion')
            crear_asignacion(json1,json2,json3,personas,activos,zonas,asignaciones)
    except ValueError:
        print('dato invalido, vuelve a digitar el activo')
        crear_asignacion(json1,json2,json3,personas,activos,zonas,asignaciones)
        
    # asignacion de activos a personas
    if op == 1:
        identificacion=int(input('escriba el numero de identificacion:\n'))
        for persona in personas:
            if  persona["num_identificacion"] == identificacion:
                identificacion_act = input('escriba el codigo del campus del activo:\n')
                for activo in activos:
                    if activo["codcampus"] == identificacion_act:
                        persona["asignaciones"]= {str(numero_asignacion):activo}
                        with open('personas.json', 'w') as result:
                            json.dump(personas, result, indent =4 )
                        with open('resultados.json', 'w') as result:
                            json.dump(personas, result, indent =4 )
                        

                            
                return None  
        return None

    #asignacion de activos a zonas
    if op == 2:
        identificacion=input('escriba el numero de identificacion de la zona:\n')
        bandera = True
        while bandera:
            for zona in zonas:
                if zona["num_identificacion"] == identificacion:
                    if len(zona["asignaciones"]) <= zona["capacidad"]:
                        identificacionproduct = input('escriba el codigo del campus del activo:\n')
                        for activo in activos:
                            if activo["codcampus"] == identificacionproduct:
                                zona["asignaciones"] = {str(numero_asignacion):activo},
                                #print(f'el numero de asignaciones en la zona es: {len(zona["asignaciones"])}')
                                with open('zonas.json', 'w') as result:
                                    json.dump(zonas, result, indent =4 )
                                with open('resultados.json', 'w') as result:
                                    json.dump(zonas, result, indent =4 )
                    else:
                        print('lo siento ya esta zona alcanzo su maxima capacidad')              
                    return None  
                else:
                    print('numero de identificacion de zona no encontrado. ')
                    pausar_pantalla()
            return None
        bandera=False
        
           
#buscador de asignaciones por zona o activo...    
def buscarasignaciones(asignaciones):
    with open('resultados.json', 'r') as archivo:
        personas = json.load(archivo)
    list_asignaciones = personas
    identificacion=input('escriba el numero de identificacion de la asignacion:\n')
    for asignacion in list_asignaciones:
        if  identificacion in asignacion.get("asignaciones",{}) :
            print(asignacion)
            pausar_pantalla()
        else: 
            print('no se encontro la asignacion. ')
            pausar_pantalla()
            

        
    
    
        
  
    

                    
            
             
            
        
        

# Activos:
#  NroActivo    


    
        
        
            
    
    
    
    