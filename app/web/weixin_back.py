from datetime import date

from flask import Blueprint, json, request, flash
from app import db
from app.models.pro import Note, Note_yet

weixin = Blueprint("weixin", __name__)


@weixin.route('/fuxue', methods=['POST'])
def fuxue():
    name = str(json.loads(request.values.get('name')))
    number = str(json.loads(request.values.get('number')))
    reason = str(json.loads(request.values.get('reason')))
    userxh = Note.query.filter_by(xh=number).first()
    student = Note.query.filter_by(xm=name).first()

    if userxh and userxh.xm == name:
        if userxh.status == 'xiuxue' or userxh.status == 'baoliuxueji':
            student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, admin_id=userxh.admin_id, bj=userxh.bj,
                                    zt='fuxue', reason=reason, zy=userxh.lqzy, sex=userxh.xb)
            userxh.status = 'fuxue'
            db.session.add(student_info)
            db.session.commit()
            res = '提交成功'
            return json.dumps(res.encode('utf-8').decode('utf8'))
        else:
            res = '学生处于非休学状态，无法申请复学'
            return json.dumps(res.encode('utf-8').decode('utf8'))
    else:
        res = '账号或密码不对，请重新输入'
        return json.dumps(res.encode('utf-8').decode('utf8'))


@weixin.route('/zhuanzhuanye', methods=['POST'])
def zhuanzhuanye():
    name = str(json.loads(request.values.get('name')))
    number = str(json.loads(request.values.get('number')))
    room_number = str(json.loads(request.values.get('dom_dorm')))
    reason = str(json.loads(request.values.get('reason')))
    userxh = Note.query.filter_by(xh=number).first()
    student = Note.query.filter_by(xm=name).first()

    if userxh and userxh.xm == name:

        if userxh.status == 'xiuxue' or userxh.status == 'tuixue' or userxh.status == 'zhuxiaoxueji':
            res = '学籍处于非正常状态，请确认后再次申请'
            return json.dumps(res.encode('utf-8').decode('utf8'))
        else:
            student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, admin_id=userxh.admin_id, bj=userxh.bj,
                                    zt='zhuanzhuanye', reason=reason, dom_dorm=room_number, zy=userxh.lqzy, sex=userxh.xb)
            db.session.add(student_info)
            db.session.commit()
            res = '提交成功'
            return json.dumps(res.encode('utf-8').decode('utf8'))
    else:
        res = '账号或密码不对，请重新输入'
        return json.dumps(res.encode('utf-8').decode('utf8'))


@weixin.route('/xiuxue', methods=['POST'])
def xiuxue():
    name = str(json.loads(request.values.get('name')))
    number = str(json.loads(request.values.get('number')))
    per_tel = str(json.loads(request.values.get('per_tel')))
    home_tel = str(json.loads(request.values.get('home_tel')))
    home_address = str(json.loads(request.values.get('home_address')))
    reason = str(json.loads(request.values.get('reason')))
    userxh = Note.query.filter_by(xh=number).first()
    student = Note.query.filter_by(xm=name).first()
    if userxh and userxh.xm == name:
        if userxh.status == 'xiuxue' or userxh.status == 'tuixue' or userxh.status == 'zhuxiaoxueji':
            res = '学籍处于非正常状态，请确认后再次申请'
            return json.dumps(res.encode('utf-8').decode('utf8'))
        else:
            student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, admin_id=userxh.admin_id, bj=userxh.bj,
                                    zt='xiuxue', reason=reason, per_tel=per_tel, home_tel=home_tel,
                                    home_address=home_address, zy=userxh.lqzy, sex=userxh.xb)
            # student.status = '休学'
            db.session.add(student_info)
            db.session.commit()
            res = '提交成功'
            return json.dumps(res.encode('utf-8').decode('utf8'))
    else:
        res = '账号或密码不对，请重新输入'
        return json.dumps(res.encode('utf-8').decode('utf8'))


@weixin.route('/tuixue', methods=['POST'])
def tuixue():
    name = str(json.loads(request.values.get('name')))
    number = str(json.loads(request.values.get('number')))
    per_tel = str(json.loads(request.values.get('per_tel')))
    home_tel = str(json.loads(request.values.get('home_tel')))
    home_address = str(json.loads(request.values.get('home_address')))
    reason = str(json.loads(request.values.get('reason')))
    userxh = Note.query.filter_by(xh=number).first()
    student = Note.query.filter_by(xm=name).first()
    if userxh and userxh.xm == name:
        if userxh.status == 'tuixue' or userxh.status == 'zhuxiaoxueji':
            res = '学籍处于非正常状态，请确认后再次申请'
            return json.dumps(res.encode('utf-8').decode('utf8'))
        else:
            student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, admin_id=userxh.admin_id, bj=userxh.bj,
                                    zt='tuixue', reason=reason, per_tel=per_tel, home_tel=home_tel,
                                    home_address=home_address, zy=userxh.lqzy, sex=userxh.xb)
            # student.status = '休学'
            db.session.add(student_info)
            db.session.commit()
            res = '提交成功'
            return json.dumps(res.encode('utf-8').decode('utf8'))
    else:
        res = '账号或密码不对，请重新输入'
        return json.dumps(res.encode('utf-8').decode('utf8'))


