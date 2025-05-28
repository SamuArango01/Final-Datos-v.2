from db import execute_query

def crear_usuario():
    print("\n== CREAR USUARIO ==")
    doc = input("Documento de identidad: ")
    nombre = input("Nombre completo: ")
    email = input("Email: ")
    genero = input("Género (Masculino/Femenino/Otro): ")
    telefono = input("Teléfono: ")
    password = input("Contraseña: ")
    tipo = input("Tipo de usuario (Administrador/Profesor/Estudiante): ")

    query = """
    INSERT INTO usuarios (documento_identidad, nombre_completo, email, genero, telefono, contrasena, tipo_usuario)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    execute_query(query, (doc, nombre, email, genero, telefono, password, tipo))
    print("Usuario creado exitosamente.")

def crear_curso():
    print("\n== CREAR CURSO ==")
    nombre = input("Nombre del curso: ")
    descripcion = input("Descripción: ")
    id_categoria = int(input("ID de categoría: "))
    url = input("URL del contenido (ficticia): ")
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    anio = int(input("Año: "))
    semestre = input("Semestre (1/2/3): ")
    precio = float(input("Precio: "))

    query = """
    INSERT INTO cursos (nombre, descripcion, id_categoria, url_contenido, fecha_inicio, fecha_fin, anio, semestre, precio)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    execute_query(query, (nombre, descripcion, id_categoria, url, fecha_inicio, fecha_fin, anio, semestre, precio))
    print("Curso creado exitosamente.")

def asignar_profesor():
    print("\n== ASIGNAR PROFESOR A CURSO ==")
    id_curso = input("ID del curso: ")
    id_profesor = input("ID del profesor: ")

    query = """
    INSERT INTO cursos_profesores (id_curso, id_profesor)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE id_profesor = VALUES(id_profesor)
    """
    execute_query(query, (id_curso, id_profesor))
    print("Profesor asignado correctamente.")

def matricular_estudiante():
    print("\n== MATRICULAR ESTUDIANTE A CURSO ==")
    id_curso = input("ID del curso: ")
    id_estudiante = input("ID del estudiante: ")
    usuario_plataforma = input("Usuario plataforma: ")
    contrasena_plataforma = input("Contraseña plataforma: ")

    query = """
    INSERT INTO matriculas (id_estudiante, id_curso, usuario_plataforma, contrasena_plataforma)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (id_estudiante, id_curso, usuario_plataforma, contrasena_plataforma))
    print("Estudiante matriculado correctamente.")

def ver_usuarios():
    query = "SELECT id_usuario, documento_identidad, nombre_completo, tipo_usuario FROM usuarios"
    usuarios = execute_query(query, fetch=True)
    for u in usuarios:
        print(f"ID: {u['id_usuario']} | Doc: {u['documento_identidad']} | Nombre: {u['nombre_completo']} | Rol: {u['tipo_usuario']}")

def ver_cursos():
    query = "SELECT id_curso, nombre, fecha_inicio, fecha_fin FROM cursos"
    cursos = execute_query(query, fetch=True)
    for c in cursos:
        print(f"ID: {c['id_curso']} | Nombre: {c['nombre']} | Del {c['fecha_inicio']} al {c['fecha_fin']}")

def menu_administrador(usuario):
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Crear usuario")
        print("2. Crear curso")
        print("3. Asignar profesor a curso")
        print("4. Matricular estudiante a curso")
        print("5. Ver usuarios")
        print("6. Ver cursos")
        print("0. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            crear_curso()
        elif opcion == "3":
            asignar_profesor()
        elif opcion == "4":
            matricular_estudiante()
        elif opcion == "5":
            ver_usuarios()
        elif opcion == "6":
            ver_cursos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")