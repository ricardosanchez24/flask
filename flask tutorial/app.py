from flask import Flask, render_template, url_for, request
from markupsafe import escape

app = Flask(__name__)
'''
@app.route('/hello/<name>/')
def hola_mundo(name):
    name = 'ricardo'
    return f'has creado un hola mundo {name} te felicito gran paso'
'''
@app.route('/')
def index():
    lista = ['esta','es una','lista']
    data = {
        'titulo': 'principal',
        'autor': 'ricardo',
        'apodo': 'El Creador',
        'lista': lista,
        'numero_lista': len(lista)
    }
    return render_template('index.html',data=data)    

    

if __name__ == '__main__':
    app.run(debug=True)