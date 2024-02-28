
import os
import sys
def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")
def crearmenu():
    lstopciones=[1,2,3,4,5,6,7]
   
  

    titulo = """
    ____________________________
       GESTION DE INVENTARIOS
    ____________________________
    """

    borrar_pantalla()
    print(titulo)


    try:
        opciones = "1. ACTIVOS\n2. PERSONAL\n3. ZONAS\n4. ASIGNACION DE ACTIVOS\n5. REPORTES\n6. MOVIMIENTO DE ACTIVOS\n7. SALIR"
        print (opciones)
        op = int(input('-'))
        if not(op in lstopciones):
            crearmenu()
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        crearmenu()  
    else:
        return op
    
def secondmenu():
    borrar_pantalla()
    listopc=[1,2,3,4,5]
    try:
        opciones = "1. AGREGAR\n2. EDITAR\n3. ELIMINAR\n4. BUSCA\n5. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            secondmenu()
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        secondmenu()  
    else:

        if (op == 1):
            pass
        elif (op == 2):
            pass
        elif (op == 3):
            pass
        elif (op == 4):
            pass
        elif (op == 5):
            return crearmenu()
def menu_dos():
    borrar_pantalla()
    listopc=[1,2,3,4,5]
    try:
        opciones = "1. AGREGAR\n2. EDITAR\n3. ELIMINAR\n4. BUSCA\n5. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menu_dos()
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menu_dos()  
    else:

        if (op == 1):
            pass
        elif (op == 2):
            pass
        elif (op == 3):
            pass
        elif (op == 4):
            pass
        elif (op == 5):
            return crearmenu()
def menutres():
    borrar_pantalla()
    listopc=[1,2,3,4,5]
    try:
        opciones = "1. AGREGAR\n2. EDITAR\n3. ELIMINAR\n4. BUSCA\n5. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menutres()
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menutres()  
    else:

        if (op == 1):
            pass
        elif (op == 2):
            pass
        elif (op == 3):
            pass
        elif (op == 4):
            pass
        elif (op == 5):
            return crearmenu()

def menuasignacion():
    listopc=[1,2,3]
    borrar_pantalla()
    try:
        opciones = "1. CREAR ASIGNACION\n2. BUSCAR ASIGNACION\n3. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menuasignacion()
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menuasignacion()  
    else:
        if (op == 1):
            pass 
        elif (op == 2):
            pass
        elif (op == 3):
            return crearmenu()
        
def menureportes():
    borrar_pantalla()
    listopc=[1,2,3,4,5,6]
    try:
        opciones = "1. LISTAR TODOS LOS ACTIVOS\n2. LISTAR ACTIVOS POR CATEGORIA\n3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO\n4. LISTAR ACTIVOS Y ASIGNACION\n5. LISTAR HISTORIAL DE MOV. DE ACTIVO\n6. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menureportes()
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menureportes()  
    else:
        if (op == 1):
            pass 
        elif (op == 2):
            pass
        elif (op == 3):
            pass
        elif (op == 4):
            pass
        elif (op == 5):
            pass
        elif (op == 6):
            return crearmenu()
        
def menuactivos():
    borrar_pantalla()
    listopc=[1,2,3,4,5,6]
    try:
        opciones = "1. RETORNO DE ACTIVO\n2. DAR DE BAJA ACTIVO\n3. CAMBIAR ASIGNACION DE ACTIVO\n4. ENVIAR A GARANTIA ACTIVO\n5. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menuactivos()
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menuactivos()  
    else:
        if (op == 1):
            pass 
        elif (op == 2):
            pass
        elif (op == 3):
            pass
        elif (op == 4):
            pass
        elif (op == 5):
            return crearmenu()

        

    
    

    






