from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from huojingyuan import app, login_manager
from flask_migrate import Migrate
from flask_login import UserMixin,current_user
from datetime import date
from flask import current_app, url_for

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(180))
    name = db.Column(db.String(30))
    role = db.Column(db.String(30))
    xy = db.Column(db.String(50))
    articles = db.relationship('Note_yet', lazy='dynamic')
    articles_Note = db.relationship('Note')

    @staticmethod
    def query_all(name, stime, etime, matter,page=1):
        activites = current_user.articles
        if name != '':
            activites = activites.filter(Note_yet.xm.like('%' + name + '%'))
        if stime != '' and etime == '':
            # etime = stime
            activites = activites.filter(Note_yet.created_date == stime)
        elif stime != '' and etime != '':
            activites = activites.filter(Note_yet.created_date.between(stime, etime))
        else:
            pass
        if matter != 'info':
            activites = activites.filter(Note_yet.zt == matter)
        return activites.paginate(
            page, per_page=current_app.config['POST_PER_PAGE']
        )


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    xh = db.Column(db.String(128))
    xm = db.Column(db.String(10))
    xy = db.Column(db.String(50))
    bj = db.Column(db.String(30))
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))
    status = db.Column(db.String(10))


# 学生输入姓名账号后，从Note中复制得到的表
class Note_yet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    xh = db.Column(db.String(128))
    xm = db.Column(db.String(10))
    xy = db.Column(db.String(50))
    bj = db.Column(db.String(30))
    zt = db.Column(db.String(30))
    created_date = db.Column(db.Date, default=date.today)
    reason = db.Column(db.String(256))
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))
    status = db.Column(db.String(10))
    home_address = db.Column(db.String(50))         #家庭地址
    home_tel = db.Column(db.String(12))             #家庭通讯
    per_tel = db.Column(db.String(12))              #个人通讯
    identity = db.Column(db.String(18))             #身份证
    school_sttime = db.Column(db.String(16))        #入校时间
    school_endtime = db.Column(db.String(16))       #离校时间
    dom_campus = db.Column(db.String(10))           #校区
    dom_built = db.Column(db.String(5))             #宿舍楼号
    dom_dorm = db.Column(db.String(5))              #寝室号
    school = db.Column(db.String(50))               #学校
    campus = db.Column(db.String(20))               #院系
    code = db.Column(db.String(50))                 #证书编号
    sex = db.Column(db.String(5))                   #性别
    leng_school = db.Column(db.String(8))           #学制···未加
    discipline = db.Column(db.String(20))           #专业···未加

    def to_json(self):
        if self.zt == '学历':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('xueli',name_id=self.id) + " target=\"_blank\">学历证明</a></span></div>"

        elif self.zt == '学籍':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('xueji', name_id=self.id) + " target=\"_blank\">在校生学籍证明</a></span></div>"

        elif self.zt == '注销':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('zhuxiaoxueji', name_id=self.id) + " target=\"_blank\">注销学籍</a></span></div>"

        elif self.zt == '保留学籍':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('xuejilixiaoqingdan', name_id=self.id) + " target=\"_blank\">保留学籍离校清单</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('xuejishenqingbiao', name_id=self.id) + " target=\"_blank\">保留学籍申请表</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('xuejitongzhishu', name_id=self.id) + " target=\"_blank\">保留学籍通知书</a></span></div>"

        elif self.zt == '复学':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('fuxueshenqing', name_id=self.id) + " target=\"_blank\">复学申请</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('fuxueruban', name_id=self.id) + " target=\"_blank\">复学入班通知单</a></span><br></div>"

        elif self.zt == '退学':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('tuixueshenqing', name_id=self.id) + " target=\"_blank\">退学申请</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('tuixue_lixiaoqingdan', name_id=self.id) + " target=\"_blank\">退学离校清单</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('tuixue_tongzhi', name_id=self.id) + " target=\"_blank\">退学通知书</a></span></div>"

        elif self.zt == '休学':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('xiuxueshenqing', name_id=self.id) + " target=\"_blank\">休学申请</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('xiuxuelixiaoqingdan', name_id=self.id) + " target=\"_blank\">休学离校清单</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('xiuxuetongzhi', name_id=self.id) + " target=\"_blank\">休学通知书</a></span></div>"

        else:
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('zhuanyeshenqing', name_id=self.id) + " target=\"_blank\">转专业申请</a></span><br>" \
                 "<span class=\"layui-badge-rim\"><a href=" + url_for('zhuanyeruban', name_id=self.id) + " target=\"_blank\">转专业入班</a></span><br></div>"

        if (self.zt == '退学' or self.zt == '休学' or self.zt == '注销') and (self.status == None or self.status == '') :
            cz = "<div>" \
                 "<form method=\"post\" action=" + url_for('delete_stu',name_id=self.id) + ">" \
                 "<a class=\"layui-btn\" style=\"background: #9acfea\" href=\"/confirm_tx/"+ str(self.id) +"\">确认</a>" \
                 "<input class=\"layui-btn\" id=\"Submit\" name=\"Submit\" type=\"submit\" value=\"删除\">" \
                 "<a class=\"layui-btn layui-btn-primary\" href=\"/edit/"+ str(self.id) +"\">编辑</a>" \
                 "</form>" \
                 "</div>"
        else:
            cz = "<div>" \
                 "<form method=\"post\" action=" + url_for('delete_stu',name_id=self.id) + ">" \
                 "<input class=\"layui-btn\" id=\"Submit\" name=\"Submit\" type=\"submit\" value=\"删除\">" \
                 "<a class=\"layui-btn layui-btn-primary\" href=\"/edit/"+ str(self.id) +"\">编辑</a>" \
                 "</form>" \
                 "</div>"
        return {
            'xm': self.xm,
            'xh': self.xh,
            'xy': self.xy,
            'bj': self.bj,
            'sh': sh,
            'created_date': str(self.created_date),
            'reason': self.reason,
            'cz': cz
        }

    @staticmethod  #静态回调
    def query_all(name, stime, etime, matter, department, page, per_page):
        activites = Note_yet.query
        if name != '':
            activites = activites.filter(Note_yet.xm.like('%' + name + '%'))
        if stime != '' and etime == '':
            # etime = stime
            activites = activites.filter(Note_yet.created_date == stime)
        elif stime != '' and etime != '':
            activites = activites.filter(Note_yet.created_date.between(stime, etime))
        else:
            pass
        if matter != 'info':
            activites = activites.filter(Note_yet.zt == matter)
        if department != 'admin':
            activites = activites.filter(Note_yet.xy == department)
        return activites.paginate(
            page, per_page=per_page
        )


# flask_login load_user函数
@login_manager.user_loader
def load_user(user_id):
    user = Admin.query.get(int(user_id))
    return user
