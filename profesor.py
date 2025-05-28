from db import execute_query

def menu_profesor(usuario):
    while True:
        print("\n=== MENÚ PROFESOR ===")
        print("1. Ver mis cursos")
        print("2. Ver estudiantes del curso")
        print("3. Subir material")
        print("4. Crear foro")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_cursos_profesor(usuario["id_usuario"])
        elif opcion == "2":
            listar_estudiantes_curso()
        elif opcion == "3":
            subir_material(usuario["id_usuario"])
        elif opcion == "4":
            crear_foro(usuario["id_usuario"])
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def listar_cursos_profesor(id_usuario):
    query = """
    SELECT c.id_curso, c.nombre 
    FROM cursos c
    JOIN cursos_profesores cp ON c.id_curso = cp.id_curso
    JOIN profesores p ON p.id_profesor = cp.id_profesor
    WHERE p.id_usuario = %s
    """
    cursos = execute_query(query, (id_usuario,), fetch=True)
    for curso in cursos:
        print(f"ID: {curso['id_curso']} | Nombre: {curso['nombre']}")

def listar_estudiantes_curso():
    id_curso = input("Ingrese ID del curso: ")
    query = """
    SELECT u.nombre_completo 
    FROM usuarios u
    JOIN estudiantes e ON u.id_usuario = e.id_usuario
    JOIN matriculas m ON m.id_estudiante = e.id_estudiante
    WHERE m.id_curso = %s
    """
    alumnos = execute_query(query, (id_curso,), fetch=True)
    for alumno in alumnos:
        print(f"- {alumno['nombre_completo']}")

def subir_material(id_usuario):
    id_curso = input("ID del curso: ")
    titulo = input("Título del material: ")
    descripcion = input("Descripción: ")
    nombre_archivo = input("Nombre del archivo (URL simulada): ")

    query = """
    INSERT INTO materiales (id_curso, id_profesor, titulo, descripcion, nombre_archivo)
    VALUES (%s, (SELECT id_profesor FROM profesores WHERE id_usuario=%s), %s, %s, %s)
    """
    execute_query(query, (id_curso, id_usuario, titulo, descripcion, nombre_archivo))
    print("Material subido exitosamente.")

def crear_foro(id_usuario):
    id_curso = input("ID del curso: ")
    titulo = input("Título del foro: ")
    descripcion = input("Descripción: ")

    query = """
    INSERT INTO foros (id_curso, id_profesor, titulo, descripcion)
    VALUES (%s, (SELECT id_profesor FROM profesores WHERE id_usuario=%s), %s, %s)
    """
    execute_query(query, (id_curso, id_usuario, titulo, descripcion))
    print("Foro creado.")