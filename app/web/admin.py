import os

from app import limiter, db, csrf
from app.extraposition.upload_student import random_filename, excel
from app.models.pro import Note_yet, Note, Admin
from app.forms.Administrator import EditForm, DeleteForm, QueryForm, UploadForm
from app.forms.Admin_edit import ZXXJ_EDIT, ZXSXJ_EDIT, ZZY_EDIT, XLZM_EDIT, FX_EDIT, BLXJS_EDIT, XX_EDIT, TXL_EDIT

from datetime import date, datetime
from flask_login import login_required, current_user
from flask import Blueprint, flash, render_template, request, redirect, url_for, abort, jsonify

admin_edit = Blueprint("admin_edit", __name__)


# 教师删除对应的学生信息
@admin_edit.route('/delete/<int:name_id>', methods=['POST'])
@csrf.exempt
@limiter.exempt
@login_required
def delete_stu(name_id):
    if request.method == 'POST':
        name = Note_yet.query.get(name_id)
        db.session.delete(name)
        db.session.commit()
        flash(name.xm + '已经删除')
    else:
        abort(400)
    return redirect(request.referrer)


# 教师确定
@admin_edit.route('/confirm_tx/<int:name_id>')
@limiter.exempt
@login_required
def confirm_tx(name_id):
    # 获取退学、休学申请学生name，将其在Note表和Note_yet表status设置为退学或休学状态
    name = Note_yet.query.get(name_id)
    # 获取Note表中对应name的学生
    student = Note.query.filter_by(xh=name.xh).first()
    if name.zt == 'tuixue' or name.zt == 'xiuxue' or name.zt == 'zhuxiao':
        student.status = name.zt
        name.status = name.zt
        db.session.commit()
    elif name.zt == 'fuxue':
        student.status = ''
        name.status = ''
        db.session.commit()
    return redirect(request.referrer or url_for('new_all'))


# 管理员上传数据
@admin_edit.route('/upload', methods=['GET', 'POST'])
@limiter.exempt
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.file.data
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, '../static/uploads', random_filename(f.filename))
        f.save(upload_path)
        a = os.path.join(upload_path)
        excel(a)
        return '上传成功'
    return render_template('Admin_edit/upload.html', form=form)


@admin_edit.route("/query_json", methods=['GET', 'POST'])
@limiter.exempt
@login_required
def query_json():
    if request.method == 'POST':
        dati = request.form
        starttime = dati['datetimestart']
        endtime = dati['datetimeend']
        matter = dati['matter']
        name = dati['name']
        department = dati['department']

        page = int(dati['page'])
        per_page = int(dati['limit'])

        if current_user.xy == 'admin':
            if starttime == '' and name == '' and endtime == '' and matter == 'info' and (
                    department == 'admin' or department is None):
                data = Note_yet.query
                num = data.count()
                item = data.paginate(page=page, per_page=per_page).items
                return jsonify(data=[i.to_json() for i in item],
                               count=num,
                               msg='',
                               code=0)
            else:
                data = Note_yet.query
                if name != '':
                    data = data.filter(Note_yet.xm.like('%' + name + '%'))
                if starttime != '' and endtime == '':
                    data = data.filter(Note_yet.created_date == starttime)
                elif starttime != '' and endtime != '':
                    data = data.filter(Note_yet.created_date.between(starttime, endtime))
                if matter != 'info':
                    data = data.filter(Note_yet.zt == matter)
                if department != 'admin':
                    admin_id = Admin.query.filter_by(xy=department).first()
                    data = data.filter(Note_yet.admin_id == admin_id.id)
                else:
                    pass
                num = data.count()
                item = data.paginate(page=page, per_page=per_page).items
                return jsonify(data=[i.to_json() for i in item],
                               count=num,
                               msg='',
                               code=0)
        else:
            if starttime == '' and name == '' and endtime == '' and matter == 'info' and (
                    department == 'admin' or department is None):
                data = Note_yet.query
                num = data.count()
                item = data.paginate(page=page, per_page=per_page).items
                return jsonify(data=[i.to_json() for i in item],
                               count=num,
                               msg='',
                               code=0)
            else:
                data = Note_yet.query.filter(Note_yet.admin_id == current_user.id)
                if name != '':
                    data = data.filter(Note_yet.xm.like('%' + name + '%'))
                if starttime != '' and endtime == '':
                    data = data.filter(Note_yet.created_date == starttime)
                elif starttime != '' and endtime != '':
                    data = data.filter(Note_yet.created_date.between(starttime, endtime))
                if matter != 'info':
                    data = data.filter(Note_yet.zt == matter)
                else:
                    pass
                num = data.count()
                item = data.paginate(page=page, per_page=per_page).items
                return jsonify(data=[i.to_json() for i in item],
                               count=num,
                               msg='',
                               code=0)


