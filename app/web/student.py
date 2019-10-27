from datetime import date
import datetime
from flask import Blueprint, flash, render_template, redirect, url_for
from app import limiter, db
from app.forms.Student_upload import (FX, ZZY, XX, TXL, XLZM, BLXJS, ZXXJ, ZXSXJ)
from app.models.pro import Note_yet, Note



student = Blueprint("student", __name__)

# 学生 上传数据
@student.route("/front", methods=['GET', 'POST'])
@limiter.limit("10000/day")
def front():
    FX_FORM = FX()
    ZZY_FORM =ZZY()
    XX_FORM = XX()
    TXL_FORM = TXL()
    XLZM_FORM = XLZM()
    BLXJS_FORM = BLXJS()
    ZXXJ_FORM = ZXXJ()
    ZXSXJ_FORM = ZXSXJ()

    today = datetime.date.today()

    if FX_FORM.Submit_FX.data and FX_FORM.validate():
        name = FX_FORM.name.data
        stu_num = FX_FORM.stu_num.data
        matter = 'fuxue'
        reason = FX_FORM.reason.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt=matter,
                                        zy=userxh.lqzy, sex=userxh.xb,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))

    if ZZY_FORM.Submit_ZZU.data and ZZY_FORM.validate():
        name = ZZY_FORM.name.data
        stu_num = ZZY_FORM.stu_num.data
        campus = ZZY_FORM.campus.data
        reason = ZZY_FORM.reason.data
        dom_dorm = ZZY_FORM.dom_dorm.data
        discipline = ZZY_FORM.discipline.data
        matter='zhuanzhuanye'
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(
                                        xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt=matter, sex=userxh.xb,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        discipline=discipline if discipline is not None else '',
                                        campus=campus if campus is not None else '',zy=userxh.lqzy,
                                        dom_dorm=dom_dorm if dom_dorm is not None else ''
                                        )
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))

    if XX_FORM.Submit_XX.data and XX_FORM.validate():
        name = XX_FORM.name.data
        stu_num = XX_FORM.stu_num.data
        matter = 'xiuxue'
        reason = XX_FORM.reason.data
        per_tel = XX_FORM.per_tel.data
        home_address = XX_FORM.home_address.data
        home_tel = XX_FORM.home_tel.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='休学', sex=userxh.xb,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        home_address=home_address if home_address is not None else '',
                                        home_tel=home_tel if home_tel is not None else '',zy=userxh.lqzy,
                                        per_tel=per_tel if per_tel is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))
    if TXL_FORM.Submit_TXL.data and TXL_FORM.validate():
        name = TXL_FORM.name.data
        stu_num = TXL_FORM.stu_num.data
        matter = 'tuixue'
        reason = TXL_FORM.reason.data
        per_tel = TXL_FORM.per_tel.data
        home_address = TXL_FORM.home_address.data
        home_tel = TXL_FORM.home_tel.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt=matter, sex=userxh.xb,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        home_address=home_address if home_address is not None else '',
                                        home_tel=home_tel if home_tel is not None else '',zy=userxh.lqzy,
                                        per_tel=per_tel if per_tel is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))
    if XLZM_FORM.Submit_XLZM.data and XLZM_FORM.validate():
        name = XLZM_FORM.name.data
        stu_num = XLZM_FORM.stu_num.data
        matter = 'xueli'
        reason = XLZM_FORM.reason.data
        school_sttime = str(datetime.datetime.now().date())[0:2]+stu_num[0:2]+'-09-01'
        school_endtime = str(int(str(datetime.datetime.now().date())[0:2]+stu_num[0:2]) + XLZM_FORM.leng_school.data) +'-07-01'
        school = XLZM_FORM.school.data
        campus = XLZM_FORM.campus.data
        discipline = XLZM_FORM.discipline.data
        code = XLZM_FORM.code.data
        leng_school = XLZM_FORM.leng_school.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt=matter, sex=userxh.xb,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        school_sttime=school_sttime if school_sttime is not None else '',
                                        school_endtime=school_endtime if school_endtime is not None else today,
                                        school=school if school is not None else '',
                                        campus=campus if campus is not None else '',
                                        code=code if code is not None else '',zy=userxh.lqzy,
                                        leng_school=leng_school if leng_school is not None else '',
                                        discipline=discipline if discipline is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))
    if BLXJS_FORM.Submit_BLXJS.data and BLXJS_FORM.validate():
        name = BLXJS_FORM.name.data
        stu_num = BLXJS_FORM.stu_num.data
        matter = 'baoliuxueji'
        reason = BLXJS_FORM.reason.data

        school_endtime = BLXJS_FORM.school_endtime.data
        per_tel = BLXJS_FORM.per_tel.data
        home_address = BLXJS_FORM.home_address.data
        home_tel = BLXJS_FORM.home_tel.data

        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt=matter, sex=userxh.xb,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        school_endtime=school_endtime if school_endtime is not None else today,
                                        home_address=home_address if home_address is not None else '',
                                        home_tel=home_tel if home_tel is not None else '',zy=userxh.lqzy,
                                        per_tel=per_tel if per_tel is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))
    if ZXXJ_FORM.Submit_ZXXJ.data and ZXXJ_FORM.validate():
        name = ZXXJ_FORM.name.data
        stu_num = ZXXJ_FORM.stu_num.data
        matter = 'zhuxiao'
        reason = ZXXJ_FORM.reason.data

        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt=matter,zy=userxh.lqzy,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))
    if ZXSXJ_FORM.Submit_ZXSXJ.data and ZXSXJ_FORM.validate():
        name = ZXSXJ_FORM.name.data
        stu_num = ZXSXJ_FORM.stu_num.data
        matter = 'xueji'
        reason = ZXSXJ_FORM.reason.data
        identity = ZXSXJ_FORM.identity.data
        leng_school = ZXSXJ_FORM.leng_school.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (userxh.status == 'tuixue' or userxh.status == 'xiuxue') and matter == 'xueji':
                return '处于休学或退学状态，无法申请在校生学籍'
            if userxh.rxrq < today <userxh.byrq:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt=matter, sex=userxh.xb,
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        identity=identity if identity is not None else '',zy=userxh.lqzy,
                                        leng_school=leng_school if leng_school is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            else:
                flash("学籍处于非正常状态，请确认后再次申请")
            return redirect(url_for('student.front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('student.front'))
    return render_template('Student/S_upload.html', FX_FORM=FX_FORM, ZZY_FORM = ZZY_FORM, XX_FORM = XX_FORM, TXL_FORM = TXL_FORM,
                           XLZM_FORM = XLZM_FORM, BLXJS_FORM = BLXJS_FORM, ZXXJ_FORM = ZXXJ_FORM, ZXSXJ_FORM = ZXSXJ_FORM)