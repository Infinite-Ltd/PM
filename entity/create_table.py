from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB
#from entity.organization import
db = getDB()

class Role(db.Model):
    'role for mysql'
    __tablename__ = 'PMS_role'
    role_id = db.Column(db.String(45), primary_key=True)
    roleName = db.Column(db.String(20), nullable=False, unique=True)
    authority = db.Column(db.String(10), default='ordinary')#ordinary;administrator;
    users = db.relationship('User', backref='PMS_role')


class User(db.Model):
    'user model for mysql'
    __tablename__ = 'PMS_user'
    wid = db.Column(db.String(10),primary_key=True)
    authority = db.Column(db.String(45), db.ForeignKey('PMS_role.role_id'))
    password = db.Column(db.String(45),nullable=False, default='000000')
    name= db.Column(db.String(15),nullable=False,index=True)
    org_name = db.Column(db.String(45))
    org_guid = db.Column(db.String(45),db.ForeignKey('PMS_org.org_guid'))
    programs = db.relationship('Program', backref='PMS_user')
    trainings = db.relationship('Training', backref='PMS_user')
    isleader = db.Column(db.String(45),nullable=False,default='no')
    dirleader= db.Column(db.String(45))
    picture = db.Column(db.Binary(2048))
    enabled = db.Column(db.String(10), default='在职')  #在职：1 离职：0


class Review(db.Model):
    'review model for mysql'
    __tablename__ = 'PMS_review'
    review_guid = db.Column(db.String(45), primary_key=True)
    review_name = db.Column(db.String(20),unique=True, nullable=False)
    review_date = db.Column(db.DateTime)
    review_author = db.Column(db.String(16),nullable=False)
    author_id = db.Column(db.String(16), db.ForeignKey('PMS_user.wid'))
    review_pic = db.Column(db.String(16), db.ForeignKey('PMS_user.wid'))
    spend_time = db.Column(db.String(8))
    tips_number = db.Column(db.String(10),unique=True)
    contents = db.relationship('ReviewContent', backref='PMS_review')

class ReviewContent(db.Model):
    'the content of review'
    __tablename__ = 'PMS_reviewcontent'
    content_guid = db.Column(db.String(45), primary_key=True)
    contents = db.Column(db.String(200), nullable=False)
    review_guid = db.Column(db.String(15), db.ForeignKey('PMS_review.review_guid'))
    review_name = db.Column(db.String(20),nullable=False)

class Organization(db.Model):
    'organization model for mysql'
    __tablename__ = 'PMS_org'
    org_guid = db.Column(db.String(45), primary_key=True)
    org_name = db.Column(db.String(45), nullable=False)
    dir_name = db.Column(db.String(45))
    dir_guid = db.Column(db.String(45))
    users = db.relationship('User', backref='org')

class Program(db.Model):
    'program model for mysql'
    __tablename__ = 'PMS_program'
    prog_guid = db.Column(db.String(45), primary_key=True)
    prog_name = db.Column(db.String(20), nullable=False, unique=True, index=True)
    Prog_introduction = db.Column(db.String(200))
    plan_time = db.Column(db.String(14),index=True)
    real_time = db.Column(db.String(14),index=True)
    spend_days= db.Column(db.String(4),index=True)
    pic_guid = db.Column(db.String(45),db.ForeignKey('PMS_user.wid'))#foreign key refer to table 'PMS_user'
    manpower = db.Column(db.String(10))
    manpower_per_day = db.Column(db.String(10))
    test_instruction = db.Column(db.String(200))
    execTestCaseNum = db.Column(db.String(10))
    etcn_average = db.Column(db.String(15))
    remark = db.Column(db.String(200))
    schedule = db.Column(db.String(10), default='新建', nullable=False)

class PlanAndSummary(db.Model):
    'summary of per day for mysql'
    __tablename__ = 'PMS_summary'
    pas_guid = db.Column(db.String(45),primary_key=True)
    workPlan = db.Column(db.String(200), nullable=False)
    workStatus = db.Column(db.String(3), default='新建')
    summary = db.Column(db.String(200),nullable=False)
    createTime = db.Column(db.String(20), nullable=False)
    author_guid = db.Column(db.String(45), db.ForeignKey('PMS_user.wid'))
    author_name = db.Column(db.String(20))


class TestCase(db.Model):
    'testcase of program for mysql'
    __tablename__ = 'PMS_testcase'
    caseId = db.Column(db.String(45), primary_key=True)
    caseName = db.Column(db.String(20))
    preCase = db.Column(db.String(100), nullable=False)
    testSteps = db.Column(db.String(200), nullable=False)
    testResult = db.Column(db.String(100), nullable = False)
    createTime = db.Column(db.DateTime)
    author_guid = db.Column(db.String(45), db.ForeignKey('PMS_user.wid'))
    author_name = db.Column(db.String(20), nullable = False)
    enabled = db.Column(db.String(2), default='1')

class Training(db.Model):
    'training for mysql'
    __tablename__ = 'PMS_training'
    train_guid = db.Column(db.String(45), primary_key=True)
    train_name = db.Column(db.String(35),nullable=False)
    train_content = db.Column(db.String(100))
    train_time = db.Column(db.String(25))
    pic_guid = db.Column(db.String(45), db.ForeignKey('PMS_user.wid'))
    pic_name = db.Column(db.String(16), nullable=False)
    remarks = db.Column(db.Text)

db.create_all()
#db.drop_all()