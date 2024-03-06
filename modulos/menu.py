
import os
import sys
from tabulate import tabulate
import modulos.datos as md
import modulos.personas as mp
import modulos.zonas as mz
import modulos.asignacion as ma


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
    
def secondmenu(activos,identificacion):
    borrar_pantalla()
    titulo = [['MENU ACTIVOS']]
    print(tabulate(titulo,tablefmt=('double_grid')))
    listopc=[1,2,3,4,5]
    try:
        opciones = "1. AGREGAR\n2. EDITAR\n3. ELIMINAR\n4. BUSCAR\n5. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            secondmenu(activos,identificacion)
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        secondmenu(activos,identificacion)  
    else:

        if (op == 1):
            borrar_pantalla()
            md.addactivo(activos,identificacion)
            pausar_pantalla()
        elif (op == 2):
            borrar_pantalla()
            md.editar_activo(activos,identificacion)
        elif (op == 3):
            borrar_pantalla()
            md.eliminar_activo(activos, identificacion)
        elif (op == 4):
            borrar_pantalla()
            md.mostrar_activo(activos, identificacion)
            pausar_pantalla()
        elif (op == 5):
            return crearmenu()
        
def menu_dos(personas,identificacion):
    borrar_pantalla()
    titulo = [['MENU PERSONAS']]
    print(tabulate(titulo,tablefmt=('double_grid')))
    listopc=[1,2,3,4,5]
    try:
        opciones = "1. AGREGAR\n2. EDITAR\n3. ELIMINAR\n4. BUSCAR\n5. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menu_dos(personas,identificacion)
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menu_dos(personas,identificacion)  
    else:

        if (op == 1):
            borrar_pantalla()
            mp.addpersonas(personas,identificacion)
           
        elif (op == 2):
            borrar_pantalla()
            mp.editar_persona(personas,identificacion)
            
        elif (op == 3):
            borrar_pantalla()
            mp.eliminar_persona(personas,identificacion)
            
        elif (op == 4):
            borrar_pantalla()
            mp.mostrar_persona(personas,identificacion)
            pausar_pantalla()
           

        elif (op == 5):
            return crearmenu()
        

def menutres(zonas,identificacion):
    borrar_pantalla()
    titulo = [['MENU ZONAS']]
    print(tabulate(titulo,tablefmt=('double_grid')))
    listopc=[1,2,3,4,5]
    try:
        opciones = "1. AGREGAR\n2. EDITAR\n3. ELIMINAR\n4. BUSCAR\n5. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menutres(zonas,identificacion)
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menutres(zonas,identificacion)  
    else:

        if (op == 1):
            borrar_pantalla()
            mz.addzonas(zonas,identificacion)
        elif (op == 2):
            borrar_pantalla()
            mz.editar_zona(zonas, identificacion)
            pausar_pantalla()
        elif (op == 3):
            borrar_pantalla()
            mz.eliminar_zona(zonas, identificacion)
            pausar_pantalla()
        elif (op == 4):
            borrar_pantalla()
            mz.mostrar_zona(zonas,identificacion)
            pausar_pantalla()
        elif (op == 5):
            return crearmenu()
        



def menuasignacion(json1,json2,json3,personas,activos,zonas,asignaciones):
    listopc=[1,2,3]
    borrar_pantalla()
    titulo = [['MENU ASIGNACION']]
    print(tabulate(titulo,tablefmt=('double_grid')))
    try:
        opciones = "1. CREAR ASIGNACION\n2. BUSCAR ASIGNACION\n3. REGRESAR AL MENU PRINCIPAL"
        print (opciones)
        op = int(input('-'))
        if not(op in listopc):
            menuasignacion(json1,json2,json3,personas,activos,zonas,asignaciones)
    except ValueError:
        print('dato invalido') 
        pausar_pantalla()
        menuasignacion(json1,json2,json3,personas,activos,zonas,asignaciones)  
    else:
        if (op == 1):
            ma.crear_asignacion(json1,json2,json3,personas,activos,zonas,asignaciones)
            pausar_pantalla()
            return menuasignacion(json1,json2,json3,personas,activos,zonas,asignaciones)
        elif (op == 2):
            ma.buscarasignaciones(asignaciones)
            return menuasignacion(json1,json2,json3,personas,activos,zonas,asignaciones)
        elif (op == 3):
            return crearmenu()
        

        
def menureportes():
    borrar_pantalla()
    titulo = [['MENU REPORTES']]
    print(tabulate(titulo,tablefmt=('double_grid')))
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
            return menureportes()
        elif (op == 2):
            return menureportes()
        elif (op == 3):
            return menureportes()
        elif (op == 4):
            return menureportes()
        elif (op == 5):
            return menureportes()
        elif (op == 6):
            return crearmenu()
        
def menuactivos():
    borrar_pantalla()
    titulo = [['MENU MOVIMIENTO ACTIVOS']]
    print(tabulate(titulo,tablefmt=('double_grid')))
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
            return menuactivos() 
        elif (op == 2):
            return menuactivos()
        elif (op == 3):
            return menuactivos()
        elif (op == 4):
            return menuactivos()
        elif (op == 5):
            return crearmenu()

        

    
    

    






