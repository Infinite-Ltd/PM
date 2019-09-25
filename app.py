#from entity.db_object import getDB
from flask import request
#from app_obj import app
from flask import Flask,session
from flask_bootstrap import Bootstrap
from flask import  render_template
from forms.userform import UserForm
from forms.orgform import OrgForm
from forms.programform import ProgramForm
from forms.trainingform import TrainingForm
from entity.userinfo import User
from entity.role import Role
from entity.training import Training
import json
from flask_sqlalchemy import SQLAlchemy
import uuid
from entity.program import Program
from entity.organization import Organization
#from flask_sqlalchemy import
from flask_wtf import *
from datetime import  timedelta

app = Flask(__name__)
from entity.db_object import getDB
app.config["SECRET_KEY"] = 'weq!@#'
app.config["PREMANENT_SESSION_LIFETIME"] =timedelta(days=1)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/PMS?charset=utf8'
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#db = SQLAlchemy(app, use_native_unicode='utf8')
db = getDB()
#db = getDB()
bootstrap = Bootstrap(app)



@app.route('/login', methods=['post', 'get'])
def login():
    user = User()
    username = ''
    password = ''
    message = ''
    print(request.form.get('username'))
    print(request.form.get('pwd'))
    if request.form != None:
        username = request.form.get('username')
        password = request.form.get('pwd')
    if user.query.filter_by(wid = username).all():
        if user.query.filter_by(wid = username).all()[0].password == password:
            session['username'] = username
            return render_template('base.html', name=username)
        else:
            message = '密码或者用户名有问题啊！！！'
    return render_template('login.html', message=message)


@app.route('/register', methods=['post', 'get'])
def register():
    user = UserForm()
    wid = user.workId.data
    role = Role()
    authority = ''
    if user.validate_on_submit():
        if user.isleader.data == '1':
            authority = 'admin'
        else:
            authority = 'ordinary'
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&')

        users = User(wid=wid, authority=Role.query.filter_by(roleName=authority).all()[0].role_id, password=user.password.data.encode('utf8'),
                     name=user.username.data.encode('utf8'), org_name=user.department.data.encode('utf8'),
                     org_guid=Organization.query.filter_by(org_name=user.department.data).all()[0].org_guid,
                     isleader=user.isleader.data.encode('utf8'),
                     dirleader=user.dirleader.data.encode('utf8'), picture=None, enabled='1')
        db.session.add(users)
        print('rrrrrrrrrrrrrr')
        db.session.commit()
        print(User.query.filter_by(wid=user.workId.data).all())
        return render_template('login.html')
    return render_template('formbase.html', form=user,name='嘿嘿',title='用户',modle='user')

@app.route('/GG', methods=['get','post'])
def hello_world():
    user = UserForm()
    print(user.username)
    return render_template('formbase.html',form=user, name='啦啦啦',title='用户', modle ='user')


@app.route('/cms')
def home():
    return render_template('base.html')


@app.route('/add', methods=['get','post'])
def addProgram():
    pro = ProgramForm()
    return render_template('formbase.html', form=pro, title='项目')


@app.route('/home', methods=['get','post'])
def toHome():
    return render_template('homepage.html')


@app.route('/org/<operate>', methods=['get','post'])
def orgDao(operate):
    org = OrgForm()
    if operate == 'add' and org.validate_on_submit() :
        print('oooooooo%%%%%%%%%')
        print(org.dirorg_name.data)
        print()
        orgObject = Organization(org_guid=str(uuid.uuid1()).encode('utf8'), org_name=org.org_name.data,dir_name=org.dirorg_name.data.encode('utf8'),
                                 dir_guid=Organization.query.filter_by(org_name=org.dirorg_name.data).all()[0].org_guid)
        print('执行到这里')
        db.session.add(orgObject)
        db.session.commit()
        print('执行了')
    return render_template('formbase.html',form=org,name='嘿嘿',title='组织机构',modle='org')


@app.route('/user/<operate>', methods=['get', 'post'])
def userDao(operate):
    user = UserForm()
    wid = user.workId.data
    authority = ''
    if operate == 'add' and user.validate_on_submit():
        if user.isleader.data == '1':
            authority = 'admin'
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print(user.isleader.data)
        users = User(wid=wid,authority=authority, password=user.password.data.encode('utf8'), name=user.username.data.encode('utf8'), org_name=user.department.data.encode('utf8'),
                     org_guid=Organization.query.filter_by(org_name=user.department.data).all()[0].encode('utf8'), isleader = user.isleader.data.encode('utf8'),
                     dirleader=user.dirleader.data.encode('utf8'),picture=None,enabled='1')
        db.session.add(users)
        print('rrrrrrrrrrrrrr')
        db.session.commit()
        print(User.query.filter_by(wid=user.workId.data).all())
        return render_template('base.html', name=user.username.data)
    elif operate == 'delete':
        db.session.delete(user)
    elif operate == 'modify':
        db.session.add(user)
    elif operate == 'query':
        #User.query.filter_by(wid = )
        pass
    elif operate == 'queryall':
        datas = User.query.all()
        return render_template('showusers.html', datas=datas)
    return render_template('formbase.html', form=user, name='啦啦啦',title='用户', modle ='user')


@app.route('/program/<operator>', methods=['get', 'post'])
def programDao(operator):
    form = ProgramForm()
    if operator == 'queryall':
        print('enter into..............')
        datas = Program.query.all()
        return render_template('showprograms.html', datas=datas)


@app.route('/training/<operator>', methods=['get', 'post'])
def trainingDao(operator):
    trainForm = TrainingForm()
    if operator == 'add' and trainForm.validate_on_submit():
        train = Training(train_guid=str(uuid.uuid1()).encode('utf8'), train_name=trainForm.train_name.data,
                         train_content=trainForm.train_content.data,train_time=trainForm.train_time.data,
                         pic_guid=trainForm.pic_guid.data,pic_name=User.query.filter_by(wid=trainForm.pic_guid.data).all()[0].name,
                         remarks=trainForm.remarks.data)
        db.session.add(train)
        db.session.commit()
        datas = Training.query.all()
        return render_template('showtrainings.html',datas = datas)
    if operator == 'delete':
        trainName = request.data
        train = Training(train_name = trainName)
        db.session.delete()
        db.session.commit()
    if operator == 'queryall':
        datas = Training.query.all()
        return render_template('showtrainings.html',datas = datas )
    return render_template('formbase.html',form=trainForm,title='培训',modle='training')



@app.route('/query',methods=['post','get'])
def test():
    data = {{'字段一':'测试部','字段二':'哈哈哈'},{'字段一':'哈尔滨','字段二':'啦啦啦'}}
    datas = json.dumps(data)
    print('ajax^^^^^^^^^^^^^^')
    return datas


@app.route('/test', methods=['post','get'])
def s():
    return render_template('homepage.html')

@app.route('/22')
def yy():
    return render_template('tables.html')

# print(__name__)
if __name__ == '__main__':
    print('aaaaaaaaa')
    app.run(host='0.0.0.0',port='5633')
