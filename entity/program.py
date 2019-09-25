from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB

db = getDB()


class Program(db.Model):
    'program model for mysql'
    __tablename__ = 'PMS_program'
    prog_guid = db.Column(db.String(10), primary_key=True)
    prog_name = db.Column(db.String(20), nullable=False, unique=True, index=True)
    Prog_introduction = db.Column(db.String(200))
    plan_time = db.Column(db.String(14),index=True)
    real_time = db.Column(db.String(14),index=True)
    spend_days= db.Column(db.String(4),index=True)
    pic_guid = db.Column(db.String(10),db.ForeignKey('PMS_user.wid'))#foreign key refer to table 'PMS_user'
    manpower = db.Column(db.String(10))
    manpower_per_day = db.Column(db.String(10))
    test_instruction = db.Column(db.String(200))
    execTestCaseNum = db.Column(db.String(10))
    etcn_average = db.Column(db.String(15))
    remark = db.Column(db.String(200))
    schedule = db.Column(db.String(10), default='新建', nullable=False)
