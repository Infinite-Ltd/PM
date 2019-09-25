from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB

db = getDB()


class TestCase(db.Model):
    'testcase of program for mysql'
    __tablename__ = 'PMS_testcase'
    caseId = db.Column(db.String(11), primary_key=True)
    caseName = db.Column(db.String(20))
    preCase = db.Column(db.String(100), nullable=False)
    testSteps = db.Column(db.String(200), nullable=False)
    testResult = db.Column(db.String(100), nullable = False)
    createTime = db.Column(db.DateTime)
    author_guid = db.Column(db.String(16), db.ForeignKey('PMS_user.wid'))
    author_name = db.Column(db.String(20), nullable = False)
    enabled = db.Column(db.String(2), default='1')