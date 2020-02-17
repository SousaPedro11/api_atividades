import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(basedir, 'atividade.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "Miguel@12345"
