class BaseConfig(object):
     DEBUG = True

     # Mysqlの場合の例
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
         'user': 'mysql',
         'password': 'pass',
         'host': 'localhost',
         'db_name': 'flask_vue_test'
     })
     SQLALCHEMY_TRACK_MODIFICATIONS = False
     SQLALCHEMY_ECHO = False 