# 查看所有
@admin_edit.route("/all", methods=['GET', 'POST'])
@limiter.exempt
@login_required
def new_all():
    today = date.today()
    form = QueryForm()
    delete_form = DeleteForm()
    return render_template('Admin_edit/index.html', form=form, delete_form=delete_form, today=today)


@admin_edit.route('/select_xy', methods=["POST"])
@limiter.exempt
def select_xq():
    if request.method == 'POST':
        if request.json['XQ'] == '':
            pass
        else:
            xy = Note.query.filter(Note.xq == request.json['XQ']).with_entities(Note.xy).distinct().all()
            return jsonify(
                xy
            )


@admin_edit.route('/select_zy', methods=["POST"])
@limiter.exempt
def select_zy():
    if request.method == 'POST':
        all = request.json
        xq = all['XQ']
        xy = all['XY']
        zy = Note.query.filter(Note.xq == xq, Note.xy == xy).with_entities(Note.lqzy).distinct().all()
        return jsonify(
            zy
        )


@admin_edit.route('/select_bj', methods=["POST"])
@limiter.exempt
def select_bj():
    if request.method == 'POST':
        all = request.json
        xq = all['XQ']
        xy = all['XY']
        zy = all['ZY']
        zy = Note.query.filter(Note.xq == xq, Note.xy == xy, Note.lqzy == zy).with_entities(Note.bj).distinct().all()
        return jsonify(
            zy
        )


@admin_edit.route("/update", methods=['GET'])
@limiter.exempt
def update():
    alld = Note.query.all()
    for i in alld:
        j = str(i.xh)[0:2]
        i.nj = j
        print(j, i.nj)
    db.session.commit()
    return 'ok'


