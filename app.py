from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '<KEY>'
app.secret_key = 'secret_key'

USERNAME = 'admin'
PASSWORD = '1234'

listEntrada = []
listSaida = []
totalEntrada = 0
totalSaida = 0
saldo = totalEntrada-totalSaida




@app.route('/')
def home():


    if "username" in session:
        return render_template('home.html', username=session['username'], listEntrada=listEntrada, listSaida = listSaida, totalSaida = totalSaida, totalEntrada = totalEntrada, saldo=saldo)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')



        if username == USERNAME and password == PASSWORD:
            session['username'] = username

            return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/atualizado', methods=['POST'])
def atualizado():

    if request.method == 'POST':
        global saldo, totalSaida, totalEntrada
        valor = float(request.form.get('valor'))
        operacao = request.values.get('btn-valor')


        if operacao == 'entrada':

            listEntrada.append(valor)
            totalEntrada = somar_total(listEntrada)

            saldo = totalEntrada - totalSaida

            print(totalEntrada)


            return redirect(url_for('home'))
        else:
            listSaida.append(valor)
            totalSaida = somar_total(listSaida)

            saldo = totalEntrada - totalSaida

            print(totalSaida)
            return redirect(url_for('home'))

def somar_total(lista):
    total = 0


    print(type(lista))
    for item in lista:
        total += item

    return total


if __name__ == '__main__':
    app.run(debug=True)