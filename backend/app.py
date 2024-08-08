from flask import Flask, request, jsonify
import pandas as pd
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY, date TEXT, description TEXT, amount REAL)''')
    conn.commit()
    conn.close()

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_csv(file)
    # Perform any data processing here

    # Example of inserting data into SQLite
    conn = sqlite3.connect('data.db')
    df.to_sql('transactions', conn, if_exists='append', index=False)
    conn.close()

    return jsonify({"message": "File processed and data stored."})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
