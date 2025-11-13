# Importamos la función que devolverá una instancia de una conexión

#from Usuarios.config.mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import connectToMySQL #importamos desde config
# Creamos la clase basada en la tabla de Usuarios

class Usuario:

    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Creamos un método de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # Llamamos a función connectToMySQL con el esquema al que te diriges
        resultados = connectToMySQL('practica_usuarios').query_db(query)
        # Creamos una lista vacía para agregar nuestras instancias de usuario
        usuarios = []
        # Iteramos sobre los resultados de la base de datos y crear instancias de usuarios con cls
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    
    # Agregamos un método de clase para generar un nuevo registro de usuario
    # el parámetro "datos" es un diccionario que se pasará al método desde el server
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('practica_usuarios').query_db(query, datos)

    
    # Obtener un usuario por ID (para editar)
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos = {'id': id}
        resultado = connectToMySQL('practica_usuarios').query_db(query, datos)
        if resultado:
            return cls(resultado[0])
            return None

    # Crear nuevo usuario
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('practica_usuarios').query_db(query, datos)
    
    # Actualizar usuario (para el botón Editar)
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('practica_usuarios').query_db(query, datos)

     # Eliminar usuario (para el botón Eliminar)
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        datos = {'id': id}

        return connectToMySQL('practica_usuarios').query_db(query, datos)
    
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('practica_usuarios').query_db(query, datos)

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos = {'id': id}
        resultado = connectToMySQL('practica_usuarios').query_db(query, datos)
        
        # Si encontramos el usuario, creamos una instancia
        if resultado:
            return cls(resultado[0])
        return None


