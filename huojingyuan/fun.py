import xlrd
import pymysql
import os
import uuid


def excel(excel):
    excel = xlrd.open_workbook(excel)
    sheet = excel.sheet_by_name("sheet")
    department = {
        '动物科技学院': 7,
        '动物医学院': 13,
        '工商管理学院': 15,
        '食品与生物工程学院': 16,
        '会计学院': 9,
        '金融学院': 6,
        '制药工程学院': 12,
        '包装与印刷工程学院': 17,
        '农林经济管理学院': 18,
        '物流与电商学院': 19,
        '工程管理学院': 11,
        '智能制造与自动化学院': 3,
        '艺术学院': 10,
        '能源与动力工程学院': 8,
        '软件学院': 20,
        '经济贸易学院': 21,
        '信息工程学院': 22,
        '文法学院': 5,
        '旅游学院': 23,
        '外国语学院': 14,
        '国际教育学院': 4
    }
    #自己修改
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='huojingyuan',
        port=3306,
        charset='utf8'
    )

    cur = conn.cursor()
    query = 'insert into note (xh,xm,xy,bj,admin_id) values (%s, %s, %s, %s, %s)'
    for r in range(sheet.nrows):
        xh = sheet.cell(r, 0).value
        xm = sheet.cell(r, 1).value
        xy = sheet.cell(r, 2).value
        bj = sheet.cell(r, 3).value
        admin_id = department[sheet.cell(r, 2).value]
        values = (xh, xm, xy, bj, admin_id)
        cur.execute(query, values)

    cur.close()
    conn.commit()
    conn.close()


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


