from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB
#from entity.organization import
db = getDB()

class Role(db.Model):
    'role for mysql'
    __tablename__ = 'PMS_role'
    role_id = db.Column(db.String(16), primary_key=True)
    roleName = db.Column(db.String(20), nullable=False, unique=True)
    authority = db.Column(db.String(10), default='ordinary')#ordinary;administrator;
    users = db.relationship('User', backref='PMS_role')