# Importar nuestro Framework, en este caso Flask
from flask import Flask

# Importar función para permitir el render de los templates
from flask import render_template,request,redirect

# Conexión con la base de datos en MySql
from flask_mysqldb import MySQL


# Crear Aplicación
app = Flask(__name__)

# Configurar MySQL
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""  # Asegúrate de poner tu contraseña aquí
app.config['MYSQL_DB'] = "usuarios_cafeteria"
# app.config['MYSQL_DATABASE_PORT'] = 3307  # Descomentar si necesitas cambiar el puerto

mysql = MySQL(app)

# Ruta de la raíz del sitio

@app.route('/')
def index():
    return render_template('usuarios/index.html')

@app.route('/carrito.html')
def carrito():
    return render_template('usuarios/html/carrito.html')


@app.route('/nosotros.html')
def nosotros():
    return render_template('usuarios/html/nosotros.html')

@app.route('/usuarios')
def usuarios():
    # Consulta SQL para insertar datos
    #sql = "INSERT INTO `usuarios` (`id`, `Usuario`, `pass`, `Nombre`, `Apellido`) VALUES ('NULL', 'Fabian', 'admin', 'fabian34', 'admin');"
    sql="SELECT * FROM `usuarios`;"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    
    db_usuarios=cursor.fetchall()
    
    print("-"*60)
    for usuarios in db_usuarios:
        print(usuarios)
        print("-"*60)
    
    conn.commit()
    cursor.close()
    
    return render_template('usuarios/html/usuarios.html',usuarios=db_usuarios)

#funcion para eliminar un registro
@app.route('/destroy/<int:id>')
def destroy(id):
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `usuarios` WHERE id =%s",(id,))
    
    conn.commit()
    return redirect('/usuarios')

#funcion para editar un registro
@app.route('/edit/<int:id>')
def edit(id):
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `usuarios` WHERE id =%s",(id,))
    db_usuarios=cursor.fetchall()
    cursor.close()
    return render_template('/usuarios/edit.html',usuarios=db_usuarios)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        # Obtener datos del formulario
        _name = request.form['txtname']
        _lastname = request.form['txtlastname']
        _username = request.form['txtusername']
        _password = request.form['txtpassword']
        
        
        conn = mysql.connection
        cursor = conn.cursor()
        sql = "UPDATE `usuarios` SET `Usuario` = '"+_username+"', `pass` = '"+_password+"', `Nombre` = '"+_name+"', `Apellido` = '"+_lastname+"' WHERE `usuarios`.`id` = "+str(id)+";"
        #params = (_username,_password,_name,_lastname,id)   
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        
        return redirect('/usuarios')


@app.route('/create')
def create():
    return render_template('usuarios/create.html')

@app.route('/store', methods=['POST'])
def store():
    if request.method == 'POST':
        # Obtener datos del formulario
        _name = request.form['txtname']
        _lastname = request.form['txtlastname']
        _username = request.form['txtusername']
        _password = request.form['txtpassword']
        
        sql = "INSERT INTO `usuarios` (`id`, `Usuario`, `pass`, `Nombre`, `Apellido`) VALUES ('NULL', '"+_username+"', '"+_password+"', '"+_name+"', '"+_lastname+"');"
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        
        return redirect('/usuarios')
    
    

# Líneas requeridas por Python para empezar a trabajar con la app
if __name__ == '__main__':
    app.run(debug=True)
