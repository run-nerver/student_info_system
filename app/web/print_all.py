import string

from app import limiter
from app.models.pro import Note_yet

from datetime import date
from flask import Blueprint, render_template
from flask_login import login_required

print_all = Blueprint('print_all', __name__)


@print_all.route('/xueli/<int:name_id>')
@limiter.exempt
@login_required
def xueli(name_id):
    today = date.today()
    format_today = today.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
    name = Note_yet.query.get(name_id)
    start_time = str(name.school_sttime)
    end_time = str(name.school_endtime)
    return render_template('print_all/xueli.html', name=name, format_today=format_today, start_time=start_time,
                           end_time=end_time)


# 2学籍证明
@print_all.route('/xueji/<int:name_id>')
@limiter.exempt
@login_required
def xueji(name_id):
    today = date.today()
    format_today = today.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
    name = Note_yet.query.get(name_id)
    return render_template('print_all/xueji.html', name=name, format_today=format_today)


# 3注销学籍
@print_all.route('/zhuxiaoxueji/<int:name_id>')
@limiter.exempt
@login_required
def zhuxiaoxueji(name_id):
    name = Note_yet.query.get(name_id)
    return render_template('print_all/zhuxiaoxueji.html', name=name)


# 4保留学籍离校清单
@print_all.route('/xuejilixiaoqingdan/<int:name_id>')
@limiter.exempt
@login_required
def xuejilixiaoqingdan(name_id):
    name = Note_yet.query.get(name_id)
    # name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    name_zy = name.bj.strip(string.digits)  # 去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/xuejilixiaoqingdan.html', name=name, name_zy=name_zy, format_today=format_today)


# 5保留学籍申请表
@print_all.route('/xuejishenqingbiao/<int:name_id>')
@limiter.exempt
@login_required
def xuejishenqingbiao(name_id):
    name = Note_yet.query.get(name_id)
    # name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    name_zy = name.bj.strip(string.digits)  # 去除两边数字
    #today = date.today()
    #format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    created_date = name.created_date.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    start_time = str(name.school_sttime)
    end_time = str(name.school_endtime)
    return render_template('print_all/xuejishenqingbiao.html', name=name, name_zy=name_zy, created_date=created_date, start_time=start_time, end_time=end_time)


# 6复学申请
@print_all.route('/fuxueshenqing/<int:name_id>')
@limiter.exempt
@login_required
def fuxueshenqing(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.strip(string.digits)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/fuxueshenqing.html', name=name, name_zy=name_zy, format_today=format_today)


# 7复学入班通知书
@print_all.route('/fuxueruban/<int:name_id>')
@limiter.exempt
@login_required
def fuxueruban(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/fuxueruban.html', name=name, format_today=format_today)


# 8退学申请
@print_all.route('/tuixueshenqing/<int:name_id>')
@limiter.exempt
@login_required
def tuixueshenqing(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/tuixueshenqing.html', name=name, format_today=format_today)


# 9退学离校清单
@print_all.route('/tuixuelixiaoqingdan/<int:name_id>')
@limiter.exempt
@login_required
def tuixue_lixiaoqingdan(name_id):
    name = Note_yet.query.get(name_id)
    # name_zy = filter(str.isalpha, name.bj)
    # name_zy = filter(lambda x: x.isalpha(), name.bj)
    name_zy = name.bj.strip(string.digits)  # q
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/tuixuelixiaoqingdan.html', name=name, format_today=format_today, name_zy=name_zy)


# 10退学通知书
@print_all.route('/tuixuetongzhi/<int:name_id>')
@limiter.exempt
@login_required
def tuixue_tongzhi(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    name_zy = name.bj.rstrip(string.digits)
    return render_template('print_all/tuixuetongzhi.html', name=name, format_today=format_today, name_zy=name_zy)


# 11休学申请
@print_all.route('/xiuxueshenqing/<int:name_id>')
@limiter.exempt
@login_required
def xiuxueshenqing(name_id):
    name = Note_yet.query.get(name_id)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/xiuxueshenqing.html', name=name, format_today=format_today)


# 12休学离校清单
@print_all.route('/xiuxuelixiaoqingdan/<int:name_id>')
@limiter.exempt
@login_required
def xiuxuelixiaoqingdan(name_id):
    name = Note_yet.query.get(name_id)
    return render_template('print_all/xiuxuelixiaoqingdan.html', name=name)


# 13休学通知书
@print_all.route('/xiuxuetongzhi/<int:name_id>')
@limiter.exempt
@login_required
def xiuxuetongzhi(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/xiuxuetongzhi.html', name=name, name_zy=name_zy, format_today=format_today)


# 14转专业申请
@print_all.route('/zhuanyeshenqing/<int:name_id>')
@limiter.exempt
@login_required
def zhuanyeshenqing(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/zhuanyeshenqing.html', name=name, name_zy=name_zy, format_today=format_today)


# 15转专业入班
@print_all.route('/zhuanyeruban/<int:name_id>')
@limiter.exempt
@login_required
def zhuanyeruban(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/zhuanyeruban.html', name=name, name_zy=name_zy, format_today=format_today)


# 保留学籍通知书 ----------------------------------------------------------
@print_all.route('/xuejitongzhishu/<int:name_id>')
@limiter.exempt
@login_required
def xuejitongzhishu(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    start_time = str(name.school_sttime)
    end_time = str(name.school_endtime)
    return render_template('print_all/xuejitongzhishu.html', name=name, name_zy=name_zy, format_today=format_today,
                           end_time=end_time, start_time=start_time)


# 旷课记录表
@print_all.route('/kuangkejilubiao/<int:name_id>')
@limiter.exempt
@login_required
def kuangkejilubiao(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/kuangkejilubiao.html', name=name, name_zy=name_zy, format_today=format_today)


# 旷课建议表
@print_all.route('/kuangkejianyibiao/<int:name_id>')
@limiter.exempt
@login_required
def kuangkejianyibiao(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/kuangkejianyibiao.html', name=name, name_zy=name_zy, format_today=format_today)


# 旷课处分详情表
@print_all.route('/kuangkechufenxiangqing/<int:name_id>')
@limiter.exempt
@login_required
def kuangkechufenxiangqing(name_id):
    name = Note_yet.query.get(name_id)
    name_zy = name.bj.rstrip(string.digits)  # 去除最右边数字
    # name_zy = name.bj.strip(string.digits)  #去除两边数字
    today = date.today()
    format_today = today.strftime(' %Y{y} %m{m} %d{d}').format(y='年 ', m='月', d='日')
    return render_template('print_all/kuangkechufenxiangqing.html', name=name, name_zy=name_zy,
                           format_today=format_today)