@weixin.route('/xueli', methods=['POST'])
def xueli():
    name = str(json.loads(request.values.get('name')))
    sex = str(json.loads(request.values.get('sex')))
    number = str(json.loads(request.values.get('number')))
    xiaoqu = str(json.loads(request.values.get('xiaoqu')))
    yuanxi = str(json.loads(request.values.get('yuanxi')))
    major = str(json.loads(request.values.get('major')))
    leng_school = str(json.loads(request.values.get('leng_school')))
    code = str(json.loads(request.values.get('code')))
    reason = str(json.loads(request.values.get('reason')))
    entrance_school = str(json.loads(request.values.get('entrance_school')))
    entrance_school = entrance_school + '-09'+'-01'
    leave_school = str(json.loads(request.values.get('leave_school')))
    leave_school = leave_school + '-06' + '-30'
    # userxh = Note.query.filter_by(xh=number).first()
    # student = Note.query.filter_by(xm=name).first()
    # if userxh and userxh.xm == name:
    #     if student.status == '退学' or student.status == '注销学籍':
    #         res = '学籍处于非正常状态，请确认后再次申请'
    #         return json.dumps(res.encode('utf-8').decode('utf8'))
    #     else:
    student_info = Note_yet(xm=name, xh=number, xy=yuanxi, sex=sex,
                            zt='xueli', reason=reason, dom_campus=xiaoqu, campus=yuanxi, discipline=major, code=code,
                            school_sttime=entrance_school, school_endtime=leave_school,leng_school=leng_school)
    # student.status = '休学'
    db.session.add(student_info)
    db.session.commit()
    res = '提交成功'
    return json.dumps(res.encode('utf-8').decode('utf8'))


@weixin.route('/baoliuxueji', methods=['POST'])
def baoliuxueji():
    name = str(json.loads(request.values.get('name')))
    number = str(json.loads(request.values.get('number')))
    per_tel = str(json.loads(request.values.get('per_tel')))
    home_tel = str(json.loads(request.values.get('home_tel')))
    home_address = str(json.loads(request.values.get('home_address')))
    bl_date = str(json.loads(request.values.get('bl_date')))
    reason = str(json.loads(request.values.get('reason')))
    userxh = Note.query.filter_by(xh=number).first()
    student = Note.query.filter_by(xm=name).first()
    if userxh and userxh.xm == name:
        if userxh.status == 'xiuxue' or userxh.status == 'tuixue' or userxh.status == 'zhuxiaoxueji':
            res = '学籍处于非正常状态，请确认后再次申请'
            return json.dumps(res.encode('utf-8').decode('utf8'))
        else:
            student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, admin_id=userxh.admin_id, bj=userxh.bj,
                                    zt='baoliuxueji', reason=reason, per_tel=per_tel, home_tel=home_tel,
                                    home_address=home_address, school_endtime=bl_date, zy=userxh.lqzy, sex=userxh.xb)
            userxh.status = 'baoliuxueji'
            db.session.add(student_info)
            db.session.commit()
            res = '提交成功'
            return json.dumps(res.encode('utf-8').decode('utf8'))
    else:
        res = '账号或密码不对，请重新输入'
        return json.dumps(res.encode('utf-8').decode('utf8'))


@weixin.route('/zhuxiao', methods=['POST'])
def zhuxiao():
    name = str(json.loads(request.values.get('name')))
    number = str(json.loads(request.values.get('number')))
    reason = str(json.loads(request.values.get('reason')))
    userxh = Note.query.filter_by(xh=number).first()
    student = Note.query.filter_by(xm=name).first()

    if userxh and userxh.xm == name:
        student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, admin_id=userxh.admin_id, bj=userxh.bj,
                                zt='zhuxiao', reason=reason, zy=userxh.lqzy, sex=userxh.xb)
        userxh.status = 'zhuxiao'
        db.session.add(student_info)
        db.session.commit()
        res = '提交成功'
        return json.dumps(res.encode('utf-8').decode('utf8'))
    else:
        res = '账号或密码不对，请重新输入'
        return json.dumps(res.encode('utf-8').decode('utf8'))


@weixin.route('/xuejizhengming', methods=['POST'])
def xuejizhengming():
    name = str(json.loads(request.values.get('name')))
    number = str(json.loads(request.values.get('number')))
    identity = str(json.loads(request.values.get('identity')))
    leng_school = str(json.loads(request.values.get('leng_school')))
    reason = str(json.loads(request.values.get('reason')))
    userxh = Note.query.filter_by(xh=number).first()
    student = Note.query.filter_by(xm=name).first()

    # if userxh.rxrq < date.today() < userxh.byrq:
    #     flash("提交成功，请通知老师在系统进行下一步工作")
    # else:
    #     flash("学籍处于非正常状态，请确认后再次申请")

    if userxh and userxh.xm == name:
        if userxh.status == 'tuixue' or userxh.status == 'xiuxue' or userxh.status == 'baoliuxueji':
            res = '学生学籍处于非正常状态，无法申请'
            return json.dumps(res.encode('utf-8').decode('utf8'))
        else:
            student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, admin_id=userxh.admin_id, bj=userxh.bj,
                                    zt='xueji', reason=reason, identity=identity, leng_school=leng_school, zy=userxh.lqzy,
                                    sex=userxh.xb)
            # student.status = '学籍证明'
            db.session.add(student_info)
            db.session.commit()
            res = '提交成功'
            return json.dumps(res.encode('utf-8').decode('utf8'))

    else:
        res = '账号或密码不对，请重新输入'
        return json.dumps(res.encode('utf-8').decode('utf8'))
