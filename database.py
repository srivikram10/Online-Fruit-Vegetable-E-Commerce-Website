import mysql.connector
from flask import g
from config import Config

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, args)
    db.commit()
    last_id = cursor.lastrowid
    cursor.close()
    return last_id

def init_app(app):
    app.teardown_appcontext(close_db)
