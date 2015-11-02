# coding:utf8
#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
import xlrd
import datetime

def main():
    from hr.models import Employee
    bk = xlrd.open_workbook('/Users/apple/Desktop/test4.xls')

    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in test named Sheet1"

    nrows = sh.nrows
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows,ncols)



    row_list = []
    #获取各行数据
    for i in range(1, nrows):
        row = sh.row_values(i)
        row[5] = int(row[5])

        _s_date= datetime.date(1899, 12, 31).toordinal()-1
        d = int(row[7])
        d1 = int(row[10])
        d = datetime.date.fromordinal(_s_date+d)
        d1 = datetime.date.fromordinal(_s_date+d1)
        row[7] = d.strftime("%Y-%m-%d")
        row[10] = d1.strftime("%Y-%m-%d")

        # 处理时间为标准格式

        employee = Employee(user_name=row[0],
                            user_position=row[1],
                            user_mail=row[2],
                            user_workcode=row[3],
                            user_school_id=4,
                            user_phonenumber=row[5],
                            user_salary=row[6],
                            user_arrivetime=row[7],
                            user_ID=row[8],
                            user_gender=row[9],
                            user_birthday=row[10],
                            user_diploma=row[11],
                            user_graduate_colledge=row[12],
                            user_major=row[13]
                            )

        row_list.append(employee)

    Employee.objects.bulk_create(row_list)


if __name__ == "__main__":
    main()
    print('Done!')

