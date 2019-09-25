from entity.db_object import db
from wtforms import StringField, SubmitField, RadioField,PasswordField,SelectField
from wtforms.validators import Required,EqualTo,Length
from flask_wtf import FlaskForm

class UserForm(FlaskForm):

    workId = StringField('工号: ', validators=[],)
    username = StringField('姓名: ', validators=[])
    password = PasswordField('密码: ',validators=[Length(6,12, message='密码为6-12位')])
    passwordg = PasswordField('密码again:', validators=[EqualTo('password', message='两次密码不一致')])
    department = StringField('部门: ', validators=[])
    isleader = SelectField('领导?', choices=[('yes','yes'), ('no','no')])
    dirleader = StringField('上级领导: ')
    career = StringField('职位: ')
    submit = SubmitField('保存')
    #cancel = SubmitField('取消')


