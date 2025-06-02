Claro, Samuel. Aquí tienes tu README corregido con los encabezados bien estructurados (siguiendo sintaxis Markdown) y con una redacción más clara y profesional. Puedes copiarlo tal cual y se verá bien en cualquier visualizador Markdown como GitHub o Visual Studio Code:

---

# 📍 Sistemas de Gestión de Datos 📍

### 👩🏻‍💻👨🏽‍💻 Estudiantes: Samuel Arango Echeverri - Nathalia Cardoza

[sarangoe3@eafit.edu.co](mailto:sarangoe3@eafit.edu.co) - [nvcardozaa@eafit.edu.co](mailto:nvcardozaa@eafit.edu.co)

### 🦾 Profesor: Edwin Nelson Montoya

[emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

---

# 📝 LMS Nodo EAFIT 📝

## 👀 1. Breve descripción de la actividad

El proyecto corresponde al desarrollo de un sistema LMS (Learning Management System) básico en Python, con conexión a una base de datos MySQL. Este LMS permite gestionar usuarios con diferentes roles (Administrador, Profesor, Estudiante), así como cursos, materiales, foros y matrículas.

### ✅ 1.1. Aspectos cumplidos de la actividad

* Autenticación de usuarios con roles diferenciados.
* CRUD básico para usuarios y cursos.
* Asociación de profesores a cursos y matrícula de estudiantes.
* Visualización de materiales, creación de foros y participación en ellos.
* Conexión funcional con una base de datos MySQL.

---

## 🗺 2. Diseño de alto nivel y arquitectura

* Arquitectura modular, con un archivo por rol (`administrador.py`, `profesor.py`, `estudiante.py`).
* Módulo `db.py` para abstracción de operaciones con MySQL.
* Módulo `auth.py` para manejo de autenticación.
* Patrón estructural sencillo con separación de responsabilidades por archivo.

---

## 📲 3. Ambiente de desarrollo

* **Lenguaje:** Python 3.11+
* **Base de datos:** MySQL 8.0
* **Conector:** `mysql-connector-python==8.0.33`

### 👾 Compilación y ejecución

```bash
pip install mysql-connector-python  
python main.py
```

### 📌 Detalles técnicos

* El archivo `db.py` contiene las funciones `get_connection()` y `execute_query()`.
* Las consultas están parametrizadas para evitar inyecciones SQL.

### ⚡ Configuración del proyecto

En `db.py`, ajustar los siguientes datos:

```python
host = 'localhost'  
database = 'nodo_eafit_lms'  
user = 'root'  
password = 'Tu contraseña'
```

> Esto permite conectar con la base de datos desde Workbench o tu entorno local.

---

## 📖 4. Estructura del código

```
.
├── main.py
├── db.py
├── auth.py
├── administrador.py
├── profesor.py
└── estudiante.py
```

### 📚 Resultados (opcional)

El sistema se ejecuta en consola y muestra menús dinámicos según el rol del usuario.

---

## 👾 5. Ambiente de ejecución (producción)

* **Lenguaje:** Python 3.11
* **Base de datos:** MySQL Server 8.0
* **Librería:** `mysql-connector-python`

### ⚙ Configuración

La misma que en desarrollo, ya que se ejecuta en entorno local. En caso de despliegue, se deben ajustar:

* El `host` (según IP o dominio).
* Variables de entorno para `user` y `password`.

### 💻 Lanzamiento del servidor

```bash
python main.py
```

---

## 💡 6. Mini guía de uso para usuario final

1. Ejecutar `main.py`.
2. Iniciar sesión con documento de identidad y contraseña.
3. Según el rol, el usuario podrá:

* **Administrador:** gestionar usuarios, cursos y matrículas.
* **Profesor:** gestionar materiales y foros.
* **Estudiante:** ver cursos, materiales y participar en foros.

---

## 🪄 7. Otra información relevante

* El sistema requiere una base de datos previamente creada, con las siguientes tablas:
  `usuarios`, `cursos`, `profesores`, `estudiantes`, `materiales`, `foros`, `mensajes_foros`, `cursos_profesores`, `matriculas`, entre otras.
* Se recomienda trabajar con un esquema de pruebas para poblar los datos.
* En nuestro caso, esta base de datos ya fue creada y se llama **`nodo_lms_eafit`**.

---

Si necesitas que te genere este README en archivo `.md`, también puedo hacerlo. ¿Lo quieres así?

