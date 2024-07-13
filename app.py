from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('dishes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/dishes', methods=['GET'])
def get_dishes():
    conn = get_db_connection()
    dishes = conn.execute('SELECT * FROM dishes').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in dishes])

@app.route('/dishes/<string:dish_id>/toggle', methods=['POST'])
def toggle_dish(dish_id):
    conn = get_db_connection()
    dish = conn.execute('SELECT isPublished FROM dishes WHERE dishId = ?', (dish_id,)).fetchone()
    if dish is None:
        conn.close()
        return jsonify({'error': 'Dish not found'}), 404

    new_status = not dish['isPublished']
    conn.execute('UPDATE dishes SET isPublished = ? WHERE dishId = ?', (new_status, dish_id))
    conn.commit()
    conn.close()
    return jsonify({'dishId': dish_id, 'isPublished': new_status})

if __name__ == '__main__':
    app.run(debug=True)
