from app import limiter, db
from app.models.pro import Admin
from app.forms.Administrator import LoginForm,  EditTeacher

from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user, logout_user ,login_required, current_user



admin_login = Blueprint('admin_login', __name__, static_folder="")


@admin_login.route("/logout")
@limiter.exempt
@login_required
def logout():
    logout_user()
    flash("登出成功")
    return redirect(url_for("admin_login.login"))


@admin_login.route("/login", methods=['GET', 'POST'])
@limiter.limit("50 per day")
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = form.name.data
        password = form.password.data
        remember = form.remember.data
        user = Admin.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user, remember)
            # flash('登陆成功')
            return redirect(url_for('admin_edit.new_all'))
        flash('账号或密码不正确，请重新输入')
        return redirect(url_for('admin_login.login'))
    return render_template('Admin/login.html', form=form)


@admin_login.route('/edit_teacher',methods=['GET','POST'])
@limiter.exempt
@login_required
def teacher_change_password():
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
                return redirect(url_for('admin_login.logout'))
            else:
                flash('两次密码不一致，请重新修改')
                return redirect(url_for('admin_login.teacher_change_password'))
        else:
            flash('原密码错误')
            return redirect(url_for('admin_login.teacher_change_password'))
    return render_template('Admin/change_password.html', form=form)