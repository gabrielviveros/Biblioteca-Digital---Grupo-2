import _mysql_connector
import conexion

def crear_tabla():
    cursor = conexion.cursor()

    # Definir las consultas SQL para crear las tablas
    sql_libros = '''
    CREATE TABLE LIBROS (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Autor VARCHAR(255) NOT NULL,
        Titulo VARCHAR(255) NOT NULL,
        Anio_edicion INT,
        Editorial VARCHAR(255),
        Materia VARCHAR(255)
    )
    '''

    sql_usuarios = '''
    CREATE TABLE USUARIOS (
        Nombres VARCHAR(255) NOT NULL,
        Apellidos VARCHAR(255) NOT NULL,
        DNI CHAR(9) PRIMARY KEY
    )
    '''

    # Ejecutar las consultas SQL para crear las tablas
    cursor.execute(sql_libros)
    cursor.execute(sql_usuarios)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()

# Llama a la función para crear las tablas
#crear_tabla()

# Cierra la conexión a la base de datos
conexion.close()