from entity.db_object import db
from wtforms import StringField, SubmitField, RadioField,PasswordField,SelectField
from wtforms.validators import Required,EqualTo
from flask_wtf import Form

class ProgramForm(Form):
    prog_name = StringField('项目名称', validators=[Required])
    prog_intro = StringField('项目介绍', validators=[Required])
    plan_time = StringField('计划时间', validators=[Required])
    real_time = StringField('实际时间', )
    spend_days = StringField('花费时间', validators=[Required])
    pic_guid = StringField('负责人工号', validators=[Required])
    manpower = StringField('投入总人力', validators=[Required])
    manpower_per_day = StringField('日均人力', validators=[Required])
    test_instruction = StringField('测试策略', validators=[Required])
    execTestCaseNum = StringField('总执行用例数')
    etcn_average = StringField('日均执行用例数')
    remark = StringField('备注')
    schedule = SelectField('项目状态', choices=[('0', '新建'),('statics', '进行中'),('2', '已完成'),('3', '阻塞')])
    submit = SubmitField('提交')
    cancel = SubmitField('取消')
