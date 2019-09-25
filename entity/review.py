from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from entity.db_object import getDB

db = getDB()

class Review(db.Model):
    'review model for mysql'
    __tablename__ = 'PMS_review'
    review_guid = db.Column(db.String(15), primary_key=True)
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
    content_guid = db.Column(db.String(16), primary_key=True)
    contents = db.Column(db.String(200), nullable=False)
    review_guid = db.Column(db.String(15), db.ForeignKey('PMS_review.review_guid'))
    review_name = db.Column(db.String(20),nullable=False)
