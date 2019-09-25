from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB
from entity.program import Program
from entity.training import Training
from entity.role import Role
#from entity.organization import
db = getDB()


class User(db.Model):
    'user model for mysql'
    __tablename__ = 'PMS_user'
    wid = db.Column(db.String(10),primary_key=True)
    authority = db.Column(db.String(10), db.ForeignKey('PMS_role.role_id'))
    password = db.Column(db.String(12),nullable=False, default='000000')
    name= db.Column(db.String(15),nullable=False,index=True)
    org_name = db.Column(db.String(45))
    org_guid = db.Column(db.String(17),db.ForeignKey('PMS_org.org_guid'))
    programs = db.relationship('Program', backref='PMS_user')
    trainings = db.relationship('Training', backref='PMS_user')
    isleader = db.Column(db.String(10),nullable=False,default='no')
    dirleader= db.Column(db.String(15))
    picture = db.Column(db.Binary(2048))
    enabled = db.Column(db.String(10), default='在职')  #在职：1 离职：0


