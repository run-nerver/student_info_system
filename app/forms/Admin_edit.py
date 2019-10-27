from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired


class Core(FlaskForm):
    xh = StringField('学号')
    xm = StringField('姓名')
    sex = SelectField('性别', choices=[('none', 'none'), ('男', '男'), ('女', '女')])
    xy = StringField('学院')
    bj = StringField('班级')
    zt = StringField('办理事项')
    reason = TextAreaField('原因')


class ZZY_EDIT(Core):
    dom_dorm = StringField('原宿舍号')
    school = SelectField('校区', default='', choices=[('','请输入你所在的校区'),('龙子湖校区','龙子湖校区'),('北林校区','北林校区'),('英才校区','英才校区')])
    campus = StringField('院系')
    discipline = StringField('专业')
    classgrade = StringField('班级')
    dom_built = StringField('原楼号')
    dom_campus = StringField('原校区')
    dorm = StringField('拟转宿舍号')
    Submit_ZZY = SubmitField('提交')


class FX_EDIT(Core): # OK
    school = SelectField('校区', default='', choices=[('','请输入你所在的校区'), ('龙子湖校区','龙子湖校区'), ('北林校区','北林校区'), ('英才校区','英才校区')])
    campus = StringField('院系')
    discipline = StringField('专业')
    classgrade = StringField('班级')
    Submit_FX = SubmitField('提交')


class XX_EDIT(Core): # OK
    home_address = StringField('通讯地址')
    home_tel = StringField('家庭联系方式')
    per_tel = StringField('个人联系方式')
    Submit_XX = SubmitField('提交')


class TXL_EDIT(Core):
    home_address = StringField('通讯地址')
    home_tel = StringField('家庭联系方式')
    per_tel = StringField('个人联系方式')
    Submit_TXL = SubmitField('提交')


class XLZM_EDIT(Core):  # OK
    school_sttime = DateField('入校时间')
    school_endtime = DateField('离校时间')
    school = SelectField('所在校区',choices=[('','请输入你所在的校区'),('龙子湖校区','龙子湖校区'),('北林校区','北林校区'),('英才校区','英才校区')])
    campus = StringField('所在院系')
    discipline = StringField('专业')
    code = StringField('证书编号')
    leng_school = SelectField('学制',choices=[(4,'四年制'),(3,'三年制'),(2,'二年制')],coerce = int)
    Submit_XLZM = SubmitField('提交')


class ZXXJ_EDIT(Core): # OK
    Submit_ZXXJ = SubmitField('提交')


class ZXSXJ_EDIT(Core):
    identity = StringField('身份证号码')
    leng_school = SelectField('学制',choices=[(4,'四年制'),(3,'三年制'),(2,'二年制')],coerce = int)
    Submit_ZXSXJ = SubmitField('提交')


class BLXJS_EDIT(Core):
    home_address = StringField('通讯地址')
    home_tel = StringField('家庭联系方式')
    per_tel = StringField('个人联系方式')
    bl_date = DateField('截至时间')
    Submit_BLXJS = SubmitField('提交')