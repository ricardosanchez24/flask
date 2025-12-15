# Importa los módulos necesarios de la biblioteca Flask
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy


# 1. Inicialización de la Aplicación
app = Flask(__name__) 

# 2. Almacén de Datos

app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://root:123456789@localhost/lista_tareas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tarea(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     contenido = db.Column(db.String(200), nullable = True)
     completada = db.Column(db.Boolean, default = False)
     
     def __repr__(self):
          return f'tarea: {self.id} '

# 3. Definición de la Ruta Principal (Home)

@app.route('/', methods = ['POST','GET'])
def formulario_backend():

    if request.method == 'POST':
        nueva_tarea = request.form.get('tarea')
        if nueva_tarea:
            nueva_tarea_db = Tarea(contenido=nueva_tarea) 
            db.session.add(nueva_tarea_db)
            db.session.commit()
        
        return redirect(url_for('formulario_backend'))

    tareas_db = Tarea.query.all()
    return render_template('index.html', tareas=tareas_db)

@app.route('/eliminar/<int:id_tarea>', methods = ['POST'])
def eliminar_tarea(id_tarea):
        
        tarea_eliminar = Tarea.query.get_or_404(id_tarea)
        db.session.delete(tarea_eliminar)
        db.session.commit()

        return redirect(url_for('formulario_backend'))

@app.route('/completar/<int:tarea_id>', methods = ['POST'])
def completar_tarea(tarea_id):
      
    actualizar_tarea = Tarea.query.get_or_404(tarea_id)
    
    actualizar_tarea.completada = not actualizar_tarea.completada

    db.session.commit()
 
    return redirect(url_for('formulario_backend'))                  

if __name__ == '__main__':
    with app.app_context():
         #db.drop_all()
         db.create_all()

    app.run(debug=True)