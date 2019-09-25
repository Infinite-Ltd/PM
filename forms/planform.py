from entity.db_object import db
from wtforms import StringField, SubmitField, RadioField,PasswordField,SelectField,TextAreaField
from wtforms.validators import Required,EqualTo
from flask_wtf import FlaskForm

class PlanForm(FlaskForm):

    pas_guid = StringField('负责人工号', validators=[Required])
    workPlan = TextAreaField('工作计划', validators=[Required])
    summary = TextAreaField('工作总结', validators=[Required])
    comment = TextAreaField('领导评语', validators=[Required])
    workStatus = SelectField('计划状态', choices=[('0', '新建'), ('statics', '进行中'), ('2', '完成')])
    submit = SubmitField('提交')
    cancel = SubmitField('取消')