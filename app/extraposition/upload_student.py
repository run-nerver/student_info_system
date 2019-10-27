import xlrd, pymysql, os, uuid, datetime


def excel(excel):
    excel = xlrd.open_workbook(excel)
    sheet = excel.sheet_by_name("Sheet1")
    department = {
        '动物科技学院': 2,
        '动物医药学院': 3,
        '食品与生物工程学院（酒业学院）': 4,
        '工商管理学院': 5,
        '金融与会计学院': 6,
        '包装与印刷工程学院': 7,
        '经济与贸易学院': 8,
        '物流与电商学院': 9,
        '能源与智能工程学院': 10,
        '信息工程学院（软件学院）': 11,
        '文法学院': 12,
        '艺术学院（公共艺术教学部）': 13,
        '旅游学院': 14,
        '外国语学院': 15,
        '马克思主义学院': 16,
        '理学部': 17,
        '体育部': 18,
        '国际教育学院': 19,
        '继续教育学院': 20,
        '艺术学院': 21
    }
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='Qwer123456',
        db='xueji',
        port=3306,
        charset='utf8'
    )

    cur = conn.cursor()
    query = 'insert into note(xh, bj, cc, xy,xq, xm, nj, xb, mz, lqzy, ksh, rxrq, byrq, admin_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    for r in range(sheet.nrows):
        xh = sheet.cell(r, 0).value
        bj = sheet.cell(r, 1).value
        cc = sheet.cell(r, 2).value

        xy = sheet.cell(r, 3).value
        xq = sheet.cell(r, 4).value
        xm = sheet.cell(r, 5).value
        nj = sheet.cell(r, 11).value
        xb = sheet.cell(r, 6).value
        mz = sheet.cell(r, 7).value
        lqzy = sheet.cell(r, 8).value
        ksh = sheet.cell(r, 9).value
        rxrq = sheet.cell(r, 10).value
        rx_date_s = rxrq[0:4] + '-' + rxrq[5:7] + '-' + rxrq[8:]
        if cc in ['本科', '普通本科', '合作办学本科', '艺术本科']:
            byrq_s = str(int(rxrq[0:4]) + 4) + '-07-01'
            byrq = datetime.datetime.strptime(byrq_s, '%Y-%m-%d').date()
        if cc in ['合作办学专科', '普通专科', '艺术专科', '专科']:
            byrq_s = str(int(rxrq[0:4]) + 3) + '-07-01'
            byrq = datetime.datetime.strptime(byrq_s, '%Y-%m-%d').date()
        if cc in ['软件学院专科', '专升本']:
            byrq_s = str(int(rxrq[0:4]) + 2) + '-07-01'
            byrq = datetime.datetime.strptime(byrq_s, '%Y-%m-%d').date()

        rxrq = datetime.datetime.strptime(rx_date_s, '%Y-%m-%d').date()
        admin_id = department[sheet.cell(r, 3).value]
        print(sheet.cell(r, 3).value, rxrq, byrq, nj)
        values = (xh, bj, cc, xy, xq, xm, nj, xb, mz, lqzy, ksh, rxrq, byrq, admin_id)
        cur.execute(query, values)

    cur.close()
    conn.commit()
    conn.close()


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename
