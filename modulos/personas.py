import json

def cargar_personas():
    try:
        with open('personas.json', 'r') as archivo:
            personas = json.load(archivo)
    except FileNotFoundError:
        personas = []
    return personas
def guardar_personas(personas):
    with open('personas.json', 'r') as archivo:
        json.dump(personas, archivo, indent=4)

def addpersonas(personas):
    num_identificacion = input('ingrese el numero de identificacion (cc/nit): ')
    nombre =input('ingrese el nombre: ')
    email = input('ingresa tu correo electronico')
    telefonos = {
        'movil': '',
        'casa' : '',
        'personal': '',
        'oficina':''
    }
    bandera = True
    while bandera:
        listel = [1,2,3,4]
        try:
            opciones= print('1. movil\n2. casa\n3. personal\4 oficina')
            op =  int(input('ingrese el numero del telefono que desea agregar: '))
            if not(op in listel):
                return opciones
        except ValueError:
            print('dato invalido')
            return opciones
        else:
            if op == 1:
                telefonos['movil']=input('ingrese el numero de movil')
            elif op == 2:
                telefonos['casa']=input('ingrese el numero de movil')
            elif op == 3:
                telefonos['personal']=input('ingrese el numero de movil')
            elif op == 4:
                telefonos['oficina']=input('ingrese el numero de movil')
    
    
    nueva_persona = {"num_identificacion": num_identificacion , "nombre": nombre, "email": email, "telefono": telefonos}
    cargar_personas(personas)
    personas.append(nueva_persona)
    guardar_personas(personas)
    


