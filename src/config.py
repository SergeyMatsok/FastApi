import os

from dotenv import load_dotenv

# Работа с переменным окружением

load_dotenv(os.path.join('.env'))

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

SECRET = os.environ.get('SECRET')
