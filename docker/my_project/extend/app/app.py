from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/db')
def db_test():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get('POSTGRES_DB'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            host='db'  # имя сервиса базы данных
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        conn.close()
        return jsonify({"PostgreSQL version": version[0]})
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
