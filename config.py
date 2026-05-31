import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-fresh-basket-2024'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Srivikram@10'  # Update with your MySQL password
    MYSQL_DB = 'fresh_basket'
    UPLOAD_FOLDER = os.path.join('static', 'img', 'products')
