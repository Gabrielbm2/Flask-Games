from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'senha'


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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST', ])
def authenticate():
    if '12345' == request.form['senha']:
        session['Usuário_logado'] = request.form['usuario']
        flash(session['Usuário_logado'] + 'logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não logado, senha incorreta!')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['Usuário logado'] = None
    flash('Usuário deslogado')
    return redirect('/')


app.run(debug=True)
