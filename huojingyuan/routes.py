from huojingyuan import app, login_manager, limiter,csrf
from flask import render_template, redirect, flash, url_for, request, current_app, abort, jsonify, render_template_string
from huojingyuan.forms import LoginForm, QueryForm, DeleteForm, EditForm, UploadForm, EditTeacher, FX, ZZY, XX, TXL, XLZM, BLXJS, ZXXJ, ZXSXJ
from huojingyuan.models import Note, Note_yet, db, Admin
from flask_login import login_user, current_user, login_required, logout_user
from datetime import date
from huojingyuan.fun import excel, random_filename
import os,click, string, json, uuid



@app.route('/xueli/<int:name_id>')
@limiter.exempt
@login_required
def xueli(name_id):
    today = date.today()
    format_today = today.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
    name = Note_yet.query.get(name_id)
    return render_template('xueli.html', name=name,format_today=format_today)


# 2学籍证明
@app.route('/xueji/<int:name_id>')
@limiter.exempt
@login_required
def xueji(name_id):
    today = date.today()
    format_today = today.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
    name = Note_yet.query.get(name_id)
    return render_template('xueji.html', name=name, format_today=format_today)


# 3注销学籍
@app.route('/zhuxiaoxueji/<int:name_id>')
@limiter.exempt
@login_required
def zhuxiaoxueji(name_id):
    name = Note_yet.query.get(name_id)
    return render_template('zhuxiaoxueji2.html', name=name)


# 4保留学籍离校清单
@app.route('/xuejilixiaoqingdan/<int:name_id>')
@limiter.exempt
@login_required
def xuejilixiaoqingdan(name_id):
    name = Note_yet.query.get(name_id)
    # name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    name_zy = name.bj.strip(string.digits)  # 去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('xuejilixiaoqingdan.html', name=name, name_zy=name_zy, format_today=format_today)


# 5保留学籍申请表
@app.route('/xuejishenqingbiao/<int:name_id>')
@limiter.exempt
@login_required
def xuejishenqingbiao(name_id):
    name = Note_yet.query.get(name_id)
    # name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    name_zy = name.bj.strip(string.digits)  # 去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('xuejishenqingbiao.html', name=name, name_zy=name_zy, format_today=format_today)


