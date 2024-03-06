import modulos.menu as mm
import modulos.personas as mp
import modulos.zonas as mz
import modulos.datos as md
import modulos.asignacion as ma

if __name__ == '__main__':
    running = True
    while running:
        personas = mp.cargar_personas()
        identificacion = mp.buscar_persona
        zonas = mz.cargar_zonas()
        identificacion_zonas= mz.buscar_zona
        activos = md.cargar_activos()
        identificacion_activo = md.buscar_activo
        json1 = ma.cargar_zonas
        json2 = ma.cargar_personas
        json3 = ma.cargar_activos
        asignaciones= ma.buscarasignaciones

        op= mm.crearmenu()
        if (op == 1):
            mm.secondmenu(activos,identificacion_activo)
        elif (op == 2):
            mm.menu_dos(personas,identificacion)
        elif (op == 3):
            mm.menutres(zonas,identificacion_zonas)
        elif (op == 4):
            mm.menuasignacion(json1,json2,json3,personas,activos,zonas,asignaciones)
        elif (op == 5):
            mm.menureportes()
        elif (op == 6):
            mm.menuactivos()
        elif (op == 7):
            running= False