@admin_edit.route("/edit_new/<ZT>/<int:name_id>", methods=['GET', 'POST'])
@limiter.exempt
def edit_new(ZT, name_id):
    forms = request.form
    FX_FORM = FX_EDIT()
    ZZY_FORM = ZZY_EDIT()
    XX_FORM = XX_EDIT()
    TXL_FORM = TXL_EDIT()
    ZXXJ_FORM = ZXXJ_EDIT()
    BLXJS_FORM = BLXJS_EDIT()
    XLZM_FORM = XLZM_EDIT()
    ZXSXJ_FORM = ZXSXJ_EDIT()

    name = Note_yet.query.get(name_id)
    student = Note.query.filter_by(xh=name.xh).first()
    student_admin_id = Admin.query.filter_by(xy=ZZY_FORM.campus.data).first()

    if ZT == 'zhuanzhuanye':
        if ZZY_FORM.validate_on_submit():
            name.xy = ZZY_FORM.xy.data
            name.bj = ZZY_FORM.bj.data
            # name.xy = ZZY_FORM.campus.data
            # name.bj = ZZY_FORM.classgrade.data
            name.dom_dorm = ZZY_FORM.dom_dorm.data
            name.school = ZZY_FORM.school.data
            name.campus = ZZY_FORM.campus.data
            name.discipline = ZZY_FORM.discipline.data
            name.classgrade = ZZY_FORM.classgrade.data
            name.dorm = ZZY_FORM.dorm.data
            name.reason = ZZY_FORM.reason.data
            name.admin_id = student_admin_id.id
            student.xq = ZZY_FORM.school.data
            student.xy = ZZY_FORM.campus.data
            student.lqzy = ZZY_FORM.discipline.data
            student.bj = ZZY_FORM.classgrade.data
            student.admin_id = student_admin_id.id
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        ZZY_FORM.xm.data = name.xm
        ZZY_FORM.xh.data = name.xh
        ZZY_FORM.sex.data = name.sex
        ZZY_FORM.xy.data = name.xy
        ZZY_FORM.bj.data = name.bj
        ZZY_FORM.dom_dorm.data = name.dom_dorm
        ZZY_FORM.dorm.data = name.dorm
        ZZY_FORM.school.data = name.school
        ZZY_FORM.campus.data = name.campus
        ZZY_FORM.classgrade.data = name.classgrade
        ZZY_FORM.reason.data = name.reason
    if ZT == 'zhuxiao':
        if ZXXJ_FORM.validate_on_submit():
            name.xy = ZXXJ_FORM.xy.data
            name.bj = ZXXJ_FORM.bj.data
            name.reason = ZXXJ_FORM.reason.data
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        ZXXJ_FORM.xm.data = name.xm
        ZXXJ_FORM.xh.data = name.xh
        ZXXJ_FORM.sex.data = name.sex
        ZXXJ_FORM.xy.data = name.xy
        ZXXJ_FORM.bj.data = name.bj
        ZXXJ_FORM.reason.data = name.reason
    if ZT == 'fuxue':
        if FX_FORM.validate_on_submit():
            name.xy = FX_FORM.xy.data
            name.bj = FX_FORM.bj.data
            name.school = FX_FORM.school.data
            name.campus = FX_FORM.campus.data
            name.discipline = FX_FORM.discipline.data
            name.classgrade = FX_FORM.classgrade.data
            name.reason = FX_FORM.reason.data
            student.xq = ZZY_FORM.school.data
            student.xy = ZZY_FORM.campus.data
            student.lqzy = ZZY_FORM.discipline.data
            student.bj = ZZY_FORM.classgrade.data
            student.admin_id = student_admin_id.id
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        FX_FORM.xm.data = name.xm
        FX_FORM.xh.data = name.xh
        FX_FORM.sex.data = name.sex
        FX_FORM.xy.data = name.xy
        FX_FORM.bj.data = name.bj
        FX_FORM.campus.data = name.campus
        FX_FORM.discipline.data = name.discipline
        FX_FORM.classgrade.data = name.classgrade
        FX_FORM.reason.data = name.reason
    if ZT == 'xiuxue':
        if XX_FORM.validate_on_submit():
            name.xy = XX_FORM.xy.data
            name.bj = XX_FORM.bj.data
            name.per_tel = XX_FORM.per_tel.data
            name.home_tel = XX_FORM.home_tel.data
            name.home_address = XX_FORM.home_address.data
            name.reason = XX_FORM.reason.data
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        XX_FORM.xm.data = name.xm
        XX_FORM.xh.data = name.xh
        XX_FORM.sex.data = name.sex
        XX_FORM.xy.data = name.xy
        XX_FORM.bj.data = name.bj
        XX_FORM.per_tel.data = name.per_tel
        XX_FORM.home_tel.data = name.home_tel
        XX_FORM.home_address.data = name.home_address
        XX_FORM.reason.data = name.reason
    if ZT == 'tuixue':
        if TXL_FORM.validate_on_submit():
            name.xy = FX_FORM.xy.data
            name.bj = FX_FORM.bj.data
            name.per_tel = FX_FORM.per_tel.data
            name.home_tel = FX_FORM.home_tel.data
            name.home_address = FX_FORM.home_address.data
            name.reason = FX_FORM.reason.data
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        TXL_FORM.xm.data = name.xm
        TXL_FORM.xh.data = name.xh
        TXL_FORM.sex.data = name.sex
        TXL_FORM.xy.data = name.xy
        TXL_FORM.bj.data = name.bj
        TXL_FORM.per_tel.data = name.per_tel
        TXL_FORM.home_tel.data = name.home_tel
        TXL_FORM.home_address.data = name.home_address
        TXL_FORM.reason.data = name.reason
    if ZT == 'zhuxiao':
        if ZXXJ_FORM.validate_on_submit():
            name.xy = ZXXJ_FORM.xy.data
            name.bj = ZXXJ_FORM.bj.data
            name.reason = ZXXJ_FORM.reason.data
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        ZXXJ_FORM.xm.data = name.xm
        ZXXJ_FORM.xh.data = name.xh
        ZXXJ_FORM.sex.data = name.sex
        ZXXJ_FORM.xy.data = name.xy
        ZXXJ_FORM.bj.data = name.bj
        ZXXJ_FORM.reason.data = name.reason
    if ZT == 'baoliuxueji':
        if BLXJS_FORM.validate_on_submit():
            name.per_tel = BLXJS_FORM.per_tel.data
            name.home_tel = BLXJS_FORM.home_tel.data
            name.home_address = BLXJS_FORM.home_address.data
            name.school_endtime = BLXJS_FORM.school_endtime.data
            name.reason = BLXJS_FORM.reason.data
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        BLXJS_FORM.xm.data = name.xm
        BLXJS_FORM.xh.data = name.xh
        BLXJS_FORM.sex.data = name.sex
        BLXJS_FORM.per_tel.data = name.per_tel
        BLXJS_FORM.home_tel.data = name.home_tel
        BLXJS_FORM.home_address.data = name.home_address
        BLXJS_FORM.bl_date.data = name.bl_date
        BLXJS_FORM.reason.data = name.reason
    if ZT == 'xueli':
        if XLZM_FORM.validate_on_submit():
            name.school = XLZM_FORM.school.data
            name.campus = XLZM_FORM.campus.data
            name.discipline = XLZM_FORM.discipline.data
            name.leng_school = XLZM_FORM.leng_school.data
            name.school_sttime = XLZM_FORM.school_sttime.data
            name.school_endtime = XLZM_FORM.school_endtime.data
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        XLZM_FORM.xm.data = name.xm
        XLZM_FORM.xh.data = name.xh
        XLZM_FORM.sex.data = name.sex
        XLZM_FORM.school.data = name.school
        XLZM_FORM.campus.data = name.campus
        XLZM_FORM.discipline.data = name.discipline
        XLZM_FORM.leng_school.data = name.leng_school
        XLZM_FORM.school_sttime.data = name.school_sttime
        XLZM_FORM.school_endtime.data = name.school_endtime
        XLZM_FORM.reason.data = name.reason
        XLZM_FORM.code.data = name.code
    if ZT == 'xueji':
        if ZXSXJ_FORM.validate_on_submit():
            name.leng_school = ZXSXJ_FORM.leng_school.data
            name.identity = ZXSXJ_FORM.identity.data
            name.xy = ZXSXJ_FORM.xy.data
            name.bj = ZXSXJ_FORM.bj.data
            name.reason = ZXSXJ_FORM.reason.data
            db.session.commit()
            flash('修改成功')
            return redirect(url_for('admin_edit.new_all'))
        ZXSXJ_FORM.xm.data = name.xm
        ZXSXJ_FORM.xh.data = name.xh
        ZXSXJ_FORM.sex.data = name.sex
        ZXSXJ_FORM.identity.data = name.identity
        ZXSXJ_FORM.leng_school.data = name.leng_school
        ZXSXJ_FORM.xy.data = name.xy
        ZXSXJ_FORM.bj.data = name.bj
        ZXSXJ_FORM.reason.data = name.reason
    return render_template('Admin_edit/edit_student.html', FX_FORM=FX_FORM,
                           ZZY_FORM=ZZY_FORM, XX_FORM=XX_FORM, TXL_FORM=TXL_FORM,
                           ZXXJ_FORM=ZXXJ_FORM, BLXJS_FORM=BLXJS_FORM,
                           XLZM_FORM=XLZM_FORM, ZXSXJ_FORM=ZXSXJ_FORM, name=name)
