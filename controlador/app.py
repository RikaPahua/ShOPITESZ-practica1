from flask import Flask,render_template, request
app = Flask(__name__, template_folder='../vista')

@app.route('/')
def inicio():
    return render_template('comunes/Index.html')

@app.route('/consultarProductos')
def consultarProductos():
    return render_template('Productos/consultarProductos.html')

@app.route('/registrarProducto')
def registrarProducto():
    return render_template('Productos/registrarProducto.html')

if __name__ == '__main__':
    app.run(debug=True)