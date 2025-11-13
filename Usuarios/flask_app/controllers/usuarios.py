from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

#from usuario import Usuarios #Importamos la clase

from flask_app.models.usuario import Usuario #Importamos desde models


@app.route("/")
def root():
    return redirect('/usuarios')

@app.route("/usuarios")
def index():
    try:
        # Invocamos al método de clase get all para obtener todas las usuarios
        todos_usuarios = Usuario.get_all()
        print("lista de Usuarios:", todos_usuarios)
    
        # Pasar las mascotas a la plantilla
        return render_template("usuarios.html", lista_usuarios = todos_usuarios)
    
    except Exception as e:
        print("Error en la ruta principal:", e)
        return f"Error: {e}"

@app.route("/usuarios/nuevo", methods=['GET','POST'])
def crear_usuario():

    # Si es GET, puedes mostrar un formulario (opcional)
    return render_template("nuevo_usuario.html")

@app.route("/usuarios/crear", methods=['GET','POST'])
def guardar_usuario():

#Creamos un diccionario a partir del request.form que recibimos de la plantilla
   #IMPORTANTE: las claves deben de coincidir con las variables en el query
    if request.method == 'POST':
        datos = {
            "nombre": request.form['nombre'],
            "apellido": request.form['apellido'],
            "email": request.form['email']
        }
   #Enviamos el diccionario al metodo save de usuario
    Usuario.save(datos)
    return redirect('/usuarios')

#enlace editar usuario
@app.route('/usuarios/editar/<int:id>') #, methods=['GET','POST'])
def editar_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template('editar_usuario.html', usuario=usuario)

#actualiza el item usuario
@app.route('/usuarios/actualizar', methods = ['POST'])
def actualizar_usuarios():
        datos = {
            "id": request.form['id'],
            "nombre": request.form['nombre'],
            "apellido": request.form['apellido'],
            "email": request.form['email']
        }

         #Enviamos el diccionario al metodo save de usuario
        Usuario.update(datos)
        return redirect('/usuarios')

# eliminar Usuario
@app.route('/usuarios/eliminar/<int:id>')
def eliminar_usuario(id):

    Usuario.delete(id)
    return redirect('/')

@app.route("/usuarios/ver/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("ver_usuario.html", un_usuario=usuario)