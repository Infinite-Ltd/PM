from entity.db_object import db
from wtforms import StringField, SubmitField,TextAreaField,DateTimeField, RadioField,PasswordField,SelectField
from wtforms.validators import Required,EqualTo,Length
from flask_wtf import FlaskForm

class TrainingForm(FlaskForm):
    train_name = StringField('培训名称', validators=[])
    train_content = TextAreaField('培训内容', validators=[])
    train_time = StringField('培训时间', validators=[])
    pic_guid = StringField('培训人', validators=[])
    remarks = TextAreaField('备注')
    submit = SubmitField('保存')
    #cancel = SubmitField('取消')