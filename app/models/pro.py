from app import db

import jinja2

from datetime import date
from flask import current_app, url_for
from flask_login import UserMixin, current_user, login_manager


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
    def query_all(name, stime, etime, matter, page=1):
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
    xh = db.Column(db.String(128))  # 学号
    xm = db.Column(db.String(10))  # 姓名
    nj = db.Column(db.String(6))  # 年级
    xy = db.Column(db.String(50))  # 学院
    bj = db.Column(db.String(30))  # 班级

    ksh = db.Column(db.String(20))  # 考生号
    lqzy = db.Column(db.String(20))  # 录取专业
    cc = db.Column(db.String(30))  # 专本科 层次
    xq = db.Column(db.String(30))  # 校区
    xb = db.Column(db.String(10))  # 性别
    mz = db.Column(db.String(10))  # 民族
    rxrq = db.Column(db.Date)  # 入学日期
    byrq = db.Column(db.Date)  # 已经毕业日期
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))
    status = db.Column(db.String(12))


# 学生输入姓名账号后，从Note中复制得到的表
class Note_yet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    xh = db.Column(db.String(128))
    xm = db.Column(db.String(10))
    xy = db.Column(db.String(50))
    bj = db.Column(db.String(30))
    zt = db.Column(db.String(30))
    zy = db.Column(db.String(20))  # 录取专业
    created_date = db.Column(db.Date, default=date.today)
    reason = db.Column(db.String(256))
    status = db.Column(db.String(12))
    home_address = db.Column(db.String(50))  # 家庭地址
    home_tel = db.Column(db.String(12))  # 家庭通讯
    per_tel = db.Column(db.String(12))  # 个人通讯
    identity = db.Column(db.String(18))  # 身份证
    school_sttime = db.Column(db.Date)  # 入校时间
    school_endtime = db.Column(db.Date)  # 离校时间
    bl_date = db.Column(db.Date)  # 保留学籍截至日期
    dom_campus = db.Column(db.String(10))  # 校区
    # dom_built = db.Column(db.String(5))             #宿舍楼号
    dom_dorm = db.Column(db.String(20))  # 寝室号
    school = db.Column(db.String(50))  # 学校
    campus = db.Column(db.String(50))  # 转专业新入院系
    code = db.Column(db.String(50))  # 证书编号
    sex = db.Column(db.String(5))  # 性别
    leng_school = db.Column(db.String(8))  # 学制
    discipline = db.Column(db.String(50))  # 转专业新入专业
    classgrade = db.Column(db.String(20))  # 转专业新入班级
    dorm = db.Column(db.String(20))
    admin_id = db.Column(db.Integer, db.ForeignKey(Admin.id))

    def to_json(self):

        # 暂定
        student = Note.query.filter(Note.xh == self.xh).first()

        if self.zt == 'xueli':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.xueli',
                                                                           name_id=self.id) + " target=\"_blank\">学历证明</a></span></div>"

        elif self.zt == 'xueji':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.xueji',
                                                                           name_id=self.id) + " target=\"_blank\">在校生学籍证明</a></span></div>"

        elif self.zt == 'zhuxiao':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.zhuxiaoxueji',
                                                                           name_id=self.id) + " target=\"_blank\">注销学籍</a></span></div>"

        elif self.zt == 'baoliuxueji':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.xuejilixiaoqingdan',
                                                                           name_id=self.id) + " target=\"_blank\">保留学籍离校清单</a></span><br>" \
                                                                                              "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.xuejishenqingbiao', name_id=self.id) + " target=\"_blank\">保留学籍申请表</a></span><br>" \
                                                                  "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.xuejitongzhishu', name_id=self.id) + " target=\"_blank\">保留学籍通知书</a></span></div>"

        elif self.zt == 'fuxue':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.fuxueshenqing',
                                                                           name_id=self.id) + " target=\"_blank\">复学申请</a></span><br>" \
                                                                                              "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.fuxueruban', name_id=self.id) + " target=\"_blank\">复学入班通知单</a></span><br></div>"

        elif self.zt == 'tuixue':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.tuixueshenqing',
                                                                           name_id=self.id) + " target=\"_blank\">退学申请</a></span><br>" \
                                                                                              "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.tuixue_lixiaoqingdan', name_id=self.id) + " target=\"_blank\">退学离校清单</a></span><br>" \
                                                                     "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.tuixue_tongzhi', name_id=self.id) + " target=\"_blank\">退学通知书</a></span></div>"

        elif self.zt == 'xiuxue':
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.xiuxueshenqing',
                                                                           name_id=self.id) + " target=\"_blank\">休学申请</a></span><br>" \
                                                                                              "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.xiuxuelixiaoqingdan', name_id=self.id) + " target=\"_blank\">休学离校清单</a></span><br>" \
                                                                    "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.xiuxuetongzhi', name_id=self.id) + " target=\"_blank\">休学通知书</a></span></div>"

        else:
            sh = "<div><span class=\"layui-badge-rim\"><a href=" + url_for('print_all.zhuanyeshenqing',
                                                                           name_id=self.id) + " target=\"_blank\">转专业申请</a></span><br>" \
                                                                                              "<span class=\"layui-badge-rim\"><a href=" + url_for(
                'print_all.zhuanyeruban', name_id=self.id) + " target=\"_blank\">转专业入班</a></span><br></div>"

            # 暂定
        if (self.zt == 'tuixue' or self.zt == 'xiuxue' or self.zt == 'zhuxiao' or self.zt == 'fuxue') and (
                student.status == None or student.status == ''):
            cz = "<div>" \
                 "<form method=\"post\" action=" + url_for('admin_edit.delete_stu', name_id=self.id) + ">" \
                                                                                                       "<a class=\"layui-btn\" style=\"background: #9acfea\" href=\"" + url_for(
                'admin_edit.confirm_tx', name_id=self.id) + "\">确认</a>" \
                                                            "<input class=\"layui-btn\" id=\"Submit\" name=\"Submit\" type=\"submit\" value=\"删除\">" \
                                                            "<a class=\"layui-btn layui-btn-primary\" href=\"" + url_for(
                'admin_edit.edit_new', ZT=self.zt, name_id=self.id) + "\">编辑</a>" \
                                                                      "</form>" \
                                                                      "</div>"
        else:
            cz = "<div>" \
                 "<form method=\"post\" action=" + url_for('admin_edit.delete_stu', name_id=self.id) + ">" \
                                                                                                       "<input class=\"layui-btn\" id=\"Submit\" name=\"Submit\" type=\"submit\" value=\"删除\">" \
                                                                                                       "<a class=\"layui-btn layui-btn-primary\" href=\"" + url_for(
                'admin_edit.edit_new', ZT=self.zt, name_id=self.id) + "\">编辑</a>" \
                                                                      "</form>" \
                                                                      "</div>"

        if (self.zt == 'zhuanzhuanye' or self.zt == 'fuxue') and self.discipline is not None and self.classgrade is not None:
            bj = self.classgrade,
            xy = self.campus
        else:
            bj = self.bj
            xy = self.xy


        return {
            'xm': self.xm,
            'xh': self.xh,
            'xy': xy,
            'bj': bj,
            # 'xy': self.xy,
            # 'bj': self.bj,
            'sh': sh,
            'created_date': str(self.created_date),
            'reason': jinja2.escape(self.reason),
            'cz': cz,
            'discipline': self.discipline,
            'classgrade': self.classgrade
        }

    @staticmethod  # 静态回调
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
