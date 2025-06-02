📍# Sistemas de Gestión de Datos 📍

👩🏻‍💻👨🏽‍💻### Estudiantes: Samuel Arango Echeverri - Nathalia Cardoza ### 👩🏻‍💻👨🏽‍💻

[sarangoe3@eafit.edu.co](mailto:sarangoe3@eafit.edu.co) - [nvcardozaa@eafit.edu.co](mailto:nvcardozaa@eafit.edu.co)

🦾 ### Profesor: Edwin Nelson Montoya - [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co) ###🦾

---

📝 # LMS Nodo EAFIT 📝

👀 ## 1. Breve descripción de la actividad 👀

El proyecto corresponde al desarrollo de un sistema LMS (Learning Management System) básico en Python con conexión a una base de datos MySQL. Este LMS permite gestionar usuarios con diferentes roles (Administrador, Profesor, Estudiante), así como cursos, materiales, foros y matrículas.

✅ ### 1.1. Aspectos cumplidos de la actividad ✅

* Autenticación de usuarios con roles diferenciados.
* CRUD básico para usuarios y cursos.
* Asociación de profesores a cursos y matrícula de estudiantes.
* Visualización de materiales, creación de foros y participación en ellos.
* Conexión funcional con una base de datos MySQL.


🗺 ## 2. Diseño de alto nivel y arquitectura 🗺

* Arquitectura modular con un archivo por rol (administrador, profesor, estudiante).
* Módulo db.py para abstracción de operaciones con MySQL.
* Módulo auth.py para manejo de autenticación.
* Patrón estructural sencillo con separación de responsabilidades por archivo.

---

📲 ## 3. Ambiente de desarrollo 📲

* Lenguaje: Python 3.11+
* Base de datos: MySQL 8.0
* Conector: mysql-connector-python==8.0.33

👾 ### Compilación y ejecución 👾

bash
pip install mysql-connector-python
python main.py


📌 ### Detalles técnicos

* El archivo db.py contiene las funciones get_connection() y execute_query().
* Las consultas están parametrizadas para evitar inyecciones SQL.

⚡ ### Configuración del proyecto ⚡

python
# En db.py:
host='localhost'
database='nodo_eafit_lms'
user='root'
password='Tu contraseña'

Con el fin de conectar con la base de datos en Workbench


📖 ### Estructura del código 📖


.
├── main.py
├── db.py
├── auth.py
├── administrador.py
├── profesor.py
└── estudiante.py


📚 ### Resultados (opcional) 📚

Pantallas por consola que muestran la navegación por menús según el rol.

---

👾 ## 4. Ambiente de ejecución (producción) 👾

* Python 3.11
* MySQL Server 8.0
* Librería: mysql-connector-python

⚙ ### Configuración ⚙

Misma que en desarrollo, ya que se ejecuta en entorno local. En caso de despliegue, ajustar:

* host según IP o dominio.
* Variables de entorno para user y password.

💻 ### Lanzamiento del servidor 💻

bash
python main.py


💡 ### Mini guía de uso para usuario final 💡

1. Ejecutar main.py.
2. Ingresar con documento de identidad y contraseña.
3. Según el rol:

   * Administrador: gestión de usuarios, cursos, matrículas.
   * Profesor: gestión de materiales y foros.
   * Estudiante: visualización de cursos, materiales y participación en foros.

---

🪄 ## 5. Otra información relevante 🪄

* El sistema requiere una base de datos creada previamente con las tablas: usuarios, cursos, profesores, estudiantes, materiales, foros, mensajes_foros, cursos_profesores, matriculas, etc.
* Se recomienda trabajar con un esquema de pruebas para poblar datos.
* En nuestro caso ya esta base de datos ha sido previamente creada y poblada y se llama "nodo_lms_eafit".
---

