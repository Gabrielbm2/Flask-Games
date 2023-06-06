from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('League of Legends', 'MOBA', 'PC')
jogo2 = Jogo('Elden Ring', 'RPG', 'PC, Playstation, Xbox')
jogo3 = Jogo('Valorant', 'FPS', 'PC')
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/newGame')
def newGame():
    return render_template('novo.html', titulo='New Game')


@app.route('/create', methods=['POST', ])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


app.run(debug=True)
