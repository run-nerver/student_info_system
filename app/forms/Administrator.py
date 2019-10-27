from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField, RadioField, validators, ValidationError, TextAreaField
from app.models.pro import Admin
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired


# 登录表单
class LoginForm(FlaskForm):
    name = StringField('姓名')
    password = PasswordField('密码')
    remember = BooleanField('Remember me')
    Submit = SubmitField('登陆')


# 管理员查询事项表单
class QueryForm(FlaskForm):
    name = StringField('姓名')
    matter = SelectField('办理事项', choices=[
        ('info', '请选择办理事项'),
        ('xueli', '1、学历证明申请'),
        ('xueji', '2、在校生学籍申请'),
        ('zhuxiao', '3、注销学籍申请'),
        ('fuxue', '4、复学类申请'),
        ('xiuxue','5、休学类申请'),
        ('baoliuxueji','6、保留学籍类申请'),
        ('zhuanzhuanye','7、转专业类申请'),
        ('tuixue', '8、退学类申请')])
    datetimestart = DateField('起始时间')
    datetimeend = DateField('截止时间')
    department = SelectField('院系')
    Submit = SubmitField('查询')

    # 页面下拉自动关联数据库（根据院系查询）
    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.department.choices = [(v.xy, v.xy) for v in Admin.query.all()]


# 删除学生表单
class DeleteForm(FlaskForm):
    Submit = SubmitField('删除')


# 编辑学生表单
class EditForm(FlaskForm):
    xh = StringField('学号')
    xm = StringField('姓名')
    xy = StringField('学院')
    bj = StringField('班级', validators=[DataRequired])
    zt = StringField('办理事项')
    created_date = DateField('申请日期')
    reason = TextAreaField('原因')
    status = StringField('状态')

    sex = SelectField('性别', choices=[('none', 'none'), ('男', '男'), ('女', '女')])
    # 保留学籍、退学、休学
    school_sttime = DateField('入校时间')
    school_endtime = DateField('离校时间')
    home_address = StringField('通讯地址')
    home_tel = StringField('家庭联系方式')
    per_tel = StringField('个人联系方式')

    # 转专业
    dom_campus = StringField('原校区')
    dom_built = StringField('原楼号')
    dom_dorm = StringField('原宿舍号')

    # 学历证明
    school = SelectField('所在校区',choices=[('','请输入你所在的校区'),('龙子湖校区','龙子湖校区'),('北林校区','北林校区'),('英才校区','英才校区')])
    campus = StringField('所在院系')
    code = StringField('证书编号')
    identity = StringField('身份证号码')
    leng_school = SelectField('学制',choices=[('四年制','四年制'),('三年制','三年制'),('二年制','二年制')])
    discipline = StringField('专业')
    # new_dorm = StringField('原宿舍号')

    Submit = SubmitField('提交')


class EditTeacher(FlaskForm):
    old_password = PasswordField('Old Password')
    new_password = PasswordField('New Password')
    repeat_password = PasswordField('Repeat Password')
    Submit = SubmitField('确认修改')


# 上传表单
class UploadForm(FlaskForm):
    file = FileField('上传', validators=[FileRequired(), FileAllowed(['xls'])])
    submit = SubmitField()