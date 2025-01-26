import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import jsonify
import banco

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", uniformes=banco.select())

@app.route("/uniforme")
def form():
    return render_template("uniforme.html")

@app.route("/enviar", methods=["POST"])
def submit_uniform_request():
    nome = request.form["nome"]
    modelo = request.form["modelo"]
    cor = request.form["cor"]
    tamanho = request.form["tamanho"]
    vestuario = request.form["vestuario"]

    conn = sqlite3.connect('uniformes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO uniformes (nome, modelo, cor, tamanho, vestuario)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, modelo, cor, tamanho, vestuario))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_rows():
    data = request.get_json()
    ids = data.get('ids', [])

    if not ids:
        return jsonify({'success': False, 'message': 'No IDs provided'})

    try:
        conn = sqlite3.connect('uniformes.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM uniformes WHERE id IN ({})'.format(','.join('?' * len(ids))), ids)
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == "__main__":
    app.run(debug=True)