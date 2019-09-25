from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB
#from entity.organization import
db = getDB()


class PlanAndSummary(db.Model):
    'summary of per day for mysql'
    __tablename__ = 'PMS_summary'
    pas_guid = db.Column(db.String(20),primary_key=True)
    workPlan = db.Column(db.String(200), nullable=False)
    workStatus = db.Column(db.String(3), default='新建')
    summary = db.Column(db.String(200),nullable=False)
    createTime = db.Column(db.String(20), nullable=False)
    author_guid = db.Column(db.String(16), db.ForeignKey('PMS_user.wid'))
    author_name = db.Column(db.String(20))




db.create_all()