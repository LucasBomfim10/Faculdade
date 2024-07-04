from flask import Flask, render_template, request, redirect, session, g
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Chave secreta para sessões

DATABASE = 'usuarios.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()






@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def is_authenticated():
    return 'username' in session

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome_usuario = request.form['username']
        senha = request.form['password']

        db = get_db()
        cursor = db.cursor()

        # Construindo a consulta SQL diretamente com os valores do usuário (inseguro)
        query = "SELECT * FROM usuarios WHERE nome_usuario = '{}' AND senha = '{}'".format(nome_usuario, senha)

        # Executando a consulta SQL
        cursor.execute(query)

        # Obtendo o resultado da consulta
        usuario = cursor.fetchone()

        """
        cursor.execute('SELECT * FROM usuarios WHERE nome_usuario = ? AND senha = ?', (nome_usuario, senha))
        usuario = cursor.fetchone()
        """
        if usuario:
            session['username'] = nome_usuario
            return redirect('/interno')
        else:
            mensagem_erro = 'Nome de usuário ou senha inválidos.'
            return render_template('login.html', mensagem_erro=mensagem_erro)

    return render_template('login.html')

@app.route('/interno')
def interno():
    if is_authenticated():
        return render_template('interno.html')
    else:
        return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
