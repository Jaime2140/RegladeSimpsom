from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/MetodosNumericos", methods=["POST"])
def calcular():
    funcion = request.form["Funcion"].replace("^", "**")
    a = float(request.form["ValorA"])
    b = float(request.form["ValorB"])
    c = (a + b) / 2

    def f(x):
        return eval(funcion, {"x": x, "np": np})

    fa, fb, fc = f(a), f(b), f(c)
    I = (b - a) * (fa + 4 * fc + fb) / 6

    x_vals = np.linspace(a, b, 100)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title("Regla de Simpson 1/3")
    plt.legend()
    
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/grafica.png")
    plt.close()

    return render_template("resultado.html", fa=fa, fb=fb, fc=fc, I=I)

if __name__ == "__main__":
    app.run(debug=True)
