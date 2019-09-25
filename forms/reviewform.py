from entity.db_object import db
from wtforms import StringField, SubmitField, RadioField,PasswordField,SelectField,DateTimeField,TextAreaField
from wtforms.validators import Required,EqualTo
from flask_wtf import FlaskForm

class ReviewForm(FlaskForm):

    review_name = StringField('评审名称', validators=[Required])
    review_date = DateTimeField('评审时间', validators=[Required])
    review_author = StringField('评审负责人')
    review_participate = StringField('评审参与者')
    spend_time = StringField('花费时间', validators=[Required])
    tips_number = StringField('意见数量')
    submit = SubmitField('提交')
    #cancel = SubmitField('取消')


class ReviewContent(FlaskForm):

    contents = TextAreaField('评审意见', validators=[Required])
    submit = SubmitField('提交')
    #cancel = SubmitField('取消')