import mysql.connector

# Configura la conexión al servidor MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prueba!123",
    port='3306'
)

# Crea un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Nombre de la base de datos que deseas crear
nombre_base_de_datos = "biblioteca"

# Intenta crear la base de datos
try:
    cursor.execute(f"CREATE DATABASE {nombre_base_de_datos}")
    print(f"Base de datos '{nombre_base_de_datos}' creada con éxito.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Cierra el cursor y la conexión
cursor.close()
conexion.close()