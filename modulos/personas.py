import json
import modulos.menu as mm
def vali_num_enteros():
    try:
        x=int(input('->'))
        return x
    except ValueError:
        print('numero no valido')
        return vali_num_enteros()
    
def cargar_personas():
    try:
        with open('personas.json', 'r') as archivo:
            personas = json.load(archivo)
    except FileNotFoundError:
        personas = []
    return personas

def guardar_personas(personas):
    with open('personas.json', 'w') as archivo:
        json.dump(personas, archivo, indent=4)

def addpersonas(personas,identificacion):
    try:
        num_identificacion = int(input('Ingrese el número de identificación: '))
    except ValueError:
        print('ingrese un dato numerico')
        return addpersonas(personas,identificacion)
    nombre = input('Ingrese el nombre: ')
    email = input('Ingrese el correo electrónico: ')
    

    telefonos = {
        'movil': '',
        'casa' : '',
        'personal': '',
        'oficina':''
    }
    
    bandera = True
    while bandera:
        listel = [1, 2, 3, 4]
        try:
            opciones = print('1. Móvil\n2. Casa\n3. Personal\n4. Oficina')
            op = int(input('Ingrese el número del teléfono que desea agregar: '))
            if not(op in listel):
                return opciones
        except ValueError:
            print('Dato inválido')
            return opciones
        else:
            if op == 1:
                telefonos['movil'] = input('Ingrese el número de móvil: ')
            elif op == 2:
                telefonos['casa'] = input('Ingrese el número de casa: ')
            elif op == 3:
                telefonos['personal'] = input('Ingrese el número personal: ')
            elif op == 4:
                telefonos['oficina'] = input('Ingrese el número de oficina: ')
            bandera=False
    
    # Crea un diccionario para la nueva persona
    nueva_persona = {
        "num_identificacion": num_identificacion,
        "nombre": nombre,
        "email": email,
        "telefono": telefonos,
        "asignaciones": []
    }
    
    # Carga las personas existentes del archivo
    personas = cargar_personas()
    
    # Agrega la nueva persona a la lista de personas
    personas.append(nueva_persona)
    
    # Guarda la lista actualizada de personas en el archivo
    guardar_personas(personas)
    mm.menu_dos(personas, identificacion)

def buscar_persona(personas, identificacion):
    identificacion=int(input('escriba el numero de identificacion:\n'))
    for persona in personas:
        if persona["num_identificacion"] == identificacion:
            return persona
    return None


def editar_persona(personas, identificacion):
    persona = buscar_persona(personas, identificacion)
    if persona:
        print("Información actual de la persona:")
        print(persona)
        
        campo = input("¿Qué campo desea editar? (nombre/email/telefono): ").lower()
        
        if campo == "nombre":
            nuevo_valor = input("Ingrese el nuevo nombre: ")
            persona["nombre"] = nuevo_valor
        elif campo == "email":
            nuevo_valor = input("Ingrese el nuevo correo electrónico: ")
            persona["email"] = nuevo_valor
        if campo == "telefono":
                bandera = True
                while bandera:
                    listel = [1, 2, 3, 4]
                    try:
                        opciones = print('1. Móvil\n2. Casa\n3. Personal\n4. Oficina')
                        op = int(input('Ingrese el número del teléfono que desea agregar: '))
                        if not(op in listel):
                            return opciones
                    except ValueError:
                        print('Dato inválido')
                        return opciones
                    else:
                        if op == 1:
                            persona["telefono"]['movil'] = input('Ingrese el número de móvil: ')
                        elif op == 2:
                            persona["telefono"]['casa'] = input('Ingrese el número de casa: ')
                        elif op == 3:
                            persona["telefono"]['personal'] = input('Ingrese el número personal: ')
                        elif op == 4:
                            persona["telefono"]['oficina'] = input('Ingrese el número de oficina: ')
                        bandera=False    
        else:
            print("Campo inválido.")
            return
        
        # Guardar los cambios en el archivo
        guardar_personas(personas)
        
        print("Información de la persona actualizada correctamente.")
    else:
        print("No se encontró ninguna persona con ese número de identificación.")
    mm.menu_dos(personas, identificacion)

def eliminar_persona(personas, identificacion):
    persona = buscar_persona(personas, identificacion)
    if persona:
        print("Información de la persona a eliminar:")
        print(persona)
        personas.remove(persona)  # Elimina la persona de la lista
        guardar_personas(personas)  # Guarda los cambios en el archivo
        print("La información de la persona ha sido eliminada.")
        mm.menu_dos(personas, identificacion)

def mostrar_persona(personas,identificacion):
    persona = buscar_persona(personas, identificacion)
    print(persona)
    mm.pausar_pantalla()
    mm.menu_dos(personas, identificacion)





