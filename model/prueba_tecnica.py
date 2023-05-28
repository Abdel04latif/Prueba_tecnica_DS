import pandas as pd
import sqlite3
import os




# Cargar datos en el DataFrame 'tweets_db' desde un archivo CSV
tweets_db = pd.read_csv('C:/Users/PC/Desktop/Documents/Admin/DS_TheBridgeBBK_FBIL2023/4-Data_Engineering/Entregas/model/datos.csv')

# Convertir la columna de fecha a datetime
tweets_db['Date'] = pd.to_datetime(tweets_db['Date'])

# Establecer la conexión a la base de datos SQLite
connection = sqlite3.connect('tweets_df')

# Eliminar la base de datos existente si existe
if os.path.exists('tweets.db'):
    os.remove('tweets.db')

# Crear la tabla 'usuarios' si no existe
connection.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY,
        nombre TEXT,
        nombre_usuario TEXT
    )
''')

# Crear la tabla 'tweets' si no existe
connection.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
        id_tweet INTEGER PRIMARY KEY,
        cuerpo_texto TEXT,
        fecha TEXT,
        id_autor INTEGER,
        retweet INTEGER,
        reply INTEGER,
        likes INTEGER,
        quote INTEGER,
        FOREIGN KEY (id_autor) REFERENCES usuarios(id_usuario)
    )
''')

# Insertar los datos en las tablas
for _, row in tweets_db.iterrows():
    # Insertar en la tabla 'usuarios'
    connection.execute('''
        INSERT INTO usuarios (id_usuario, nombre, nombre_usuario)
        VALUES (?, ?, ?)
    ''', (row['Author ID'], row['Author Name'], row['Author Username']))

    # Insertar en la tabla 'tweets'
    connection.execute('''
        INSERT INTO tweets (id_tweet, cuerpo_texto, fecha, id_autor, retweet, reply, likes, quote)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (row['ID'], row['Text'], row['Date'].strftime('%Y-%m-%d %H:%M:%S'), row['Author ID'], row['Retweets'], row['Replies'], row['Likes'], row['Quotes']))

# Guardar los cambios en la base de datos
connection.commit()

# Cerrar la conexión a la base de datos
connection.close()

# Establecer la conexión a la base de datos SQLite
connection = sqlite3.connect('f')

# Ejecutar la consulta para encontrar registros duplicados en la columna 'id_usuario'
duplicate_users = connection.execute('''
    SELECT id_usuario, COUNT(*) as count
    FROM usuarios
    GROUP BY id_usuario
    HAVING COUNT(*) > 1
''')

# Obtener los registros duplicados
duplicate_records = duplicate_users.fetchall()

# Mostrar los registros duplicados
if len(duplicate_records) > 0:
    print("Registros duplicados encontrados en la tabla 'usuarios':")
    for record in duplicate_records:
        print(f"id_usuario: {record[0]}, count: {record[1]}")
else:
    print("No se encontraron registros duplicados en la tabla 'usuarios'.")

# Cerrar la conexión a la base de datos
connection.close()




