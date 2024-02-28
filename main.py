import modulos.menu as mm

if __name__ == '__main__':
    running = True
    while running:
        op= mm.crearmenu()
        if (op == 1):
            mm.secondmenu()
        elif (op == 2):
            mm.menu_dos()
        elif (op == 3):
            mm.menutres()
        elif (op == 4):
            mm.menuasignacion()
        elif (op == 5):
            mm.menureportes()
        elif (op == 6):
            mm.menuactivos()
        elif (op == 7):
            running= False