# 6复学申请
@app.route('/fuxueshenqing/<int:name_id>')
@limiter.exempt
@login_required
def fuxueshenqing(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.strip(string.digits)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('fuxueshenqing.html', name=name, name_zy=name_zy, format_today=format_today)


# 7复学入班通知书
@app.route('/fuxueruban/<int:name_id>')
@limiter.exempt
@login_required
def fuxueruban(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('fuxueruban.html', name=name, format_today=format_today)


# 8退学申请
@app.route('/tuixueshenqing/<int:name_id>')
@limiter.exempt
@login_required
def tuixueshenqing(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('tuixueshenqing2.html', name=name, format_today=format_today)


# 9退学离校清单
@app.route('/tuixuelixiaoqingdan/<int:name_id>')
@limiter.exempt
@login_required
def tuixue_lixiaoqingdan(name_id):
    name = Note_yet.query.get(name_id)
    # name_zy = filter(str.isalpha, name.bj)
    # name_zy = filter(lambda x: x.isalpha(), name.bj)
    name_zy = name.bj.strip(string.digits)  # q
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('tuixuelixiaoqingdan.html', name=name, format_today=format_today, name_zy=name_zy)


# 10退学通知书
@app.route('/tuixuetongzhi/<int:name_id>')
@limiter.exempt
@login_required
def tuixue_tongzhi(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    name_zy = name.bj.rstrip(string.digits)
    return render_template('tuixuetongzhi.html', name=name, format_today=format_today, name_zy=name_zy)


# 11休学申请
@app.route('/xiuxueshenqing/<int:name_id>')
@limiter.exempt
@login_required
def xiuxueshenqing(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('xiuxueshenqing.html', name=name, format_today=format_today)


# 12休学离校清单
@app.route('/xiuxuelixiaoqingdan/<int:name_id>')
@limiter.exempt
@login_required
def xiuxuelixiaoqingdan(name_id):
    name = Note_yet.query.get(name_id)
    return render_template('xiuxuelixiaoqingdan.html', name=name)


# 13休学通知书
@app.route('/xiuxuetongzhi/<int:name_id>')
@limiter.exempt
@login_required
def xiuxuetongzhi(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('xiuxuetongzhi.html', name=name, name_zy=name_zy, format_today=format_today)


# 14转专业申请
@app.route('/zhuanyeshenqing/<int:name_id>')
@limiter.exempt
@login_required
def zhuanyeshenqing(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('zhuanyeshenqing.html', name=name, name_zy=name_zy, format_today=format_today)


# 15转专业入班
@app.route('/zhuanyeruban/<int:name_id>')
@limiter.exempt
@login_required
def zhuanyeruban(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('zhuanyeruban.html', name=name, name_zy=name_zy, format_today=format_today)


# 保留学籍通知书 ----------------------------------------------------------
@app.route('/xuejitongzhishu/<int:name_id>')
@limiter.exempt
@login_required
def xuejitongzhishu(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('xuejitongzhishu.html', name=name, name_zy=name_zy, format_today=format_today)

#旷课记录表
@app.route('/kuangkejilubiao/<int:name_id>')
@limiter.exempt
@login_required
def kuangkejilubiao(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('kuangkejilubiao.html', name=name, name_zy=name_zy, format_today=format_today)

#旷课建议表
@app.route('/kuangkejianyibiao/<int:name_id>')
@limiter.exempt
@login_required
def kuangkejianyibiao(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('kuangkejianyibiao.html', name=name, name_zy=name_zy, format_today=format_today)

#旷课处分详情表
@app.route('/kuangkechufenxiangqing/<int:name_id>')
@limiter.exempt
@login_required
def kuangkechufenxiangqing(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('kuangkechufenxiangqing.html', name=name, name_zy=name_zy, format_today=format_today)


@app.errorhandler(404)
@limiter.exempt
def miss(error):
    return render_template('404.html'),404


@app.errorhandler(500)
@limiter.exempt
def type(error):
    return render_template('500.html'),500





@app.route("/logout")
@limiter.exempt
@login_required
def logout():
    logout_user()
    flash("登出成功")
    return redirect("admin_login")



@app.route('/delete/<int:name_id>', methods=['POST'])
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
@app.route('/confirm_tx/<int:name_id>')
@limiter.exempt
@login_required
def confirm_tx(name_id):
    # 获取退学、休学申请学生name，将其在Note表和Note_yet表status设置为退学或休学状态
    name = Note_yet.query.get(name_id)
    # 获取Note表中对应name的学生
    student = Note.query.filter_by(xh=name.xh).first()
    student.status = name.zt
    name.status = name.zt
    db.session.commit()
    return redirect(request.referrer or url_for('new_all'))



@app.route('/edit/<int:name_id>', methods=[ 'GET','POST'])
@limiter.exempt
@login_required
def edit_student(name_id):
    form = EditForm()
    name = Note_yet.query.get(name_id)
    # 获取Note表中对应name的学生
    student = Note.query.filter_by(xh=name.xh).first()
    if request.method == 'POST':
    # if form.validate_on_submit():
        name.xh = form.xh.data
        name.xm = form.xm.data
        name.xy = form.xy.data
        name.bj = form.bj.data
        name.zt = form.zt.data
        # name.created_date = form.created_date.data
        name.reason = form.reason.data
        name.status = form.status.data
        name.campus = form.campus.data                          #所在院系
        name.code = form.code.data                              #证书编号
        name.dom_dorm = form.dom_dorm.data                      #原宿舍号
        name.dom_built = form.dom_built.data                    #宿舍楼
        name.dom_campus = form.dom_campus.data                  #宿舍楼
        name.home_address = form.home_address.data              #家庭住址
        name.home_tel = form.home_tel.data                      #家庭联系方式
        name.identity = form.identity.data                      #身份证号码
        name.per_tel = form.per_tel.data                        #个人联系方式
        name.school = form.school.data                          #所在学校
        name.school_sttime = form.school_sttime.data            #入校时间
        name.school_endtime = form.school_endtime.data          #离校时间
        name.sex = form.sex.data                                #个人性别
        name.discipline = form.discipline.data                  #专业
        name.leng_school = form.leng_school.data                #学制
        # name.created_date = form.created_date.data

        student.xh = form.xh.data
        student.xm = form.xm.data
        student.xy = form.xy.data
        student.bj = form.bj.data
        student.zt = form.zt.data
        student.created_date = form.created_date.data
        student.reason = form.reason.data
        student.status = form.status.data

        db.session.commit()
        flash('修改成功')
        return redirect(url_for('new_all'))



    form.xh.data = name.xh
    form.xm.data = name.xm
    form.xy.data = name.xy
    form.bj.data = name.bj
    form.zt.data = name.zt
    form.reason.data = name.reason
    form.status.data = name.status
    form.school.data = name.school                              # 所在学校
    form.campus.data = name.campus                              # 所在院系
    form.discipline.data = name.discipline                      # 专业
    form.code.data = name.code                                  # 证书编号
    form.dom_dorm.data = name.dom_dorm                          # 原宿舍号
    form.home_address.data = name.home_address                  # 家庭住址
    form.home_tel.data = name.home_tel                          # 家庭联系方式
    form.identity.data = name.identity                          # 身份证号码
    form.per_tel.data = name.per_tel                            # 个人联系方式
    form.school_sttime.data = name.school_sttime                # 入校时间
    form.school_endtime.data = name.school_endtime              # 离校时间
    form.sex.data = name.sex                                    # 个人性别
    form.leng_school.data = name.leng_school                    # 学制
    form.dom_built.data = name.dom_built                        # 原宿舍号
    form.dom_campus.data = name.dom_campus                      # 原宿舍楼号




    return render_template('new-edit.html', form=form,name=name)


# 管理员上传数据
@app.route('/upload', methods=['GET', 'POST'])
@limiter.exempt
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.file.data
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'uploads', random_filename(f.filename))
        f.save(upload_path)
        a = os.path.join(upload_path)
        excel(a)
        return '上传成功'
    return render_template('upload.html', form=form)


@app.route("/admin_login", methods=['GET', 'POST'])
@limiter.exempt
def admin_login():

    form = LoginForm()
    if request.method == 'POST':
        username = form.name.data
        password = form.password.data
        remember = form.remember.data
        user = Admin.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user, remember)
            # flash('登陆成功')
            return redirect(url_for('new_all'))
        flash('账号或密码不正确，请重新输入')
        return redirect(url_for('admin_login'))
    return render_template('admin_login2.html', form=form)



@app.route('/edit_teacher',methods=['GET','POST'])
@limiter.exempt
@login_required
def edit_teacher():
    form = EditTeacher()
    if request.method == 'POST':
        o_password = form.old_password.data
        n_password = form.new_password.data
        r_password = form.repeat_password.data
        user = Admin.query.filter_by(username=current_user.username).first()
        if user.password == o_password:
            if n_password == r_password:
                user.password = r_password
                db.session.commit()
                flash('密码修改成功')
                flash('请使用新密码登录')
                return redirect(url_for('logout'))
            else:
                flash('两次密码不一致，请重新修改')
                return redirect(url_for('edit_teacher'))
        else:
            flash('原密码错误')
            return redirect(url_for('edit_teacher'))
    return render_template('edit_teacher.html', form=form)



@app.route("/query_json", methods=['GET','POST'])
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
                item = data.paginate(page=page,per_page=per_page).items
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
                    data = data.filter(Note_yet.xy == department)
                else:
                    pass
                num = data.count()
                item = data.paginate(page=page,per_page=per_page).items
                return jsonify(data=[i.to_json()for i in item],
                               count = num,
                               msg= '',
                               code= 0)
        else:
            if starttime == '' and name == '' and endtime == '' and matter == 'info' and (
                    department == 'admin' or department is None):
                data = Note_yet.query
                num = data.count()
                item = data.paginate(page=page,per_page=per_page).items
                return jsonify(data=[i.to_json() for i in item],
                               count=num,
                               msg='',
                               code=0)
            else:
                data = Note_yet.query.filter(Note_yet.xy == current_user.xy)
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


@app.route("/front", methods=['GET', 'POST'])
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

    today = date.today()

    if FX_FORM.Submit_FX.data and FX_FORM.validate():
        name = FX_FORM.name.data
        stu_num = FX_FORM.stu_num.data
        matter = '复学'
        reason = FX_FORM.reason.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='复学',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))

    if ZZY_FORM.Submit_ZZU.data and ZZY_FORM.validate():
        name = ZZY_FORM.name.data
        stu_num = ZZY_FORM.stu_num.data
        campus = ZZY_FORM.campus.data
        reason = ZZY_FORM.reason.data
        dom_dorm = ZZY_FORM.dom_dorm.data
        discipline = ZZY_FORM.discipline.data
        matter='转专业'
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='转专业',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        discipline=discipline if discipline is not None else '',
                                        campus=campus if campus is not None else '',
                                        dom_dorm=dom_dorm if dom_dorm is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))

    if XX_FORM.Submit_XX.data and XX_FORM.validate():
        name = XX_FORM.name.data
        stu_num = XX_FORM.stu_num.data
        matter = '休学'
        reason = XX_FORM.reason.data
        per_tel = XX_FORM.per_tel.data
        home_address = XX_FORM.home_address.data
        home_tel = XX_FORM.home_tel.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='休学',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        home_address=home_address if home_address is not None else '',
                                        home_tel=home_tel if home_tel is not None else '',
                                        per_tel=per_tel if per_tel is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))
    if TXL_FORM.Submit_TXL.data and TXL_FORM.validate():
        name = TXL_FORM.name.data
        stu_num = TXL_FORM.stu_num.data
        matter = '退学'
        reason = TXL_FORM.reason.data
        per_tel = TXL_FORM.per_tel.data
        home_address = TXL_FORM.home_address.data
        home_tel = TXL_FORM.home_tel.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='退学',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        home_address=home_address if home_address is not None else '',
                                        home_tel=home_tel if home_tel is not None else '',
                                        per_tel=per_tel if per_tel is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))
    if XLZM_FORM.Submit_XLZM.data and XLZM_FORM.validate():
        name = XLZM_FORM.name.data
        stu_num = XLZM_FORM.stu_num.data
        matter = '学历'
        reason = XLZM_FORM.reason.data
        school_sttime = XLZM_FORM.school_sttime.data
        school_endtime = XLZM_FORM.school_endtime.data
        school = XLZM_FORM.school.data
        campus = XLZM_FORM.campus.data
        discipline = XLZM_FORM.discipline.data
        code = XLZM_FORM.code.data
        leng_school = XLZM_FORM.leng_school.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='学历',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        school_sttime=school_sttime if school_sttime is not None else '',
                                        school_endtime=school_endtime if school_endtime is not None else today,
                                        school=school if school is not None else '',
                                        campus=campus if campus is not None else '',
                                        code=code if code is not None else '',
                                        leng_school=leng_school if leng_school is not None else '',
                                        discipline=discipline if discipline is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))
    if BLXJS_FORM.Submit_BLXJS.data and BLXJS_FORM.validate():
        name = BLXJS_FORM.name.data
        stu_num = BLXJS_FORM.stu_num.data
        matter = '保留学籍'
        reason = BLXJS_FORM.reason.data

        school_endtime = BLXJS_FORM.school_endtime.data
        per_tel = BLXJS_FORM.per_tel.data
        home_address = BLXJS_FORM.home_address.data
        home_tel = BLXJS_FORM.home_tel.data

        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='保留学籍',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        school_endtime=school_endtime if school_endtime is not None else today,
                                        home_address=home_address if home_address is not None else '',
                                        home_tel=home_tel if home_tel is not None else '',
                                        per_tel=per_tel if per_tel is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))
    if ZXXJ_FORM.Submit_ZXXJ.data and ZXXJ_FORM.validate():
        name = ZXXJ_FORM.name.data
        stu_num = ZXXJ_FORM.stu_num.data
        matter = '注销'
        reason = ZXXJ_FORM.reason.data

        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='注销',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))
    if ZXSXJ_FORM.Submit_ZXSXJ.data and ZXSXJ_FORM.validate():
        name = ZXSXJ_FORM.name.data
        stu_num = ZXSXJ_FORM.stu_num.data
        matter = '学籍'
        reason = ZXSXJ_FORM.reason.data
        identity = ZXSXJ_FORM.identity.data
        leng_school = ZXSXJ_FORM.leng_school.data
        userxh = Note.query.filter_by(xh=stu_num).first()  # 调取学号进行查阅数据库
        student = Note.query.filter_by(xm=name).first()
        # if Note.query.filter(name.in_(Note.xm)):
        if userxh and userxh.xm == name:  # 有业务逻辑错误
            if (student.status == '退学' or student.status == '休学') and matter == '学籍':
                return '处于休学或退学状态，无法申请在校生学籍'
            else:
                student_info = Note_yet(xh=userxh.xh, xm=userxh.xm, xy=userxh.xy, bj=userxh.bj, zt='学籍',
                                        admin_id=userxh.admin_id, reason=reason if reason is not None else '',
                                        identity=identity if identity is not None else '',
                                        leng_school=leng_school if leng_school is not None else '')
                db.session.add(student_info)
                db.session.commit()
                # flash("成功申请，请找老师打印")
                flash("提交成功，请通知老师在系统进行下一步工作")
            return redirect(url_for('front'))

        else:
            flash("账号或学号不正确，请重新输入")
            return redirect(url_for('front'))
    return render_template('front.html', FX_FORM=FX_FORM, ZZY_FORM = ZZY_FORM, XX_FORM = XX_FORM, TXL_FORM = TXL_FORM,
                           XLZM_FORM = XLZM_FORM, BLXJS_FORM = BLXJS_FORM, ZXXJ_FORM = ZXXJ_FORM, ZXSXJ_FORM = ZXSXJ_FORM)


#查看所有
@app.route("/all", methods=['GET','POST'])
@limiter.exempt
@login_required
def new_all():
    today = date.today()
    form = QueryForm()
    delete_form = DeleteForm()
    return render_template('new_layui_index.html', form=form, delete_form=delete_form, today=today)


@app.cli.command()
@app.cli.command()
def initdb():
    db.create_all()
    click.echo('initdb')