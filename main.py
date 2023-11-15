from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formularionotas', methods=['GET', 'POST'])
def fomularionotas():
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        numero3 = float(request.form['numero3'])
        asistencia = float(request.form['asistencia'])
        resultado = (numero1 + numero2 + numero3) / 3
        aprobar = ''
        if asistencia < 75:
            aprobar = "has reprobado por poca asistencia"
            return render_template('formularionotas.html', aprobar=aprobar, resultado=resultado, numero1=numero1, numero2=numero2, numero3=numero3, asistencia=asistencia)
        elif asistencia >= 75 and resultado < 40:
            aprobar = "has reprobado por malas notas"
            return render_template('formularionotas.html', aprobar=aprobar, resultado=resultado, numero1=numero1, numero2=numero2, numero3=numero3, asistencia=asistencia)
        elif asistencia >= 75 and resultado >= 40:
            aprobar = "has aprobado! Felicidades =)"
            return render_template('formularionotas.html', aprobar=aprobar, resultado=resultado, numero1=numero1, numero2=numero2, numero3=numero3, asistencia=asistencia)
    return render_template('formularionotas.html')

@app.route('/nombres', methods=['GET', 'POST'])
def nombres():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        resultado = ""
        resultado2 = ""
        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            resultado = f"El nombre con más caracteres es '{nombre1}'"
            resultado2 = f"El nombre {nombre1} tiene: {len(nombre1)} caracteres"
            return render_template('nombres.html', nombre1=nombre1, resultado=resultado, resultado2=resultado2)

        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            resultado = f"El nombre con más caracteres es '{nombre2}'"
            resultado2 = f"El nombre {nombre2} tiene: {len(nombre2)} caracteres"
            return render_template('nombres.html', nombre2=nombre2, resultado=resultado, resultado2=resultado2)

        elif len(nombre3) > len(nombre1) and len(nombre3) > len(nombre2):
            resultado = f"El nombre con más caracteres es '{nombre3}'"
            resultado2 = f"El nombre {nombre3} tiene: {len(nombre3)} caracteres"
            return render_template('nombres.html', nombre3=nombre3, resultado=resultado, resultado2=resultado2)
    return render_template('nombres.html')

if __name__ == '__main__':
    app.run(debug=True)
