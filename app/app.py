from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.before_request
def before_request():
    print('Antes de cada petición')

@app.after_request
def after_request(response):
    print('Después de cada petición')
    return response    

#falta la parte de conexion con la base de datos aqui

@app.route('/')
def hola_mundo():
    cursos = ['Python', 'Flask', 'Django', 'JavaScript']
    data = {
        'title': 'Hola Mundo',
        'message': '¡Bienvenido a mi aplicación Flask!',
        'courses': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html',data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre,edad):
    data = {
        'title': 'contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html',data=data )

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'Hola, soy una cadena de consulta'  

def pagina_no_encontrada(error):
    #return render_template('404.html'), 404
    return redirect(url_for('hola_mundo'))      

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)