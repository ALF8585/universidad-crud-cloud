from flask import Flask, render_template
from models import Universidad, Carrera

app = Flask(__name__)

# Aquí debajo
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/universidades')
def listar_universidades():
    universidades = Universidad.query.all()
    return render_template('universidades.html', universidades=universidades)

@app.route('/carreras')
def listar_carreras():
    carreras = Carrera.query.all()
    return render_template('carreras.html', carreras=carreras)
if __name__ == '__main__':
    app.run(debug=True)

