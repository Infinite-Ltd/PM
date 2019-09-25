from entity.db_object import db
from wtforms import StringField, SubmitField, RadioField,PasswordField,SelectField
from wtforms.validators import Required,EqualTo
from flask_wtf import FlaskForm

class OrgForm(FlaskForm):

    org_name = StringField('组织机构名称', validators=[])
    dirorg_name = StringField('上级组织机构名称', validators=[])

    submit = SubmitField('保存')
    #cancel = SubmitField('取消')