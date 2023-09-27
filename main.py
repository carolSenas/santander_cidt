# Importar flask ----> Render templates para poder enlazar el HTML
from flask import Flask, render_template, request, redirect, url_for

#Importar la conexión a la BD
from conexionDB import *

#Iniciar Flask
app= Flask(__name__)

#Crear ruta del index: Indicar que index es el archivo raiz
@app.route('/')

#renderizar el html (función que se encarga de presentar una plantilla en el texto realizado con HTML)
def home(): 
    return render_template('index.html')

# Ruta para agregar un establecimiento
@app.route('/agregar_establecimiento', methods=['POST'])
def agregar_establecimiento():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        responsable = request.form.get('responsable')
        direccion = request.form.get('direccion')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar un nuevo establecimiento
            cursor.execute("INSERT INTO establecimientos (nombre, responsable, direccion) VALUES (%s, %s, %s)",
                           (nombre, responsable, direccion))

            conexion.commit()
            cursor.close() #Cerrando conexion SQL
            conexion.close() #Cerrando conexion de la DB 

            return redirect(url_for('index', msg='Establecimiento agregado exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar establecimientos
@app.route('/listar_establecimientos')
def listar_establecimientos():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todos los establecimientos
        cursor.execute("SELECT * FROM establecimientos")
        establecimientos = cursor.fetchall()

        cursor.close() #Cerrando conexion SQL
        conexion.close() #Cerrando conexion de la DB

        return render_template('listar_establecimientos.html', establecimientos=establecimientos)
    except Exception as e:
        return render_template('index.html', error=str(e))
    
# Ruta para agregar un servicio
@app.route('/agregar_servicio', methods=['POST'])
def agregar_servicio():
    if request.method == 'POST':
        codigo_establecimiento = request.form.get('codigo_establecimiento')
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        tipo = request.form.get('tipo')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar un nuevo servicio
            cursor.execute("INSERT INTO servicios (codigo_establecimiento, nombre, descripcion, tipo) VALUES (%s, %s, %s, %s)",
                           (codigo_establecimiento, nombre, descripcion, tipo))

            conexion.commit()
            cursor.close()
            conexion.close()

            return redirect(url_for('index', msg='Servicio agregado exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar servicios
@app.route('/listar_servicios')
def listar_servicios():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todos los servicios
        cursor.execute("SELECT * FROM servicios")
        servicios = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template('listar_servicios.html', servicios=servicios)
    except Exception as e:
        return render_template('index.html', error=str(e))
    
# Ruta para agregar un usuario
@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    if request.method == 'POST':
        documento = request.form.get('documento')
        codigo_servicio = request.form.get('codigo_servicio')
        contraseña = request.form.get('contraseña')
        tipo_documento = request.form.get('tipo_documento')
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        telefono = request.form.get('telefono')
        ocupacion = request.form.get('ocupacion')
        correo = request.form.get('correo')
        ciudad = request.form.get('ciudad')
        direccion = request.form.get('direccion')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar un nuevo usuario
            cursor.execute("INSERT INTO usuarios (documento, codigo_servicio, contraseña, tipo_documento, nombre, apellidos, telefono, ocupacion, correo, ciudad, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (documento, codigo_servicio, contraseña, tipo_documento, nombre, apellidos, telefono, ocupacion, correo, ciudad, direccion))

            conexion.commit()
            cursor.close()
            conexion.close()

            return redirect(url_for('index', msg='Usuario agregado exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar usuarios
@app.route('/listar_usuarios')
def listar_usuarios():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todos los usuarios
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template('listar_usuarios.html', usuarios=usuarios)
    except Exception as e:
        return render_template('index.html', error=str(e))

# Ruta para agregar una categoría
@app.route('/agregar_categoria', methods=['POST'])
def agregar_categoria():
    if request.method == 'POST':
        codigo_servicio = request.form.get('codigo_servicio')
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar una nueva categoría
            cursor.execute("INSERT INTO categorías (codigo_servicio, nombre, descripcion) VALUES (%s, %s, %s)",
                           (codigo_servicio, nombre, descripcion))

            conexion.commit()
            cursor.close()
            conexion.close()

            return redirect(url_for('index', msg='Categoría agregada exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar categorías
@app.route('/listar_categorias')
def listar_categorias():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todas las categorías
        cursor.execute("SELECT * FROM categorías")
        categorias = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template('listar_categorias.html', categorias=categorias)
    except Exception as e:
        return render_template('index.html', error=str(e))
    
# Ruta para agregar un detalle de servicio
@app.route('/agregar_detalle_servicio', methods=['POST'])
def agregar_detalle_servicio():
    if request.method == 'POST':
        documento = request.form.get('documento')
        codigo_servicio = request.form.get('codigo_servicio')
        fecha = request.form.get('fecha')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar un nuevo detalle de servicio
            cursor.execute("INSERT INTO detalles_servicios (documento, codigo_servicio, fecha) VALUES (%s, %s, %s)",
                           (documento, codigo_servicio, fecha))

            conexion.commit()
            cursor.close()
            conexion.close()

            return redirect(url_for('index', msg='Detalle de servicio agregado exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar detalles de servicios
@app.route('/listar_detalles_servicios')
def listar_detalles_servicios():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todos los detalles de servicios
        cursor.execute("SELECT * FROM detalles_servicios")
        detalles_servicios = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template('listar_detalles_servicios.html', detalles_servicios=detalles_servicios)
    except Exception as e:
        return render_template('index.html', error=str(e))

# Ruta para agregar un municipio
@app.route('/agregar_municipio', methods=['POST'])
def agregar_municipio():
    if request.method == 'POST':
        codigo_municipio = request.form.get('codigo_municipio')
        nombre = request.form.get('nombre')
        departamento = request.form.get('departamento')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar un nuevo municipio
            cursor.execute("INSERT INTO municipios (codigo_municipio, nombre, departamento) VALUES (%s, %s, %s)",
                           (codigo_municipio, nombre, departamento))

            conexion.commit()
            cursor.close()
            conexion.close()

            return redirect(url_for('index', msg='Municipio agregado exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar municipios
@app.route('/listar_municipios')
def listar_municipios():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todos los municipios
        cursor.execute("SELECT * FROM municipios")
        municipios = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template('listar_municipios.html', municipios=municipios)
    except Exception as e:
        return render_template('index.html', error=str(e))
    
# Ruta para agregar una manzana
@app.route('/agregar_manzana', methods=['POST'])
def agregar_manzana():
    if request.method == 'POST':
        codigo_manzana = request.form.get('codigo_manzana')
        codigo_municipio = request.form.get('codigo_municipio')
        codigo_servicio = request.form.get('codigo_servicio')
        nombre = request.form.get('nombre')
        localidad = request.form.get('localidad')
        direccion = request.form.get('direccion')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar una nueva manzana
            cursor.execute("INSERT INTO manzanas (codigo_manzana, codigo_municipio, codigo_servicio, nombre, localidad, direccion) VALUES (%s, %s, %s, %s, %s, %s)",
                           (codigo_manzana, codigo_municipio, codigo_servicio, nombre, localidad, direccion))

            conexion.commit()
            cursor.close()
            conexion.close()

            return redirect(url_for('index', msg='Manzana agregada exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar manzanas
@app.route('/listar_manzanas')
def listar_manzanas():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todas las manzanas
        cursor.execute("SELECT * FROM manzanas")
        manzanas = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template('listar_manzanas.html', manzanas=manzanas)
    except Exception as e:
        return render_template('index.html', error=str(e))

# Ruta para agregar un servicio a un establecimiento
@app.route('/agregar_servicio_establecimiento', methods=['POST'])
def agregar_servicio_establecimiento():
    if request.method == 'POST':
        codigo_servicio_establecimiento = request.form.get('codigo_servicio_establecimiento')
        codigo_servicio = request.form.get('codigo_servicio')
        codigo_establecimiento = request.form.get('codigo_establecimiento')

        try:
            # Conectar a la base de datos
            conexion = conexionBD()
            cursor = conexion.cursor()

            # Insertar un nuevo servicio en un establecimiento
            cursor.execute("INSERT INTO servicio_establecimiento (codigo_servicio_establecimiento, codigo_servicio, codigo_establecimiento) VALUES (%s, %s, %s)",
                           (codigo_servicio_establecimiento, codigo_servicio, codigo_establecimiento))

            conexion.commit()
            cursor.close()
            conexion.close()

            return redirect(url_for('index', msg='Servicio en establecimiento agregado exitosamente'))
        except Exception as e:
            return render_template('index.html', error=str(e))

# Ruta para listar servicios en establecimientos
@app.route('/listar_servicios_establecimientos')
def listar_servicios_establecimientos():
    try:
        # Conectar a la base de datos
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Obtener todos los servicios en establecimientos
        cursor.execute("SELECT * FROM servicio_establecimiento")
        servicios_establecimientos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template('listar_servicios_establecimientos.html', servicios_establecimientos=servicios_establecimientos)
    except Exception as e:
        return render_template('index.html', error=str(e))

#Validar que el directorio este disponible (Escuchando)
if __name__ == '__main__': 
    # Se ejecuta en modo prueba
    app.run(debug=True, port=5500)