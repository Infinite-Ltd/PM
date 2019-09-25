from flask_sqlalchemy import SQLAlchemy
from flask import Flask
#from app_obj import app
#from app import getDBs
#from app import app

app = Flask(__name__)
#app = getApp()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/PMS?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app, use_native_unicode='utf8')

def getDB():
    'get a instance of the database'
    return db

# if __name__ == '__main__':
#     print('uuuuuuuuuu')
#     app.run(host='0.0.0.0', port='5633')