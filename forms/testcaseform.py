from entity.db_object import db
from wtforms import StringField, SubmitField, RadioField,PasswordField,SelectField,TextAreaField
from wtforms.validators import Required,EqualTo
from flask_wtf import FlaskForm

class TestcaseForm(FlaskForm):

    caseName = StringField('用例名称', validators=[Required])
    precase = TextAreaField('前置条件', validators=[Required])
    testSteps = TextAreaField('测试步骤', validators=[Required])
    testResult = TextAreaField('预期结果')
    enable = SelectField('是否可用', choices=[('0', '可用'), ('statics', '不可用')])
    automatic = SelectField('是否可自动化', choices==[('0', '是'), ('statics', '否')])
    submit = SubmitField('提交')
    #cancel = SubmitField('取消')