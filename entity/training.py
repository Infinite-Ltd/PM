from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB

db = getDB()

class Training(db.Model):
    'training for mysql'
    __tablename__ = 'PMS_training'
    train_guid = db.Column(db.String(45), primary_key=True)
    train_name = db.Column(db.String(35), nullable=False)
    train_content = db.Column(db.String(100))
    train_time = db.Column(db.String(25))
    pic_guid = db.Column(db.String(16), db.ForeignKey('PMS_user.wid'))
    pic_name = db.Column(db.String(16), nullable=False)
    remarks = db.Column(db.Text)