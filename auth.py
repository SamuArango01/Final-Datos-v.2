from db import execute_query

def login():
    doc_id = input("Documento de identidad: ").strip()
    password = input("Contraseña: ").strip()

    query = "SELECT * FROM usuarios WHERE documento_identidad = %s AND contrasena = %s AND activo = TRUE"
    result = execute_query(query, (doc_id, password), fetch=True)

    if result:
        user = result[0]
        print(f"Bienvenido, {user['nombre_completo']} ({user['tipo_usuario']})")
        return user
    else:
        print("Usuario o contraseña incorrectos.")
        return None

def logout():
    print("Sesión cerrada.")