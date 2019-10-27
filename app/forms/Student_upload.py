from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class Zong(FlaskForm):
    name = StringField('姓名',validators=[DataRequired(u"姓名不能为空")])
    stu_num = StringField('学号',validators=[DataRequired(u"学号不能为空")])
    reason = TextAreaField('申请原因', validators=[Length(0, 60, message='长度不符合要求，重新输入')])

class FX(Zong):
    Submit_FX = SubmitField('提交')


class ZZY(Zong):
    dom_dorm = StringField('原宿舍号')
    campus = StringField('所在院系')
    discipline = StringField('专业')
    Submit_ZZU = SubmitField('提交')


class XX(Zong):
    home_address = StringField('通讯地址')
    home_tel = StringField('家庭联系方式')
    per_tel = StringField('个人联系方式')
    Submit_XX = SubmitField('提交')


class TXL(Zong):
    home_address = StringField('通讯地址')
    home_tel = StringField('家庭联系方式')
    per_tel = StringField('个人联系方式')
    Submit_TXL = SubmitField('提交')


class XLZM(Zong):
    # school_sttime = DateField('入校时间')
    # school_endtime = DateField('离校时间')
    school = SelectField('所在校区',choices=[('','请输入你所在的校区'),('龙子湖校区','龙子湖校区'),('北林校区','北林校区'),('英才校区','英才校区')])
    campus = StringField('所在院系')
    discipline = StringField('专业')
    code = StringField('证书编号')
    leng_school = SelectField('学制',choices=[(4,'四年制'),(3,'三年制'),(2,'二年制')],coerce = int)
    Submit_XLZM = SubmitField('提交')


class ZXXJ(Zong):
    Submit_ZXXJ = SubmitField('提交')


class ZXSXJ(Zong):
    identity = StringField('身份证号码')
    leng_school = SelectField('学制',choices=[(4,'四年制'),(3,'三年制'),(2,'二年制')],coerce = int)
    Submit_ZXSXJ = SubmitField('提交')


class BLXJS(Zong):
    home_address = StringField('通讯地址')
    home_tel = StringField('家庭联系方式')
    per_tel = StringField('个人联系方式')
    school_endtime = DateField('离校时间')
    Submit_BLXJS = SubmitField('提交')