import xlwt


workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = workbook.add_sheet('test',cell_overwrite_ok=True)
sheet.write(0,0,'员工编号')
sheet.write(0,1,'姓名')
sheet.write(0,2,'身份证号')
sheet.write(0,3,'性别')
sheet.write(0,4,'出生年月')
sheet.write(0,5,'省份')
sheet.write(0,6,'家庭住址')
sheet.write(0,7,'部门')
sheet.write(0,8,'职务')
sheet.write(0,9,'入职日期')
sheet.write(0,10,'手机号码')
sheet.write(0,11,'邮箱')
sheet.write(0,12,'信用卡号')


from faker import Faker
import datetime
import random



f = Faker(locale = 'zh_CN')

for i in range(1,1001):

    ##用Faker产生数据
    female_name = f.name() #产生男性姓名
    female_sex = '男'
    male_sex = '女' # 产生女性姓名
    ssns = f.ssn() #产生身份证号
    sexs = int(ssns[16:17])#判断性别
    start_date = datetime.date(year = 1970,month = 1,day = 1)
    end_date = datetime.date(year = 2000,month = 1,day = 1)
    born_date = str(f.date_between_dates(start_date,end_date)) #产生出生日期
    provinces = f.province() #产生省份
    address = f.address() #产生地址
    department1 = '管理部'
    department2 = '设计部'
    department3 = '营销部'
    jobs = f.job() #产生工作
    s_date = datetime.date(year = 2010,month = 1,day = 1)
    e_date = datetime.date(year = 2020,month = 10,day = 13)
    job_date = str(f.date_between_dates(s_date,e_date)) # 产生入职日期
    phone_num = f.phone_number() #产生手机号
    mail_addr = f.email()#产生邮箱
    credit_card = f.credit_card_number()#产生信用卡号


    ##下方代码开始将数据写入excel表
    sheet.write(i,0,i) #写入excel表员工编号
    sheet.write(i,1,female_name)
    sheet.write(i,2,ssns)         #填充身份证号
    if sexs % 2 != 0:    #填充性别
        sheet.write(i,3,female_sex)
    else:
        sheet.write(i,3,male_sex)
    sheet.write(i,4,born_date)#填充出生日期
    sheet.write(i,5,provinces)#省份
    sheet.write(i,6,address)#家庭住址
    rand = random.randint(50,1001)
    if i >= 1 and i <= 5:
        sheet.write(i,7,department1)#部门
    elif i > 5 and i<20:
        sheet.write(i,7,department2)
    elif i >= 20 and rand == i:
        sheet.write(i,7,department1)
    elif i >= 20 and rand <=i:
        sheet.write(i,7,department3)
    elif i >= 20 and rand >= i:
        sheet.write(i,7,department2)
    sheet.write(i,8,jobs)#工作
    sheet.write(i,9,job_date)#入职日期
    sheet.write(i,10,phone_num)#手机号
    sheet.write(i,11,mail_addr)#邮箱
    sheet.write(i,12,credit_card)#信用卡号


    workbook.save(r'emplpyee.xls')#保存