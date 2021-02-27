
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cor = request.form['correo']
        cont = request.form['contraseña']
        return redirect(url_for('inicio'))
    else:
        return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True)



