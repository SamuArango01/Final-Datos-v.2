from db import execute_query

def menu_estudiante(usuario):
    while True:
        print("\n=== MENÚ ESTUDIANTE ===")
        print("1. Ver mis cursos")
        print("2. Ver materiales del curso")
        print("3. Ver foros y participar")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_cursos_estudiante(usuario["id_usuario"])
        elif opcion == "2":
            ver_materiales_curso()
        elif opcion == "3":
            participar_foro(usuario["id_usuario"])
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def listar_cursos_estudiante(id_usuario):
    query = """
    SELECT c.id_curso, c.nombre 
    FROM cursos c
    JOIN matriculas m ON c.id_curso = m.id_curso
    JOIN estudiantes e ON e.id_estudiante = m.id_estudiante
    WHERE e.id_usuario = %s
    """
    cursos = execute_query(query, (id_usuario,), fetch=True)
    for curso in cursos:
        print(f"ID: {curso['id_curso']} | Nombre: {curso['nombre']}")

def ver_materiales_curso():
    id_curso = input("ID del curso: ")
    query = "SELECT titulo, nombre_archivo FROM materiales WHERE id_curso = %s"
    materiales = execute_query(query, (id_curso,), fetch=True)
    for mat in materiales:
        print(f"Título: {mat['titulo']} | Archivo: {mat['nombre_archivo']}")

def participar_foro(id_usuario):
    id_foro = input("ID del foro: ")
    titulo = input("Título del mensaje: ")
    contenido = input("Contenido del mensaje: ")

    query = """
    INSERT INTO mensajes_foros (id_foro, id_usuario, titulo, contenido)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (id_foro, id_usuario, titulo, contenido))
    print("Mensaje enviado.")