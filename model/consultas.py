import sqlite3

# Establecer la conexión a la base de datos SQLite
connection = sqlite3.connect('nombre_base_de_datos.db')

# Definir las consultas
consulta_1 = '''
    SELECT COUNT(*) FROM tweets
'''

# Ejecutar las consultas
resultado_1 = connection.execute(consulta_1).fetchone()

# Imprimir los resultados
print("Cantidad de tweets:", resultado_1[0])

# Cerrar la conexión a la base de datos
connection.close()
