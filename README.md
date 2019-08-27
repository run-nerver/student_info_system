# 学生信息打印辅助系统

## 2019.8.26增加测试地址：  
前台业务: http://139.9.7.123:8000/front    
前台业务测试数据：（在对应业务输入学号+姓名，其他随便写即可）
10001	王三
10002	李四
10003	赵五
10004	秦六
10005	李七
10006	孟八
10007	李九
10008	郭十
10009	张十一
10010	张十二
10011	刘十三
10012	李十四
10013	刘十五
10014	汪十六
10015	庞十七
10016	黄十八
10017	刘十九
10018	孙二十
10019	刘二十一  
后台管理：http://139.9.7.123:8000/admin_login  
测试账号：账号test 密码123456  
小型创业团队测试使用服务器，请勿对服务器进行攻击，拜谢！

学生在校期间避免不了要和各种证明打交道，比如学籍证明、转专业申请、休学申请、退学申请等等。此类业务一般流程都是学生去找老师告知要办的证明类型，然后老师帮助学生在电子版证明表格中填入各种信息（也有可能学生自己写），然后再打印出来。繁琐的步骤让老师和学生都叫苦不迭，于是很多学校都用上了学生信息自助打印机，像下面这种：
![http://pic.printyun.cn/%E8%87%AA%E5%8A%A9%E6%89%93%E5%8D%B0%E6%9C%BA1.jpg](http://pic.printyun.cn/%E8%87%AA%E5%8A%A9%E6%89%93%E5%8D%B0%E6%9C%BA1.jpg)
![http://pic.printyun.cn/%E8%87%AA%E5%8A%A9%E6%89%93%E5%8D%B0%E6%9C%BA2.png](http://pic.printyun.cn/%E8%87%AA%E5%8A%A9%E6%89%93%E5%8D%B0%E6%9C%BA2.png)
学生自行去机器上就可以打印证明了，可是这种解决方案弊端也很明显：  
1、价格太贵，一般学校都不会出资购买  
2、就算购买，一般也只会在职能部门购置一台，无法大面积服务全体学生  
3、可打印证明类太少，有的甚至无法自定义格式打印  

解决办法也很简单，做一个系统，学生手机打开网页输入姓名、学号等信息，系统自动匹配数据库中学生的信息，然后将信息生成对应的业务表格，老师在后台可以查询每个学生的业务申请，更可以直接通过打印机打印。（如果有需要也可以加上自动打印，不久后我们就会开源一套云打印系统）

## 系统优势：
1、便宜！便宜！便宜！重要的事情说三遍，仅需一台有公网ip的主机就可以（ubuntu最好）  
2、可以分配多个账号给不同的院系管理员，总管理员可以查看所有学生业务，院系管理员仅可查看自己院系业务  
3、可根据各种条件查询所有历史业务，方便统计  
4、类似退学、休学等需要所负责老师先在后台确认，方可继续打印，防止出现一些意外情况  
5、更多功能后续开发中...  
![http://pic.printyun.cn/stu-2.png](http://pic.printyun.cn/stu-2.png)

## 部署
说明：因为目前未考虑到大面积使用项目情况，还未添加比较方便的初始化数据库功能，需要暂时按照下面方法初始化数据库，后续会增加更加的便捷的初始化功能。  
### 1、本机测试  
1、安装pipenv
   ```python
   pip install pipenv
   ```
2、在项目根目录下运行
   ```python
   pipenv install
   ```
3、进入虚拟环境
   ```python
   pipenv shell
   ```
4、修改huojingyuan/config.py和fun.py数据库配置
```python
#config.py 7行
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/huojingyuan'
```
```python
#fun.py 34-41行
conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='huojingyuan',
        port=3306,
        charset='utf8'
    )
```
5、初始化数据库
```python
flask initdb
```
将项目根目录admin.sql导入数据库的admin表（表中内容可以自行修改，修改完后需要将fun.py文件中对应department修改，方便上传学生信息）

6、运行
```python
flask run
```
浏览器打开http://127.0.0.1:5000/upload
上传根目录test.xlsx到数据库即可使用(此文件可以根据实际情况增加信息，但是不要更改里面的列位置)

### 2、Docker部署  
也可以只配置数据库信息（只做上面4、5步），然后通过Docker方式进行部署。dockerfile仅做参考，可以自行修改。  
1、建立image  
```
docker image build -t student_info_system .
```
2、建立container
```
docker container run -d -p 8000:8000 --name student_info_system student_info_system
```
3、宿主机器打开http://127.0.0.1:8000/upload
上传根目录test.xlsx到数据库即可使用(此文件可以根据实际情况增加信息，但是不要更改里面的列位置)

***


## 相关URL
/front 前台，将此地址展示给学生即可开始业务流程  
/admin_login 后台登录入口




## 部分截图
![http://pic.printyun.cn/stu-1.png](http://pic.printyun.cn/stu-1.png)
![http://pic.printyun.cn/stu-3.png](http://pic.printyun.cn/stu-3.png)
![http://pic.printyun.cn/stu-4.png](http://pic.printyun.cn/stu-4.png)