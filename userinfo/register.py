from entity.db_object import db
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_wtf import Form
from urllib import request

def register(request):
    db.