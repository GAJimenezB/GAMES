from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Inicialización de la base de datos
def init_db():
    conn = sqlite3.connect('moves.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS moves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direccion TEXT,
            x INTEGER,
            y INTEGER,
            shoot BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

# Guardar un movimiento en la base de datos
def save_move(direccion, x, y, shoot):
    conn = sqlite3.connect('moves.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO moves (direccion, x, y, shoot)
        VALUES (?, ?, ?, ?)
    ''', (direccion, x, y, shoot))  # Corregir el "VALUES"
    conn.commit()
    conn.close()

# Ruta para guardar un movimiento
@app.route('/moves', methods=['POST'])
def movimiento():
    data = request.get_json()
    direccion = data.get('direccion')
    x = data.get('x')
    y = data.get('y')
    shoot = data.get('shoot', False)
    save_move(direccion, x, y, shoot)
    return jsonify({"message": "Move saved correctly"}), 200

if __name__ == "__main__":
    init_db()  # Inicializa la base de datos
    app.run(debug=True, host='0.0.0.0', port=5000)
