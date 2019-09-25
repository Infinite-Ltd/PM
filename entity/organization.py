from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB
from entity.userinfo import User

db = getDB()
class Organization(db.Model):
    'organization model for mysql'
    __tablename__ = 'PMS_org'
    org_guid = db.Column(db.String(45), primary_key=True)
    org_name = db.Column(db.String(45), nullable=False)
    dir_name = db.Column(db.String(45))
    dir_guid = db.Column(db.String(45))
    users = db.relationship('User', backref='org')

