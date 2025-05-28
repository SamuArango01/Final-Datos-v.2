from auth import login, logout
from administrador import menu_administrador
from profesor import menu_profesor
from estudiante import menu_estudiante

def main():
    while True:
        print("\n== LMS NODO EAFIT ==")
        print("1. Login")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            usuario = login()
            if usuario:
                if usuario["tipo_usuario"] == "Administrador":
                    menu_administrador(usuario)
                elif usuario["tipo_usuario"] == "Profesor":
                    menu_profesor(usuario)
                elif usuario["tipo_usuario"] == "Estudiante":
                    menu_estudiante(usuario)
        elif opcion == "0":
            logout()
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()